import json

import mt940
from mt940.models import Transaction as Mt940Transaction

from transactions import Transaction

ACCOUNT_TYPES = ["Assets", "Liabilities", "Equity", "Income", "Expenses"]


def convert_transaction(transaction: Mt940Transaction) -> Transaction:
    return Transaction(
        date=transaction.data["date"],
        amount=transaction.data["amount"].amount,
        applicant=transaction.data["applicant_name"],
        purpose=transaction.data["purpose"],
    )


def main():
    transactions = mt940.parse("transactions.sta")

    with open("transactions.bean", "w", newline="") as f:
        for transaction in transactions:
            line = convert_transaction(transaction).format_bean()
            f.write(line)

    with open("transactions.json", "w") as f:
        converted_transactions = [
            convert_transaction(t).as_json_dict() for t in transactions
        ]
        json.dump(converted_transactions, f, indent=4)


if __name__ == "__main__":
    main()
