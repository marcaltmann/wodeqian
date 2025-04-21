import json

import mt940
from mt940.models import Transaction as Mt940Transaction

from transactions import Transaction
from accounts import Account

def main():
    transactions = mt940.parse("transactions.sta")

    print(Account.ACCOUNT_TYPES)

    with open("transactions.bean", "w", newline="") as f:
        for transaction in transactions:
            line = Transaction.from_mt940(transaction).format_bean()
            f.write(line)

    with open("transactions.json", "w") as f:
        converted_transactions = [
            Transaction.from_mt940(t).as_json_dict() for t in transactions
        ]
        json.dump(converted_transactions, f, indent=4)


if __name__ == "__main__":
    main()
