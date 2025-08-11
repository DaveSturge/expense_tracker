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
    type_text("========================================")
    type_text("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

def type_text(text, newline=True):
    for char in text:
        print(char, end = "", flush=True)
        time.sleep(0.01)

    if newline:
        print("\n")

def line_delay():
    time.sleep(0.3)

def transition():
    print("")
    line_delay()
    print("")
    type_text("=============<[ CUT HERE ]>=============")
    print("")
    line_delay()
    print("")