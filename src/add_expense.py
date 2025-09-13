from utils.formatting import print_title, print_time_date, type_text, transition_to, get_user_choice, single_item_display
from utils.validation import validate_name, validate_date, validate_cost, validate_category
from models.categories import enter_new_category
from models.expense import Expense

import storage.data_manager as dm


def add_expense():
    print_title("Add  Expense")
    print_time_date()
    expense_name = get_expense_name()
    expense_date = get_expense_date()
    expense_cost = get_expense_price()
    expense_category = get_expense_category()
    
    expense_obj = Expense(expense_name, expense_date, expense_cost, expense_category)

    dm.add_expense(expense_obj)

    type_text("\n-------------Expense Saved!-------------")
    single_item_display(expense_obj)
    transition_to()

def get_expense_name():
    validated = False

    while not validated:
        name = get_user_choice(" > Item Description : ")
        formatted_name = name.title()
        validated = validate_name(formatted_name)

    return formatted_name.strip()

def get_expense_date():
    validated = False
    date_object = None

    while not validated:
        date = get_user_choice(" > Date (DD-MM-YYYY): ")
        date_object, error_code = validate_date(date)

        if date_object != None:
            validated = True
        else:
            type_text(error_code)

    return date_object

def get_expense_price():
    validated = False

    while not validated:
        cost = get_user_choice(" > Cost             : £")
        validated, decimal_cost = validate_cost(cost)

    return decimal_cost

def get_expense_category():
    validated = False
    blank = False

    while not validated:
        category = get_user_choice(" > Category         : ")
        formatted_category = category.title()

        validated, blank = validate_category(formatted_category)

        if not validated and not blank:
            type_text("\n---------Category doesn't exist---------")
            new_category = get_user_choice("      Enter new category?  (Y/N): ")

            if new_category.upper() == "Y":
                print("")
                transition_to()
                enter_new_category()
            else:
                user_input = get_user_choice("  View existing categories?  (Y/N): ")

                print("\n")

                if user_input.upper() == "Y":
                    num = 1
                    for cat in dm.categories:
                        type_text(f"{num}. {cat}")
                        num += 1

                    transition_to()

    return formatted_category