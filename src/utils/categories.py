from utils.formatting import print_title, get_user_choice, transition_from

categories = {"Rent", "Mortgage", "Utilities", "Car Insurance", "Groceries", "Fuel", "Savings", "Debt", "Misc"}

def enter_new_category():
    print_title("Enter New Category")
    new_category = get_user_choice(" > New Category     : ")
    categories.add(new_category)
    transition_from()