import tkinter as tk #on importe le module tkinter et on ajoute un alias: "tk"
import os #on importe le module os
import sqlite3 #on importe le module de base de donnée sqlite

conn = sqlite3.connect('imdb.db')#on se connecte à la base de donnée imdb.db
c = conn.cursor() 

#requêtes sous la forme de dictionnaire::
req3={"Combien y a-t-il de titres dans cette base de données ?": "SELECT COUNT(primaryName) FROM name_basics ;"} #requête n°3
req4={"En quelle année est sortie le film The Godfather ?": "SELECT startYear FROM title_basics WHERE primaryTitle='The Godfather';"} #requête n°4
req5={"En quelle année est sortie le premier film Superman ?": "SELECT startYear FROM title_basics WHERE primaryTitle='Superman';"} #requête n°5
req6={"Quel est le titre original du film 'Les dents de la mer' ?": "SELECT startYear FROM title_basics WHERE primaryTitle='Superman';"} #requête n°6
req7={"Quel est le métier d’Olivier Nakache ?": "SELECT originalTitle FROM title_basics WHERE primaryTitle='Jaws';"} #requête n°7
req8={"Quels sont les films d’Olivier Nakache ?": "SELECT primaryProfession FROM name_basics WHERE primaryName='Olivier Nakache'"} #requête n°
req9={"Quel est le film ayant recueilli le plus de votes ?":"SELECT primaryTitle FROM title_writers JOIN title_basics ON title_writers.tconst = title_basics.tconst WHERE writers=619923"} #requête n°9
req10={"Qui a écrit le scénario du film Taxi sorti en 1998 ?": "SELECT MAX(numVotes),primaryTitle FROM title_ratings JOIN title_basics ON title_ratings.tconst = title_basics.tconst;"} #requête n°10
# req11={"": ""}  #requête n°11
req12={"Quels sont les titres des films notés plus de 9 sur 10 avec plus de 10 000 votes ?": "SELECT primaryTitle,numVotes,averageRating FROM title_ratings JOIN title_basics ON title_ratings.tconst = title_basics.tconst WHERE averageRating>=9 AND numVotes>=10000;"} #requête n°12
req13={"Quelle sont les 5 comédies romantiques les mieux notées ?": "SELECT numVotes,primaryTitle,genres FROM title_ratings JOIN title_basics ON title_ratings.tconst = title_basics.tconst WHERE genres='Romance' ORDER BY numVotes DESC LIMIT 5;"} #requête n°13
req14={"Quels sont les 10 films d’animation ayant reçu plus de 1000 votes les mieux notés ?": "SELECT numVotes,primaryTitle,genres FROM title_ratings JOIN title_basics ON title_ratings.tconst = title_basics.tconst WHERE genres='Animation' AND numVotes>1000 ORDER BY numVotes DESC LIMIT 10;"} #requête n°14
req15={"Combien de films durent plus de 3 heures ?": "SELECT COUNT(primaryTitle) FROM title_basics WHERE runtimeMinutes>=180;"} #requête n°15

# Fonction d'execution des requête:

def sql3():#fonction représentant la requête n°3
    c.execute(req3["Combien y a-t-il de titres dans cette base de données ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on récupére tout les résultat sous la forme d'une liste
        print(list(row))

def sql4():#fonction représentant la requête n°4
    c.execute(req4["En quelle année est sortie le film The Godfather ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on récupére tout les résultat sous la forme d'une liste
        print(list(row))

def sql5():#fonction représentant la requête n°5
    c.execute(req5["En quelle année est sortie le premier film Superman ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on récupére tout les résultat sous la forme d'une liste
        print(list(row))

def sql6():#fonction représentant la requête n°6
    c.execute(req6["Quel est le titre original du film 'Les dents de la mer' ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on récupére tout les résultat sous la forme d'une liste
        print(list(row))

def sql7():#fonction représentant la requête n°7
    c.execute(req7["Quel est le métier d’Olivier Nakache ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on récupére tout les résultat sous la forme d'une liste
        print(list(row))

def sql8():#fonction représentant la requête n°8
    c.execute(req8["Quels sont les films d’Olivier Nakache ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on récupére tout les résultat sous la forme d'une liste
        print(list(row))
        
def sql9():#fonction représentant la requête n°9
    c.execute(req9["Quel est le film ayant recueilli le plus de votes ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on récupére tout les résultat sous la forme d'une liste
        print(list(row))

def sql10():#fonction représentant la requête n°10
    c.execute(req10["Qui a écrit le scénario du film Taxi sorti en 1998 ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on récupére tout les résultat sous la forme d'une liste
        print(list(row))

"""
def sql11():#fonction représentant la requête n°11
    c.execute(req11["Combien de films durent plus de 3 heures ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on récupére tout les résultat sous la forme d'une liste
        print(list(row))
"""

def sql12():#fonction représentant la requête n°12
    c.execute(req12["Quels sont les titres des films notés plus de 9 sur 10 avec plus de 10 000 votes ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on récupére tout les résultat sous la forme d'une liste
        print(list(row))

def sql13():#fonction représentant la requête n°13
    c.execute(req13["Quelle sont les 5 comédies romantiques les mieux notées ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on récupére tout les résultat sous la forme d'une liste
        print(list(row))

def sql14():#fonction représentant la requête n°14
    c.execute(req14["Quels sont les 10 films d’animation ayant reçu plus de 1000 votes les mieux notés ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on récupére tout les résultat sous la forme d'une liste
        print(list(row))

def sql15():#fonction représentant la requête n°15
    c.execute(req15["Combien de films durent plus de 3 heures ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on récupére tout les résultat sous la forme d'une liste
        print(list(row))


#vider la console python:
def ClearCmd():
    clear = lambda: os.system('cls') #on nettoye la console en supprimant les résultats précédents 
    clear()

#affichage de l'interface avec tkinter: 
class affichage(tk.Tk): #création de la classe affichage avec comme argument tk.Tk

    def __init__(self, *args, **kwargs): #initialisation de la classe avec une méthode __init__, et avec comme argument *args, **kwargs qui permettent de récupérer des arguments et de faire ce que l'on appel du "packing"
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self) #on créer un container avec dedans la page affiché par tkinter
        container.pack(side="top",fill="both",expand=True) # défini la position des widget, Sidé="top" détermine la position du widget parent, fill="both" remplir à la fois horizontalement et verticalement tout espace supplémentaire qui lui est alloué par le parent. Et enfin expand=True fait que le widget utilise tout espace non utilisé.
        container.grid_rowconfigure(0,weight=1) #on configure la page à la taille minimum 
        container.grid_columnconfigure(0,weight=1)
        self.frames={} #on créer un dictionnaire vide pour la page
        frame=StartPage(container, self) #frame renvoie à la classe StartPage servant à lancer la page.
        self.frames[StartPage]=frame 
        frame.grid(row=0,column=0,sticky="nsew") # on créer une "grille" avec, pour l'instant aucune colonm ni ligne. Et sticky=nsew signifie north south east west, soit nord sud est ouest en fançais, celà permet de cadré la page selon une "boussole".
        self.show_frame(StartPage) # fait appel à la méthode qui affiche la page.

    def show_frame(self,cont):#cration de la methode qui affiche la page avec comme argument self et cont pour controller
        frame=self.frames[cont] #correspond à tout les cadres utilisé
        frame.tkraise() #affiche la page 

#police utiliser dans l'affichage de la page
Titre=("arial", 20)
TaillePolice=("time new roman", 12)
clear=("time new roman", 20)

# lancement de la page:
class StartPage(tk.Frame): #création de la classe StartPage avec comme argument tk.Frame, soit tous ce qu'il y a dans la page

    def __init__(self,parent,controller): #initialisation de la classe avec une méthode __init__, et avec comme argument parent et controller
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Requête SQL :", font=Titre) #label permet d'ajouté du texte à la page, ici, Requête SQL :, et avec font représentant la police correspondante.
        label.pack(pady=50,padx=400) #on pack le texte dans la page avec une marge de 50px en haute et 400px en largeur
        #on créer des bouton executant les fonctions de requêtes sql fait plus tôt. les argument text représente ce qu'il y a d'écrit sur les bouton, command représente la fonction a executé, et font la police choisi.
        button1=tk.Button(self,text="RequêteSQL3", command=sql3, font=TaillePolice)
        button2=tk.Button(self,text="RequêteSQL4", command=sql4, font=TaillePolice)
        button3=tk.Button(self,text="RequêteSQL5", command=sql5, font=TaillePolice)
        button4=tk.Button(self,text="RequêteSQL6", command=sql6, font=TaillePolice)
        button5=tk.Button(self,text="RequêteSQL7", command=sql7, font=TaillePolice)
        button6=tk.Button(self,text="RequêteSQL8", command=sql8, font=TaillePolice)
        button7=tk.Button(self,text="RequêteSQL9", command=sql9, font=TaillePolice)
        button8=tk.Button(self,text="RequêteSQL10", command=sql10, font=TaillePolice)
        # button9=tk.Button(self,text="RequêteSQL11", command=sql15, font=TaillePolice)
        button10=tk.Button(self,text="RequêteSQL12", command=sql12, font=TaillePolice)
        button11=tk.Button(self,text="RequêteSQL13", command=sql13, font=TaillePolice)
        button12=tk.Button(self,text="RequêteSQL14", command=sql14, font=TaillePolice)
        button13=tk.Button(self,text="RequêteSQL15", command=sql15, font=TaillePolice)
        button14=tk.Button(self,text="Vider la console", command=ClearCmd, font=clear)
        #on pack les boutton avec une marge de 10px en hauteur et 400 en largeur
        button1.pack(pady=10,padx=400)
        button2.pack(pady=10,padx=400)
        button3.pack(pady=10,padx=400)
        button4.pack(pady=10,padx=400)
        button5.pack(pady=10,padx=400)
        button6.pack(pady=10,padx=400)
        button7.pack(pady=10,padx=400)
        button8.pack(pady=10,padx=400)
        # button9.pack()
        button10.pack(pady=10,padx=400)
        button11.pack(pady=10,padx=400)
        button12.pack(pady=10,padx=400)
        button13.pack(pady=10,padx=400)
        button14.pack(pady=10,padx=400)
        
app=affichage() #on assigne la classe principal: affichage à la variable app
app.mainloop() #permet de lancer tout les événement de la page, soit la démarrer

