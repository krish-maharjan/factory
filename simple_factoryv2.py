from abc import ABC, abstractmethod

# Base product interface


class BasePayment(ABC):
    @abstractmethod
    def verify(self) -> str:
        pass


# Concrete products
class Esewa(BasePayment):
    def verify(self) -> str:
        return "Verified by Esewa"


class Khalti(BasePayment):
    def verify(self) -> str:
        return "Verified by Khalti"


# Simple Factory
class PaymentFactory:
    @staticmethod
    def create_wallet(method: str) -> BasePayment:
        """
        Creates and returns a wallet based on the method name.
        Acts as a Simple Factory because the decision is centralized.
        """
        method = method.upper()
        if method == "ESEWA":
            return Esewa()
        elif method == "KHALTI":
            return Khalti()
        else:
            raise ValueError(f"Unknown payment method: {method}")


wallet: BasePayment = PaymentFactory.create_wallet("Esewa")
print(wallet.verify())
