import pandas as pd
import argparse
from utils.teams import TEAMS
from helpers.classes import Team

# Check command line arguments
def validate_args():
    parser = argparse.ArgumentParser(description="Simulate a game between two teams.")

    # Required positional arguments (no switches)
    parser.add_argument("team1", help="Home team, abbrev., i.e. GSW, SAS, BOS")
    parser.add_argument("team2", help="Away team, abbrev., i.e. GSW, SAS, BOS")

    # Optional flags (switches)
    parser.add_argument("--verbose", action="store_true", help="Enable detailed output")
    parser.add_argument("-p", "--possessions", type=int, default=100, help="Number of possessions (default: 100)")

    args = parser.parse_args()

    # Example validation
    if args.team1.lower() == args.team2.lower():
        parser.error("HOME team and AWAY team must be different.")
    if args.possessions <= 0:
       parser.error("Possessions must be greater than 0.")

    return args

def main():
    args = validate_args()
    print(f"HOME: {TEAMS[args.team1]}")
    print(f"AWAY: {TEAMS[args.team2]}")
    print(f"Verbose: {args.verbose}")
    print(f"Possessions: {args.possessions}")

    home_team = args.team1
    #py maway_team = args.team2

    # Load team stats
    df_per = pd.read_csv("data/2025-nba-teams-per.csv")

    df_home_team = df_per[df_per["Team"] == TEAMS[home_team]].iloc[0]
    #df_away_team = df_per[df_per["Team"] == TEAMS[away_team]].iloc[0]

    home = Team(*df_home_team[["Team","FGA","3PA","3P%","PF","FT%","ORB"]].values)
    print(f"Play-by-play for {home.name}")

    # Simulate a play several times
    count = 0

    while True:
        count += 1
        print(f"Play #{count}: ",end="")
        home.play()


        if count >= args.possessions:
            break

    home.summary()

if __name__ == "__main__":
    main()

