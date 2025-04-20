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
