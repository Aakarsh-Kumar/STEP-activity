# gdb/tests/test_interface_factory.py
from gdb.domain.account_factory import AccountFactory
from gdb.domain.iaccount import IAccount
from gdb.exceptions import AccountException

def main():
    print("=== Activity 12: Factory-Driven System Suite ===")

    accounts = [
        AccountFactory.create_account("SAVINGS", "SA100", "Alice", 25, 5000.0, "Active", "1234"),
        AccountFactory.create_account("CURRENT", "CA200", "Bob", 35, 10000.0, "Active", "5678"),
        AccountFactory.create_account("SALARY", "SAL300", "Charlie", 28, 0.0, "Active", "9999"),
        AccountFactory.create_account("FIXEDDEPOSIT", "FD400", "Diana", 45, 50000.0, "Active", "0000"),
    ]
    assert all(isinstance(account, IAccount) for account in accounts)
    assert [account.get_account_type() for account in accounts] == ["Savings", "Current", "Salary", "FixedDeposit"]
    assert [account.balance for account in accounts] == [5000.0, 10000.0, 0.0, 50000.0]

    for account in accounts:
        account.deposit(100.0)
        account.withdraw(50.0)
        assert account.balance >= 50.0

    try:
        AccountFactory.create_account("UNKNOWN", "X500", "Eve", 30, 100.0)
    except AccountException:
        pass
    else:
        raise AssertionError("Unknown account types must fail")

    print("Interface-only client tests passed!")

if __name__ == "__main__":
    main()
