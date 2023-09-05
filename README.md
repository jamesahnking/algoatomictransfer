# Algorand atomic transfer using Algokit

Two accounts A and B send account C 1Algo each. Account C then send both accounts 2 Asa. 

Application Start: 

1. Account C is created, funded, then creates 3 ASA assets.
2. Account A is created funded, then opts into the assetID of the ASA held by Account C
3. Account B is created funded, then opts into the assetID of the ASA held by Account C
4. An atomic TX is then made between accounts 

The Atomic Transfer is bundled as followed:

1. Account A Sends 1 Algo to Account C
2. Account B Sends 1 Algo to Account C
3. Account C Sends 1 ASA to Account A
4. Account C Sends 1 ASA to Account B

## The Application Steps

![AtomicTxAlgorandAlgokitIllus](https://github.com/jamesahnking/algoatomictransfer/assets/4562552/4bcee8b8-7526-44d1-94d1-2c86099ca501)

## Application Output
```
(playground-py3.11) MBP:james$ python atomicnfttx.py
address C:  XOFLMNK5O75OL2E5N2KT2SNWWMYJ3DHJCNXTFR6DTTFD4KV7A6NEB3PW7A
{'address': 'XOFLMNK5O75OL2E5N2KT2SNWWMYJ3DHJCNXTFR6DTTFD4KV7A6NEB3PW7A',
 'amount': 0,
 'amount-without-pending-rewards': 0,
 'apps-local-state': [],
 'apps-total-schema': {'num-byte-slice': 0, 'num-uint': 0},
 'assets': [],
 'created-apps': [],
 'created-assets': [],
 'min-balance': 100000,
 'pending-rewards': 0,
 'reward-base': 0,
 'rewards': 0,
 'round': 111,
 'status': 'Offline',
 'total-apps-opted-in': 0,
 'total-assets-opted-in': 0,
 'total-created-apps': 0,
 'total-created-assets': 0}
Successfully sent transaction with txID: 3T2RTZAFKTQMBUFJPZSSL5PV772XENVYL7N4TJR2T3WD377CR4XA
{'address': 'XOFLMNK5O75OL2E5N2KT2SNWWMYJ3DHJCNXTFR6DTTFD4KV7A6NEB3PW7A',
 'amount': 2099000,
 'amount-without-pending-rewards': 2099000,
 'apps-local-state': [],
 'apps-total-schema': {'num-byte-slice': 0, 'num-uint': 0},
 'assets': [{'amount': 3, 'asset-id': 1118, 'is-frozen': False}],
 'created-apps': [],
 'created-assets': [{'index': 1118,
                     'params': {'creator': 'XOFLMNK5O75OL2E5N2KT2SNWWMYJ3DHJCNXTFR6DTTFD4KV7A6NEB3PW7A',
                                'decimals': 0,
                                'default-frozen': False,
                                'total': 3}}],
 'min-balance': 200000,
 'pending-rewards': 0,
 'reward-base': 0,
 'rewards': 0,
 'round': 113,
 'status': 'Offline',
 'total-apps-opted-in': 0,
 'total-assets-opted-in': 1,
 'total-created-apps': 0,
 'total-created-assets': 1}
assetID:  1118
address A:  OWTCN5BCZRVR4PS7ACJ7FMP3HICXTVKFDLQ3NB2CHSRDOHLPCFUC5X6NAM
Successfully sent transaction with txID: YCTQRNE72A2FOJT5GSNAJZ4PITRLJXPENTWUPEXKGKG6P4KH233Q
{'address': 'OWTCN5BCZRVR4PS7ACJ7FMP3HICXTVKFDLQ3NB2CHSRDOHLPCFUC5X6NAM',
 'amount': 2099000,
 'amount-without-pending-rewards': 2099000,
 'apps-local-state': [],
 'apps-total-schema': {'num-byte-slice': 0, 'num-uint': 0},
 'assets': [{'amount': 0, 'asset-id': 1118, 'is-frozen': False}],
 'created-apps': [],
 'created-assets': [],
 'min-balance': 200000,
 'pending-rewards': 0,
 'reward-base': 0,
 'rewards': 0,
 'round': 115,
 'status': 'Offline',
 'total-apps-opted-in': 0,
 'total-assets-opted-in': 1,
 'total-created-apps': 0,
 'total-created-assets': 0}
address B:  3PFDSVBLKPNMVTPSPQG7E7VJIJKIIW3BQO3ZP3MLQX57IQJLD3SJL23DKI
Successfully sent transaction with txID: BKB7I6NYZTXZ4RQVIXLNBN2EMC5MAW4OPKRBZLJL4V5VT4V2WBKQ
{'address': '3PFDSVBLKPNMVTPSPQG7E7VJIJKIIW3BQO3ZP3MLQX57IQJLD3SJL23DKI',
 'amount': 2099000,
 'amount-without-pending-rewards': 2099000,
 'apps-local-state': [],
 'apps-total-schema': {'num-byte-slice': 0, 'num-uint': 0},
 'assets': [{'amount': 0, 'asset-id': 1118, 'is-frozen': False}],
 'created-apps': [],
 'created-assets': [],
 'min-balance': 200000,
 'pending-rewards': 0,
 'reward-base': 0,
 'rewards': 0,
 'round': 117,
 'status': 'Offline',
 'total-apps-opted-in': 0,
 'total-assets-opted-in': 1,
 'total-created-apps': 0,
 'total-created-assets': 0}
Successfully sent transaction group with txID: RWY52Z3SMBKYZCZIX2GJQ64VQS46XTJBEKOF5AO64HSFXJZKAY5A
{'address': 'OWTCN5BCZRVR4PS7ACJ7FMP3HICXTVKFDLQ3NB2CHSRDOHLPCFUC5X6NAM',
 'amount': 1098000,
 'amount-without-pending-rewards': 1098000,
 'apps-local-state': [],
 'apps-total-schema': {'num-byte-slice': 0, 'num-uint': 0},
 'assets': [{'amount': 1, 'asset-id': 1118, 'is-frozen': False}],
 'created-apps': [],
 'created-assets': [],
 'min-balance': 200000,
 'pending-rewards': 0,
 'reward-base': 0,
 'rewards': 0,
 'round': 118,
 'status': 'Offline',
 'total-apps-opted-in': 0,
 'total-assets-opted-in': 1,
 'total-created-apps': 0,
 'total-created-assets': 0}
{'address': '3PFDSVBLKPNMVTPSPQG7E7VJIJKIIW3BQO3ZP3MLQX57IQJLD3SJL23DKI',
 'amount': 1098000,
 'amount-without-pending-rewards': 1098000,
 'apps-local-state': [],
 'apps-total-schema': {'num-byte-slice': 0, 'num-uint': 0},
 'assets': [{'amount': 1, 'asset-id': 1118, 'is-frozen': False}],
 'created-apps': [],
 'created-assets': [],
 'min-balance': 200000,
 'pending-rewards': 0,
 'reward-base': 0,
 'rewards': 0,
 'round': 118,
 'status': 'Offline',
 'total-apps-opted-in': 0,
 'total-assets-opted-in': 1,
 'total-created-apps': 0,
 'total-created-assets': 0}
{'address': 'XOFLMNK5O75OL2E5N2KT2SNWWMYJ3DHJCNXTFR6DTTFD4KV7A6NEB3PW7A',
 'amount': 4097000,
 'amount-without-pending-rewards': 4097000,
 'apps-local-state': [],
 'apps-total-schema': {'num-byte-slice': 0, 'num-uint': 0},
 'assets': [{'amount': 1, 'asset-id': 1118, 'is-frozen': False}],
 'created-apps': [],
 'created-assets': [{'index': 1118,
                     'params': {'creator': 'XOFLMNK5O75OL2E5N2KT2SNWWMYJ3DHJCNXTFR6DTTFD4KV7A6NEB3PW7A',
                                'decimals': 0,
                                'default-frozen': False,
                                'total': 3}}],
 'min-balance': 200000,
 'pending-rewards': 0,
 'reward-base': 0,
 'rewards': 0,
 'round': 118,
 'status': 'Offline',
 'total-apps-opted-in': 0,
 'total-assets-opted-in': 1,
 'total-created-apps': 0,
 'total-created-assets': 1}
```
