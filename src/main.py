from models.expense import Expense
from utils.formatting import print_header
from main_menu import main_menu
import time

def main():
    running = True
    
    while running:
        print_header()
        main_menu()
        running = False
    
if __name__ == "__main__":
    main()