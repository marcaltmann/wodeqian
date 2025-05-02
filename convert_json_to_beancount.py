import json

from transactions import Transaction


def main():
    with open("transactions_real.json") as f:
        json_transactions = json.load(f)
        transactions = [Transaction.from_json_dict(t) for t in json_transactions]

    with open("transactions_real.bean", "w", newline="") as f:
        for t in transactions:
            line = t.format_bean()
            f.write(line)


if __name__ == "__main__":
    main()
