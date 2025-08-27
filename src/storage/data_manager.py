from models.expense import Expense

import utils.formatting as fm

import json
import uuid
import os

expenses = {}

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

    for expense in expenses.values():
        fm.single_item_display(expense)

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