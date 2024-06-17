### June 2024
### Author: T.Hillairet
### Script to set up GeoGuessr DataFrames

#########################################

import pandas as pd
import os
from datetime import datetime

path_directory = os.path.dirname(os.path.abspath(__file__))

def create_data():
    """
    Create the data from the csv file
    """
    data = pd.DataFrame(columns=['id','date','map','mode','score','time','r1','r2','r3','r4','r5','nb5k','context_1','context_2'])
    data.to_csv(f'{path_directory}/data/geoguessr.csv', index=False)

def load_data():
    """
    Load the data from the csv file
    """
    try:
        data = pd.read_csv(f'{path_directory}/data/geoguessr.csv')
    except:
        create_data()
        data = pd.read_csv(f'{path_directory}/data/geoguessr.csv')
    return data

def add_data(map, mode, score, time, r1, r2, r3, r4, r5, context_1, context_2):
    """
    Add data to the csv file
    """
    try:
        if map == "":
            map = None
        if mode == "":
            mode = None
        if score == "":
            score = None
        if time == "":
            time = None
        if r1 == "":
            r1 = None
        if r2 == "":
            r2 = None
        if r3 == "":
            r3 = None
        if r4 == "":
            r4 = None
        if r5 == "":
            r5 = None
        if context_1 == "":
            context_1 = None
        if context_2 == "":
            context_2 = None
        data = load_data()
        id = len(data)
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        nb5k = [r1, r2, r3, r4, r5].count(5000)
        attr = [id, date, map, mode, score, time, r1, r2, r3, r4, r5, nb5k, context_1, context_2]
        data.loc[len(data)] = attr
        data.to_csv(f'{path_directory}/data/geoguessr.csv', index=False)
        return f"Partie {id} ajoutée:\n- {map}\n- {mode}\n- {score}\n- {time}\n- {r1}\n- {r2}\n- {r3}\n- {r4}\n- {r5}\n- {nb5k}\n- {context_1}\n- {context_2}"
    except Exception as e:
        return f"Erreur lors de l'ajout de la partie: {e}"

def remove_data(sel):

    try:
        data = load_data()
        if not sel == "":
            sel = sel.split(",")
            for s in sel:
                s = s.split("=")
                nb = len(data[data[s[0]] == s[1]])
                data = data[data[s[0]] != s[1]]

        data.to_csv(f'{path_directory}/data/geoguessr.csv', index=False)

        return f"{nb} Parties supprimées: {sel}"
    
    except Exception as e:
        return f"Erreur lors de la suppression des parties: {e}"

def convert_duration_to_seconds(duration):
    """
    Convert a duration string in the format "MM:SS" to seconds (int)
    """
    minutes, seconds = duration.split(":")
    total_seconds = int(minutes) * 60 + int(seconds)
    return total_seconds