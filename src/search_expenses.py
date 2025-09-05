import utils.formatting as fm
import storage.data_manager as dm

def search_expenses():
    fm.print_title("Search Expenses")
    fm.print_time_date()

    

    while True:
        print_menu()

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

            case "2":
                pass
            case "3":
                pass
            case "4":
                fm.transition_to()
            case "5":
                print_footer()
                dm.save_expenses()
                quit()
            case _:
                fm.type_text("\n-------------Invalid Option-------------")
        
        user_choice = fm.get_user_choice("      Search Again? (Y/N): ")

        match user_choice.upper():
            case "Y":
                pass
            case "N":
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