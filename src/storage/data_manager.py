from models.expense import Expense

import json
import uuid
import os

expenses = {}
categories = set()

def load_expenses():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    save_data = os.path.join(base_dir, "data", "expenses.json")
    
    try:
        with open (save_data, "r") as f:
            loaded_json = json.load(f)

        for expense_id, data in loaded_json.items():
            expense_obj = Expense.from_dict(data)
            expenses[expense_id] = expense_obj
    except FileNotFoundError:
        pass

def save_expenses():
    expense_dict = {}

    for key, value in expenses.items():
        expense_dict[key] = value.to_dict()

    base_dir = os.path.dirname(os.path.dirname(__file__))
    expense_json = os.path.join(base_dir, "data", "expenses.json")

    with open (expense_json, "w") as f:
        json.dump(expense_dict, f)

def add_expense(expense_obj):
    expense_id = str(uuid.uuid4())
    expenses[expense_id] = expense_obj
    save_expenses()

def load_categories():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    save_data = os.path.join(base_dir, "data", "categories.json")

    try:
        with open(save_data, "r") as f:
            loaded_json = json.load(f)

        for cat in loaded_json:
            categories.add(cat)

        #categories = set(loaded_json)

    except FileNotFoundError:
        pass
    
def save_categories():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    save_data = os.path.join(base_dir, "data", "categories.json")

    with open (save_data, "w") as f:
        json.dump(list(categories), f)

def add_category(category):
    categories.add(category)
    save_categories()