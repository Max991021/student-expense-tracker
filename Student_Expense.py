import csv
class Tracker:
    
    def __init__(self,item = None,price = None):
        self.item = item
        self.price = price
    
    def items(self):
        with open('expenses.csv', 'r', errors='ignore') as file:
            content = file.read.split(',')
            
            names = content[0]
            expense_catagory = []
            price = []
            for i in range(1,len(content),2):
                expense_catagory.append(content[i])
            
            for i in range(2,len(content),2):
                price.append(content[i])
                
            
                
    
    def amount(self):
        with open('expense_tracker.csv', 'w', errors='ignore') as file:
            file.read()
