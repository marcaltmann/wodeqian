from dataclasses import dataclass
from datetime import date
from decimal import Decimal


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
