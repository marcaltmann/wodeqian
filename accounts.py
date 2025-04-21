from dataclasses import dataclass, field
from enum import StrEnum
from typing import Optional, Self


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
    name: str
    parent: Optional[Self] = None
    children: Optional[list[Self]] = field(default_factory=list)

    def __str__(self):
        if self.parent:
            return f"{self.parent}:{self.name}"
        else:
            return self.name
