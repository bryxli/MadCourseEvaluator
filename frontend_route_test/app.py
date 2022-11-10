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