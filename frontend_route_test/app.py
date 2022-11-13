from flask import Flask

api = Flask(__name__)

@api.route('/courselist')
def courselist():
    return {
        "48496": {
            "cCode": "ACCT I S 100",
            "cCredits": "3 credits",
            "cDescription": "Examines generally accepted accounting principles for measurement and reporting of financial information in a balance sheet, income statement, and statement of cash flows; introduction to analysis and interpretation of financial accounting data for decision-making purposes.",
            "cName": "INTRODUCTORY FINANCIAL ACCOUNTING",
            "cReq": "Requisites: Not open to students with credit for ACCTIS300",
            "cSubject": "Accounting and Information Systems",
            "cUID": 48496
        },
        "48497": {
            "cCode": "ACCT I S 211",
            "cCredits": "3 credits",
            "cDescription": "Managerial accounting concepts relevant for decision-making; use of accounting information for planning, decision-making, and control of business operations in various management and business environments.",
            "cName": "INTRODUCTORY MANAGERIAL ACCOUNTING",
            "cReq": "Requisites: ACCTIS100 or declared in undergraduate Business Exchange program",
            "cSubject": "Accounting and Information Systems",
            "cUID": 48497
        },
        "48498": {
            "cCode": "ACCT I S 300",
            "cCredits": "3 credits",
            "cDescription": "Examines both financial and managerial accounting for business decisions. Emphasizes preparation and interpretation of financial statements, analysis of financial information, determination of costs for products and services, and use of accounting information for planning and control of business operations.",
            "cName": "ACCOUNTING PRINCIPLES",
            "cReq": "Requisites: Satisfied Quantitative Reasoning (QR) A requirement. Not open to students with credit for ACCTIS100.",
            "cSubject": "Accounting and Information Systems",
            "cUID": 48498
        }
    }

@api.route('/graphDistribution/48496')
def courselist():
    return {
    "courseOfferings": [
        {
            "cumulative": {
                "aCount": 112,
                "abCount": 52,
                "bCount": 124,
                "bcCount": 37,
                "cCount": 38,
                "crCount": 0,
                "dCount": 13,
                "fCount": 10,
                "iCount": 5,
                "nCount": 0,
                "nrCount": 0,
                "nwCount": 1,
                "otherCount": 0,
                "pCount": 0,
                "sCount": 0,
                "total": 392,
                "uCount": 0
            },
            "sections": [
                {
                    "aCount": 33,
                    "abCount": 19,
                    "bCount": 61,
                    "bcCount": 15,
                    "cCount": 26,
                    "crCount": 0,
                    "dCount": 4,
                    "fCount": 0,
                    "iCount": 0,
                    "instructors": [
                        {
                            "id": 2601579,
                            "name": "ERIC BACH"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 0,
                    "nwCount": 1,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 0,
                    "sectionNumber": 1,
                    "total": 159,
                    "uCount": 0
                },
                {
                    "aCount": 49,
                    "abCount": 30,
                    "bCount": 60,
                    "bcCount": 22,
                    "cCount": 12,
                    "crCount": 0,
                    "dCount": 9,
                    "fCount": 10,
                    "iCount": 5,
                    "instructors": [
                        {
                            "id": 6043085,
                            "name": "MARC RENAULT"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 0,
                    "nwCount": 0,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 0,
                    "sectionNumber": 2,
                    "total": 197,
                    "uCount": 0
                },
                {
                    "aCount": 30,
                    "abCount": 3,
                    "bCount": 3,
                    "bcCount": 0,
                    "cCount": 0,
                    "crCount": 0,
                    "dCount": 0,
                    "fCount": 0,
                    "iCount": 0,
                    "instructors": [
                        {
                            "id": 3382449,
                            "name": "DIETER VAN MELKEBEEK"
                        },
                        {
                            "id": 6218829,
                            "name": "X / NICOLLAS MOCELIN SDROIEVSKI"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 0,
                    "nwCount": 0,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 0,
                    "sectionNumber": 3,
                    "total": 36,
                    "uCount": 0
                }
            ],
            "termCode": 1222
        },
        {
            "cumulative": {
                "aCount": 62,
                "abCount": 63,
                "bCount": 95,
                "bcCount": 67,
                "cCount": 49,
                "crCount": 0,
                "dCount": 9,
                "fCount": 8,
                "iCount": 0,
                "nCount": 0,
                "nrCount": 1,
                "nwCount": 0,
                "otherCount": 0,
                "pCount": 0,
                "sCount": 1,
                "total": 355,
                "uCount": 0
            },
            "sections": [
                {
                    "aCount": 27,
                    "abCount": 28,
                    "bCount": 51,
                    "bcCount": 32,
                    "cCount": 27,
                    "crCount": 0,
                    "dCount": 4,
                    "fCount": 7,
                    "iCount": 0,
                    "instructors": [
                        {
                            "id": 3085603,
                            "name": "JIN-YI CAI"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 1,
                    "nwCount": 0,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 0,
                    "sectionNumber": 1,
                    "total": 177,
                    "uCount": 0
                },
                {
                    "aCount": 35,
                    "abCount": 35,
                    "bCount": 44,
                    "bcCount": 35,
                    "cCount": 22,
                    "crCount": 0,
                    "dCount": 5,
                    "fCount": 1,
                    "iCount": 0,
                    "instructors": [
                        {
                            "id": 3382449,
                            "name": "DIETER VAN MELKEBEEK"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 0,
                    "nwCount": 0,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 1,
                    "sectionNumber": 2,
                    "total": 178,
                    "uCount": 0
                }
            ],
            "termCode": 1212
        },
        {
            "cumulative": {
                "aCount": 184,
                "abCount": 48,
                "bCount": 106,
                "bcCount": 12,
                "cCount": 5,
                "crCount": 0,
                "dCount": 3,
                "fCount": 0,
                "iCount": 0,
                "nCount": 0,
                "nrCount": 0,
                "nwCount": 0,
                "otherCount": 0,
                "pCount": 0,
                "sCount": 59,
                "total": 426,
                "uCount": 9
            },
            "sections": [
                {
                    "aCount": 114,
                    "abCount": 25,
                    "bCount": 44,
                    "bcCount": 5,
                    "cCount": 1,
                    "crCount": 0,
                    "dCount": 0,
                    "fCount": 0,
                    "iCount": 0,
                    "instructors": [
                        {
                            "id": 4195806,
                            "name": "SHUCHI CHAWLA"
                        },
                        {
                            "id": 5911784,
                            "name": "X / YUXIN SUN"
                        },
                        {
                            "id": 6217789,
                            "name": "X / ROJIN REZVANSANGSARI"
                        },
                        {
                            "id": 6099944,
                            "name": "KEXIN LI"
                        },
                        {
                            "id": 6099078,
                            "name": "X / JEREMY MCMAHAN"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 0,
                    "nwCount": 0,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 25,
                    "sectionNumber": 1,
                    "total": 216,
                    "uCount": 2
                },
                {
                    "aCount": 55,
                    "abCount": 15,
                    "bCount": 57,
                    "bcCount": 2,
                    "cCount": 4,
                    "crCount": 0,
                    "dCount": 3,
                    "fCount": 0,
                    "iCount": 0,
                    "instructors": [
                        {
                            "id": 6088766,
                            "name": "X / EVANGELIA GERGATSOULI"
                        },
                        {
                            "id": 6088839,
                            "name": "X / VASILEIOS KONTONIS"
                        },
                        {
                            "id": 6211888,
                            "name": "X / JONG HO PARK"
                        },
                        {
                            "id": 6123269,
                            "name": "CHRISTOS TZAMOS"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 0,
                    "nwCount": 0,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 32,
                    "sectionNumber": 2,
                    "total": 171,
                    "uCount": 3
                },
                {
                    "aCount": 15,
                    "abCount": 8,
                    "bCount": 5,
                    "bcCount": 5,
                    "cCount": 0,
                    "crCount": 0,
                    "dCount": 0,
                    "fCount": 0,
                    "iCount": 0,
                    "instructors": [
                        {
                            "id": 6043085,
                            "name": "MARC RENAULT"
                        },
                        {
                            "id": 6210608,
                            "name": "X / HAILEY FIELDS"
                        },
                        {
                            "id": 5022570,
                            "name": "ALEXANDER BROOKS"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 0,
                    "nwCount": 0,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 2,
                    "sectionNumber": 3,
                    "total": 39,
                    "uCount": 4
                }
            ],
            "termCode": 1204
        },
        {
            "cumulative": {
                "aCount": 51,
                "abCount": 59,
                "bCount": 69,
                "bcCount": 54,
                "cCount": 42,
                "crCount": 0,
                "dCount": 5,
                "fCount": 10,
                "iCount": 1,
                "nCount": 0,
                "nrCount": 0,
                "nwCount": 1,
                "otherCount": 0,
                "pCount": 0,
                "sCount": 0,
                "total": 292,
                "uCount": 0
            },
            "sections": [
                {
                    "aCount": 20,
                    "abCount": 25,
                    "bCount": 31,
                    "bcCount": 12,
                    "cCount": 24,
                    "crCount": 0,
                    "dCount": 5,
                    "fCount": 7,
                    "iCount": 1,
                    "instructors": [
                        {
                            "id": 2601579,
                            "name": "ERIC BACH"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 0,
                    "nwCount": 0,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 0,
                    "sectionNumber": 1,
                    "total": 125,
                    "uCount": 0
                },
                {
                    "aCount": 31,
                    "abCount": 34,
                    "bCount": 38,
                    "bcCount": 42,
                    "cCount": 18,
                    "crCount": 0,
                    "dCount": 0,
                    "fCount": 3,
                    "iCount": 0,
                    "instructors": [
                        {
                            "id": 3382449,
                            "name": "DIETER VAN MELKEBEEK"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 0,
                    "nwCount": 1,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 0,
                    "sectionNumber": 2,
                    "total": 167,
                    "uCount": 0
                }
            ],
            "termCode": 1202
        },
        {
            "cumulative": {
                "aCount": 60,
                "abCount": 62,
                "bCount": 84,
                "bcCount": 90,
                "cCount": 36,
                "crCount": 0,
                "dCount": 1,
                "fCount": 2,
                "iCount": 1,
                "nCount": 0,
                "nrCount": 0,
                "nwCount": 0,
                "otherCount": 0,
                "pCount": 0,
                "sCount": 1,
                "total": 337,
                "uCount": 0
            },
            "sections": [
                {
                    "aCount": 60,
                    "abCount": 62,
                    "bCount": 84,
                    "bcCount": 90,
                    "cCount": 36,
                    "crCount": 0,
                    "dCount": 1,
                    "fCount": 2,
                    "iCount": 1,
                    "instructors": [
                        {
                            "id": 3382449,
                            "name": "DIETER VAN MELKEBEEK"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 0,
                    "nwCount": 0,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 1,
                    "sectionNumber": 1,
                    "total": 337,
                    "uCount": 0
                }
            ],
            "termCode": 1194
        },
        {
            "cumulative": {
                "aCount": 56,
                "abCount": 28,
                "bCount": 143,
                "bcCount": 57,
                "cCount": 19,
                "crCount": 0,
                "dCount": 2,
                "fCount": 7,
                "iCount": 0,
                "nCount": 0,
                "nrCount": 0,
                "nwCount": 0,
                "otherCount": 0,
                "pCount": 0,
                "sCount": 0,
                "total": 312,
                "uCount": 0
            },
            "sections": [
                {
                    "aCount": 41,
                    "abCount": 18,
                    "bCount": 101,
                    "bcCount": 34,
                    "cCount": 8,
                    "crCount": 0,
                    "dCount": 2,
                    "fCount": 4,
                    "iCount": 0,
                    "instructors": [
                        {
                            "id": 4195806,
                            "name": "SHUCHI CHAWLA"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 0,
                    "nwCount": 0,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 0,
                    "sectionNumber": 1,
                    "total": 208,
                    "uCount": 0
                },
                {
                    "aCount": 15,
                    "abCount": 10,
                    "bCount": 42,
                    "bcCount": 23,
                    "cCount": 11,
                    "crCount": 0,
                    "dCount": 0,
                    "fCount": 3,
                    "iCount": 0,
                    "instructors": [
                        {
                            "id": 6123269,
                            "name": "CHRISTOS TZAMOS"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 0,
                    "nwCount": 0,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 0,
                    "sectionNumber": 2,
                    "total": 104,
                    "uCount": 0
                }
            ],
            "termCode": 1192
        },
        {
            "cumulative": {
                "aCount": 60,
                "abCount": 43,
                "bCount": 174,
                "bcCount": 50,
                "cCount": 44,
                "crCount": 0,
                "dCount": 4,
                "fCount": 2,
                "iCount": 0,
                "nCount": 0,
                "nrCount": 0,
                "nwCount": 0,
                "otherCount": 0,
                "pCount": 0,
                "sCount": 0,
                "total": 377,
                "uCount": 0
            },
            "sections": [
                {
                    "aCount": 40,
                    "abCount": 23,
                    "bCount": 122,
                    "bcCount": 27,
                    "cCount": 27,
                    "crCount": 0,
                    "dCount": 3,
                    "fCount": 2,
                    "iCount": 0,
                    "instructors": [
                        {
                            "id": 4195806,
                            "name": "SHUCHI CHAWLA"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 0,
                    "nwCount": 0,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 0,
                    "sectionNumber": 1,
                    "total": 244,
                    "uCount": 0
                },
                {
                    "aCount": 20,
                    "abCount": 20,
                    "bCount": 52,
                    "bcCount": 23,
                    "cCount": 17,
                    "crCount": 0,
                    "dCount": 1,
                    "fCount": 0,
                    "iCount": 0,
                    "instructors": [
                        {
                            "id": 4151665,
                            "name": "BARIS AYDINLIOGLU"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 0,
                    "nwCount": 0,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 0,
                    "sectionNumber": 2,
                    "total": 133,
                    "uCount": 0
                }
            ],
            "termCode": 1184
        },
        {
            "cumulative": {
                "aCount": 22,
                "abCount": 33,
                "bCount": 46,
                "bcCount": 56,
                "cCount": 70,
                "crCount": 0,
                "dCount": 5,
                "fCount": 2,
                "iCount": 0,
                "nCount": 0,
                "nrCount": 0,
                "nwCount": 0,
                "otherCount": 0,
                "pCount": 0,
                "sCount": 0,
                "total": 234,
                "uCount": 0
            },
            "sections": [
                {
                    "aCount": 22,
                    "abCount": 33,
                    "bCount": 46,
                    "bcCount": 56,
                    "cCount": 70,
                    "crCount": 0,
                    "dCount": 5,
                    "fCount": 2,
                    "iCount": 0,
                    "instructors": [
                        {
                            "id": 3085603,
                            "name": "JIN-YI CAI"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 0,
                    "nwCount": 0,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 0,
                    "sectionNumber": 1,
                    "total": 234,
                    "uCount": 0
                }
            ],
            "termCode": 1182
        },
        {
            "cumulative": {
                "aCount": 36,
                "abCount": 31,
                "bCount": 118,
                "bcCount": 42,
                "cCount": 19,
                "crCount": 0,
                "dCount": 1,
                "fCount": 1,
                "iCount": 0,
                "nCount": 0,
                "nrCount": 0,
                "nwCount": 0,
                "otherCount": 0,
                "pCount": 0,
                "sCount": 1,
                "total": 249,
                "uCount": 0
            },
            "sections": [
                {
                    "aCount": 36,
                    "abCount": 31,
                    "bCount": 118,
                    "bcCount": 42,
                    "cCount": 19,
                    "crCount": 0,
                    "dCount": 1,
                    "fCount": 1,
                    "iCount": 0,
                    "instructors": [
                        {
                            "id": 4195806,
                            "name": "SHUCHI CHAWLA"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 0,
                    "nwCount": 0,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 1,
                    "sectionNumber": 1,
                    "total": 249,
                    "uCount": 0
                }
            ],
            "termCode": 1174
        },
        {
            "cumulative": {
                "aCount": 34,
                "abCount": 33,
                "bCount": 47,
                "bcCount": 40,
                "cCount": 17,
                "crCount": 0,
                "dCount": 7,
                "fCount": 1,
                "iCount": 0,
                "nCount": 0,
                "nrCount": 0,
                "nwCount": 1,
                "otherCount": 0,
                "pCount": 0,
                "sCount": 0,
                "total": 180,
                "uCount": 0
            },
            "sections": [
                {
                    "aCount": 19,
                    "abCount": 15,
                    "bCount": 25,
                    "bcCount": 27,
                    "cCount": 9,
                    "crCount": 0,
                    "dCount": 4,
                    "fCount": 0,
                    "iCount": 0,
                    "instructors": [
                        {
                            "id": 2601579,
                            "name": "ERIC BACH"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 0,
                    "nwCount": 1,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 0,
                    "sectionNumber": 1,
                    "total": 100,
                    "uCount": 0
                },
                {
                    "aCount": 15,
                    "abCount": 18,
                    "bCount": 22,
                    "bcCount": 13,
                    "cCount": 8,
                    "crCount": 0,
                    "dCount": 3,
                    "fCount": 1,
                    "iCount": 0,
                    "instructors": [
                        {
                            "id": 4151665,
                            "name": "BARIS AYDINLIOGLU"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 0,
                    "nwCount": 0,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 0,
                    "sectionNumber": 2,
                    "total": 80,
                    "uCount": 0
                }
            ],
            "termCode": 1172
        },
        {
            "cumulative": {
                "aCount": 38,
                "abCount": 19,
                "bCount": 71,
                "bcCount": 26,
                "cCount": 11,
                "crCount": 0,
                "dCount": 7,
                "fCount": 1,
                "iCount": 0,
                "nCount": 0,
                "nrCount": 0,
                "nwCount": 0,
                "otherCount": 0,
                "pCount": 0,
                "sCount": 0,
                "total": 173,
                "uCount": 0
            },
            "sections": [
                {
                    "aCount": 16,
                    "abCount": 5,
                    "bCount": 29,
                    "bcCount": 10,
                    "cCount": 5,
                    "crCount": 0,
                    "dCount": 3,
                    "fCount": 0,
                    "iCount": 0,
                    "instructors": [
                        {
                            "id": 2601579,
                            "name": "ERIC BACH"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 0,
                    "nwCount": 0,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 0,
                    "sectionNumber": 1,
                    "total": 68,
                    "uCount": 0
                },
                {
                    "aCount": 22,
                    "abCount": 14,
                    "bCount": 42,
                    "bcCount": 16,
                    "cCount": 6,
                    "crCount": 0,
                    "dCount": 4,
                    "fCount": 1,
                    "iCount": 0,
                    "instructors": [
                        {
                            "id": 4195806,
                            "name": "SHUCHI CHAWLA"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 0,
                    "nwCount": 0,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 0,
                    "sectionNumber": 2,
                    "total": 105,
                    "uCount": 0
                }
            ],
            "termCode": 1164
        },
        {
            "cumulative": {
                "aCount": 48,
                "abCount": 25,
                "bCount": 31,
                "bcCount": 33,
                "cCount": 35,
                "crCount": 0,
                "dCount": 5,
                "fCount": 0,
                "iCount": 0,
                "nCount": 0,
                "nrCount": 0,
                "nwCount": 0,
                "otherCount": 0,
                "pCount": 0,
                "sCount": 4,
                "total": 181,
                "uCount": 0
            },
            "sections": [
                {
                    "aCount": 27,
                    "abCount": 15,
                    "bCount": 12,
                    "bcCount": 15,
                    "cCount": 21,
                    "crCount": 0,
                    "dCount": 3,
                    "fCount": 0,
                    "iCount": 0,
                    "instructors": [
                        {
                            "id": 3382449,
                            "name": "DIETER VAN MELKEBEEK"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 0,
                    "nwCount": 0,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 1,
                    "sectionNumber": 1,
                    "total": 94,
                    "uCount": 0
                },
                {
                    "aCount": 21,
                    "abCount": 10,
                    "bCount": 19,
                    "bcCount": 18,
                    "cCount": 14,
                    "crCount": 0,
                    "dCount": 2,
                    "fCount": 0,
                    "iCount": 0,
                    "instructors": [
                        {
                            "id": 3382449,
                            "name": "DIETER VAN MELKEBEEK"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 0,
                    "nwCount": 0,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 3,
                    "sectionNumber": 2,
                    "total": 87,
                    "uCount": 0
                }
            ],
            "termCode": 1162
        },
        {
            "cumulative": {
                "aCount": 86,
                "abCount": 39,
                "bCount": 40,
                "bcCount": 18,
                "cCount": 22,
                "crCount": 0,
                "dCount": 4,
                "fCount": 2,
                "iCount": 0,
                "nCount": 0,
                "nrCount": 1,
                "nwCount": 0,
                "otherCount": 0,
                "pCount": 0,
                "sCount": 0,
                "total": 212,
                "uCount": 0
            },
            "sections": [
                {
                    "aCount": 53,
                    "abCount": 26,
                    "bCount": 30,
                    "bcCount": 10,
                    "cCount": 13,
                    "crCount": 0,
                    "dCount": 3,
                    "fCount": 0,
                    "iCount": 0,
                    "instructors": [
                        {
                            "id": 843570,
                            "name": "DEBORAH JOSEPH"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 1,
                    "nwCount": 0,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 0,
                    "sectionNumber": 1,
                    "total": 136,
                    "uCount": 0
                },
                {
                    "aCount": 33,
                    "abCount": 13,
                    "bCount": 10,
                    "bcCount": 8,
                    "cCount": 9,
                    "crCount": 0,
                    "dCount": 1,
                    "fCount": 2,
                    "iCount": 0,
                    "instructors": [
                        {
                            "id": 2601579,
                            "name": "ERIC BACH"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 0,
                    "nwCount": 0,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 0,
                    "sectionNumber": 2,
                    "total": 76,
                    "uCount": 0
                }
            ],
            "termCode": 1154
        },
        {
            "cumulative": {
                "aCount": 27,
                "abCount": 24,
                "bCount": 49,
                "bcCount": 18,
                "cCount": 15,
                "crCount": 0,
                "dCount": 2,
                "fCount": 3,
                "iCount": 1,
                "nCount": 0,
                "nrCount": 0,
                "nwCount": 0,
                "otherCount": 0,
                "pCount": 0,
                "sCount": 1,
                "total": 140,
                "uCount": 0
            },
            "sections": [
                {
                    "aCount": 8,
                    "abCount": 10,
                    "bCount": 31,
                    "bcCount": 5,
                    "cCount": 1,
                    "crCount": 0,
                    "dCount": 0,
                    "fCount": 2,
                    "iCount": 0,
                    "instructors": [
                        {
                            "id": 4195806,
                            "name": "SHUCHI CHAWLA"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 0,
                    "nwCount": 0,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 1,
                    "sectionNumber": 1,
                    "total": 58,
                    "uCount": 0
                },
                {
                    "aCount": 19,
                    "abCount": 14,
                    "bCount": 18,
                    "bcCount": 13,
                    "cCount": 14,
                    "crCount": 0,
                    "dCount": 2,
                    "fCount": 1,
                    "iCount": 1,
                    "instructors": [
                        {
                            "id": 3382449,
                            "name": "DIETER VAN MELKEBEEK"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 0,
                    "nwCount": 0,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 0,
                    "sectionNumber": 2,
                    "total": 82,
                    "uCount": 0
                }
            ],
            "termCode": 1152
        },
        {
            "cumulative": {
                "aCount": 167,
                "abCount": 9,
                "bCount": 17,
                "bcCount": 2,
                "cCount": 4,
                "crCount": 0,
                "dCount": 8,
                "fCount": 2,
                "iCount": 1,
                "nCount": 0,
                "nrCount": 0,
                "nwCount": 0,
                "otherCount": 0,
                "pCount": 0,
                "sCount": 0,
                "total": 210,
                "uCount": 0
            },
            "sections": [
                {
                    "aCount": 74,
                    "abCount": 2,
                    "bCount": 9,
                    "bcCount": 0,
                    "cCount": 2,
                    "crCount": 0,
                    "dCount": 1,
                    "fCount": 0,
                    "iCount": 0,
                    "instructors": [
                        {
                            "id": 843570,
                            "name": "DEBORAH JOSEPH"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 0,
                    "nwCount": 0,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 0,
                    "sectionNumber": 1,
                    "total": 88,
                    "uCount": 0
                },
                {
                    "aCount": 93,
                    "abCount": 7,
                    "bCount": 8,
                    "bcCount": 2,
                    "cCount": 2,
                    "crCount": 0,
                    "dCount": 7,
                    "fCount": 2,
                    "iCount": 1,
                    "instructors": [
                        {
                            "id": 843570,
                            "name": "DEBORAH JOSEPH"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 0,
                    "nwCount": 0,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 0,
                    "sectionNumber": 2,
                    "total": 122,
                    "uCount": 0
                }
            ],
            "termCode": 1144
        },
        {
            "cumulative": {
                "aCount": 26,
                "abCount": 8,
                "bCount": 41,
                "bcCount": 9,
                "cCount": 13,
                "crCount": 0,
                "dCount": 5,
                "fCount": 0,
                "iCount": 2,
                "nCount": 0,
                "nrCount": 0,
                "nwCount": 0,
                "otherCount": 0,
                "pCount": 0,
                "sCount": 1,
                "total": 105,
                "uCount": 0
            },
            "sections": [
                {
                    "aCount": 10,
                    "abCount": 4,
                    "bCount": 20,
                    "bcCount": 6,
                    "cCount": 4,
                    "crCount": 0,
                    "dCount": 1,
                    "fCount": 0,
                    "iCount": 2,
                    "instructors": [
                        {
                            "id": 2601579,
                            "name": "ERIC BACH"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 0,
                    "nwCount": 0,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 0,
                    "sectionNumber": 1,
                    "total": 47,
                    "uCount": 0
                },
                {
                    "aCount": 16,
                    "abCount": 4,
                    "bCount": 21,
                    "bcCount": 3,
                    "cCount": 9,
                    "crCount": 0,
                    "dCount": 4,
                    "fCount": 0,
                    "iCount": 0,
                    "instructors": [
                        {
                            "id": 3382449,
                            "name": "DIETER VAN MELKEBEEK"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 0,
                    "nwCount": 0,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 1,
                    "sectionNumber": 2,
                    "total": 58,
                    "uCount": 0
                }
            ],
            "termCode": 1142
        },
        {
            "cumulative": {
                "aCount": 116,
                "abCount": 14,
                "bCount": 17,
                "bcCount": 7,
                "cCount": 3,
                "crCount": 0,
                "dCount": 3,
                "fCount": 3,
                "iCount": 2,
                "nCount": 0,
                "nrCount": 3,
                "nwCount": 0,
                "otherCount": 0,
                "pCount": 0,
                "sCount": 0,
                "total": 168,
                "uCount": 0
            },
            "sections": [
                {
                    "aCount": 116,
                    "abCount": 14,
                    "bCount": 17,
                    "bcCount": 7,
                    "cCount": 3,
                    "crCount": 0,
                    "dCount": 3,
                    "fCount": 3,
                    "iCount": 2,
                    "instructors": [
                        {
                            "id": 843570,
                            "name": "DEBORAH JOSEPH"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 3,
                    "nwCount": 0,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 0,
                    "sectionNumber": 1,
                    "total": 168,
                    "uCount": 0
                }
            ],
            "termCode": 1134
        },
        {
            "cumulative": {
                "aCount": 28,
                "abCount": 13,
                "bCount": 35,
                "bcCount": 12,
                "cCount": 10,
                "crCount": 0,
                "dCount": 4,
                "fCount": 3,
                "iCount": 0,
                "nCount": 0,
                "nrCount": 0,
                "nwCount": 0,
                "otherCount": 0,
                "pCount": 0,
                "sCount": 1,
                "total": 106,
                "uCount": 0
            },
            "sections": [
                {
                    "aCount": 11,
                    "abCount": 6,
                    "bCount": 22,
                    "bcCount": 6,
                    "cCount": 3,
                    "crCount": 0,
                    "dCount": 2,
                    "fCount": 0,
                    "iCount": 0,
                    "instructors": [
                        {
                            "id": 4195806,
                            "name": "SHUCHI CHAWLA"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 0,
                    "nwCount": 0,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 1,
                    "sectionNumber": 1,
                    "total": 51,
                    "uCount": 0
                },
                {
                    "aCount": 17,
                    "abCount": 7,
                    "bCount": 13,
                    "bcCount": 6,
                    "cCount": 7,
                    "crCount": 0,
                    "dCount": 2,
                    "fCount": 3,
                    "iCount": 0,
                    "instructors": [
                        {
                            "id": 3382449,
                            "name": "DIETER VAN MELKEBEEK"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 0,
                    "nwCount": 0,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 0,
                    "sectionNumber": 2,
                    "total": 55,
                    "uCount": 0
                }
            ],
            "termCode": 1132
        },
        {
            "cumulative": {
                "aCount": 21,
                "abCount": 17,
                "bCount": 20,
                "bcCount": 9,
                "cCount": 7,
                "crCount": 0,
                "dCount": 4,
                "fCount": 2,
                "iCount": 0,
                "nCount": 0,
                "nrCount": 1,
                "nwCount": 0,
                "otherCount": 0,
                "pCount": 0,
                "sCount": 0,
                "total": 81,
                "uCount": 0
            },
            "sections": [
                {
                    "aCount": 9,
                    "abCount": 10,
                    "bCount": 8,
                    "bcCount": 7,
                    "cCount": 2,
                    "crCount": 0,
                    "dCount": 3,
                    "fCount": 0,
                    "iCount": 0,
                    "instructors": [
                        {
                            "id": 3085603,
                            "name": "JIN-YI CAI"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 0,
                    "nwCount": 0,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 0,
                    "sectionNumber": 1,
                    "total": 39,
                    "uCount": 0
                },
                {
                    "aCount": 12,
                    "abCount": 7,
                    "bCount": 12,
                    "bcCount": 2,
                    "cCount": 5,
                    "crCount": 0,
                    "dCount": 1,
                    "fCount": 2,
                    "iCount": 0,
                    "instructors": [
                        {
                            "id": 3085603,
                            "name": "JIN-YI CAI"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 1,
                    "nwCount": 0,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 0,
                    "sectionNumber": 2,
                    "total": 42,
                    "uCount": 0
                }
            ],
            "termCode": 1122
        },
        {
            "cumulative": {
                "aCount": 68,
                "abCount": 6,
                "bCount": 12,
                "bcCount": 5,
                "cCount": 1,
                "crCount": 0,
                "dCount": 2,
                "fCount": 0,
                "iCount": 0,
                "nCount": 0,
                "nrCount": 1,
                "nwCount": 0,
                "otherCount": 0,
                "pCount": 0,
                "sCount": 0,
                "total": 95,
                "uCount": 0
            },
            "sections": [
                {
                    "aCount": 56,
                    "abCount": 3,
                    "bCount": 10,
                    "bcCount": 4,
                    "cCount": 1,
                    "crCount": 0,
                    "dCount": 2,
                    "fCount": 0,
                    "iCount": 0,
                    "instructors": [
                        {
                            "id": 843570,
                            "name": "DEBORAH JOSEPH"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 0,
                    "nwCount": 0,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 0,
                    "sectionNumber": 1,
                    "total": 76,
                    "uCount": 0
                },
                {
                    "aCount": 12,
                    "abCount": 3,
                    "bCount": 2,
                    "bcCount": 1,
                    "cCount": 0,
                    "crCount": 0,
                    "dCount": 0,
                    "fCount": 0,
                    "iCount": 0,
                    "instructors": [
                        {
                            "id": 3382449,
                            "name": "DIETER VAN MELKEBEEK"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 1,
                    "nwCount": 0,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 0,
                    "sectionNumber": 2,
                    "total": 19,
                    "uCount": 0
                }
            ],
            "termCode": 1114
        },
        {
            "cumulative": {
                "aCount": 12,
                "abCount": 4,
                "bCount": 24,
                "bcCount": 9,
                "cCount": 5,
                "crCount": 0,
                "dCount": 1,
                "fCount": 0,
                "iCount": 0,
                "nCount": 0,
                "nrCount": 0,
                "nwCount": 0,
                "otherCount": 0,
                "pCount": 0,
                "sCount": 1,
                "total": 56,
                "uCount": 0
            },
            "sections": [
                {
                    "aCount": 12,
                    "abCount": 4,
                    "bCount": 24,
                    "bcCount": 9,
                    "cCount": 5,
                    "crCount": 0,
                    "dCount": 1,
                    "fCount": 0,
                    "iCount": 0,
                    "instructors": [
                        {
                            "id": 4195806,
                            "name": "SHUCHI CHAWLA"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 0,
                    "nwCount": 0,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 1,
                    "sectionNumber": 1,
                    "total": 56,
                    "uCount": 0
                }
            ],
            "termCode": 1112
        },
        {
            "cumulative": {
                "aCount": 13,
                "abCount": 2,
                "bCount": 27,
                "bcCount": 5,
                "cCount": 5,
                "crCount": 0,
                "dCount": 3,
                "fCount": 3,
                "iCount": 0,
                "nCount": 0,
                "nrCount": 0,
                "nwCount": 0,
                "otherCount": 0,
                "pCount": 0,
                "sCount": 0,
                "total": 58,
                "uCount": 0
            },
            "sections": [
                {
                    "aCount": 13,
                    "abCount": 2,
                    "bCount": 27,
                    "bcCount": 5,
                    "cCount": 5,
                    "crCount": 0,
                    "dCount": 3,
                    "fCount": 3,
                    "iCount": 0,
                    "instructors": [
                        {
                            "id": 4195806,
                            "name": "SHUCHI CHAWLA"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 0,
                    "nwCount": 0,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 0,
                    "sectionNumber": 1,
                    "total": 58,
                    "uCount": 0
                }
            ],
            "termCode": 1104
        },
        {
            "cumulative": {
                "aCount": 22,
                "abCount": 10,
                "bCount": 9,
                "bcCount": 8,
                "cCount": 10,
                "crCount": 0,
                "dCount": 1,
                "fCount": 1,
                "iCount": 0,
                "nCount": 0,
                "nrCount": 0,
                "nwCount": 0,
                "otherCount": 0,
                "pCount": 0,
                "sCount": 0,
                "total": 61,
                "uCount": 0
            },
            "sections": [
                {
                    "aCount": 22,
                    "abCount": 10,
                    "bCount": 9,
                    "bcCount": 8,
                    "cCount": 10,
                    "crCount": 0,
                    "dCount": 1,
                    "fCount": 1,
                    "iCount": 0,
                    "instructors": [
                        {
                            "id": 843570,
                            "name": "DEBORAH JOSEPH"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 0,
                    "nwCount": 0,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 0,
                    "sectionNumber": 1,
                    "total": 61,
                    "uCount": 0
                }
            ],
            "termCode": 1102
        },
        {
            "cumulative": {
                "aCount": 24,
                "abCount": 16,
                "bCount": 41,
                "bcCount": 6,
                "cCount": 0,
                "crCount": 0,
                "dCount": 0,
                "fCount": 0,
                "iCount": 0,
                "nCount": 0,
                "nrCount": 0,
                "nwCount": 0,
                "otherCount": 0,
                "pCount": 0,
                "sCount": 0,
                "total": 87,
                "uCount": 0
            },
            "sections": [
                {
                    "aCount": 24,
                    "abCount": 16,
                    "bCount": 41,
                    "bcCount": 6,
                    "cCount": 0,
                    "crCount": 0,
                    "dCount": 0,
                    "fCount": 0,
                    "iCount": 0,
                    "instructors": [
                        {
                            "id": 843570,
                            "name": "DEBORAH JOSEPH"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 0,
                    "nwCount": 0,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 0,
                    "sectionNumber": 1,
                    "total": 87,
                    "uCount": 0
                }
            ],
            "termCode": 1094
        },
        {
            "cumulative": {
                "aCount": 8,
                "abCount": 8,
                "bCount": 19,
                "bcCount": 12,
                "cCount": 3,
                "crCount": 0,
                "dCount": 1,
                "fCount": 0,
                "iCount": 0,
                "nCount": 0,
                "nrCount": 0,
                "nwCount": 0,
                "otherCount": 0,
                "pCount": 0,
                "sCount": 1,
                "total": 52,
                "uCount": 0
            },
            "sections": [
                {
                    "aCount": 8,
                    "abCount": 8,
                    "bCount": 19,
                    "bcCount": 12,
                    "cCount": 3,
                    "crCount": 0,
                    "dCount": 1,
                    "fCount": 0,
                    "iCount": 0,
                    "instructors": [
                        {
                            "id": 2601579,
                            "name": "ERIC BACH"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 0,
                    "nwCount": 0,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 1,
                    "sectionNumber": 1,
                    "total": 52,
                    "uCount": 0
                }
            ],
            "termCode": 1092
        },
        {
            "cumulative": {
                "aCount": 15,
                "abCount": 16,
                "bCount": 26,
                "bcCount": 6,
                "cCount": 4,
                "crCount": 0,
                "dCount": 1,
                "fCount": 1,
                "iCount": 0,
                "nCount": 0,
                "nrCount": 0,
                "nwCount": 0,
                "otherCount": 0,
                "pCount": 0,
                "sCount": 0,
                "total": 69,
                "uCount": 0
            },
            "sections": [
                {
                    "aCount": 15,
                    "abCount": 16,
                    "bCount": 26,
                    "bcCount": 6,
                    "cCount": 4,
                    "crCount": 0,
                    "dCount": 1,
                    "fCount": 1,
                    "iCount": 0,
                    "instructors": [
                        {
                            "id": 843570,
                            "name": "DEBORAH JOSEPH"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 0,
                    "nwCount": 0,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 0,
                    "sectionNumber": 1,
                    "total": 69,
                    "uCount": 0
                }
            ],
            "termCode": 1084
        },
        {
            "cumulative": {
                "aCount": 5,
                "abCount": 7,
                "bCount": 8,
                "bcCount": 5,
                "cCount": 1,
                "crCount": 0,
                "dCount": 2,
                "fCount": 2,
                "iCount": 0,
                "nCount": 0,
                "nrCount": 1,
                "nwCount": 1,
                "otherCount": 0,
                "pCount": 0,
                "sCount": 0,
                "total": 32,
                "uCount": 0
            },
            "sections": [
                {
                    "aCount": 5,
                    "abCount": 7,
                    "bCount": 8,
                    "bcCount": 5,
                    "cCount": 1,
                    "crCount": 0,
                    "dCount": 2,
                    "fCount": 2,
                    "iCount": 0,
                    "instructors": [
                        {
                            "id": 3382449,
                            "name": "DIETER VAN MELKEBEEK"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 1,
                    "nwCount": 1,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 0,
                    "sectionNumber": 1,
                    "total": 32,
                    "uCount": 0
                }
            ],
            "termCode": 1082
        },
        {
            "cumulative": {
                "aCount": 23,
                "abCount": 9,
                "bCount": 17,
                "bcCount": 3,
                "cCount": 5,
                "crCount": 0,
                "dCount": 0,
                "fCount": 4,
                "iCount": 0,
                "nCount": 0,
                "nrCount": 0,
                "nwCount": 0,
                "otherCount": 0,
                "pCount": 0,
                "sCount": 0,
                "total": 61,
                "uCount": 0
            },
            "sections": [
                {
                    "aCount": 11,
                    "abCount": 9,
                    "bCount": 17,
                    "bcCount": 3,
                    "cCount": 5,
                    "crCount": 0,
                    "dCount": 0,
                    "fCount": 2,
                    "iCount": 0,
                    "instructors": [
                        {
                            "id": 843570,
                            "name": "DEBORAH JOSEPH"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 0,
                    "nwCount": 0,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 0,
                    "sectionNumber": 1,
                    "total": 47,
                    "uCount": 0
                },
                {
                    "aCount": 12,
                    "abCount": 0,
                    "bCount": 0,
                    "bcCount": 0,
                    "cCount": 0,
                    "crCount": 0,
                    "dCount": 0,
                    "fCount": 2,
                    "iCount": 0,
                    "instructors": [
                        {
                            "id": 843570,
                            "name": "DEBORAH JOSEPH"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 0,
                    "nwCount": 0,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 0,
                    "sectionNumber": 2,
                    "total": 14,
                    "uCount": 0
                }
            ],
            "termCode": 1074
        },
        {
            "cumulative": {
                "aCount": 3,
                "abCount": 9,
                "bCount": 7,
                "bcCount": 6,
                "cCount": 3,
                "crCount": 0,
                "dCount": 1,
                "fCount": 1,
                "iCount": 0,
                "nCount": 0,
                "nrCount": 0,
                "nwCount": 0,
                "otherCount": 0,
                "pCount": 0,
                "sCount": 0,
                "total": 30,
                "uCount": 0
            },
            "sections": [
                {
                    "aCount": 3,
                    "abCount": 9,
                    "bCount": 7,
                    "bcCount": 6,
                    "cCount": 3,
                    "crCount": 0,
                    "dCount": 1,
                    "fCount": 1,
                    "iCount": 0,
                    "instructors": [
                        {
                            "id": 4195806,
                            "name": "SHUCHI CHAWLA"
                        }
                    ],
                    "nCount": 0,
                    "nrCount": 0,
                    "nwCount": 0,
                    "otherCount": 0,
                    "pCount": 0,
                    "sCount": 0,
                    "sectionNumber": 1,
                    "total": 30,
                    "uCount": 0
                }
            ],
            "termCode": 1072
        }
    ],
    "courseUuid": "1f36cc02-0eee-3fcf-be09-1ad17aecf83c",
    "cumulative": {
        "aCount": 1427,
        "abCount": 707,
        "bCount": 1517,
        "bcCount": 704,
        "cCount": 496,
        "crCount": 0,
        "dCount": 104,
        "fCount": 71,
        "iCount": 13,
        "nCount": 0,
        "nrCount": 8,
        "nwCount": 4,
        "otherCount": 0,
        "pCount": 0,
        "sCount": 71,
        "total": 5131,
        "uCount": 9
    }
}

