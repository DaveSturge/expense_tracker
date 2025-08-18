from utils.formatting import print_title, print_time_date, print_footer, type_text, transition_to, get_user_choice
from utils.validation import validate_name, validate_date, validate_cost, validate_category
from utils.categories import enter_new_category, categories

def add_expense():
    print_title("Add  Expense")
    print_time_date()
    expense_name = get_expense_name()
    expense_date = get_expense_date()
    expense_cost = get_expense_price()
    expense_category = get_expense_category()

    #print(f"Expense: {expense_name}: £{expense_cost:.2f} | {expense_date} | Category: {expense_category}")
    
    

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
        formatted_category = category.title()

        validated = validate_category(formatted_category)

        if not validated:
            type_text("\n---------Category doesn't exist---------")
            new_category = get_user_choice("      Enter new category?  (Y/N): ")

            if new_category.upper() == "Y":
                transition_to()
                enter_new_category()
            else:
                user_input = get_user_choice("  View existing categories?  (Y/N): ")

                if user_input.upper() == "Y":
                    num = 1
                    for cat in categories:
                        print("\n")
                        type_text(f"{num}. {cat}")
                        num += 1

    return formatted_category
    