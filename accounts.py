from dataclasses import dataclass
from enum import StrEnum


class AccountType(StrEnum):
    """Represents the five account types."""
    ASSETS = "Assets"
    LIABILITIES = "Liabilities"
    EQUITY = "Equity"
    INCOME = "Income"
    EXPENSES = "Expenses"


@dataclass
class Account:
    """Represents accounts."""
    type: AccountType
    name: str

    def __str__(self):
        return f"{self.type}:{self.name}"
