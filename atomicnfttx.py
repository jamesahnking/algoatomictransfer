import algokit_utils as algokit
import algosdk as algosdk
from pprint import pprint


def main():

    #####################################################################
    # Create ACCOUNT C - 'Creator Account' generate 3 NFTs
    #####################################################################

    # instatiate algod client on localnet
    algod = algokit.get_algod_client(
        algokit.get_default_localnet_config("algod"))

    # Generate Creator Account accountC
    accountC = algokit.Account.new_account()
    print("address C: ", accountC.address)

    # get info about accountC from algod
    pprint(algod.account_info(accountC.address))

    # instatiate kmd client on localnet
    kmd = algokit.get_algod_client(
        algokit.get_default_localnet_config("algod"))

    # Fund Creator account - accountC
    algokit.ensure_funded(
        algod,
        algokit.EnsureBalanceParameters(
            account_to_fund=accountC.address,
            min_spending_balance_micro_algos=2_000_000
        )
    )

    # accountC create 3 ASA (Algorand Standard Asset, token, asset, NFT, etc.)
    unsigned_tx = algosdk.transaction.AssetCreateTxn(
        sender=accountC.address,
        sp=algod.suggested_params(),
        total=3,
        decimals=0,
        default_frozen=False
    )

    # sign transaction
    signed_txn = unsigned_tx.sign(accountC.private_key)

    # submit transaction
    txid = algod.send_transaction(signed_txn)
    print("Successfully sent transaction with txID: {}".format(txid))

    # get info about accountA, accountB, accountC from algod
    pprint(algod.account_info(accountC.address))

    # print the assetID of my new asset from algod
    results = algod.pending_transaction_info(txid)
    assetID = results["asset-index"]
    print("assetID: ", assetID)

    #####################################################################
    # Create ACCOUNT A
    #####################################################################

    accountA = algokit.Account.new_account()
    print("address A: ", accountA.address)

    # accountB Funding
    algokit.ensure_funded(
        algod,
        algokit.EnsureBalanceParameters(
            account_to_fund=accountA.address,
            min_spending_balance_micro_algos=2_000_000
        )
    )

    # accountB Opt-In
    unsigned_txn = algosdk.transaction.AssetTransferTxn(
        sender=accountA.address,
        sp=algod.suggested_params(),
        receiver=accountA.address,
        amt=0,
        index=assetID,
    )

    # sign transaction
    signed_txn = unsigned_txn.sign(accountA.private_key)

    # submit transaction
    txid = algod.send_transaction(signed_txn)
    print("Successfully sent transaction with txID: {}".format(txid))

    # print to see optIn
    pprint(algod.account_info(accountA.address))

    #####################################################################
    # Create ACCOUNT B
    #####################################################################

    accountB = algokit.Account.new_account()
    print("address B: ", accountB.address)

    # accountB Funding
    algokit.ensure_funded(
        algod,
        algokit.EnsureBalanceParameters(
            account_to_fund=accountB.address,
            min_spending_balance_micro_algos=2_000_000
        )
    )

    # accountB Opt-In
    unsigned_txn = algosdk.transaction.AssetTransferTxn(
        sender=accountB.address,
        sp=algod.suggested_params(),
        receiver=accountB.address,
        amt=0,
        index=assetID,
    )

    # sign transaction
    signed_txn = unsigned_txn.sign(accountB.private_key)

    # submit transaction
    txid = algod.send_transaction(signed_txn)
    print("Successfully sent transaction with txID: {}".format(txid))

    # print to see optIn
    pprint(algod.account_info(accountB.address))

    #####################################################################
    # ATOMIC TXNs -
    # 1. Account A Sends 1 Algo to Account C
    # 2. Account B Sends 1 Aclgo to Account C
    # 3. Account C Sends 1 ASA to Account A
    # 4. Account C Sends 1 ASA to Account B
    # 5. Account C Sends 1.5 Algo to Account D
    #####################################################################

    # 1. Account A Sends 1 Algo to Account C
    payment_txn_A = algosdk.transaction.PaymentTxn(
        sender=accountA.address,
        sp=algod.suggested_params(),
        receiver=accountC.address,
        amt=1_000_000
    )

    # 2. Account B Sends 1 Algo to Account C
    payment_txn_B = algosdk.transaction.PaymentTxn(
        sender=accountB.address,
        sp=algod.suggested_params(),
        receiver=accountC.address,
        amt=1_000_000
    )

    # 3. Account C Sends 1 ASA to Account A
    payment_txn_C2A = algosdk.transaction.AssetTransferTxn(
        sender=accountC.address,
        sp=algod.suggested_params(),
        receiver=accountA.address,
        amt=1,
        index=assetID,
    )

    # 4. Account C Sends 1 ASA to Account B
    payment_txn_C2B = algosdk.transaction.AssetTransferTxn(
        sender=accountC.address,
        sp=algod.suggested_params(),
        receiver=accountB.address,
        amt=1,
        index=assetID,
    )   

    #####################################################################
    # Group Transactions
    #####################################################################

    group_id = algosdk.transaction.calculate_group_id(
        [payment_txn_A, payment_txn_B, payment_txn_C2A, payment_txn_C2B])
    payment_txn_A.group = group_id
    payment_txn_B.group = group_id
    payment_txn_C2A.group = group_id
    payment_txn_C2B.group = group_id

    #####################################################################
    # Sign Transactions
    #####################################################################

    stxn_1 = payment_txn_A.sign(accountA.private_key)
    stxn_2 = payment_txn_B.sign(accountB.private_key)
    stxn_3 = payment_txn_C2A.sign(accountC.private_key)
    stxn_4 = payment_txn_C2B.sign(accountC.private_key)

    #####################################################################
    # Assemble Transactions Group
    #####################################################################

    signed_group = [stxn_1, stxn_2, stxn_3, stxn_4]

    #####################################################################
    # Submit Atomic Transactions Group
    #####################################################################

    txid = algod.send_transactions(signed_group)
    print("Successfully sent transaction group with txID: {}".format(txid))
    
    #####################################################################
    # Confirm Atomic Transfer
    #####################################################################
   
    pprint(algod.account_info(accountA.address))
    pprint(algod.account_info(accountB.address))
    pprint(algod.account_info(accountC.address))

main()
