import pandas as pd
import numpy as np
from gpt3 import try_gpt


def create_your_own_json():
    play_dct = {}
    play_dct['game_date'] = '2022-12-01'
    play_dct['sp'] = 1
    play_dct['touchdown'] = 1
    play_dct['drive'] = np.random.choice(list(range(5, 11)))
    play_dct['time'] = '0:30'
    play_dct['qtr'] = 4
    play_dct['quarter_seconds_remaining'] = 30
    play_dct['half_seconds_remaining'] = 30
    play_dct['game_seconds_remaining'] = 30
    play_dct['game_half'] = 'Half2'
    play_dct['goal_to_go'] = 0
    yards = np.random.choice(list(range(10, 16)))
    play_dct['down'] = 4
    play_dct['yardline_100'] = yards
    play_dct['yards_gained'] = yards
    play_dct['score_differential'] = 0
    play_dct['posteam_score'] = 21
    play_dct['defteam_score'] = 21
    play_dct['score_differential_post'] = 6
    play_dct['posteam_score_post'] = 27
    play_dct['defteam_score_post'] = 21

    print("First let's pick teams! In the input below, give us the name of your chosen home team and away team.")
    print("For now let's keep it to NFL teams; our testing has not confirmed that random abbreviations will work.")
    print("Here are some examples:")
    print("- NYG")
    print("- TB")
    print("- MIA")
    print("- WAS")
    print("- LA")
    print("- LAC")
    print()
    play_dct['home_team'] = input("Your selected home team is: ")
    print()
    play_dct['away_team'] = input("Your selected away team is: ")
    print()
    print("Excellent! Make sure you read the output from the previous cell to make sure your home and away teams were set as desired.")
    print("Now let's move on; which team has the ball?")
    print()
    play_dct['posteam'] = input("The team with possession is: ")
    print()
    if play_dct['home_team'] == play_dct['posteam']:
        play_dct['posteam_type'] = 'home'
        play_dct['defteam'] = play_dct['away_team']
    else:
        play_dct['posteam_type'] = 'away'
        play_dct['defteam'] = play_dct['home_team']
    play_dct['td_team'] = play_dct['posteam']
    print("Great! That means that the", play_dct['posteam_type'], "team has the ball, and", play_dct['defteam'], "is defending!")
    print("Now let's get into the thick of it. What kind of play was just made? Your choices are between 'pass' and 'rush'.")
    print()
    play_dct['play_type'] = input("Choose your play type: ")
    play_dct[play_dct['play_type']+'_touchdown'] = 1
    print()
    if play_dct['play_type'] == 'pass':
        print("Who was throwing the ball? Be as creative as you want! Name should be formatted as follows:")
        print("First letter of first name, last name, ie. T. Brady, R. Wilson. ")
        print()
        play_dct['passer_player_name'] = input("Dream QB here please: ")
        print()
        print("Who was receiving the ball? Follow the same formatting as above!")
        print()
        play_dct['receiver_player_name'] = input("Best receiver in the NFL here please: ")
        print()
        print("Now a quickfire round: How many yards did the qb throw the ball, was it deep or short, and which direction?")
        print("The number of yards should be lesser than or equal to", str(play_dct['yards_gained']) + '.')
        print("Direction can be right, left or straight.")
        print()
        play_dct['air_yards'] = float(input("How far did the QB throw the pigskin: "))
        print()
        play_dct['yards_after_catch'] = play_dct['yards_gained'] - play_dct['air_yards']
        play_dct['pass_length'] = input("deep or short (watch the casing!): ")
        print()
        play_dct['pass_location'] = input("right, left or straight: ")
    elif play_dct['play_type'] == 'rush':
        print("Who was running the ball, and was it the QB? Name should be formatted as follows:")
        print("First letter of first name, last name, ie. T. Brady, R. Wilson.")
        print()
        play_dct['rusher_player_name'] = input("Most insane player on the team goes here: ")
        print()
        play_dct['qb_scramble'] = int(input('Would you say the QB was scrambling? Y/N please! ') == 'Y')
        print()
        print("And finally, which way did the rusher go? Valid answers include right, left, and straight. Watch the casing!")
        play_dct['run_location'] = input("right, left, or straight: ")
    print()
    print("And that's all that we need from you! Now watch as GPT-3 works its magic on your generated data object!")
    print("For reference here is what your object looks like: ")
    print()
    print(play_dct)
    print()
    print("Now we'll make an API call to GPT-3 and generate your customized commentary!")
    print()
    transcript = try_gpt(str(play_dct)).strip()
    print(transcript)
    return (play_dct, transcript)