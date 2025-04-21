from dataclasses import dataclass
from datetime import date
from decimal import Decimal

from mt940.models import Transaction as Mt940Transaction


@dataclass
class Transaction:
    """Class for keeping track of a transaction."""

    date: date
    amount: Decimal
    applicant: str
    purpose: str

    def __str__(self) -> str:
        return f"{self.date} {self.amount}€ {self.applicant} {self.purpose}"

    def as_json_dict(self) -> dict:
        return {
            "date": str(self.date),
            "amount": float(self.amount),
            "applicant": self.applicant,
            "purpose": self.purpose,
        }

    def format_bean(self) -> str:
        date_str = self.date.strftime("%Y-%m-%d")
        return f'{date_str} * "{self.applicant}" "{self.purpose}"\n\n'

    @classmethod
    def from_mt940(cls, transaction: Mt940Transaction):
        transaction1 = cls(
            date=transaction.data["date"],
            amount=transaction.data["amount"].amount,
            applicant=transaction.data["applicant_name"],
            purpose=transaction.data["purpose"],
        )
        return transaction1

    @classmethod
    def from_json_dict(cls, transaction: dict):
        transaction1 = cls(
            date=date.fromisoformat(transaction["date"]),
            amount=Decimal(transaction["amount"]),
            applicant=transaction["applicant"],
            purpose=transaction["purpose"],
        )
        return transaction1
