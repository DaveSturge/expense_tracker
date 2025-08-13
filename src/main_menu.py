from utils.formatting import print_title, print_time_date, print_footer, type_text, transition, get_user_choice
from add_expense import add_expense

def main_menu():
    print_title("Main  Menu")
    print_time_date()
    print_main_menu()
    user_choice = get_user_choice("            Select Option: ")
    print("")
    type_text("----------------------------------------")

    match user_choice:
        case "1":
            transition()
            add_expense()
        case "2":
            print("Option 2")
        case "3":
            print("Option 3")
        case "4":
            print("Option 4")
        case "5":
            print_footer()

def print_main_menu():
    type_text("1. Add Expense")
    type_text("2. View Expenses")
    type_text("3. Search Expenses")
    type_text("4. Generate Report")
    type_text("5. Exit")
    type_text("----------------------------------------")