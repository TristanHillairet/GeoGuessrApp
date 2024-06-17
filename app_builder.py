## June 2024
## Author: T.Hillairet
## Interface tools for application

##################################

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QListWidget
import geoguessr as gg
import plot as pl

def run_app():
    """
    Run the application
    """

    #
    # Create the application
    #
    app = QApplication.instance()
    if not app: 
        app = QApplication(sys.argv)

    #
    # Create the main window
    #
    fen = Window("GeoGuessr Stats App", 800, 600)
    fen.show()

    #
    # Create the Ajouter une partie window
    #
    fen2 = Window("Ajouter une partie", 400, 300)

    #
    # Add the widgets to the window Ajouter une partie
    #
    fen2.add_label("Map *")
    map = fen2.add_line_edit("")
    fen2.add_label("Mode *")
    mode = fen2.add_line_edit("")
    fen2.add_label("Score *")
    score = fen2.add_line_edit("")
    fen2.add_label("Time (MM:SS)")
    time = fen2.add_line_edit("00:00")
    fen2.add_label("Round 1")
    r1 = fen2.add_line_edit("")
    fen2.add_label("Round 2")
    r2 = fen2.add_line_edit("")
    fen2.add_label("Round 3")
    r3 = fen2.add_line_edit("")
    fen2.add_label("Round 4")
    r4 = fen2.add_line_edit("")
    fen2.add_label("Round 5")
    r5 = fen2.add_line_edit("")
    fen2.add_label("Contexte")
    context1 = fen2.add_line_edit("")
    fen2.add_label("Contexte 2")
    context2 = fen2.add_line_edit("")

    #
    # Add the button to the window Ajouter une partie
    #
    fen2_output = Window("Message de sortie", 200, 100, x=400, y=300)

    #
    # Def the action of the button Ajouter
    #
    def add_partie():
        map_text = str(map.text())
        mode_text = str(mode.text())
        score_text =int(score.text())
        time_text = gg.convert_duration_to_seconds(time.text())
        try:
            r1_text = int(r1.text())
        except:
            r1_text = None
        try:
            r2_text = int(r2.text())
        except:
            r2_text = None
        try:
            r3_text = int(r3.text())
        except:
            r3_text = None
        try:
            r4_text = int(r4.text())
        except:
            r4_text = None
        try:
            r5_text = int(r5.text())
        except:
            r5_text = None
        context1_text = str(context1.text())
        context2_text = str(context2.text())
        out_str = gg.add_data(map_text, mode_text, score_text, time_text, r1_text, r2_text, r3_text, r4_text, r5_text, context1_text, context2_text)
        fen2_output.add_label(out_str)
        fen2_output.add_button("OK",fen2_output.clear_all)
        fen2_output.show()
    fen2.add_button("Ajouter",add_partie)

    #
    # Add the button to the main window to open the Ajouter une partie window
    #
    def create_window_ajouter_partie():
        fen2.show()
    fen.add_button("Ajouter une Partie",create_window_ajouter_partie)

    #
    # Create the remove parties window
    #
    fen5 = Window("Supprimer des parties", 400, 300)

    #
    # Add the widgets to the window Supprimer des parties
    #
    fen5.add_label("Selections (champs1=valeur1,champs2=valeur2,...)")
    select_supp = fen5.add_line_edit("")
    fen5.add_label("!!! Attention, cette action est irréversible !!!")

    #
    # Output message window Supprimer des parties
    #
    fen5_output = Window("Message de sortie", 200, 100, x=400, y=300)

    #
    # Def the action of the button Supprimer
    #
    def remove_partie():
        select_suppr_text = str(select_supp.text())
        out_str = gg.remove_data(select_suppr_text)
        fen5_output.add_label(out_str)
        fen5_output.add_button("OK",fen5_output.clear_all)
        fen5_output.show()
    fen5.add_button("Supprimer",remove_partie)

    #
    # Add the button to the main window to open the Supprimer des parties window
    #
    def create_window_remove_parties():
        fen5.show()
    fen.add_button("Supprimer des parties",create_window_remove_parties)

    #
    # Create the Récupérer statistiques window
    #
    fen3 = Window("Récupérer statistiques", 400, 300)

    #
    # Add the widgets to the window Récupérer statistiques
    #
    fen3.add_label("Type de graphique")
    type_graph = fen3.add_list_widget(["Bar", "Histogramme", "Line", "TreeMap", "Box", "Scatter", "Stats"])
    fen3.add_label("Abscisses")
    abscisse = fen3.add_list_widget(["context_1","context_2","date","id","map","mode","nb5k","r1","r2","r3","r4","r5","score", "time"])
    fen3.add_label("Ordonnées")
    ordonnees = fen3.add_list_widget(["TotNumber","context_1","context_2","date","id","map","mode","nb5k","r1","r2","r3","r4","r5","score", "time"])
    fen3.add_label("Couleurs")
    couleurs = fen3.add_list_widget(["None","context_1","context_2","date","map","mode","nb5k","r1","r2","r3","r4","r5","score", "time"])
    fen3.add_label("Selections (champs1=valeur1,champs2=valeur2,...)")
    select = fen3.add_line_edit("All")

    #
    # Add the button to the window Récupérer statistiques
    #
    fen3_output = Window("Message de sortie", 200, 100, x=400, y=300)
    def create_graphique():
        type_graph_text = str(type_graph.currentItem().text())
        abscisse_text = str(abscisse.currentItem().text())
        ordonnees_text = str(ordonnees.currentItem().text())
        couleurs_text = str(couleurs.currentItem().text())
        select_text = str(select.text())
        out_str = pl.plot(type_graph_text,abscisse_text,ordonnees_text,couleurs_text,select_text)
        fen3_output.add_label(out_str)
        fen3_output.add_button("OK",fen3_output.clear_all)
        fen3_output.show()
    fen3.add_button("Créer le graphique",create_graphique)
    def create_window_recuperer_statistiques():
        fen3.show()
    fen.add_button("Récupérer statistiques",create_window_recuperer_statistiques)

    fen4 = Window("Aides", 400, 300)
    fen4.add_label("Bienvenue dans mon application pour explorer vos statistiques sur GeoGuessr\n"
                   "\n"
                   "Avec cette application vous pouvez :\n"
                   "- Ajouter une partie à vos statistiques existantes\n"
                   "- Récupérer des statistiques (des beaux graphiques)\n"
                   "\n"
                   "Pour ajouter une partie, cliquez sur le bouton 'Ajouter une Partie'\n"
                   "Une fois sur la page remplissez les champs qui vous sont demandés puis appuyez sur le boutons 'Ajouter'\n"
                   "\n"
                   "Pour récupérer des statistiques, cliquez sur le bouton 'Récupérer statistiques'\n"
                   "Une fois sur la page, choisissez le type de graphique que vous sohaitez dans la liste à gauche\n"
                   "Puis choisissez le champ à utiliser en abscisses dans la liste du milieu\n"
                   "Enfin choisissez le champ à utiliser en ordonnées dans la liste de droite\n"
                   "Appuyez sur le bouton 'Créer le graphique' pour afficher le graphique\n"
                   "!!! Attention, pour récupérer des statistiques, il faut avoir ajouté des parties !!!\n"
                   "\n"
                   "Si vous avez des questions ou des suggestions, n'hésitez pas à me contacter\n"
                   "discord : tpietav\n")
    def create_window_aides():
        fen4.show()
    fen.add_button("Aides",create_window_aides)

    app.exec_()

    return app

class Window(QWidget):

    def __init__(self, title, width, height, x=0, y=0):
        super().__init__()
        self.setWindowTitle(title)
        self.resize(width, height)
        self.move(x, y)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

    def add_button(self, text, func=None):

        button = QPushButton(text)
        button.clicked.connect(func)
        button.setStyleSheet("background-color: #f0f0f0")
        self.layout.addWidget(button)
        self.setLayout(self.layout)
        return button
    
    def add_label(self, text):
        label = QLabel(text)
        self.layout.addWidget(label)
        self.setLayout(self.layout)
        return label
    
    def add_line_edit(self, text):
        line_edit = QLineEdit(text)
        self.layout.addWidget(line_edit)
        self.setLayout(self.layout)
        return line_edit
    
    def add_list_widget(self, items):
        list_widget = QListWidget()
        for item in items:
            list_widget.addItem(item)
        self.layout.addWidget(list_widget)
        self.setLayout(self.layout)
        return list_widget
    
    def clear_all(self):
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().deleteLater()
    


if __name__ == "__main__":

    run_app()