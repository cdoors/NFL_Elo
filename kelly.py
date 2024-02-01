def kelly_criterion(prob_win, decimal_odds, bankroll):
    """Calculate the optimal bet size using the Kelly Criterion."""
    return ((prob_win * (decimal_odds - 1) - (1 - prob_win)) / (decimal_odds - 1)) * bankroll

def get_user_input(prompt):
    """Get user input and convert it to a float."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def main():
    print("Betting Calculator")
    decimal_odds = get_user_input("Enter the decimal odds: ")
    win_percentage = get_user_input("Enter your win percentage (as a decimal): ")
    bankroll = get_user_input("Enter your bankroll: ")

    optimal_bet = kelly_criterion(win_percentage, decimal_odds, bankroll)
    print(f"Recommended bet amount: ${optimal_bet:.2f}")

if __name__ == "__main__":
    main()
