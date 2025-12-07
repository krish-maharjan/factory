from abc import ABC, abstractmethod


class AccountTypeAbstractBaseClass(ABC):
    @abstractmethod
    def interest_calculation(self):
        """
        Interest Calculation
        """


class SavingAccountType(AccountTypeAbstractBaseClass):
    def interest_calculation(self):
        return "5%"


class CurrentAccountType(AccountTypeAbstractBaseClass):
    def interest_calculation(self):
        return "0%"


class AccountFactory:
    def __init__(self, account_type):
        self.account_type = account_type.lower()

    def get_account(self) -> AccountTypeAbstractBaseClass:
        if self.account_type == "saving":
            return SavingAccountType()
        elif self.account_type == "current":
            return CurrentAccountType()


saving = AccountFactory("saving")
account = saving.get_account()
print(account.interest_calculation())
