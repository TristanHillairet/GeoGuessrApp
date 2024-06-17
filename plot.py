## June 2024
## Author: T.Hillairet
## Graphics buiders for GeoGuessr Stats App

###########################################

import plotly.express as px
from datetime import datetime
import os
import pandas as pd

path_directory = os.path.dirname(os.path.abspath(__file__))

def plot_bar(data,abscisse,ordonnees,color):
    try:
        fig = px.bar(data, x=abscisse, y=ordonnees, color=color)
        date = datetime.now().strftime("%Y-%m-%d")
        fig.write_image(f"{path_directory}/plots/bar_{abscisse}_{ordonnees}_{date}.png")
        fig.show()
        return f"{path_directory}/plots/bar_{abscisse}_{ordonnees}_{date}.png"
    except Exception as e:
        return f"Erreur lors de la création du graphique {e}"

def plot_box(data,abscisse,ordonnees,color):
    try:
        fig = px.box(data, x=abscisse, y=ordonnees, color=color)
        date = datetime.now().strftime("%Y-%m-%d")
        fig.write_image(f"{path_directory}/plots/box_{abscisse}_{ordonnees}_{date}.png")
        fig.show()
        return f"{path_directory}/plots/box_{abscisse}_{ordonnees}_{date}.png"
    except Exception as e:
        return f"Erreur lors de la création du graphique {e}"
    
def plot_hist(data,abscisse,ordonnees,color):
    try:
        fig = px.histogram(data, x=abscisse, y=ordonnees, color=color)
        date = datetime.now().strftime("%Y-%m-%d")
        fig.write_image(f"{path_directory}/plots/hist_{abscisse}_{ordonnees}_{date}.png")
        fig.show()
        return f"{path_directory}/plots/hist_{abscisse}_{ordonnees}_{date}.png"
    except Exception as e:
        return f"Erreur lors de la création du graphique {e}"

def plot_line(data,abscisse,ordonnees,color):
    try:
        fig = px.line(data, x=abscisse, y=ordonnees,color=color)
        date = datetime.now().strftime("%Y-%m-%d")
        fig.write_image(f"{path_directory}/plots/line_{abscisse}_{ordonnees}_{date}.png")
        fig.show()
        return f"{path_directory}/plots/line_{abscisse}_{ordonnees}_{date}.png"
    except Exception as e:
        return f"Erreur lors de la création du graphique {e}"

def plot_scatter(data,abscisse,ordonnees,color):
    try:
        fig = px.scatter(data, x=abscisse, y=ordonnees,color=color)
        fig.update_traces(marker_size=10)
        date = datetime.now().strftime("%Y-%m-%d")
        fig.write_image(f"{path_directory}/plots/scatter_{abscisse}_{ordonnees}_{date}.png")
        fig.show()
        return f"{path_directory}/plots/scatter_{abscisse}_{ordonnees}_{date}.png"
    except Exception as e:
        return f"Erreur lors de la création du graphique {e}"

def plot_treemap(data,abscisse,ordonnees,color):
    try:
        fig = px.treemap(data, path=[abscisse], values=ordonnees, color=color)
        date = datetime.now().strftime("%Y-%m-%d")
        fig.write_image(f"{path_directory}/plots/treemap_{abscisse}_{ordonnees}_{date}.png")
        fig.show()
        return f"{path_directory}/plots/treemap_{abscisse}_{ordonnees}_{date}.png"
    except Exception as e:
        return f"Erreur lors de la création du graphique {e}"

def plot_stats(data):
    return str(data.describe())
    

def plot(type,abscisse,ordonnees,color,sel):

    data = pd.read_csv(f'{path_directory}/data/geoguessr.csv')

    if not sel == "All":
        sel = sel.split(",")
        for s in sel:
            s = s.split("=")
            data = data[data[s[0]] == s[1]]
    
    if ordonnees == "TotNumber":
        data = pd.DataFrame(dict(data[abscisse].value_counts()).items(), columns=[abscisse,ordonnees])
    
    if color == "None":
        color = abscisse
    
    if type == "Bar":
        str = plot_bar(data,abscisse,ordonnees,color)
    
    elif type == "Box":
        str = plot_box(data,abscisse,ordonnees,color)
    
    elif type == "Histogramme":
        str = plot_hist(data,abscisse,ordonnees,color)
    
    elif type == "Line":
        str = plot_line(data,abscisse,ordonnees,color)
    
    elif type == "Scatter":
        str = plot_scatter(data,abscisse,ordonnees,color)
    
    elif type == "Stats":
        str = plot_stats(data)

    elif type == "TreeMap":
        str = plot_treemap(data,abscisse,ordonnees,color)
    
    return str
    
