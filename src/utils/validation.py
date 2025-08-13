from utils.formatting import type_text
from datetime import datetime

def validate_name(name):
    if not name.strip():   
        type_text("\n----------Name cannot be empty----------")
        return False
    
    if len(name) > 18:
        type_text("\n--------Character Limit Exceeded--------")
        return False
    
    return True

def validate_date(date):
    if not date.strip():   
        type_text("\n----------Date cannot be empty----------")
        return False