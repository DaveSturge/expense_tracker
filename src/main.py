from models.expense import Expense

def main():
    expense1 = Expense("McDonalds", "09/08/2025", 6.50, "Fast Food")
    expense2 = Expense("KFC", "06/05/2025", 7.52)

    print(expense1)
    print(expense2)


if __name__ == "__main__":
    main()