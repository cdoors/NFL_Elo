import csv

def main():
    """
    Main function to process games, predict match winners, and optionally display ELO rankings.
    """
    file_path = 'nfl_scores.csv'
    process_games(file_path)
    predict_match_winner('San Francisco 49ersSF', 'Detroit LionsDET')
    predict_match_winner('Kansas City ChiefsKC', 'Baltimore RavensBAL')
    
    # Uncomment the following lines to display ELO rankings
    # display_elo_rankings()

def calculate_expected_score(rating_team, rating_opponent):
    """
    Calculate the expected score for a team against an opponent.
    
    Args:
    rating_team (float): ELO rating of the team
    rating_opponent (float): ELO rating of the opponent
    
    Returns:
    float: Expected score (probability of winning)
    
    Operations:
    Uses the ELO formula to calculate the expected score.
    """
    return 1 / (1 + 10 ** ((rating_opponent - rating_team) / 400))

def update_elo_ratings(winning_team, losing_team):
    """
    Update ELO ratings for two teams after a match.
    
    Args:
    winning_team (str): Name of the winning team
    losing_team (str): Name of the losing team
    
    Returns:
    None
    
    Operations:
    Retrieves current ratings, calculates new ratings using a dynamic K-factor,
    and updates the global teams_elo dictionary.
    """
    winner_rating = teams_elo.get(winning_team, 1500)
    loser_rating = teams_elo.get(losing_team, 1500)

    rating_diff = abs(winner_rating - loser_rating)
    K = 40 if rating_diff > 100 else 20

    expected_winner = calculate_expected_score(winner_rating, loser_rating)
    expected_loser = calculate_expected_score(loser_rating, winner_rating)

    teams_elo[winning_team] = winner_rating + K * (1 - expected_winner)
    teams_elo[losing_team] = loser_rating + K * (0 - expected_loser)

def read_games_from_csv(file_path):
    """
    Read games data from a CSV file.
    
    Args:
    file_path (str): Path to the CSV file
    
    Returns:
    list: List of games, where each game is a list of strings
    
    Operations:
    Opens the CSV file and reads its contents into a list.
    """
    games = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row:
                games.append(row)
    return games

def process_games(file_path):
    """
    Process games from a CSV file and update ELO ratings.
    
    Args:
    file_path (str): Path to the CSV file containing game data
    
    Returns:
    None
    
    Operations:
    Reads games from CSV, determines winners and losers, and updates ELO ratings.
    """
    games = read_games_from_csv(file_path)
    for game in games:
        try:
            team1, score1, team2, score2 = game
            score1 = int(score1.strip())
            score2 = int(score2.strip())

            winning_team = team1.strip() if score1 > score2 else team2.strip()
            losing_team = team2.strip() if winning_team == team1.strip() else team1.strip()
            update_elo_ratings(winning_team, losing_team)
        except ValueError:
            print(f"Skipping invalid row: {game}")
            continue

def predict_match_winner(team1, team2):
    """
    Predict the winner of a match between two teams.
    
    Args:
    team1 (str): Name of the first team
    team2 (str): Name of the second team
    
    Returns:
    None
    
    Operations:
    Calculates and prints the probability of each team winning based on their ELO ratings.
    """
    team1_rating = teams_elo.get(team1, 1500)
    team2_rating = teams_elo.get(team2, 1500)

    team1_expected = calculate_expected_score(team1_rating, team2_rating)
    team2_expected = calculate_expected_score(team2_rating, team1_rating)

    print(f"Probability of {team1} winning: {team1_expected * 100:.2f}%")
    print(f"Probability of {team2} winning: {team2_expected * 100:.2f}%")

def display_elo_rankings():
    """
    Display ELO rankings for all teams.
    
    Args:
    None
    
    Returns:
    None
    
    Operations:
    Sorts teams by ELO rating and prints the rankings.
    """
    sorted_teams = sorted(teams_elo.items(), key=lambda x: x[1], reverse=True)
    for index, (team, elo) in enumerate(sorted_teams, start=1):
        print(f"#{index} {team}: {elo}")

# Initialize ELO ratings
teams_elo = {}

if __name__ == "__main__":
    main()
