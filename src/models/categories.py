from utils.formatting import print_title, get_user_choice, transition_from_category

import storage.data_manager as dm

def enter_new_category():
    print_title("Enter New Category")
    new_category = get_user_choice(" > New Category     : ")
    dm.add_category(new_category)
    transition_from_category()