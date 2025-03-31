import csv
import pprint

import mt940
from mt940.models import Transaction


ACCOUNT_TYPES = ["Assets", "Liabilities", "Equity", "Income", "Expenses"]


def convert_transaction(transaction: Transaction) -> list:
    return {
        "date": transaction.data["date"],
        "amount": transaction.data["amount"].amount,
        "applicant": transaction.data["applicant_name"],
        "purpose": transaction.data["purpose"],
    }


def format_transaction(transaction: list) -> str:
    date = transaction["date"].strftime("%Y-%m-%d")
    purpose = f'{transaction["applicant"]}: {transaction["purpose"]}'
    return f'{date} * "{purpose}"\n\n'


def main():
    transactions = mt940.parse("transactions.sta")

    with open("transactions.bean", "w", newline="") as f:
        for transaction in transactions:
            line = format_transaction(convert_transaction(transaction))
            f.write(line)


if __name__ == "__main__":
    main()
