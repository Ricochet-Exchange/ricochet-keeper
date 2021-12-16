DISTRIBUTE_ABI = """[{
      "inputs": [],
      "name": "distribute",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    }]"""


ERC20_ABI = """
[
    {
        "constant": true,
        "inputs": [],
        "name": "name",
        "outputs": [
            {
                "name": "",
                "type": "string"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [
            {
                "name": "_spender",
                "type": "address"
            },
            {
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "approve",
        "outputs": [
            {
                "name": "",
                "type": "bool"
            }
        ],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "totalSupply",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [
            {
                "name": "_from",
                "type": "address"
            },
            {
                "name": "_to",
                "type": "address"
            },
            {
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "transferFrom",
        "outputs": [
            {
                "name": "",
                "type": "bool"
            }
        ],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "decimals",
        "outputs": [
            {
                "name": "",
                "type": "uint8"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [
            {
                "name": "_owner",
                "type": "address"
            }
        ],
        "name": "balanceOf",
        "outputs": [
            {
                "name": "balance",
                "type": "uint256"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "symbol",
        "outputs": [
            {
                "name": "",
                "type": "string"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [
            {
                "name": "_to",
                "type": "address"
            },
            {
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "transfer",
        "outputs": [
            {
                "name": "",
                "type": "bool"
            }
        ],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [
            {
                "name": "_owner",
                "type": "address"
            },
            {
                "name": "_spender",
                "type": "address"
            }
        ],
        "name": "allowance",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "payable": true,
        "stateMutability": "payable",
        "type": "fallback"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "name": "owner",
                "type": "address"
            },
            {
                "indexed": true,
                "name": "spender",
                "type": "address"
            },
            {
                "indexed": false,
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "Approval",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "name": "from",
                "type": "address"
            },
            {
                "indexed": true,
                "name": "to",
                "type": "address"
            },
            {
                "indexed": false,
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "Transfer",
        "type": "event"
    }
]
"""

HARVEST_ABI = """
[
    {
        "inputs": [],
        "name": "harvest",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    }
]
"""

REX_ABI = """v
[
    {
        "inputs": [
            {"internalType": "contract ISuperfluid", "name": "host", "type": "address"},
            {
                "internalType": "contract IConstantFlowAgreementV1",
                "name": "cfa",
                "type": "address",
            },
            {
                "internalType": "contract IInstantDistributionAgreementV1",
                "name": "ida",
                "type": "address",
            },
            {
                "internalType": "contract ISuperToken",
                "name": "inputToken",
                "type": "address",
            },
            {
                "internalType": "contract ISuperToken",
                "name": "pairToken",
                "type": "address",
            },
            {
                "internalType": "contract ISuperToken",
                "name": "outputToken",
                "type": "address",
            },
            {
                "internalType": "contract ISuperToken",
                "name": "subsidyToken",
                "type": "address",
            },
            {
                "internalType": "contract IUniswapV2Router02",
                "name": "sushiRouter",
                "type": "address",
            },
            {"internalType": "address payable", "name": "oracle", "type": "address"},
            {"internalType": "uint256", "name": "requestId", "type": "uint256"},
            {"internalType": "string", "name": "registrationKey", "type": "string"},
        ],
        "stateMutability": "nonpayable",
        "type": "constructor",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "previousOwner",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "newOwner",
                "type": "address",
            },
        ],
        "name": "OwnershipTransferred",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "from",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "int96",
                "name": "newRate",
                "type": "int96",
            },
            {
                "indexed": false,
                "internalType": "int96",
                "name": "totalInflow",
                "type": "int96",
            },
        ],
        "name": "UpdatedStream",
        "type": "event",
    },
    {"stateMutability": "payable", "type": "fallback"},
    {
        "inputs": [
            {
                "internalType": "contract ISuperToken",
                "name": "_superToken",
                "type": "address",
            },
            {"internalType": "address", "name": "_agreementClass", "type": "address"},
            {"internalType": "bytes32", "name": "", "type": "bytes32"},
            {"internalType": "bytes", "name": "_agreementData", "type": "bytes"},
            {"internalType": "bytes", "name": "", "type": "bytes"},
            {"internalType": "bytes", "name": "_ctx", "type": "bytes"},
        ],
        "name": "afterAgreementCreated",
        "outputs": [{"internalType": "bytes", "name": "newCtx", "type": "bytes"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "internalType": "contract ISuperToken",
                "name": "_superToken",
                "type": "address",
            },
            {"internalType": "address", "name": "_agreementClass", "type": "address"},
            {"internalType": "bytes32", "name": "", "type": "bytes32"},
            {"internalType": "bytes", "name": "_agreementData", "type": "bytes"},
            {"internalType": "bytes", "name": "", "type": "bytes"},
            {"internalType": "bytes", "name": "_ctx", "type": "bytes"},
        ],
        "name": "afterAgreementTerminated",
        "outputs": [{"internalType": "bytes", "name": "newCtx", "type": "bytes"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "internalType": "contract ISuperToken",
                "name": "_superToken",
                "type": "address",
            },
            {"internalType": "address", "name": "_agreementClass", "type": "address"},
            {"internalType": "bytes32", "name": "", "type": "bytes32"},
            {"internalType": "bytes", "name": "_agreementData", "type": "bytes"},
            {"internalType": "bytes", "name": "", "type": "bytes"},
            {"internalType": "bytes", "name": "_ctx", "type": "bytes"},
        ],
        "name": "afterAgreementUpdated",
        "outputs": [{"internalType": "bytes", "name": "newCtx", "type": "bytes"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "contract ISuperToken", "name": "", "type": "address"},
            {"internalType": "address", "name": "", "type": "address"},
            {"internalType": "bytes32", "name": "", "type": "bytes32"},
            {"internalType": "bytes", "name": "", "type": "bytes"},
            {"internalType": "bytes", "name": "", "type": "bytes"},
        ],
        "name": "beforeAgreementCreated",
        "outputs": [{"internalType": "bytes", "name": "", "type": "bytes"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "contract ISuperToken", "name": "", "type": "address"},
            {"internalType": "address", "name": "", "type": "address"},
            {"internalType": "bytes32", "name": "", "type": "bytes32"},
            {"internalType": "bytes", "name": "", "type": "bytes"},
            {"internalType": "bytes", "name": "", "type": "bytes"},
        ],
        "name": "beforeAgreementTerminated",
        "outputs": [{"internalType": "bytes", "name": "", "type": "bytes"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "contract ISuperToken", "name": "", "type": "address"},
            {"internalType": "address", "name": "", "type": "address"},
            {"internalType": "bytes32", "name": "", "type": "bytes32"},
            {"internalType": "bytes", "name": "", "type": "bytes"},
            {"internalType": "bytes", "name": "", "type": "bytes"},
        ],
        "name": "beforeAgreementUpdated",
        "outputs": [{"internalType": "bytes", "name": "", "type": "bytes"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "streamer", "type": "address"}],
        "name": "closeStream",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "distribute",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "streamer", "type": "address"}],
        "name": "emergencyCloseStream",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "emergencyDrain",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "executeApprovals",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_requestId", "type": "uint256"}
        ],
        "name": "getCurrentValue",
        "outputs": [
            {"internalType": "bool", "name": "ifRetrieve", "type": "bool"},
            {"internalType": "uint256", "name": "value", "type": "uint256"},
            {
                "internalType": "uint256",
                "name": "_timestampRetrieved",
                "type": "uint256",
            },
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_requestId", "type": "uint256"},
            {"internalType": "uint256", "name": "_timestamp", "type": "uint256"},
        ],
        "name": "getDataBefore",
        "outputs": [
            {"internalType": "bool", "name": "_ifRetrieve", "type": "bool"},
            {"internalType": "uint256", "name": "_value", "type": "uint256"},
            {
                "internalType": "uint256",
                "name": "_timestampRetrieved",
                "type": "uint256",
            },
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getFeeRate",
        "outputs": [{"internalType": "uint128", "name": "", "type": "uint128"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getHarvestFeeRate",
        "outputs": [{"internalType": "uint128", "name": "", "type": "uint128"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint32", "name": "index", "type": "uint32"},
            {"internalType": "address", "name": "streamer", "type": "address"},
        ],
        "name": "getIDAShares",
        "outputs": [
            {"internalType": "bool", "name": "exist", "type": "bool"},
            {"internalType": "bool", "name": "approved", "type": "bool"},
            {"internalType": "uint128", "name": "units", "type": "uint128"},
            {
                "internalType": "uint256",
                "name": "pendingDistribution",
                "type": "uint256",
            },
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_requestId", "type": "uint256"},
            {"internalType": "uint256", "name": "_timestamp", "type": "uint256"},
        ],
        "name": "getIndexForDataBefore",
        "outputs": [
            {"internalType": "bool", "name": "found", "type": "bool"},
            {"internalType": "uint256", "name": "index", "type": "uint256"},
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getInputToken",
        "outputs": [
            {"internalType": "contract ISuperToken", "name": "", "type": "address"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getLastDistributionAt",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_requestId", "type": "uint256"}
        ],
        "name": "getNewValueCountbyRequestId",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getOuputIndexId",
        "outputs": [{"internalType": "uint32", "name": "", "type": "uint32"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getOuputToken",
        "outputs": [
            {"internalType": "contract ISuperToken", "name": "", "type": "address"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getOwner",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getRateTolerance",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getRequestId",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "streamer", "type": "address"}],
        "name": "getStreamRate",
        "outputs": [
            {"internalType": "int96", "name": "requesterFlowRate", "type": "int96"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getSubsidyIndexId",
        "outputs": [{"internalType": "uint32", "name": "", "type": "uint32"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getSubsidyRate",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getSubsidyToken",
        "outputs": [
            {"internalType": "contract ISuperToken", "name": "", "type": "address"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getSushiRouter",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getTellorOracle",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_requestId", "type": "uint256"},
            {"internalType": "uint256", "name": "_index", "type": "uint256"},
        ],
        "name": "getTimestampbyRequestIDandIndex",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getTotalInflow",
        "outputs": [{"internalType": "int96", "name": "", "type": "int96"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {
                "internalType": "contract ISuperToken",
                "name": "output",
                "type": "address",
            },
            {
                "internalType": "contract ISuperToken",
                "name": "subsidy",
                "type": "address",
            },
            {
                "internalType": "contract ISuperToken",
                "name": "sushix",
                "type": "address",
            },
            {
                "internalType": "contract ISuperToken",
                "name": "maticx",
                "type": "address",
            },
        ],
        "name": "initialize",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "isAppJailed",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_requestId", "type": "uint256"},
            {"internalType": "uint256", "name": "_timestamp", "type": "uint256"},
        ],
        "name": "isInDispute",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "owner",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "renounceOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_requestId", "type": "uint256"},
            {"internalType": "uint256", "name": "_timestamp", "type": "uint256"},
        ],
        "name": "retrieveData",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint128", "name": "feeRate", "type": "uint128"}],
        "name": "setFeeRate",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint128", "name": "feeRate", "type": "uint128"}],
        "name": "setHarvestFeeRate",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "oracle", "type": "address"}],
        "name": "setOracle",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint128", "name": "rateTolerance", "type": "uint128"}
        ],
        "name": "setRateTolerance",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "requestId", "type": "uint256"}],
        "name": "setRequestId",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint128", "name": "subsidyRate", "type": "uint128"}
        ],
        "name": "setSubsidyRate",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "newOwner", "type": "address"}],
        "name": "transferOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
]
"""


REX_BANK_ABI = """
[
    {
        "inputs": [
            {
                "internalType": "address payable",
                "name": "oracleContract",
                "type": "address",
            }
        ],
        "stateMutability": "nonpayable",
        "type": "constructor",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "borrower",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "debtAmount",
                "type": "uint256",
            },
        ],
        "name": "Liquidation",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "token",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "price",
                "type": "uint256",
            },
        ],
        "name": "PriceUpdate",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256",
            }
        ],
        "name": "ReserveDeposit",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "token",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256",
            },
        ],
        "name": "ReserveWithdraw",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "borrower",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256",
            },
        ],
        "name": "VaultBorrow",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "owner",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256",
            },
        ],
        "name": "VaultDeposit",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "borrower",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256",
            },
        ],
        "name": "VaultRepay",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "borrower",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256",
            },
        ],
        "name": "VaultWithdraw",
        "type": "event",
    },
    {
        "inputs": [],
        "name": "getBankFactoryOwner",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getCollateralTokenAddress",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getCollateralTokenLastUpdatedAt",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getCollateralTokenPrice",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getCollateralTokenPriceGranularity",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getCollateralizationRatio",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_requestId", "type": "uint256"}
        ],
        "name": "getCurrentValue",
        "outputs": [
            {"internalType": "bool", "name": "ifRetrieve", "type": "bool"},
            {"internalType": "uint256", "name": "value", "type": "uint256"},
            {
                "internalType": "uint256",
                "name": "_timestampRetrieved",
                "type": "uint256",
            },
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getDebtTokenAddress",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getDebtTokenLastUpdatedAt",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getDebtTokenPrice",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getDebtTokenPriceGranularity",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getInterestRate",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getLiquidationPenalty",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getName",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getOriginationFee",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getReserveBalance",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getReserveCollateralBalance",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getVaultCollateralAmount",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "vaultOwner", "type": "address"}
        ],
        "name": "getVaultCollateralizationRatio",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getVaultDebtAmount",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getVaultRepayAmount",
        "outputs": [
            {"internalType": "uint256", "name": "principal", "type": "uint256"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "creator", "type": "address"},
            {"internalType": "string", "name": "bankName", "type": "string"},
            {"internalType": "uint256", "name": "interestRate", "type": "uint256"},
            {"internalType": "uint256", "name": "originationFee", "type": "uint256"},
            {
                "internalType": "uint256",
                "name": "collateralizationRatio",
                "type": "uint256",
            },
            {
                "internalType": "uint256",
                "name": "liquidationPenalty",
                "type": "uint256",
            },
            {"internalType": "uint256", "name": "period", "type": "uint256"},
            {"internalType": "address", "name": "bankFactoryOwner", "type": "address"},
            {
                "internalType": "address payable",
                "name": "oracleContract",
                "type": "address",
            },
        ],
        "name": "init",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "vaultOwner", "type": "address"}
        ],
        "name": "liquidate",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "owner",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "amount", "type": "uint256"}],
        "name": "reserveDeposit",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "amount", "type": "uint256"}],
        "name": "reserveWithdraw",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "amount", "type": "uint256"}],
        "name": "reserveWithdrawCollateral",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "newOwner", "type": "address"}],
        "name": "setBankFactoryOwner",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "collateralToken", "type": "address"},
            {
                "internalType": "uint256",
                "name": "collateralTokenTellorRequestId",
                "type": "uint256",
            },
            {
                "internalType": "uint256",
                "name": "collateralTokenPriceGranularity",
                "type": "uint256",
            },
            {
                "internalType": "uint256",
                "name": "collateralTokenPrice",
                "type": "uint256",
            },
        ],
        "name": "setCollateral",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "debtToken", "type": "address"},
            {
                "internalType": "uint256",
                "name": "debtTokenTellorRequestId",
                "type": "uint256",
            },
            {
                "internalType": "uint256",
                "name": "debtTokenPriceGranularity",
                "type": "uint256",
            },
            {"internalType": "uint256", "name": "debtTokenPrice", "type": "uint256"},
        ],
        "name": "setDebt",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "newOwner", "type": "address"}],
        "name": "transferOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "updateCollateralPrice",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "updateDebtPrice",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "amount", "type": "uint256"}],
        "name": "vaultBorrow",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "amount", "type": "uint256"}],
        "name": "vaultDeposit",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "amount", "type": "uint256"}],
        "name": "vaultRepay",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "amount", "type": "uint256"}],
        "name": "vaultWithdraw",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "", "type": "address"}],
        "name": "vaults",
        "outputs": [
            {"internalType": "uint256", "name": "collateralAmount", "type": "uint256"},
            {"internalType": "uint256", "name": "debtAmount", "type": "uint256"},
            {"internalType": "uint256", "name": "createdAt", "type": "uint256"},
        ],
        "stateMutability": "view",
        "type": "function",
    },
]
"""

REX_LAUNCHPAD_API = """
[
    {
        "inputs": [
            {"internalType": "contract ISuperfluid", "name": "host", "type": "address"},
            {
                "internalType": "contract IConstantFlowAgreementV1",
                "name": "cfa",
                "type": "address",
            },
            {
                "internalType": "contract IInstantDistributionAgreementV1",
                "name": "ida",
                "type": "address",
            },
            {"internalType": "string", "name": "registrationKey", "type": "string"},
        ],
        "stateMutability": "nonpayable",
        "type": "constructor",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "previousOwner",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "newOwner",
                "type": "address",
            },
        ],
        "name": "OwnershipTransferred",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "from",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "int96",
                "name": "newRate",
                "type": "int96",
            },
            {
                "indexed": false,
                "internalType": "int96",
                "name": "totalInflow",
                "type": "int96",
            },
        ],
        "name": "UpdatedStream",
        "type": "event",
    },
    {
        "inputs": [
            {
                "internalType": "contract ISuperToken",
                "name": "_superToken",
                "type": "address",
            },
            {"internalType": "address", "name": "_agreementClass", "type": "address"},
            {"internalType": "bytes32", "name": "", "type": "bytes32"},
            {"internalType": "bytes", "name": "_agreementData", "type": "bytes"},
            {"internalType": "bytes", "name": "", "type": "bytes"},
            {"internalType": "bytes", "name": "_ctx", "type": "bytes"},
        ],
        "name": "afterAgreementCreated",
        "outputs": [{"internalType": "bytes", "name": "newCtx", "type": "bytes"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "internalType": "contract ISuperToken",
                "name": "_superToken",
                "type": "address",
            },
            {"internalType": "address", "name": "_agreementClass", "type": "address"},
            {"internalType": "bytes32", "name": "", "type": "bytes32"},
            {"internalType": "bytes", "name": "_agreementData", "type": "bytes"},
            {"internalType": "bytes", "name": "", "type": "bytes"},
            {"internalType": "bytes", "name": "_ctx", "type": "bytes"},
        ],
        "name": "afterAgreementTerminated",
        "outputs": [{"internalType": "bytes", "name": "newCtx", "type": "bytes"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "internalType": "contract ISuperToken",
                "name": "_superToken",
                "type": "address",
            },
            {"internalType": "address", "name": "_agreementClass", "type": "address"},
            {"internalType": "bytes32", "name": "", "type": "bytes32"},
            {"internalType": "bytes", "name": "_agreementData", "type": "bytes"},
            {"internalType": "bytes", "name": "", "type": "bytes"},
            {"internalType": "bytes", "name": "_ctx", "type": "bytes"},
        ],
        "name": "afterAgreementUpdated",
        "outputs": [{"internalType": "bytes", "name": "newCtx", "type": "bytes"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "contract ISuperToken", "name": "", "type": "address"},
            {"internalType": "address", "name": "", "type": "address"},
            {"internalType": "bytes32", "name": "", "type": "bytes32"},
            {"internalType": "bytes", "name": "", "type": "bytes"},
            {"internalType": "bytes", "name": "", "type": "bytes"},
        ],
        "name": "beforeAgreementCreated",
        "outputs": [{"internalType": "bytes", "name": "", "type": "bytes"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "contract ISuperToken", "name": "", "type": "address"},
            {"internalType": "address", "name": "", "type": "address"},
            {"internalType": "bytes32", "name": "", "type": "bytes32"},
            {"internalType": "bytes", "name": "", "type": "bytes"},
            {"internalType": "bytes", "name": "", "type": "bytes"},
        ],
        "name": "beforeAgreementTerminated",
        "outputs": [{"internalType": "bytes", "name": "", "type": "bytes"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "contract ISuperToken", "name": "", "type": "address"},
            {"internalType": "address", "name": "", "type": "address"},
            {"internalType": "bytes32", "name": "", "type": "bytes32"},
            {"internalType": "bytes", "name": "", "type": "bytes"},
            {"internalType": "bytes", "name": "", "type": "bytes"},
        ],
        "name": "beforeAgreementUpdated",
        "outputs": [{"internalType": "bytes", "name": "", "type": "bytes"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "streamer", "type": "address"}],
        "name": "closeStream",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "distribute",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "streamer", "type": "address"}],
        "name": "emergencyCloseStream",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "emergencyDrain",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getFeeRate",
        "outputs": [{"internalType": "uint128", "name": "", "type": "uint128"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint32", "name": "index", "type": "uint32"},
            {"internalType": "address", "name": "streamer", "type": "address"},
        ],
        "name": "getIDAShares",
        "outputs": [
            {"internalType": "bool", "name": "exist", "type": "bool"},
            {"internalType": "bool", "name": "approved", "type": "bool"},
            {"internalType": "uint128", "name": "units", "type": "uint128"},
            {
                "internalType": "uint256",
                "name": "pendingDistribution",
                "type": "uint256",
            },
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getInputToken",
        "outputs": [
            {"internalType": "contract ISuperToken", "name": "", "type": "address"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getLastDistributionAt",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getOutputIndexId",
        "outputs": [{"internalType": "uint32", "name": "", "type": "uint32"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getOutputRate",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getOutputToken",
        "outputs": [
            {"internalType": "contract ISuperToken", "name": "", "type": "address"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getOwner",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getSharePrice",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "streamer", "type": "address"}],
        "name": "getStreamRate",
        "outputs": [
            {"internalType": "int96", "name": "requesterFlowRate", "type": "int96"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getTotalInflow",
        "outputs": [{"internalType": "int96", "name": "", "type": "int96"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {
                "internalType": "contract ISuperToken",
                "name": "inputToken",
                "type": "address",
            },
            {
                "internalType": "contract ISuperToken",
                "name": "outputToken",
                "type": "address",
            },
            {"internalType": "address", "name": "originator", "type": "address"},
            {"internalType": "address", "name": "beneficiary", "type": "address"},
            {"internalType": "uint256", "name": "outputRate", "type": "uint256"},
            {"internalType": "uint128", "name": "feeRate", "type": "uint128"},
        ],
        "name": "initialize",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "isAppJailed",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "owner",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "renounceOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint128", "name": "feeRate", "type": "uint128"}],
        "name": "setFeeRate",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "newOwner", "type": "address"}],
        "name": "transferOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
]
"""

REX_CLOSESTREAM_ABI = """
[
    {
        "inputs": [
            {"internalType": "contract ISuperfluid", "name": "host", "type": "address"},
            {
                "internalType": "contract IConstantFlowAgreementV1",
                "name": "cfa",
                "type": "address",
            },
            {
                "internalType": "contract IInstantDistributionAgreementV1",
                "name": "ida",
                "type": "address",
            },
            {
                "internalType": "contract ISuperToken",
                "name": "inputToken",
                "type": "address",
            },
            {
                "internalType": "contract ISuperToken",
                "name": "outputToken",
                "type": "address",
            },
            {
                "internalType": "contract ISuperToken",
                "name": "subsidyToken",
                "type": "address",
            },
            {
                "internalType": "contract IUniswapV2Router02",
                "name": "sushiRouter",
                "type": "address",
            },
            {"internalType": "address payable", "name": "oracle", "type": "address"},
            {"internalType": "uint256", "name": "requestId", "type": "uint256"},
            {"internalType": "string", "name": "registrationKey", "type": "string"},
        ],
        "stateMutability": "nonpayable",
        "type": "constructor",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "previousOwner",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "newOwner",
                "type": "address",
            },
        ],
        "name": "OwnershipTransferred",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "from",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "int96",
                "name": "newRate",
                "type": "int96",
            },
            {
                "indexed": false,
                "internalType": "int96",
                "name": "totalInflow",
                "type": "int96",
            },
        ],
        "name": "UpdatedStream",
        "type": "event",
    },
    {
        "inputs": [
            {
                "internalType": "contract ISuperToken",
                "name": "_superToken",
                "type": "address",
            },
            {"internalType": "address", "name": "_agreementClass", "type": "address"},
            {"internalType": "bytes32", "name": "", "type": "bytes32"},
            {"internalType": "bytes", "name": "_agreementData", "type": "bytes"},
            {"internalType": "bytes", "name": "", "type": "bytes"},
            {"internalType": "bytes", "name": "_ctx", "type": "bytes"},
        ],
        "name": "afterAgreementCreated",
        "outputs": [{"internalType": "bytes", "name": "newCtx", "type": "bytes"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "internalType": "contract ISuperToken",
                "name": "_superToken",
                "type": "address",
            },
            {"internalType": "address", "name": "_agreementClass", "type": "address"},
            {"internalType": "bytes32", "name": "", "type": "bytes32"},
            {"internalType": "bytes", "name": "_agreementData", "type": "bytes"},
            {"internalType": "bytes", "name": "", "type": "bytes"},
            {"internalType": "bytes", "name": "_ctx", "type": "bytes"},
        ],
        "name": "afterAgreementTerminated",
        "outputs": [{"internalType": "bytes", "name": "newCtx", "type": "bytes"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "internalType": "contract ISuperToken",
                "name": "_superToken",
                "type": "address",
            },
            {"internalType": "address", "name": "_agreementClass", "type": "address"},
            {"internalType": "bytes32", "name": "", "type": "bytes32"},
            {"internalType": "bytes", "name": "_agreementData", "type": "bytes"},
            {"internalType": "bytes", "name": "", "type": "bytes"},
            {"internalType": "bytes", "name": "_ctx", "type": "bytes"},
        ],
        "name": "afterAgreementUpdated",
        "outputs": [{"internalType": "bytes", "name": "newCtx", "type": "bytes"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "contract ISuperToken", "name": "", "type": "address"},
            {"internalType": "address", "name": "", "type": "address"},
            {"internalType": "bytes32", "name": "", "type": "bytes32"},
            {"internalType": "bytes", "name": "", "type": "bytes"},
            {"internalType": "bytes", "name": "", "type": "bytes"},
        ],
        "name": "beforeAgreementCreated",
        "outputs": [{"internalType": "bytes", "name": "", "type": "bytes"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "contract ISuperToken", "name": "", "type": "address"},
            {"internalType": "address", "name": "", "type": "address"},
            {"internalType": "bytes32", "name": "", "type": "bytes32"},
            {"internalType": "bytes", "name": "", "type": "bytes"},
            {"internalType": "bytes", "name": "", "type": "bytes"},
        ],
        "name": "beforeAgreementTerminated",
        "outputs": [{"internalType": "bytes", "name": "", "type": "bytes"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "contract ISuperToken", "name": "", "type": "address"},
            {"internalType": "address", "name": "", "type": "address"},
            {"internalType": "bytes32", "name": "", "type": "bytes32"},
            {"internalType": "bytes", "name": "", "type": "bytes"},
            {"internalType": "bytes", "name": "", "type": "bytes"},
        ],
        "name": "beforeAgreementUpdated",
        "outputs": [{"internalType": "bytes", "name": "", "type": "bytes"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "streamer", "type": "address"}],
        "name": "closeStream",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "distribute",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "streamer", "type": "address"}],
        "name": "emergencyCloseStream",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_requestId", "type": "uint256"}
        ],
        "name": "getCurrentValue",
        "outputs": [
            {"internalType": "bool", "name": "ifRetrieve", "type": "bool"},
            {"internalType": "uint256", "name": "value", "type": "uint256"},
            {
                "internalType": "uint256",
                "name": "_timestampRetrieved",
                "type": "uint256",
            },
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_requestId", "type": "uint256"},
            {"internalType": "uint256", "name": "_timestamp", "type": "uint256"},
        ],
        "name": "getDataBefore",
        "outputs": [
            {"internalType": "bool", "name": "_ifRetrieve", "type": "bool"},
            {"internalType": "uint256", "name": "_value", "type": "uint256"},
            {
                "internalType": "uint256",
                "name": "_timestampRetrieved",
                "type": "uint256",
            },
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getFeeRate",
        "outputs": [{"internalType": "uint128", "name": "", "type": "uint128"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint32", "name": "index", "type": "uint32"},
            {"internalType": "address", "name": "streamer", "type": "address"},
        ],
        "name": "getIDAShares",
        "outputs": [
            {"internalType": "bool", "name": "exist", "type": "bool"},
            {"internalType": "bool", "name": "approved", "type": "bool"},
            {"internalType": "uint128", "name": "units", "type": "uint128"},
            {
                "internalType": "uint256",
                "name": "pendingDistribution",
                "type": "uint256",
            },
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_requestId", "type": "uint256"},
            {"internalType": "uint256", "name": "_timestamp", "type": "uint256"},
        ],
        "name": "getIndexForDataBefore",
        "outputs": [
            {"internalType": "bool", "name": "found", "type": "bool"},
            {"internalType": "uint256", "name": "index", "type": "uint256"},
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getInputToken",
        "outputs": [
            {"internalType": "contract ISuperToken", "name": "", "type": "address"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getLastDistributionAt",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_requestId", "type": "uint256"}
        ],
        "name": "getNewValueCountbyRequestId",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getOuputIndexId",
        "outputs": [{"internalType": "uint32", "name": "", "type": "uint32"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getOuputToken",
        "outputs": [
            {"internalType": "contract ISuperToken", "name": "", "type": "address"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getOwner",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getRateTolerance",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getRequestId",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "streamer", "type": "address"}],
        "name": "getStreamRate",
        "outputs": [{"internalType": "int96", "name": "", "type": "int96"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getSubsidyIndexId",
        "outputs": [{"internalType": "uint32", "name": "", "type": "uint32"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getSubsidyRate",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getSubsidyToken",
        "outputs": [
            {"internalType": "contract ISuperToken", "name": "", "type": "address"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getSushiRouter",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getTellorOracle",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_requestId", "type": "uint256"},
            {"internalType": "uint256", "name": "_index", "type": "uint256"},
        ],
        "name": "getTimestampbyRequestIDandIndex",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getTotalInflow",
        "outputs": [{"internalType": "int96", "name": "", "type": "int96"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "isAppJailed",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_requestId", "type": "uint256"},
            {"internalType": "uint256", "name": "_timestamp", "type": "uint256"},
        ],
        "name": "isInDispute",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "owner",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "renounceOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_requestId", "type": "uint256"},
            {"internalType": "uint256", "name": "_timestamp", "type": "uint256"},
        ],
        "name": "retrieveData",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint128", "name": "feeRate", "type": "uint128"}],
        "name": "setFeeRate",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "oracle", "type": "address"}],
        "name": "setOracle",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint128", "name": "rateTolerance", "type": "uint128"}
        ],
        "name": "setRateTolerance",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "requestId", "type": "uint256"}],
        "name": "setRequestId",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint128", "name": "subsidyRate", "type": "uint128"}
        ],
        "name": "setSubsidyRate",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "newOwner", "type": "address"}],
        "name": "transferOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
]
"""


SHARE_PRICE_ABI = """
[
    {
        "inputs": [],
        "name": "getSharePrice",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    }
]
"""


SUBMIT_VALUE_ABI = """[{
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_requestId",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_value",
          "type": "uint256"
        }
      ],
      "name": "submitValue",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    }]"""


SUPERTOKEN_ABI = """
[
    {
        "inputs": [
            {"internalType": "contract ISuperfluid", "name": "host", "type": "address"}
        ],
        "stateMutability": "nonpayable",
        "type": "constructor",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "agreementClass",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "account",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "bytes",
                "name": "state",
                "type": "bytes",
            },
        ],
        "name": "AgreementAccountStateUpdated",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "agreementClass",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "bytes32",
                "name": "id",
                "type": "bytes32",
            },
            {
                "indexed": false,
                "internalType": "bytes32[]",
                "name": "data",
                "type": "bytes32[]",
            },
        ],
        "name": "AgreementCreated",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "agreementClass",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "bytes32",
                "name": "id",
                "type": "bytes32",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "penaltyAccount",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "rewardAccount",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "rewardAmount",
                "type": "uint256",
            },
        ],
        "name": "AgreementLiquidated",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "liquidatorAccount",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "agreementClass",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "bytes32",
                "name": "id",
                "type": "bytes32",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "penaltyAccount",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "bondAccount",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "rewardAmount",
                "type": "uint256",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "bailoutAmount",
                "type": "uint256",
            },
        ],
        "name": "AgreementLiquidatedBy",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "agreementClass",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "account",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "slotId",
                "type": "uint256",
            },
        ],
        "name": "AgreementStateUpdated",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "agreementClass",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "bytes32",
                "name": "id",
                "type": "bytes32",
            },
        ],
        "name": "AgreementTerminated",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "agreementClass",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "bytes32",
                "name": "id",
                "type": "bytes32",
            },
            {
                "indexed": false,
                "internalType": "bytes32[]",
                "name": "data",
                "type": "bytes32[]",
            },
        ],
        "name": "AgreementUpdated",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "owner",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "spender",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "value",
                "type": "uint256",
            },
        ],
        "name": "Approval",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "operator",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "tokenHolder",
                "type": "address",
            },
        ],
        "name": "AuthorizedOperator",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "bailoutAccount",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "bailoutAmount",
                "type": "uint256",
            },
        ],
        "name": "Bailout",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "operator",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "from",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256",
            },
            {
                "indexed": false,
                "internalType": "bytes",
                "name": "data",
                "type": "bytes",
            },
            {
                "indexed": false,
                "internalType": "bytes",
                "name": "operatorData",
                "type": "bytes",
            },
        ],
        "name": "Burned",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "bytes32",
                "name": "uuid",
                "type": "bytes32",
            },
            {
                "indexed": false,
                "internalType": "address",
                "name": "codeAddress",
                "type": "address",
            },
        ],
        "name": "CodeUpdated",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "operator",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "to",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256",
            },
            {
                "indexed": false,
                "internalType": "bytes",
                "name": "data",
                "type": "bytes",
            },
            {
                "indexed": false,
                "internalType": "bytes",
                "name": "operatorData",
                "type": "bytes",
            },
        ],
        "name": "Minted",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "operator",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "tokenHolder",
                "type": "address",
            },
        ],
        "name": "RevokedOperator",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "operator",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "from",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "to",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256",
            },
            {
                "indexed": false,
                "internalType": "bytes",
                "name": "data",
                "type": "bytes",
            },
            {
                "indexed": false,
                "internalType": "bytes",
                "name": "operatorData",
                "type": "bytes",
            },
        ],
        "name": "Sent",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "account",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256",
            },
        ],
        "name": "TokenDowngraded",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "account",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256",
            },
        ],
        "name": "TokenUpgraded",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "from",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "to",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "value",
                "type": "uint256",
            },
        ],
        "name": "Transfer",
        "type": "event",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "account", "type": "address"},
            {"internalType": "address", "name": "spender", "type": "address"},
        ],
        "name": "allowance",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "spender", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
        ],
        "name": "approve",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "operator", "type": "address"}],
        "name": "authorizeOperator",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "account", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"internalType": "uint256", "name": "balance", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
            {"internalType": "bytes", "name": "data", "type": "bytes"},
        ],
        "name": "burn",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "bytes32", "name": "id", "type": "bytes32"},
            {"internalType": "bytes32[]", "name": "data", "type": "bytes32[]"},
        ],
        "name": "createAgreement",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "decimals",
        "outputs": [{"internalType": "uint8", "name": "", "type": "uint8"}],
        "stateMutability": "pure",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "spender", "type": "address"},
            {"internalType": "uint256", "name": "subtractedValue", "type": "uint256"},
        ],
        "name": "decreaseAllowance",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "defaultOperators",
        "outputs": [{"internalType": "address[]", "name": "", "type": "address[]"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "amount", "type": "uint256"}],
        "name": "downgrade",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "account", "type": "address"}],
        "name": "getAccountActiveAgreements",
        "outputs": [
            {
                "internalType": "contract ISuperAgreement[]",
                "name": "",
                "type": "address[]",
            }
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "agreementClass", "type": "address"},
            {"internalType": "bytes32", "name": "id", "type": "bytes32"},
            {"internalType": "uint256", "name": "dataLength", "type": "uint256"},
        ],
        "name": "getAgreementData",
        "outputs": [{"internalType": "bytes32[]", "name": "data", "type": "bytes32[]"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "agreementClass", "type": "address"},
            {"internalType": "address", "name": "account", "type": "address"},
            {"internalType": "uint256", "name": "slotId", "type": "uint256"},
            {"internalType": "uint256", "name": "dataLength", "type": "uint256"},
        ],
        "name": "getAgreementStateSlot",
        "outputs": [
            {"internalType": "bytes32[]", "name": "slotData", "type": "bytes32[]"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getCodeAddress",
        "outputs": [
            {"internalType": "address", "name": "codeAddress", "type": "address"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getHost",
        "outputs": [{"internalType": "address", "name": "host", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getUnderlyingToken",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "granularity",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "pure",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "spender", "type": "address"},
            {"internalType": "uint256", "name": "addedValue", "type": "uint256"},
        ],
        "name": "increaseAllowance",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "internalType": "contract IERC20",
                "name": "underlyingToken",
                "type": "address",
            },
            {"internalType": "uint8", "name": "underlyingDecimals", "type": "uint8"},
            {"internalType": "string", "name": "n", "type": "string"},
            {"internalType": "string", "name": "s", "type": "string"},
        ],
        "name": "initialize",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "account", "type": "address"},
            {"internalType": "uint256", "name": "timestamp", "type": "uint256"},
        ],
        "name": "isAccountCritical",
        "outputs": [{"internalType": "bool", "name": "isCritical", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "account", "type": "address"}],
        "name": "isAccountCriticalNow",
        "outputs": [{"internalType": "bool", "name": "isCritical", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "account", "type": "address"},
            {"internalType": "uint256", "name": "timestamp", "type": "uint256"},
        ],
        "name": "isAccountSolvent",
        "outputs": [{"internalType": "bool", "name": "isSolvent", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "account", "type": "address"}],
        "name": "isAccountSolventNow",
        "outputs": [{"internalType": "bool", "name": "isSolvent", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "operator", "type": "address"},
            {"internalType": "address", "name": "tokenHolder", "type": "address"},
        ],
        "name": "isOperatorFor",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "bytes32", "name": "id", "type": "bytes32"},
            {"internalType": "address", "name": "liquidator", "type": "address"},
            {"internalType": "address", "name": "penaltyAccount", "type": "address"},
            {"internalType": "uint256", "name": "rewardAmount", "type": "uint256"},
            {"internalType": "uint256", "name": "bailoutAmount", "type": "uint256"},
        ],
        "name": "makeLiquidationPayouts",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "name",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "account", "type": "address"},
            {"internalType": "address", "name": "spender", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
        ],
        "name": "operationApprove",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "account", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
        ],
        "name": "operationDowngrade",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "account", "type": "address"},
            {"internalType": "address", "name": "spender", "type": "address"},
            {"internalType": "address", "name": "recipient", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
        ],
        "name": "operationTransferFrom",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "account", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
        ],
        "name": "operationUpgrade",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "account", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
            {"internalType": "bytes", "name": "data", "type": "bytes"},
            {"internalType": "bytes", "name": "operatorData", "type": "bytes"},
        ],
        "name": "operatorBurn",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "sender", "type": "address"},
            {"internalType": "address", "name": "recipient", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
            {"internalType": "bytes", "name": "data", "type": "bytes"},
            {"internalType": "bytes", "name": "operatorData", "type": "bytes"},
        ],
        "name": "operatorSend",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "proxiableUUID",
        "outputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}],
        "stateMutability": "pure",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "account", "type": "address"},
            {"internalType": "uint256", "name": "timestamp", "type": "uint256"},
        ],
        "name": "realtimeBalanceOf",
        "outputs": [
            {"internalType": "int256", "name": "availableBalance", "type": "int256"},
            {"internalType": "uint256", "name": "deposit", "type": "uint256"},
            {"internalType": "uint256", "name": "owedDeposit", "type": "uint256"},
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "account", "type": "address"}],
        "name": "realtimeBalanceOfNow",
        "outputs": [
            {"internalType": "int256", "name": "availableBalance", "type": "int256"},
            {"internalType": "uint256", "name": "deposit", "type": "uint256"},
            {"internalType": "uint256", "name": "owedDeposit", "type": "uint256"},
            {"internalType": "uint256", "name": "timestamp", "type": "uint256"},
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "operator", "type": "address"}],
        "name": "revokeOperator",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "account", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
            {"internalType": "bytes", "name": "userData", "type": "bytes"},
        ],
        "name": "selfBurn",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "account", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
            {"internalType": "bytes", "name": "userData", "type": "bytes"},
        ],
        "name": "selfMint",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "recipient", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
            {"internalType": "bytes", "name": "data", "type": "bytes"},
        ],
        "name": "send",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "account", "type": "address"},
            {"internalType": "int256", "name": "delta", "type": "int256"},
        ],
        "name": "settleBalance",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "symbol",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "bytes32", "name": "id", "type": "bytes32"},
            {"internalType": "uint256", "name": "dataLength", "type": "uint256"},
        ],
        "name": "terminateAgreement",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "totalSupply",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "recipient", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
        ],
        "name": "transfer",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "recipient", "type": "address"}],
        "name": "transferAll",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "holder", "type": "address"},
            {"internalType": "address", "name": "recipient", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
        ],
        "name": "transferFrom",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "bytes32", "name": "id", "type": "bytes32"},
            {"internalType": "bytes32[]", "name": "data", "type": "bytes32[]"},
        ],
        "name": "updateAgreementData",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "account", "type": "address"},
            {"internalType": "uint256", "name": "slotId", "type": "uint256"},
            {"internalType": "bytes32[]", "name": "slotData", "type": "bytes32[]"},
        ],
        "name": "updateAgreementStateSlot",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "newAddress", "type": "address"}
        ],
        "name": "updateCode",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "amount", "type": "uint256"}],
        "name": "upgrade",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
            {"internalType": "bytes", "name": "data", "type": "bytes"},
        ],
        "name": "upgradeTo",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
]
"""



SWAP_ABI = """[{
    "inputs":[
        {"internalType":"uint256","name":"amountIn","type":"uint256"},
        {"internalType":"uint256","name":"amountOutMin","type":"uint256"},
        {"internalType":"address[]","name":"path","type":"address[]"},
        {"internalType":"address","name":"to","type":"address"},
        {"internalType":"uint256","name":"deadline","type":"uint256"}
    ],
    "name":"swapExactTokensForETH",
    "outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],
    "stateMutability":"nonpayable","type":"function"
}]"""

TELLOR_ABI = """[
  {
    "constant": false,
    "inputs": [
      {
        "name": "_address",
        "type": "address"
      },
      {
        "name": "_amount",
        "type": "uint256"
      }
    ],
    "name": "theLazyCoon",
    "outputs": [],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "uint256",
        "name": "_disputeId",
        "type": "uint256"
      },
      {
        "indexed": true,
        "internalType": "uint256",
        "name": "_requestId",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "_timestamp",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "address",
        "name": "_miner",
        "type": "address"
      }
    ],
    "name": "NewDispute",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "uint256",
        "name": "_disputeID",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "bool",
        "name": "_position",
        "type": "bool"
      },
      {
        "indexed": true,
        "internalType": "address",
        "name": "_voter",
        "type": "address"
      }
    ],
    "name": "Voted",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "uint256",
        "name": "_disputeID",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "int256",
        "name": "_result",
        "type": "int256"
      },
      {
        "indexed": true,
        "internalType": "address",
        "name": "_reportedMiner",
        "type": "address"
      },
      {
        "indexed": false,
        "internalType": "address",
        "name": "_reportingParty",
        "type": "address"
      },
      {
        "indexed": false,
        "internalType": "bool",
        "name": "_active",
        "type": "bool"
      }
    ],
    "name": "DisputeVoteTallied",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": false,
        "internalType": "address",
        "name": "_newTellor",
        "type": "address"
      }
    ],
    "name": "NewTellorAddress",
    "type": "event"
  },
  {
    "constant": true,
    "inputs": [
      {
        "internalType": "uint256",
        "name": "_timestamp",
        "type": "uint256"
      }
    ],
    "name": "getRequestIdByTimestamp",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [
      {
        "internalType": "uint256",
        "name": "_requestId",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "_timestamp",
        "type": "uint256"
      }
    ],
    "name": "getSubmissionsByTimestamp",
    "outputs": [
      {
        "internalType": "uint256[5]",
        "name": "",
        "type": "uint256[5]"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [
      {
        "internalType": "bytes32",
        "name": "_data",
        "type": "bytes32"
      }
    ],
    "name": "getAddressVars",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [],
    "name": "getSymbol",
    "outputs": [
      {
        "internalType": "string",
        "name": "",
        "type": "string"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [],
    "name": "getName",
    "outputs": [
      {
        "internalType": "string",
        "name": "",
        "type": "string"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [],
    "name": "totalSupply",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [],
    "name": "getVariablesOnDeck",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      },
      {
        "internalType": "string",
        "name": "",
        "type": "string"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [
      {
        "internalType": "bytes32",
        "name": "_request",
        "type": "bytes32"
      }
    ],
    "name": "getRequestIdByQueryHash",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [
      {
        "internalType": "uint256",
        "name": "_requestId",
        "type": "uint256"
      }
    ],
    "name": "getLastNewValueById",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      },
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [
      {
        "internalType": "uint256",
        "name": "_requestId",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "_timestamp",
        "type": "uint256"
      }
    ],
    "name": "isInDispute",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [
      {
        "internalType": "uint256",
        "name": "_requestId",
        "type": "uint256"
      }
    ],
    "name": "getNewValueCountbyRequestId",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [
      {
        "internalType": "address",
        "name": "_user",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "_blockNumber",
        "type": "uint256"
      }
    ],
    "name": "balanceOfAt",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [
      {
        "internalType": "bytes32",
        "name": "_data",
        "type": "bytes32"
      }
    ],
    "name": "getUintVar",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [
      {
        "internalType": "uint256",
        "name": "_index",
        "type": "uint256"
      }
    ],
    "name": "getRequestIdByRequestQIndex",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [
      {
        "internalType": "bytes32",
        "name": "_challenge",
        "type": "bytes32"
      },
      {
        "internalType": "address",
        "name": "_miner",
        "type": "address"
      }
    ],
    "name": "didMine",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [
      {
        "internalType": "uint256",
        "name": "_requestId",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "_timestamp",
        "type": "uint256"
      }
    ],
    "name": "getMinersByRequestIdAndTimestamp",
    "outputs": [
      {
        "internalType": "address[5]",
        "name": "",
        "type": "address[5]"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [
      {
        "internalType": "address",
        "name": "_user",
        "type": "address"
      }
    ],
    "name": "balanceOf",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [
      {
        "internalType": "address",
        "name": "_staker",
        "type": "address"
      }
    ],
    "name": "getStakerInfo",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [
      {
        "internalType": "uint256",
        "name": "_requestID",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "_index",
        "type": "uint256"
      }
    ],
    "name": "getTimestampbyRequestIDandIndex",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [
      {
        "internalType": "uint256",
        "name": "_disputeId",
        "type": "uint256"
      },
      {
        "internalType": "bytes32",
        "name": "_data",
        "type": "bytes32"
      }
    ],
    "name": "getDisputeUintVars",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [
      {
        "internalType": "uint256",
        "name": "_requestId",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "_timestamp",
        "type": "uint256"
      }
    ],
    "name": "retrieveData",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [
      {
        "internalType": "address",
        "name": "_user",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "_amount",
        "type": "uint256"
      }
    ],
    "name": "allowedToTrade",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [],
    "name": "getCurrentVariables",
    "outputs": [
      {
        "internalType": "bytes32",
        "name": "",
        "type": "bytes32"
      },
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      },
      {
        "internalType": "string",
        "name": "",
        "type": "string"
      },
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [
      {
        "internalType": "uint256",
        "name": "_disputeId",
        "type": "uint256"
      },
      {
        "internalType": "address",
        "name": "_address",
        "type": "address"
      }
    ],
    "name": "didVote",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [
      {
        "internalType": "uint256",
        "name": "_disputeId",
        "type": "uint256"
      }
    ],
    "name": "getAllDisputeVars",
    "outputs": [
      {
        "internalType": "bytes32",
        "name": "",
        "type": "bytes32"
      },
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      },
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      },
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      },
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      },
      {
        "internalType": "uint256[9]",
        "name": "",
        "type": "uint256[9]"
      },
      {
        "internalType": "int256",
        "name": "",
        "type": "int256"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [],
    "name": "getRequestQ",
    "outputs": [
      {
        "internalType": "uint256[51]",
        "name": "",
        "type": "uint256[51]"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [
      {
        "internalType": "uint256",
        "name": "_requestId",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "_timestamp",
        "type": "uint256"
      }
    ],
    "name": "getMinedBlockNum",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [
      {
        "internalType": "bytes32",
        "name": "_hash",
        "type": "bytes32"
      }
    ],
    "name": "getDisputeIdByDisputeHash",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [
      {
        "internalType": "address",
        "name": "_user",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "_spender",
        "type": "address"
      }
    ],
    "name": "allowance",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [
      {
        "internalType": "uint256",
        "name": "_requestId",
        "type": "uint256"
      },
      {
        "internalType": "bytes32",
        "name": "_data",
        "type": "bytes32"
      }
    ],
    "name": "getRequestUintVars",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [
      {
        "internalType": "uint256",
        "name": "_requestId",
        "type": "uint256"
      }
    ],
    "name": "getRequestVars",
    "outputs": [
      {
        "internalType": "string",
        "name": "",
        "type": "string"
      },
      {
        "internalType": "string",
        "name": "",
        "type": "string"
      },
      {
        "internalType": "bytes32",
        "name": "",
        "type": "bytes32"
      },
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [],
    "name": "getLastNewValue",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      },
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [
      {
        "internalType": "address",
        "name": "_newDeity",
        "type": "address"
      }
    ],
    "name": "changeDeity",
    "outputs": [],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [
      {
        "internalType": "address",
        "name": "_tellorContract",
        "type": "address"
      }
    ],
    "name": "changeTellorContract",
    "outputs": [],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "_tellorContract",
        "type": "address"
      }
    ],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "constructor"
  },
  {
    "payable": true,
    "stateMutability": "payable",
    "type": "fallback"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "address",
        "name": "_sender",
        "type": "address"
      }
    ],
    "name": "NewStake",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "address",
        "name": "_sender",
        "type": "address"
      }
    ],
    "name": "StakeWithdrawn",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "address",
        "name": "_sender",
        "type": "address"
      }
    ],
    "name": "StakeWithdrawRequested",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "address",
        "name": "_owner",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "address",
        "name": "_spender",
        "type": "address"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "_value",
        "type": "uint256"
      }
    ],
    "name": "Approval",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "address",
        "name": "_from",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "address",
        "name": "_to",
        "type": "address"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "_value",
        "type": "uint256"
      }
    ],
    "name": "Transfer",
    "type": "event"
  },
  {
    "constant": true,
    "inputs": [],
    "name": "name",
    "outputs": [
      {
        "internalType": "string",
        "name": "",
        "type": "string"
      }
    ],
    "payable": false,
    "stateMutability": "pure",
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [
      {
        "internalType": "address",
        "name": "_spender",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "_amount",
        "type": "uint256"
      }
    ],
    "name": "approve",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [],
    "name": "depositStake",
    "outputs": [],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [
      {
        "internalType": "address",
        "name": "_from",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "_to",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "_amount",
        "type": "uint256"
      }
    ],
    "name": "transferFrom",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [
      {
        "internalType": "address",
        "name": "_propNewTellorAddress",
        "type": "address"
      }
    ],
    "name": "proposeFork",
    "outputs": [],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [],
    "name": "requestStakingWithdraw",
    "outputs": [],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [],
    "name": "decimals",
    "outputs": [
      {
        "internalType": "uint8",
        "name": "",
        "type": "uint8"
      }
    ],
    "payable": false,
    "stateMutability": "pure",
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [
      {
        "internalType": "string",
        "name": "_c_sapi",
        "type": "string"
      },
      {
        "internalType": "string",
        "name": "_c_symbol",
        "type": "string"
      },
      {
        "internalType": "uint256",
        "name": "_granularity",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "_tip",
        "type": "uint256"
      }
    ],
    "name": "requestData",
    "outputs": [],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [
      {
        "internalType": "uint256",
        "name": "_disputeId",
        "type": "uint256"
      }
    ],
    "name": "tallyVotes",
    "outputs": [],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [],
    "name": "claimOwnership",
    "outputs": [],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [
      {
        "internalType": "string",
        "name": "_nonce",
        "type": "string"
      },
      {
        "internalType": "uint256",
        "name": "_requestId",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "_value",
        "type": "uint256"
      }
    ],
    "name": "submitMiningSolution",
    "outputs": [],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [
      {
        "internalType": "address payable",
        "name": "_pendingOwner",
        "type": "address"
      }
    ],
    "name": "proposeOwnership",
    "outputs": [],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [
      {
        "internalType": "uint256",
        "name": "_requestId",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "_tip",
        "type": "uint256"
      }
    ],
    "name": "addTip",
    "outputs": [],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [
      {
        "internalType": "uint256",
        "name": "_requestId",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "_timestamp",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "_minerIndex",
        "type": "uint256"
      }
    ],
    "name": "beginDispute",
    "outputs": [],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [],
    "name": "symbol",
    "outputs": [
      {
        "internalType": "string",
        "name": "",
        "type": "string"
      }
    ],
    "payable": false,
    "stateMutability": "pure",
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [
      {
        "internalType": "address",
        "name": "_to",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "_amount",
        "type": "uint256"
      }
    ],
    "name": "transfer",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [],
    "name": "withdrawStake",
    "outputs": [],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [
      {
        "internalType": "uint256",
        "name": "_disputeId",
        "type": "uint256"
      },
      {
        "internalType": "bool",
        "name": "_supportsDispute",
        "type": "bool"
      }
    ],
    "name": "vote",
    "outputs": [],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "address",
        "name": "_sender",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "uint256",
        "name": "_requestId",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "_tip",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "_totalTips",
        "type": "uint256"
      }
    ],
    "name": "TipAdded",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "address",
        "name": "_sender",
        "type": "address"
      },
      {
        "indexed": false,
        "internalType": "string",
        "name": "_query",
        "type": "string"
      },
      {
        "indexed": false,
        "internalType": "string",
        "name": "_querySymbol",
        "type": "string"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "_granularity",
        "type": "uint256"
      },
      {
        "indexed": true,
        "internalType": "uint256",
        "name": "_requestId",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "_totalTips",
        "type": "uint256"
      }
    ],
    "name": "DataRequested",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": false,
        "internalType": "bytes32",
        "name": "_currentChallenge",
        "type": "bytes32"
      },
      {
        "indexed": true,
        "internalType": "uint256",
        "name": "_currentRequestId",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "_difficulty",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "_multiplier",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "string",
        "name": "_query",
        "type": "string"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "_totalTips",
        "type": "uint256"
      }
    ],
    "name": "NewChallenge",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "uint256",
        "name": "_requestId",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "string",
        "name": "_query",
        "type": "string"
      },
      {
        "indexed": false,
        "internalType": "bytes32",
        "name": "_onDeckQueryHash",
        "type": "bytes32"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "_onDeckTotalTips",
        "type": "uint256"
      }
    ],
    "name": "NewRequestOnDeck",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "uint256",
        "name": "_requestId",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "_time",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "_value",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "_totalTips",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "bytes32",
        "name": "_currentChallenge",
        "type": "bytes32"
      }
    ],
    "name": "NewValue",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "address",
        "name": "_miner",
        "type": "address"
      },
      {
        "indexed": false,
        "internalType": "string",
        "name": "_nonce",
        "type": "string"
      },
      {
        "indexed": true,
        "internalType": "uint256",
        "name": "_requestId",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "_value",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "bytes32",
        "name": "_currentChallenge",
        "type": "bytes32"
      }
    ],
    "name": "NonceSubmitted",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "address",
        "name": "_previousOwner",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "address",
        "name": "_newOwner",
        "type": "address"
      }
    ],
    "name": "OwnershipTransferred",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "address",
        "name": "_previousOwner",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "address",
        "name": "_newOwner",
        "type": "address"
      }
    ],
    "name": "OwnershipProposed",
    "type": "event"
  }
]"""
