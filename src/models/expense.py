from datetime import datetime

class Expense:
    def __init__(self, desc, date, cost, category=None):
        self.desc = desc
        self.date = date
        self.cost = cost
        self.category = category

    def __str__(self):

        if self.category:
            return f"Expense: {self.desc}: £{self.display_cost()} | {self.display_date()} | Category: {self.category}"

        return f"Expense: {self.desc}: £{self.cost} | {self.date}"
    
    def display_cost(self):
        return f"{self.cost:.2f}"
    
    def display_date(self):
        return self.date.strftime("%d-%m-%y")