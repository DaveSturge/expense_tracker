from utils.formatting import print_title, print_time_date, print_footer, type_text, transition, get_user_choice
from utils.validation import validate_name, validate_date, validate_cost, validate_category

def add_expense():
    print_title("Add  Expense")
    print_time_date()
    expense_name = get_expense_name()
    expense_date = get_expense_date()
    expense_cost = get_expense_price()
    expense_category = get_expense_category()
    
    

def get_expense_name():
    validated = False

    while not validated:
        name = get_user_choice(" > Item Name        : ")
        validated = validate_name(name)

    return name.strip()

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

    while not validated:
        category = get_user_choice(" > Category         : ")
        validated = validate_cost(category)

    return category
    