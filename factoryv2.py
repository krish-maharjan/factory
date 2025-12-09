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


# Factory Method interfaces
class PaymentFactoryMethod(ABC):
    @abstractmethod
    def create_wallet(self) -> BasePayment:
        pass


# Concrete Factory Methods
class EsewaFactory(PaymentFactoryMethod):
    def create_wallet(self) -> BasePayment:
        return Esewa()


class KhaltiFactory(PaymentFactoryMethod):
    def create_wallet(self) -> BasePayment:
        return Khalti()


# Simple Factory / Factory Selector
class PaymentFactory:
    @staticmethod
    def create_factory(method: str) -> PaymentFactoryMethod | None:
        """
        This static method acts as a Simple Factory / Factory Selector.
        It decides which Factory Method subclass to instantiate at runtime.
        The combination with the concrete factories (EsewaFactory, KhaltiFactory)
        makes the system a mix of Factory Method + Simple Factory.
        """
        method = method.upper()
        method_options: dict[str, type[PaymentFactoryMethod]] = {
            "ESEWA": EsewaFactory,
            "KHALTI": KhaltiFactory
        }
        factory_class = method_options.get(method)
        if factory_class:
            return factory_class()
        return None


factory = PaymentFactory.create_factory("Esewa")
if factory:
    wallet = factory.create_wallet()
    print(wallet.verify())
