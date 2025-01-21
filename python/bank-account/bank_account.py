import threading


class BankAccount:
    def __init__(self):
        self._balance = None
        self._lock = threading.Lock()

    def get_balance(self):
        with self._lock:
            if self.is_open:
                return self._balance
            raise ValueError("account not open")

    def open(self):
        with self._lock:
            if self.is_open:
                raise ValueError("account already open")
            self._balance = 0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("amount must be greater than 0")
        with self._lock:
            if not self.is_open:
                raise ValueError("account not open")
            self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("amount must be greater than 0")
        with self._lock:
            if not self.is_open:
                raise ValueError("account not open")
            if self._balance < amount:
                raise ValueError("amount must be less than balance")
            self._balance -= amount

    def close(self):
        with self._lock:
            if not self.is_open:
                raise ValueError("account not open")
            self._balance = None

    @property
    def is_open(self):
        return not self._balance is None
