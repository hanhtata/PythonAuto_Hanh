class Customer:
    def __init__(self,name, date_of_birth, email, phone):
        self._name=name
        self._date_of_birth=date_of_birth
        self._email=email
        self._phone=phone

    @property
    def name(self):
        return self._name

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @property
    def email(self):
        return self._email

    @property
    def phone(self):
        return self._phone

    def get_info(self):
        print(self.name)
        print(self.date_of_birth)
        print(self.email)
        print(self.phone)
    
class BankAccount():
    minimum_balance = 50000

    def __init__(self, account_number, name, date_of_birth, email, phone, balance=0):
        self._owner= Customer(name, date_of_birth, email, phone)
        self._account_number = account_number
        self.balance = balance      # gọi @balance.setter

    @property
    def account_number(self):
        return self._account_number

    @property
    def owner(self):
        return self._owner

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        if balance >= 0:
            self._balance = balance
        else:
            raise ValueError("Số dư phải lớn hơn 0")

    def display(self):
        print("Số tài khoản: "+ str(self.account_number))
        print("Tên khách hàng: "+str(self.owner.name))
        print("Ngày sinh : "+str(self.owner.date_of_birth))
        print("Số điện thoại : "+str(self.owner.phone))
        print("Email : "+str(self.owner.email))
        print("Số dư tài khoản : "+str(self.balance))

    def withdraw(self, amount):
        if 0 < amount <= self.balance - BankAccount.minimum_balance:
            self.balance -= amount
        else:
            raise ValueError(
                f"Số tiền phải lớn hơn 0 và không được vượt quá số dư hiện tại")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Số tiền phải lớn hơn 0")
class SavingAccount(BankAccount):
    monthly_interest_rate=0.005
    def calculate_interest(self):
        return self.balance * SavingAccount.monthly_interest_rate

my_account = BankAccount("0123456789", "Hanhh", "01/01/2000", "hanhtth2508@gmail.com", "0987654321", 22_000_000_000_000_000_000)
my_account.display()