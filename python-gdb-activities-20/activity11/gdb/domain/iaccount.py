# gdb/domain/iaccount.py
from abc import ABC, abstractmethod

class IAccount(ABC):
    """Pure Interface defining the contract for all bank accounts."""
    @abstractmethod
    def deposit(self, amount: float) -> None: ...

    @abstractmethod
    def withdraw(self, amount: float) -> None: ...

    @abstractmethod
    def calculate_interest(self) -> float: ...

    @abstractmethod
    def display_account_info(self) -> None: ...

    @abstractmethod
    def validate_pin(self, entered_pin: str) -> bool: ...

    @abstractmethod
    def get_account_type(self) -> str: ...

    @property
    @abstractmethod
    def account_number(self) -> str: ...

    @property
    @abstractmethod
    def name(self) -> str: ...

    @property
    @abstractmethod
    def age(self) -> int: ...

    @property
    @abstractmethod
    def balance(self) -> float: ...

    @property
    @abstractmethod
    def status(self) -> str: ...
