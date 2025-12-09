"""
Abstract Factory vs Factory Method:

1. Factory Method (earlier implementation):
   - Each factory creates **a single product**.
   - Example: `EsewaFactory.create_wallet()` → returns `Esewa` object.
   - If we want another product type (e.g., Refund), we would need a separate method or separate factory.
   - Client code depends on a single factory at a time, typically creating only one product.

2. Abstract Factory (current implementation):
   - Each factory creates a **family of related products**.
   - Example: `EsewaFactory` can create both `Verify` and `Refund` objects (`create_verify()` + `create_refund()`).
   - Guarantees that products from the same family are compatible.
   - Client code works only with abstract interfaces (`BaseVerify`, `BaseRefund`) and is decoupled from concrete classes.
   - Supports adding new families (e.g., StripeFactory) without changing existing client code.

3. Additional layer (runtime selector / simple factory):
   - `PaymentFactory.create_factory(method)` allows **runtime selection of the concrete factory**.
   - This is optional for Abstract Factory but makes client code cleaner and removes if/elif logic in multiple places.

Summary:
- Factory Method → one product per factory.
- Abstract Factory → multiple related products per factory.
- Runtime selector → convenience layer to pick factories dynamically.
"""


from abc import ABC, abstractmethod


class BaseVerify(ABC):
    @abstractmethod
    def verify(self) -> str:
        pass

class BaseRefund(ABC):
    @abstractmethod
    def refund(self) -> str:
        pass


# Concrete products
class EsewaVerify(BaseVerify):
    def verify(self) -> str:
        return "Verified by Esewa"

class EsewaRefund(BaseRefund):
    def refund(self) -> str:
        return "Refund process by Esewa"


class KhaltiVerify(BaseVerify):
    def verify(self) -> str:
        return "Verified by Khalti"

class KhaltiRefund(BaseRefund):
    def refund(self) -> str:
        return "Refund process by Khalti"


class AbstractWalletFactory(ABC):
    @abstractmethod
    def create_verify(self) -> BaseVerify:
        pass

    @abstractmethod
    def create_refund(self) -> BaseRefund:
        pass


# Concrete Factory Methods
class EsewaFactory(AbstractWalletFactory):
    def create_verify(self) -> BaseVerify:
        return EsewaVerify()
    
    def create_refund(self) -> BaseRefund:
        return EsewaRefund()


class KhaltiFactory(AbstractWalletFactory):
    def create_verify(self) -> BaseVerify:
        return KhaltiVerify()

    def create_refund(self) -> BaseRefund:
        return KhaltiRefund()


# Simple Factory / Factory Selector
class PaymentFactory:
    @staticmethod
    def create_factory(method: str) -> AbstractWalletFactory | None:
        """
        This static method acts as a Simple Factory / Factory Selector.
        It decides which Factory Method subclass to instantiate at runtime.
        The combination with the concrete factories (EsewaFactory, KhaltiFactory)
        makes the system a mix of Factory Method + Simple Factory.
        """
        method = method.upper()
        method_options: dict[str, type[AbstractWalletFactory]] = {
            "ESEWA": EsewaFactory,
            "KHALTI": KhaltiFactory
        }
        factory_class = method_options.get(method)
        if factory_class:
            return factory_class()
        return None


factory: AbstractWalletFactory | None = PaymentFactory.create_factory("Esewa")
if factory:
    wallet = factory.create_verify()
    print(wallet.verify())
    refund = factory.create_refund()
    print(refund.refund())
