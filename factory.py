"""
Factory Method

Creator (abstract class): AccountCreator

Declares the abstract factory method: create_account()

Optionally defines a template method: get_interest()

Concrete Creators (subclasses):

SavingAccountTypeFactory → overrides create_account() → returns SavingAccountType

CurrentAccountTypeFactory → overrides create_account() → returns CurrentAccountType

Products:

SavingAccountType and CurrentAccountType implement the abstract AccountTypeAbstractBaseClass interface.

Polymorphic creation: Client code calls get_interest(), which internally calls create_account() — the exact product returned depends on the concrete factory subclass, not a conditional.
"""

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


class AccountCreator(ABC):
    @abstractmethod
    def create_account(self):
        """
        Create Account
        """

    def get_interest(self):
        account = self.create_account()
        return account.interest_calculation()


class SavingAccountTypeFactory(AccountCreator):
    def create_account(self):
        return SavingAccountType()


class CurrentAccountTypeFactory(AccountCreator):
    def create_account(self):
        return CurrentAccountType()


current = SavingAccountTypeFactory()
print("Alright", current.get_interest())
