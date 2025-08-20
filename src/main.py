from utils.formatting import print_header
from storage.data_manager import load_expenses
from main_menu import main_menu

def main():
    expenses = load_expenses()
    
    running = True
    
    while running:
        print_header()
        main_menu()
        running = False
    
if __name__ == "__main__":
    main()