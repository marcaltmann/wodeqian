from dataclasses import dataclass, field
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
    tags: list[str] = field(default_factory=list)

    def __str__(self) -> str:
        return f"{self.date} {self.amount}€ {self.applicant} {self.purpose}"

    def as_json_dict(self) -> dict:
        return {
            "date": str(self.date),
            "amount": str(self.amount),
            "applicant": self.applicant,
            "purpose": self.purpose,
        }

    def format_bean(self) -> str:
        date_str = self.date.strftime("%Y-%m-%d")
        first_line = f'{date_str} * "{self.applicant}" "{self.purpose}"'
        first_line += self.format_tags() if self.tags else ""
        lines = [
            first_line,
            f"  Assets:Checking",
            f"  Expenses:Misc  {self.amount} EUR",
        ]
        return "\n".join(lines) + "\n\n"

    def format_tags(self) -> str:
        tags_with_hash = [f"#{tag}" for tag in self.tags]
        return " ".join(tags_with_hash)

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
