from utils.formatting import print_title, print_time_date, print_footer, type_text, transition_to, get_user_choice
from add_expense import add_expense
from view_expenses import view_expenses

import storage.data_manager as dm

def main_menu():
    while True:

        print_title("Main  Menu")
        print_time_date()
        print_main_menu()

        while True:
            user_choice = get_user_choice("            Select Option: ")

            match user_choice:
                case "1":
                    transition_to()
                    add_expense()
                    break
                case "2":
                    transition_to()
                    view_expenses()
                    break
                case "3":
                    print_footer()
                    dm.save_expenses()
                    quit()
                case _:        
                    type_text("\n-------------Invalid Option-------------")

def print_main_menu():
    type_text(" (1) Add Expense")
    type_text(" (2) View Expenses")
    type_text(" (3) Exit")
    type_text("----------------------------------------")