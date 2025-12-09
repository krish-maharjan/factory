from abc import ABC, abstractmethod

# =========================
# Product Interfaces
# =========================


class BaseVerify(ABC):
    @abstractmethod
    def verify(self) -> str:
        pass


class BaseRefund(ABC):
    @abstractmethod
    def refund(self) -> str:
        pass

# =========================
# Abstract Factory
# =========================


class AbstractWalletFactory(ABC):
    @abstractmethod
    def create_verify(self) -> BaseVerify:
        pass

    @abstractmethod
    def create_refund(self) -> BaseRefund:
        pass

# =========================
# Registry + Factory Selector
# =========================


class PaymentFactory:
    """Central registry of all concrete wallet factories."""
    _registry: dict[str, type[AbstractWalletFactory]] = {}

    @classmethod
    def register_factory(cls, name: str, factory_class: type[AbstractWalletFactory]):
        """Register a concrete factory with a name."""
        cls._registry[name.upper()] = factory_class

    @classmethod
    def create_factory(cls, name: str) -> AbstractWalletFactory | None:
        """Return an instance of the factory by name."""
        factory_class = cls._registry.get(name.upper())
        if factory_class:
            return factory_class()
        return None

# =========================
# Decorator for auto-registration
# =========================


def register_payment(name: str):
    """Decorator to automatically register a concrete factory."""
    def decorator(cls):
        PaymentFactory.register_factory(name, cls)
        return cls
    return decorator

# =========================
# Concrete Products & Factories
# =========================

# -------------------------
# Esewa
# -------------------------


class EsewaVerify(BaseVerify):
    def verify(self) -> str:
        return "Verified by Esewa"


class EsewaRefund(BaseRefund):
    def refund(self) -> str:
        return "Refund process by Esewa"


@register_payment("ESEWA")
class EsewaFactory(AbstractWalletFactory):
    def create_verify(self) -> BaseVerify:
        return EsewaVerify()

    def create_refund(self) -> BaseRefund:
        return EsewaRefund()

# -------------------------
# Khalti
# -------------------------


class KhaltiVerify(BaseVerify):
    def verify(self) -> str:
        return "Verified by Khalti"


class KhaltiRefund(BaseRefund):
    def refund(self) -> str:
        return "Refund process by Khalti"


@register_payment("KHALTI")
class KhaltiFactory(AbstractWalletFactory):
    def create_verify(self) -> BaseVerify:
        return KhaltiVerify()

    def create_refund(self) -> BaseRefund:
        return KhaltiRefund()

# =========================
# Client Code
# =========================


factory_name = "ESEWA"
factory = PaymentFactory.create_factory(factory_name)

if factory:
    wallet = factory.create_verify()
    refund = factory.create_refund()
    print(wallet.verify())  # Verified by Esewa
    print(refund.refund())  # Refund process by Esewa

# You can swap at runtime
factory_name = "KHALTI"
factory = PaymentFactory.create_factory(factory_name)

if factory:
    wallet = factory.create_verify()
    refund = factory.create_refund()
    print(wallet.verify())  # Verified by Khalti
    print(refund.refund())  # Refund process by Khalti
