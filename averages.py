import pandas as pd

# Load the CSV file
file_path = 'nfl_scores_individual.csv'  # Replace with your CSV file path
df = pd.read_csv(file_path)

# Ensure 'Score' is numeric
df['Score1'] = pd.to_numeric(df['Score1'], errors='coerce')

# Create an empty DataFrame with unique team names as columns
unique_teams = df['Team1'].unique()
result_df = pd.DataFrame(columns=unique_teams)

# Populate the DataFrame
for team in unique_teams:
    team_scores = df[df['Team1'] == team]['Score1'].tolist()
    result_df[team] = pd.Series(team_scores)

# Reset index
result_df.reset_index(drop=True, inplace=True)

# Print or save the result
# print(result_df)

kc_avg = result_df['Detroit LionsDET'].mean()
bal_avg = result_df['San Francisco 49ersSF'].mean()

print(f"DET: {kc_avg:.2f}")
print(f"SF: {bal_avg:.2f}")
print(f"Implied score {kc_avg-bal_avg:.2f}")
print(f"O/U line: {kc_avg+bal_avg}")