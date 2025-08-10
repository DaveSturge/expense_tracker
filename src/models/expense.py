from enum import Enum

class Expense:
    def __init__(self, desc, date, cost, category=None):
        self.desc = desc
        self.date = date
        self.cost = cost
        self.category = category

    def __repr__(self):
        if self.category:
            return f"Expense: {self.desc}: £{self.cost} | {self.date} | Tag: {self.category}"

        return f"Expense: {self.desc}: £{self.cost} | {self.date}"