from utils.formatting import print_title, print_time_date, print_footer, type_text, transition, get_user_choice
from utils.validation import validate_name, validate_date

def add_expense():
    print_title("Add  Expense")
    print_time_date()
    expense_name = get_expense_name()
    date = get_user_choice(" > Date (DD-MM-YYYY): ")
    cost = get_user_choice(" > Cost             : £")
    category = get_user_choice(" > Category         : ")
    

def get_expense_name():
    validated = False

    while not validated:
        name = get_user_choice(" > Item Name        : ")
        validated = validate_name(name)

    return name

def get_expense_date():
    validated = False

    while not validated:
        date = get_user_choice(" > Date (DD-MM-YYYY): ")
        validated = validate_date(date)

    return date