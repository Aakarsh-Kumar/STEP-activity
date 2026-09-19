# gdb/domain/account_rules_engine.py
from gdb.domain.account_rules_properties_loader import AccountRulesPropertiesLoader

class AccountRulesEngine:
    """Properties-Driven Rules Engine."""
    _rules = {}

    @classmethod
    def reload_rules(cls) -> None:
        cls._rules = {account_type: AccountRulesPropertiesLoader.load_rules(account_type) for account_type in ("SAVINGS", "CURRENT", "FIXEDDEPOSIT", "SALARY")}

    @classmethod
    def reloadRules(cls) -> None:
        cls.reload_rules()

    @classmethod
    def _get_value(cls, account_type: str, key: str) -> float:
        if not cls._rules:
            cls.reload_rules()
        normalized_type = account_type.strip().upper() if account_type else ""
        value = cls._rules.get(normalized_type, {}).get(key)
        if value is None:
            return 0.0
        try:
            return float(value)
        except (TypeError, ValueError) as error:
            raise ValueError(f"Invalid {key} for {normalized_type}: {value}") from error
    @staticmethod
    def get_minimum_balance(account_type: str) -> float:
        return AccountRulesEngine._get_value(account_type, "minBalance")

    @staticmethod
    def get_interest_rate(account_type: str) -> float:
        return AccountRulesEngine._get_value(account_type, "interestRate")

    @staticmethod
    def get_overdraft_limit(account_type: str) -> float:
        return AccountRulesEngine._get_value(account_type, "overdraftLimit")

    @staticmethod
    def validate_withdrawal(account_type: str, current_balance: float, amount: float) -> bool:
        minimum_balance = AccountRulesEngine.get_minimum_balance(account_type)
        overdraft_limit = AccountRulesEngine.get_overdraft_limit(account_type)
        return current_balance - amount >= minimum_balance - overdraft_limit
