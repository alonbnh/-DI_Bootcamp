class Currency:
    def _init_(self, currency, amount):
        self.currency = currency
        self.amount = amount
    
    def _str_(self):
        print(f'{self.amount} {self.currency}')
    
    def _int_(self):
        print(f'{self.amount}')

    def _repr_(self):
        print(f'{self.amount} {self.currency}')
    
    def _add_(self, other, currency, amount):
        self.currency = currency
        self.amount = amount
        if self.currency == other.currency:
            return self.amount + other.amount
        else:
            return 'Cannot print that'







c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)




