import csv

        
        
tracker_dict = {}   
def items():
    
    with open('expenses.csv', 'r', errors='ignore') as file:
        content = file.read.split(',')
        
        names = content[0]
        expense_catagory = []
        price = []
        for i in range(1,len(content),2):
            expense_catagory.append(content[i])
        
        for i in range(2,len(content),2):
            price.append(content[i])
            
        for i in names:
            tracker_dict[i] = f'{expense_catagory[i]} R {price}'
        
        
    for i in tracker_dict:
        tracker_dict[key] = f"Total is R {sum(value)}"
        
    tracker_dict = sorted(tracker_dict, value[-1], reverse=False)
            
    for key, value in tracker_dict.items():
        print(f'{key}, {value}')
        
    return tracker_dict
def amount():
    with open('expense_tracker.csv', 'w', errors='ignore') as file:
        file.read()
        for key, value in tracker_dict.items():
            file.write(f'{key}, {value}')
