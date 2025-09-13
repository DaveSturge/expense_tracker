import utils.formatting as fm
import storage.data_manager as dm

def search_expenses():
    fm.print_title("Search Expenses")
    fm.print_time_date()

    continue_menu = True

    while continue_menu:
        print_menu()

        while True:
            user_choice = fm.get_user_choice("            Select Option: ")
            
            match user_choice:
                case "1":
                    search_value = fm.get_user_choice("\n           Search Keyword: ")

                    fm.type_text("\n----------------------------------------")

                    search_results = desc_search(search_value)
                    
                    if not search_results:       
                        fm.type_text("\n------------No Results Found------------")
                    else:
                        for result in search_results:
                            fm.single_item_display(result)

                    break
                case "2":
                    pass
                case "3":
                    search_value = fm.get_user_choice("\n           Search Keyword: ")

                    fm.type_text("\n----------------------------------------")

                    search_results = cat_search(search_value)

                    if not search_results:       
                        fm.type_text("\n------------No Results Found------------")
                    else:
                        for result in search_results:
                            fm.single_item_display(result)

                    break
                case "4":
                    fm.transition_to()
                case "5":
                    fm.print_footer()
                    dm.save_expenses()
                    quit()
                case _:
                    fm.type_text("\n-------------Invalid Option-------------")
        
        while True:
            user_choice = fm.get_user_choice("      Search Again? (Y/N): ")

            match user_choice.upper():
                case "Y":
                    fm.type_text("\n----------------------------------------")
                    break
                case "N":
                    print()
                    continue_menu = False
                    break
                case _:
                    fm.type_text("\n-------------Invalid Option-------------")
            

def print_menu():
    fm.type_text(" (1) Search via Description")
    fm.type_text(" (2) Search via Date")
    fm.type_text(" (3) Search via Category")
    fm.type_text(" (4) Main Menu")
    fm.type_text(" (5) Exit")
    fm.type_text("----------------------------------------")

def desc_search(search_value):
    results = []

    for expense_obj in dm.expenses.values():
        if search_value.lower() in expense_obj.desc.lower():
            results.append(expense_obj)

    return results

def cat_search(search_value):
    results = []

    for expense_obj in dm.expenses.values():
        if search_value.lower() in expense_obj.category.lower():
            results.append(expense_obj)
    
    return results