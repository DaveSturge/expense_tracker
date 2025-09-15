from utils.formatting import print_title, type_text, print_time_date, single_item_display, get_user_choice, transition_to, print_footer
from add_expense import add_expense

import storage.data_manager as dm

def view_expenses():
    print_title("View All Expenses")
    print_time_date()

    for expense in dm.expenses.values():
        single_item_display(expense)

    print_view_menu()

    user_choice = get_user_choice("            Select Option: ")

    match user_choice:
        case "1":
            transition_to()
            add_expense()
        case "2":
            transition_to()
        case "3":
            print_footer()
            dm.save_expenses()
            dm.save_categories()
            quit()
        case _:
            type_text("\n-------------Invalid Option-------------")

def print_view_menu():
    type_text("----------------------------------------")
    type_text(" (1) Add Expense")
    type_text(" (2) Return to Main Menu")
    type_text(" (3) Exit")
    type_text("----------------------------------------")