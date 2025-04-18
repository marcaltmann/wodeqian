import csv
import datetime
import json
import pprint

import mt940
from mt940.models import Transaction


ACCOUNT_TYPES = ["Assets", "Liabilities", "Equity", "Income", "Expenses"]


def convert_transaction(transaction: Transaction) -> dict:
    return {
        "date": transaction.data["date"],
        "amount": transaction.data["amount"].amount,
        "applicant": transaction.data["applicant_name"],
        "purpose": transaction.data["purpose"],
    }


def prepare_for_json(transaction: dict) -> dict:
    return {
        "date": str(transaction["date"]),
        "amount": float(transaction["amount"]),
        "applicant": transaction["applicant"],
        "purpose": transaction["purpose"],
    }


def format_transaction(transaction: list) -> str:
    date = transaction["date"].strftime("%Y-%m-%d")
    purpose = f"{transaction['applicant']}: {transaction['purpose']}"
    return f'{date} * "{purpose}"\n\n'


def main():
    transactions = mt940.parse("transactions.sta")

    with open("transactions.bean", "w", newline="") as f:
        for transaction in transactions:
            line = format_transaction(convert_transaction(transaction))
            f.write(line)

    with open("transactions.json", "w") as f:
        converted_transactions = [
            prepare_for_json(convert_transaction(t)) for t in transactions
        ]
        json.dump(converted_transactions, f, indent=4)


if __name__ == "__main__":
    main()
