import pandas as pd
import os
import sys

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

pd.set_option('display.expand_frame_repr', False)
df = pd.read_csv('../data/fantasy-football-leaders.csv')
df = pd.DataFrame.set_index(df, keys="Rank")
df = df.drop('Sacks', axis=1)
df = df.drop('Interceptions', axis=1)
df = df.drop('FumblesForced', axis=1)
df = df.drop('FumblesRecovered', axis=1)
points = df[ (df['FantasyPointsPPR'] < 100)].index
df.drop(points , inplace=True)
#pd.set_option('display.max_columns', 500)


def fantasy_main():
    print(f"""Choose fantasy option
    1. Top players overall
    2. Top players by postion
    3. Players by team
    4. Amount of games the player played""")

    choice = input("Choose fantasy option: ")

    if(choice == "1"):
        top_players_overall()
    elif(choice == "2"):
        top_position_overall()
    elif(choice == "3"):
        select_by_team()
    elif(choice == "4"):
        games_injured()
    else:
        print(choice)

def top_players_overall():
    #print("\nPlease choose number of players to display")
    print(f"""\nPlease choose number of players to display
    1. Top 10 players
    2. Top 20 Players
    3. Top 50 Players
    4. Top 100 Players """)
    num_players = input("Select option: ")

    if(num_players == "1"):
        print(df.head(10))
    elif(num_players == "2"):
        print(df.head(20))
    elif(num_players == "3"):
        print(df.head(50))
    elif(num_players == "4"):
        print(df.head(100))

def top_position_overall():
    print(f"""\n Please choose your position
    1. QB
    2. RB
    3. WR
    4. TE""")
    position = input("")

    qb = df.loc[df['Position'] == "QB"]
    rb = df.loc[df['Position'] == "RB"]
    wr = df.loc[df['Position'] == "WR"]
    te = df.loc[df['Position'] == "TE"]

    if(position == "1"):
        print(f"""\n How many players would you like to view?
        1. Top 5
        2. Top 10
        3. Top 20
        4. Top 50""")
        player_count = input("")

        qb = qb.drop('Receptions', axis=1)
        qb = qb.drop('ReceivingYards', axis=1)
        qb = qb.drop('ReceivingTouchdowns', axis=1)

        if(player_count == "1"):
            print(qb.head(5))
        elif(player_count == "2"):
            print(qb.head(10))
        elif(player_count == "3"):
            print(qb.head(20))
        elif(player_count == "4"):
            print(qb.head(50))

    if(position == "2"):
        print(f"""\n How many players would you like to view?
        1. Top 5
        2. Top 10
        3. Top 20
        4. Top 50""")
        player_count = input("")

        rb = rb.drop('PassingYards', axis=1)
        rb = rb.drop('PassingTouchdowns', axis=1)
        rb = rb.drop('PassingInterceptions', axis=1)

        if(player_count == "1"):
            print(rb.head(5))
        elif(player_count == "2"):
            print(rb.head(10))
        elif(player_count == "3"):
            print(rb.head(20))
        elif(player_count == "4"):
            print(rb.head(50))

    if(position == "3"):
        print(f"""\n How many players would you like to view?
        1. Top 5
        2. Top 10
        3. Top 20
        4. Top 50""")
        player_count = input("")

        wr = wr.drop('PassingYards', axis=1)
        wr = wr.drop('PassingTouchdowns', axis=1)
        wr = wr.drop('PassingInterceptions', axis=1)

        if(player_count == "1"):
            print(wr.head(5))
        elif(player_count == "2"):
            print(wr.head(10))
        elif(player_count == "3"):
            print(wr.head(20))
        elif(player_count == "4"):
            print(wr.head(50))

    if(position == "4"):
        print(f"""\n How many players would you like to view?
        1. Top 5
        2. Top 10
        3. Top 20
        4. Top 50""")
        player_count = input("")

        te = te.drop('PassingYards', axis=1)
        te = te.drop('PassingTouchdowns', axis=1)
        te = te.drop('PassingInterceptions', axis=1)

        if(player_count == "1"):
            print(te.head(5))
        elif(player_count == "2"):
            print(te.head(10))
        elif(player_count == "3"):
            print(te.head(20))
        elif(player_count == "4"):
            print(te.head(50))

def select_by_team():
    print(f""" Select a team:
    'LAR' 'BUF' 'LAC' 'TB' 'IND' 'KC' 'GB' 'SF' 'MIN' 'DAL' 'CIN' 'PHI' 'BAL'
    'PIT' 'ARI' 'TEN' 'LV' 'MIA' 'SEA' 'CAR' 'NO' 'ATL' 'HOU' 'WAS' 'DET'
    'NE' 'CHI' 'CLE' 'DEN' 'JAX' 'NYG' 'NYJ'""")
    team = input("Select team: ")
    print(df.loc[df['Team'] == team.upper()])
 
def games_injured():
    print(f"""\n Choose players based off amount of games they played
    1. 17 games
    2. 14 - 16 games
    3. 10 - 13 games
    4. less than 10 games""")
    games = input("Select option: ")

    if(games == "1"):
        all = df.loc[df['Played'] == 17]
        print(all.head(50))
    if(games == "2"):
        most = df.loc[df['Played'].isin([14, 15, 16])]
        print(most.head(50))
    if(games == "3"):
        many = df.loc[df['Played'].isin([10, 11, 12, 13])]
        print(many)
    if(games == "4"):
        least = df.loc[df['Played'] < 10]
        print(least)

#if __name__ == '__main__':
#    fantasy_main()
