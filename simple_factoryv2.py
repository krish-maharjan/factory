from abc import ABC, abstractmethod


class BasePayment(ABC):
    @abstractmethod
    def verify(self):
        pass


class Esewa(BasePayment):
    def verify(self):
        return "Verified by Esewa"


class Khalti(BasePayment):
    def verify(self):
        return "Verified by Khalti"


"""
Just these are added to the already existing simple factory
    - PaymentFactory
    - EsewaFactory
    - KhaltiFactory
"""
class PaymentFactory(ABC):
    @abstractmethod
    def create_wallet(self):
        pass


class EsewaFactory(PaymentFactory):
    def create_wallet(self):
        return Esewa()


class KhaltiFactory(PaymentFactory):
    def create_wallet(self):
        return Khalti()
"""
Until here
This makes it Factory method from Simple Factory
"""

class PaymentFactory:
    @staticmethod
    def create_factory(method):
        """
        This static method acts as a Simple Factory / Factory Selector.
        It decides which Factory Method subclass to instantiate at runtime.
        The combination with the concrete factories (EsewaFactory, KhaltiFactory)
        makes the system a mix of Factory Method + Simple Factory.
        """
        method = method.upper()
        method_options = {
            "ESEWA": EsewaFactory,
            "KHALTI": KhaltiFactory
        }
        return method_options.get(method)()


factory = PaymentFactory.create_factory("Esewa")
wallet = factory.create_wallet()
print(wallet.verify())
