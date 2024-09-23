import pandas as pd

def main():
    """
    Main function to process NFL scores, calculate team averages, and display results.
    """
    file_path = 'nfl_scores_individual.csv'
    df = load_and_preprocess_data(file_path)
    result_df = create_team_scores_dataframe(df)
    display_results(result_df)

def load_and_preprocess_data(file_path):
    """
    Load and preprocess the NFL scores data from a CSV file.
    
    Args:
    file_path (str): Path to the CSV file
    
    Returns:
    pandas.DataFrame: Preprocessed DataFrame with NFL scores
    """
    df = pd.read_csv(file_path)
    df['Score1'] = pd.to_numeric(df['Score1'], errors='coerce')
    return df

def create_team_scores_dataframe(df):
    """
    Create a DataFrame with team scores.
    
    Args:
    df (pandas.DataFrame): Preprocessed DataFrame with NFL scores
    
    Returns:
    pandas.DataFrame: DataFrame with team scores as columns
    """
    unique_teams = df['Team1'].unique()
    result_df = pd.DataFrame(columns=unique_teams)
    
    for team in unique_teams:
        team_scores = df[df['Team1'] == team]['Score1'].tolist()
        result_df[team] = pd.Series(team_scores)
    
    result_df.reset_index(drop=True, inplace=True)
    return result_df

def display_results(result_df):
    """
    Display average scores and implied statistics for specific teams.
    
    Args:
    result_df (pandas.DataFrame): DataFrame with team scores
    
    Returns:
    None
    """
    det_avg = result_df['Detroit LionsDET'].mean()
    sf_avg = result_df['San Francisco 49ersSF'].mean()

    print(f"DET: {det_avg:.2f}")
    print(f"SF: {sf_avg:.2f}")
    print(f"Implied score difference: {det_avg - sf_avg:.2f}")
    print(f"O/U line: {det_avg + sf_avg:.2f}")

if __name__ == "__main__":
    main()