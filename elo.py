import csv

# Initialize ELO ratings
teams_elo = {}

# Function to calculate expected score
def calculate_expected_score(rating_team, rating_opponent):
    return 1 / (1 + 10 ** ((rating_opponent - rating_team) / 400))

# ELO system
def update_elo_ratings(winning_team, losing_team):
    winner_rating = teams_elo.get(winning_team, 1500)
    loser_rating = teams_elo.get(losing_team, 1500)

    rating_diff = abs(winner_rating - loser_rating)
    
    # K = 30
    # Dynamic K-factor
    if rating_diff > 100:
        K = 40  # Higher K-factor for large rating differences
    else:
        K = 20  # Lower K-factor for smaller differences

    expected_winner = calculate_expected_score(winner_rating, loser_rating)
    expected_loser = calculate_expected_score(loser_rating, winner_rating)

    teams_elo[winning_team] = winner_rating + K * (1 - expected_winner)
    teams_elo[losing_team] = loser_rating + K * (0 - expected_loser)


# Function to read games from CSV
def read_games_from_csv(file_path):
    games = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row:  # Check if row is not empty
                games.append(row)
    return games

# Function to process games
def process_games(file_path):
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


# Function to predict match winner
def predict_match_winner(team1, team2):
    team1_rating = teams_elo.get(team1, 1500)
    team2_rating = teams_elo.get(team2, 1500)

    team1_expected = calculate_expected_score(team1_rating, team2_rating)
    team2_expected = calculate_expected_score(team2_rating, team1_rating)

    print(f"Probability of {team1} winning: {team1_expected * 100:.2f}%")
    print(f"Probability of {team2} winning: {team2_expected * 100:.2f}%")

# Example Usage
file_path = 'nfl_scores.csv'  # Update this path
process_games(file_path)
# predict_match_winner('New England PatriotsNE', 'Kansas City ChiefsKC')


# print("------")
# predict_match_winner('Baltimore RavensBAL', 'Houston TexansHOU')
# print()
# predict_match_winner('Green Bay PackersGB','San Francisco 49ersSF')
# print()
predict_match_winner('San Francisco 49ersSF','Detroit LionsDET')
# print()
predict_match_winner('Kansas City ChiefsKC','Baltimore RavensBAL')
# print()
# print()


# # ELO RANKING
# sorted_teams = sorted(teams_elo.items(), key=lambda x: x[1], reverse=True)
# for index, (team, elo) in enumerate(sorted_teams, start=1):
#     print(f"#{index} {team}: {elo}")

