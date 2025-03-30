import csv
import pprint

import mt940
from mt940.models import Transaction


def convert_transaction(transaction: Transaction) -> list:
    return {
        "date": transaction.data["date"],
        "amount": transaction.data["amount"].amount,
        "applicant": transaction.data["applicant_name"],
        "purpose": transaction.data["purpose"],
    }


def main():
    transactions = mt940.parse("/home/marc/umsaetze.sta")

    for transaction in transactions:
        pprint.pprint(convert_transaction(transaction))

    with open("transactions.csv", "w", newline="") as csvfile:
        spamwriter = csv.writer(
            csvfile, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL
        )
        spamwriter.writerow(["Date", "Amount", "Applicant", "Purpose"])

        for transaction in transactions:
            converted = convert_transaction(transaction)
            spamwriter.writerow(
                [
                    converted["date"],
                    converted["amount"],
                    converted["applicant"],
                    converted["purpose"],
                ]
            )


if __name__ == "__main__":
    main()
