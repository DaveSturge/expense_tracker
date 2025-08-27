from datetime import datetime
from decimal import Decimal

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

    def to_dict(self):
        return {"desc": self.desc, "date": self.display_date(), "cost": str(self.cost), "category": self.category}
    
    @classmethod
    def from_dict(cls, data):

        expense_date = datetime.strptime(data["date"], "%d-%m-%y").date()
        return cls(
            desc=data["desc"],
            date=expense_date,
            cost=Decimal(data["cost"]),
            category=data["category"]
        )