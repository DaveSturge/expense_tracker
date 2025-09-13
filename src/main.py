from utils.formatting import print_header
from main_menu import main_menu

import storage.data_manager as dm

def main():
    dm.load_expenses()
    dm.load_categories()
    
    running = True
    
    while running:
        print_header()
        main_menu()
        running = False
    
if __name__ == "__main__":
    main()