from datetime import datetime
import time

def print_header():
    type_text("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")

def print_title(page_name):

    title_string_padding = ""

    for i in range((41 - len(page_name)) // 2):
        title_string_padding += " "

    type_text("========================================")
    type_text(title_string_padding + page_name.upper())
    type_text("========================================")

def print_time_date():
    today_date = datetime.today().strftime("%d-%m-%Y")
    type_text(f"                        Date: {today_date}")
    type_text("----------------------------------------")

def print_footer():
    type_text("\n========================================")
    type_text("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

def type_text(text, newline=True):
    for char in text:
        print(char, end = "", flush=True)
        time.sleep(0.01)

    if newline:
        print("\n")

def line_delay():
    time.sleep(0.3)

def transition_to():
    print("")
    type_text(" . . . . . . . . . . . . . . . . . . . ")
    print("")

def transition_from_category():
    print("")
    line_delay()
    print("")
    type_text("---------- [ CATEGORY SAVED ] ----------")
    print("")
    line_delay()

def get_user_choice(text):
    type_text(text, newline=False)
    user_input = input()
    return user_input

def calculate_padding(text, column_size):
    text_length = len(text)

    if text_length > column_size:
        text = text[:column_size - 2] + "."
        return text.ljust(column_size)

    return text.ljust(column_size)

def single_item_display(expense_object):
    category_padding = calculate_padding(expense_object.category, 8)
    description_padding = calculate_padding(expense_object.desc, 21 - len(f"£{expense_object.display_cost()}"))

    type_text(f" {expense_object.display_date()} {category_padding}{description_padding} £{expense_object.display_cost()}")