class Tracker:
    
    def __init__(self,item = None,price = None):
        self.item = item
        self.price = price
    
    def items(self):
        with open('expenses.csv', 'r', errors='ignore') as file:
            file.read()
    
    def amount(self):
        with open('expenses.csv', 'r', errors='ignore') as file:
            file.read()