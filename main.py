from interface import get_user_input, print_report
from engine import analyze_business

def main():
    income, expenses, cash, investment = get_user_input()
    result = analyze_business(income, expenses, cash, investment)
    print_report(result)

if __name__ == "__main__":
    main()