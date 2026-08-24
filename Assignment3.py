from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        pass

class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str, cvv: str):
        self.card_number = card_number
        self.cvv = cvv

    def pay(self, amount: float) -> str:
        masked_card = f"****-****-****-{self.card_number[-4:]}"
        return f"Paid ${amount:.2f} using Credit Card ({masked_card})."

class PayPalPayment(PaymentStrategy):
    def __init__(self, email: str):
        self.email = email

    def pay(self, amount: float) -> str:
        return f"Paid ${amount:.2f} using PayPal account: {self.email}."

class BitCoinPayment(PaymentStrategy):
    def __init__(self, wallet_address: str):
        self.wallet_address = wallet_address

    def pay(self, amount: float) -> str:
        return f"Paid ${amount:.2f} using Bitcoin wallet: {self.wallet_address[:6]}..."

class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy) -> None:
        self._strategy = strategy
        print("Payment strategy updated successfully.")

    def process_payment(self, amount: float) -> None:
        if not self._strategy:
            raise ValueError("Payment strategy is not set!")
        
        result = self._strategy.pay(amount)
        print(result)

if __name__ == "__main__":
    cc_strategy = CreditCardPayment("1234567890123456", "123")
    processor = PaymentProcessor(cc_strategy)
    
    print("--- Transaction 1 ---")
    processor.process_payment(150.00)

    print("\n--- Switching to PayPal ---")
    processor.set_strategy(PayPalPayment("user@example.com"))
    processor.process_payment(45.50)

    print("\n--- Switching to Bitcoin ---")
    processor.set_strategy(BitCoinPayment("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"))
    processor.process_payment(250.00)