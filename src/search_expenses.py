import utils.formatting as fm
import storage.data_manager as dm
import add_expense as ae

def search_expenses():
    fm.print_title("Search Expenses")
    fm.print_time_date()

    continue_menu = True
    skip_search_again = False

    while continue_menu:
        print_menu()

        skip_search_again = False

        while True:
            user_choice = fm.get_user_choice("            Select Option: ")
            
            match user_choice:
                case "1": # description search
                    search_value = fm.get_user_choice("\n           Search Keyword: ")

                    fm.type_text("\n----------------------------------------")

                    search_results = desc_search(search_value)
                    
                    if not search_results:       
                        fm.type_text("\n------------No Results Found------------")
                    else:
                        for result in search_results:
                            fm.single_item_display(result)

                    fm.type_text("----------------------------------------")

                    break
                case "2": # date search

                    fm.type_text("\n----------------------------------------")

                    while True:       
                        
                        fm.type_text(" (1) Search Specific Date")
                        fm.type_text(" (2) Search Date Range")
                        fm.type_text(" (3) Back To Search Menu")
                        fm.type_text("----------------------------------------")

                        user_choice = fm.get_user_choice("            Select Option: ")

                        match user_choice:
                            case "1": # exact date search
                                print()
                                search_value = ae.get_expense_date()
                                search_results = exact_date_search(search_value)
                                fm.type_text("\n----------------------------------------")

                                if not search_results:       
                                    fm.type_text("------------No Results Found------------")
                                else:
                                    for result in search_results:
                                        fm.single_item_display(result)

                                fm.type_text("----------------------------------------")
                                break
                            case "2": # date range search
                                fm.type_text("\n------------Enter Start Date------------")
                                start_date = ae.get_expense_date()
                                fm.type_text("\n-------------Enter End Date-------------")
                                end_date = ae.get_expense_date()
                                search_results = range_date_search(start_date, end_date)
                                fm.type_text("\n----------------------------------------")

                                if not search_results:       
                                    fm.type_text("------------No Results Found------------")
                                else:
                                    for result in search_results:
                                        fm.single_item_display(result)

                                fm.type_text("----------------------------------------")
                                break
                            case "3": # return to search menu
                                skip_search_again = True
                                fm.type_text("\n----------------------------------------")
                                break
                            case _:
                                fm.type_text("\n-------------Invalid Option-------------")

                    break
                case "3": #category search
                    search_value = fm.get_user_choice("\n           Search Keyword: ")

                    fm.type_text("\n----------------------------------------")

                    search_results = cat_search(search_value)

                    if not search_results:       
                        fm.type_text("\n------------No Results Found------------")
                    else:
                        for result in search_results:
                            fm.single_item_display(result)

                    fm.type_text("----------------------------------------")
                    break
                case "4": #back to main menu
                    fm.transition_to()
                case "5": #quit
                    fm.print_footer()
                    dm.save_expenses()
                    quit()
                case _:
                    fm.type_text("\n-------------Invalid Option-------------")
        
        while True and not skip_search_again:
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

def exact_date_search(search_value):
    results = []

    for expense_obj in dm.expenses.values(): 

        if search_value.strftime("%d-%m-%y") == expense_obj.display_date():
            results.append(expense_obj)
    
    return results

def range_date_search(start_date, end_date):
    results = []

    for expense_obj in dm.expenses.values():

        if expense_obj.date >= start_date and expense_obj.date <= end_date:
            results.append(expense_obj)

    return results