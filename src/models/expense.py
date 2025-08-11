from enum import Enum
from datetime import datetime

class Expense:
    def __init__(self, desc, date, cost, category=None):
        self.desc = desc
        self.date = datetime.strptime(date, "%d-%m-%Y").date()
        self.cost = cost
        self.category = category

    def __str__(self):
        if self.category:
            return f"Expense: {self.desc}: £{self.cost} | {self.date} | Category: {self.category}"

        return f"Expense: {self.desc}: £{self.cost} | {self.date}"