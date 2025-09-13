from utils.formatting import type_text
from datetime import datetime
from decimal import Decimal

import storage.data_manager as dm

def validate_name(name):
    if not name.strip():   
        type_text("\n----------Name cannot be empty----------")
        return False
    
    if len(name) > 25:
        type_text("\n--------Character Limit Exceeded--------")
        return False
    
    return True

def validate_date(date):
    error = "\n--------------Invalid Date--------------"

    if not date.strip():   
        error = "\n----------Date cannot be empty----------"
        return None, error

    valid_formats = ["%d/%m/%Y", "%d-%m-%Y", "%d.%m.%Y", "%d/%m/%y", "%d-%m-%y", "%d.%m.%y", "%d/%b/%y", "%d-%b-%y", "%d.%b.%y", "%d %b %Y" ]
    datetime_object = None

    for format in valid_formats:
        try:
            datetime_object = datetime.strptime(date, format).date()
            break
        except ValueError:
            pass
    
    if datetime_object != None and datetime_object > datetime.today().date():
        error = "\n------Date cannot be in the future------"
        return None, error

    return datetime_object, error

def validate_cost(cost):
    if not cost.strip():   
        type_text("\n----------Cost cannot be empty----------")
        return False, None

    try:
        decimal_cost = Decimal(cost)
    except:
        type_text("\n-----------Invalid characters-----------")
        return False, None
    
    if "." in cost:
        split_cost = cost.split(".")

        if len(split_cost[1]) > 2:
            type_text("\n-------Invalid: Too many decimals-------")
            return False, None

    if decimal_cost < 0:
        type_text("\n--------Cost cannot  be negative--------")
        return False, None
        
    return True, decimal_cost

def validate_category(category):
    if not category.strip():
        type_text("\n--------Category cannot be empty--------")
        return False, True

    if category in dm.categories:
        return True, False
    
    return False, False