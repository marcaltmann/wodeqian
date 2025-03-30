import mt940
import pprint


def main():
    transactions = mt940.parse('umsaetze.sta')

    print('Transactions:')
    print(transactions)
    pprint.pprint(transactions.data)

    print()
    for transaction in transactions:
        print('Transaction: ', transaction)
        breakpoint()
        pprint.pprint(transaction.data)
        pprint.pprint(transaction.data["amount"])



if __name__ == "__main__":
    main()
