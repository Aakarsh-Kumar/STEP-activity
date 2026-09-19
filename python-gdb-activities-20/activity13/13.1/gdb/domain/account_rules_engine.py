# gdb/domain/account_rules_engine.py

class AccountRulesEngine:
    """Centralized Business Rules Engine for banking policies."""

    @staticmethod
    def get_minimum_balance(account_type: str) -> float:
        return 1000.0 if account_type and account_type.strip().upper() == "SAVINGS" else 0.0

    @staticmethod
    def get_interest_rate(account_type: str) -> float:
        normalized_type = account_type.strip().upper() if account_type else ""
        return {"SAVINGS": 4.0, "FIXEDDEPOSIT": 6.5}.get(normalized_type, 0.0)

    @staticmethod
    def get_overdraft_limit(account_type: str) -> float:
        return 10000.0 if account_type and account_type.strip().upper() == "CURRENT" else 0.0

    @staticmethod
    def validate_withdrawal(account_type: str, current_balance: float, amount: float) -> bool:
        min_bal = AccountRulesEngine.get_minimum_balance(account_type)
        overdraft = AccountRulesEngine.get_overdraft_limit(account_type)
        return (current_balance - amount) >= (min_bal - overdraft)
