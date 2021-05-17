from tkinter import * #on importe l'ensemble du module tkinter
from tkinter import ttk #on importe ttk du module tkinter
from prettytable import PrettyTable #on importe PrettyTable du module prettytable
import sqlite3 #on importe le module sqlite3
import os #on importe le module os

conn = sqlite3.connect('imdb.db')#on se connecte à la base de donnée imdb.db
c = conn.cursor()#permettra plus tard d'effectuer les requêtes SQL.

#on créer des variable nommé query qui ouvre les fichier sql correspondant au requête sql de 1 à 21, pour ce faire on utilise la command with open qui permet d'en ouvrir plusieurs, et a aussi l'avantage de fermer
# automatiquement les fichier une fois que l'on en a plus besoin.
with open('requêtes/req1.sql') as query1, \
        open('requêtes/req2.sql') as query2, \
            open('requêtes/req3.sql') as query3, \
                open('requêtes/req4.sql') as query4, \
                    open('requêtes/req5.sql') as query5, \
                        open('requêtes/req6.sql') as query6, \
                            open('requêtes/req7.sql') as query7, \
                                open('requêtes/req8.sql') as query8, \
                                    open('requêtes/req9.sql') as query9, \
                                        open('requêtes/req10.sql') as query10, \
                                            open('requêtes/req11.sql') as query11, \
                                                open("requêtes/req12.sql","r") as query12, \
                                                    open("requêtes/req13.sql","r")as query13, \
                                                        open("requêtes/req14.sql","r")as query14 ,\
                                                            open("requêtes/req15.sql","r")as query15 ,\
                                                                open("requêtes/req16.sql","r")as query16 ,\
                                                                    open("requêtes/req17.sql","r")as query17, \
                                                                        open("requêtes/req18.sql","r") as query18, \
                                                                            open("requêtes/req19.sql","r") as query19, \
                                                                                open("requêtes/req20.sql","r") as query20:

    query21=open("requêtes/req21.sql","r")#on ouvre le fichier req21.sql avec la commande open, étant donnée que l'on ne peux pas dépasser une fonction avec plus de 20 retour à la ligne on ouvre ce fichier a part des autres.
    #requêtes sous la forme de dictionnaire:
    req1={"Quels sont les différents types de titres dans cette base de données ?": query1.read()} #requête n°1
    req2={"Combien y a-t-il de titres dans cette base de données ?": query2.read()} #requête n°2
    req3={"En quelle année est sortie le film The Godfather ?": query3.read()} #requête n°3
    req4={"En quelle année est sortie le premier film Superman ?": query4.read()} #requête n°4
    req5={"Quel est le titre original du film 'Les dents de la mer' ?": query5.read()} #requête n°5
    req6={"Quel est le métier d’Olivier Nakache ?": query6.read()} #requête n°6
    req7={"Quels sont les films d’Olivier Nakache ?": query7.read()} #requête n°7
    req8={"Quel est le film ayant recueilli le plus de votes ?": query8.read()} #requête n°8
    req9={"Qui a écrit le scénario du film Taxi sorti en 1998 ?": query9.read()} #requête n°9
    req10={"Quelles sont les noms et rôles (category et job) des personnes intervenant dans la production du film Return of the Jedi ?": query10.read()}  #requête n°10
    req11={"Quels sont les titres des films notés plus de 9 sur 10 avec plus de 10 000 votes ?": query11.read()} #requête n°11
    req12={"Quelle sont les 5 comédies romantiques les mieux notées ?": query12.read()} #requête n°12
    req13={"Quels sont les 10 films d’animation ayant reçu plus de 1000 votes les mieux notés ?": query13.read()} #requête n°13
    req14={"Combien de films durent plus de 3 heures ?": query14.read()} #requête n°14
    req15={"Quelle est la durée moyenne d’un film ?": query15.read()} #requête n°15
    req16={"Quel est le film le plus long ?": query16.read()} #requête n°16
    req17={"Quels sont les 5 films les plus longs ?": query17.read()} #requête n°17
    req18={"Quels sont les titres des films les plus connus de Sean Connery ?": query18.read()} #requête n°18
    req19={"Quels sont les acteurs ayant joué le rôle de James Bond, et dans quels films ?": query19.read()} #requête n°19
    req20={"Quel sont les réalisateurs ayant fait les cinq film les mieux notés ? Indiquer les noms des films correspondants.": query20.read()} #requête n°20
    req21={"Quels sont les noms des épisodes de Game of Thrones ?": query21.read()} #requête n°21
    query21.close()#permet de fermer le fichier ouvert une fois que l'on en avons plus besoin.


def pretty_print(list, ligne="-", trait="|", angles="+"):
    """
    Fonction permettant de transformer une liste de liste en tableau.
    Arguments: 
        liste: la liste à mettre sous forme de tableau.
        ligne: charactère "-" pour délimiter les lignes du tableau.
        trait: charactère "|" pour délimiter les colonnes du tableau.
        angles: charactère "+" pour faire les angles du tableau.
    """
    #Si la liste est vide renvoie None.
    if len(list) == 0:
        return
    #détermine la longueur max de la liste:
    longueur_max = [
        max(colonnes)for colonnes in zip(*[[len(cell) for cell in row] for row in list])]
    #affiche les lignes et colonnes en fonction de la taille de la liste:
    for i in list:
        print(angles.join(["", *[ligne * l for l in longueur_max], ""]))
        print(trait.join(["", *[("{:<" + str(l) + "}").format(c)for l, c in zip(longueur_max, i)],"",]))
    print(angles.join(["", *[ligne * l for l in longueur_max], ""]))



# Fonction d'execution des requête:
#on va devoir créer plusieurs variables différentes pour les résultats en tableaux ASCII car si on en créer qu'une tous les résultats apparaîtront dans le même tableau, ce que nous ne voulons pas.
TableAscii=[]
def sql1():#fonction représentant la requête n°1
    c.execute(req1["Quels sont les différents types de titres dans cette base de données ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on parcour les résultats
        TableAscii.append(list(row))#on prend le résultat de la requête que l'on met dans un tableau ASCII
    pretty_print(TableAscii)

    root = Tk() #on créer une fenetre dans laquel va s'afficher le résultat de la requête
    Titre = ttk.Label(root, text=str(TableAscii),font="Courier 18")#on créer une zone de texte où vas s'afficher le résultat avec une police Courier 18
    Titre.pack()#on pack la zone de texte pour lui permettre de s'afficher sur la page 
    Close=Button(root,text="fermer la fenêtre",command=root.destroy,font="Calibri 18")
    Close.pack()

TableAscii1=PrettyTable()#on créer une variable tableAscii1 avec comme valeur PrettyTable() permettant d'afficher les tableau sous une plus belle forme, en ASCII.
def sql2():#fonction représentant la requête n°2
    c.execute(req2["Combien y a-t-il de titres dans cette base de données ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on parcour les résultats
        TableAscii1.add_rows([list(row)])#on prend le résultat de la requête que l'on met dans un tableau ASCII
    TableAscii1.field_names = ["primaryName"]
    root = Tk() #on créer une fenetre dans laquel va s'afficher le résultat de la requête
    Titre = ttk.Label(root, text=str(TableAscii1),font="Courier 18")#on créer une zone de texte où vas s'afficher le résultat avec une police Courier 18
    Titre.pack()#on pack la zone de texte pour lui permettre de s'afficher sur la page
    Close=Button(root,text="fermer la fenêtre",command=root.destroy,font="Calibri 18")
    Close.pack()

TableAscii2=PrettyTable()#on créer une variable tableAscii2 avec comme valeur PrettyTable() permettant d'afficher les tableau sous une plus belle forme, en ASCII.
def sql3():#fonction représentant la requête n°3
    c.execute(req3["En quelle année est sortie le film The Godfather ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on parcour les résultats
        TableAscii2.add_rows([list(row)])#on prend le résultat de la requête que l'on met dans un tableau ASCII    
    TableAscii2.field_names = ["startYear"]
    root = Tk() #on créer une fenetre dans laquel va s'afficher le résultat de la requête
    Titre = ttk.Label(root, text=str(TableAscii2),font="Courier 18")#on créer une zone de texte où vas s'afficher le résultat avec une police Courier 18
    Titre.pack()#on pack la zone de texte pour lui permettre de s'afficher sur la page   
    Close=Button(root,text="fermer la fenêtre",command=root.destroy,font="Calibri 18")
    Close.pack()

TableAscii3=PrettyTable()#on créer une variable tableAscii3 avec comme valeur PrettyTable() permettant d'afficher les tableau sous une plus belle forme, en ASCII.
def sql4():#fonction représentant la requête n°4
    c.execute(req4["En quelle année est sortie le premier film Superman ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on parcour les résultats
        TableAscii3.add_rows([list(row)])#on prend le résultat de la requête que l'on met dans un tableau ASCII  
    TableAscii3.field_names = ["startYear"]
    root = Tk() #on créer une fenetre dans laquel va s'afficher le résultat de la requête
    Titre = ttk.Label(root, text=str(TableAscii3),font="Courier 18")#on créer une zone de texte où vas s'afficher le résultat avec une police Courier 18
    Titre.pack()#on pack la zone de texte pour lui permettre de s'afficher sur la page 
    Close=Button(root,text="fermer la fenêtre",command=root.destroy,font="Calibri 18")
    Close.pack()

TableAscii4=PrettyTable()#on créer une variable tableAscii4 avec comme valeur PrettyTable() permettant d'afficher les tableau sous une plus belle forme, en ASCII.
def sql5():#fonction représentant la requête n°5
    c.execute(req5["Quel est le titre original du film 'Les dents de la mer' ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on parcour les résultats
        TableAscii4.add_rows([list(row)])#on prend le résultat de la requête que l'on met dans un tableau ASCII    
    TableAscii4.field_names = ["originalTitle"]
    root = Tk() #on créer une fenetre dans laquel va s'afficher le résultat de la requête
    Titre = ttk.Label(root, text=str(TableAscii4),font="Courier 18")#on créer une zone de texte où vas s'afficher le résultat avec une police Courier 18
    Titre.pack()#on pack la zone de texte pour lui permettre de s'afficher sur la page 
    Close=Button(root,text="fermer la fenêtre",command=root.destroy,font="Calibri 18")
    Close.pack()

TableAscii5=PrettyTable()#on créer une variable tableAscii5 avec comme valeur PrettyTable() permettant d'afficher les tableau sous une plus belle forme, en ASCII.
def sql6():#fonction représentant la requête n°6
    c.execute(req6["Quel est le métier d’Olivier Nakache ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on parcour les résultats
        TableAscii5.add_rows([list(row)])#on prend le résultat de la requête que l'on met dans un tableau ASCII    
    TableAscii5.field_names = ["primaryProfession"]
    root = Tk() #on créer une fenetre dans laquel va s'afficher le résultat de la requête
    Titre = ttk.Label(root, text=str(TableAscii5),font="Courier 18")#on créer une zone de texte où vas s'afficher le résultat avec une police Courier 18
    Titre.pack()#on pack la zone de texte pour lui permettre de s'afficher sur la page 
    Close=Button(root,text="fermer la fenêtre",command=root.destroy,font="Calibri 18")
    Close.pack()

TableAscii6=PrettyTable()#on créer une variable tableAscii6 avec comme valeur PrettyTable() permettant d'afficher les tableau sous une plus belle forme, en ASCII.
def sql7():#fonction représentant la requête n°7
    c.execute(req7["Quels sont les films d’Olivier Nakache ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on parcour les résultats
        TableAscii6.add_rows([list(row)])#on prend le résultat de la requête que l'on met dans un tableau ASCII    
    TableAscii6.field_names = ["primaryTitle"]
    root = Tk() #on créer une fenetre dans laquel va s'afficher le résultat de la requête
    Titre = ttk.Label(root, text=str(TableAscii6),font="Courier 18")#on créer une zone de texte où vas s'afficher le résultat avec une police Courier 18
    Titre.pack()#on pack la zone de texte pour lui permettre de s'afficher sur la page 
    Close=Button(root,text="fermer la fenêtre",command=root.destroy,font="Calibri 18")
    Close.pack()

TableAscii7=PrettyTable()#on créer une variable tableAscii7 avec comme valeur PrettyTable() permettant d'afficher les tableau sous une plus belle forme, en ASCII.
def sql8():#fonction représentant la requête n°8
    c.execute(req8["Quel est le film ayant recueilli le plus de votes ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on parcour les résultats
        TableAscii7.add_rows([list(row)])#on prend le résultat de la requête que l'on met dans un tableau ASCII    
    TableAscii7.field_names = ["Max(numVotes)","primaryTitle"]
    root = Tk() #on créer une fenetre dans laquel va s'afficher le résultat de la requête
    Titre = ttk.Label(root, text=str(TableAscii7),font="Courier 18")#on créer une zone de texte où vas s'afficher le résultat avec une police Courier 18
    Titre.pack()#on pack la zone de texte pour lui permettre de s'afficher sur la page 
    Close=Button(root,text="fermer la fenêtre",command=root.destroy,font="Calibri 18")
    Close.pack()

TableAscii8=PrettyTable()#on créer une variable tableAscii8 avec comme valeur PrettyTable() permettant d'afficher les tableau sous une plus belle forme, en ASCII.
def sql9():#fonction représentant la requête n°9
    c.execute(req9["Qui a écrit le scénario du film Taxi sorti en 1998 ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on parcour les résultats
        TableAscii8.add_rows([list(row)])#on prend le résultat de la requête que l'on met dans un tableau ASCII    
    TableAscii8.field_names = ["primaryName"]
    root = Tk() #on créer une fenetre dans laquel va s'afficher le résultat de la requête
    Titre = ttk.Label(root, text=str(TableAscii8),font="Courier 18")#on créer une zone de texte où vas s'afficher le résultat avec une police Courier 18
    Titre.pack()#on pack la zone de texte pour lui permettre de s'afficher sur la page 
    Close=Button(root,text="fermer la fenêtre",command=root.destroy,font="Calibri 18")
    Close.pack()


TableAscii9=PrettyTable()#on créer une variable tableAscii9 avec comme valeur PrettyTable() permettant d'afficher les tableau sous une plus belle forme, en ASCII.
def sql10():#fonction représentant la requête n°10
    c.execute(req10["Quelles sont les noms et rôles (category et job) des personnes intervenant dans la production du film Return of the Jedi ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on parcour les résultats
        TableAscii10.add_rows([list(row)])#on prend le résultat de la requête que l'on met dans un tableau ASCII    
    TableAscii10.field_names = ["primaryName","primaryProfession"]
    root = Tk() #on créer la racine de l'affichage tkinter
    root.geometry("1000x800")#on défini la taille de la page
    #on créer la fenêtre principal
    fenetre1=Frame(root)#on créer une variable fenetre1 avec comme valeur une fenetre
    fenetre1.pack(side=TOP,fill=BOTH,expand=1) #On défini la position du widget fill="both" remplir à la fois horizontalement et verticalement tout espace supplémentaire qui lui est alloué par le parent. Et enfin expand=True fait que le widget utilise tout espace non utilisé.
    #on créer un "canvas"  qui nous permettra de créer notre scrollbar.
    canvas1=Canvas(fenetre1) #on créer la variable canvas1 avec comme valeur un canvas de la fenêtre1
    canvas1.pack(side=LEFT,fill=BOTH,expand=1)#on pack le canvas pour l'afficher dans la fenêtre
    #On créer notre scrollbar
    scrollbarVertical=ttk.Scrollbar(fenetre1, orient=VERTICAL, command=canvas1.yview)#on créer une variable scrollbarVertical avec comme valeur la fenetre1, avec comme orientation vertical pour défiler la page de haute en bas, avec comme commande l'axe y du cavas1 
    scrollbarVertical.pack(side=RIGHT, fill=Y)#on pack notre scrollbar pour l'afficher sur la page.
    #configure canvas
    canvas1.configure(yscrollcommand=scrollbarVertical.set)
    canvas1.bind('<Configure>', lambda e: canvas1.configure(scrollregion=canvas1.bbox("all")))
    #seconde fenetre
    fenetre2=Frame(canvas1)
    #ajouter seconde fenetre and la page du canvas
    canvas1.create_window((0,0),window=fenetre2, anchor="nw")
    #on créer des bouton executant les fonctions de requêtes sql fait plus tôt. les argument text représente ce qu'il y a d'écrit sur les bouton, command représente la fonction a executé, et font la police choisi.
    Titre = ttk.Label(fenetre2, text=str(TableAscii10),font="Courier 14")#on créer un label sur lequel on écrit le titre dans la première fenêtre, avec un police Courier 18
    Titre.pack() #on pack le Titre pour lui permettre de s'afficher sur la page
    Close=Button(root,text="fermer la fenêtre",command=root.destroy,font="Calibri 18")
    Close.pack()
    root.mainloop() #permet de lancer tout les événement de la page, soit la démarrer.


TableAscii10=PrettyTable()#on créer une variable tableAscii10 avec comme valeur PrettyTable() permettant d'afficher les tableau sous une plus belle forme, en ASCII.
def sql11():#fonction représentant la requête n°11
    c.execute(req11["Quels sont les titres des films notés plus de 9 sur 10 avec plus de 10 000 votes ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on parcour les résultats
        TableAscii10.add_rows([list(row)])#on prend le résultat de la requête que l'on met dans un tableau ASCII    
    TableAscii10.field_names = ["primaryTitle","numVotes","averageRating"]
    root = Tk() #on créer la racine de l'affichage tkinter
    root.geometry("1000x800")#on défini la taille de la page
    #on créer la fenêtre principal
    fenetre1=Frame(root)#on créer une variable fenetre1 avec comme valeur une fenetre
    fenetre1.pack(side=TOP,fill=BOTH,expand=1) #On défini la position du widget fill="both" remplir à la fois horizontalement et verticalement tout espace supplémentaire qui lui est alloué par le parent. Et enfin expand=True fait que le widget utilise tout espace non utilisé.
    #on créer un "canvas"  qui nous permettra de créer notre scrollbar.
    canvas1=Canvas(fenetre1) #on créer la variable canvas1 avec comme valeur un canvas de la fenêtre1
    canvas1.pack(side=LEFT,fill=BOTH,expand=1)#on pack le canvas pour l'afficher dans la fenêtre
    #On créer notre scrollbar
    scrollbarVertical=ttk.Scrollbar(fenetre1, orient=VERTICAL, command=canvas1.yview)#on créer une variable scrollbarVertical avec comme valeur la fenetre1, avec comme orientation vertical pour défiler la page de haute en bas, avec comme commande l'axe y du cavas1 
    scrollbarVertical.pack(side=RIGHT, fill=Y)#on pack notre scrollbar pour l'afficher sur la page.
    #configure canvas
    canvas1.configure(yscrollcommand=scrollbarVertical.set)
    canvas1.bind('<Configure>', lambda e: canvas1.configure(scrollregion=canvas1.bbox("all")))
    #seconde fenetre
    fenetre2=Frame(canvas1)
    #ajouter seconde fenetre and la page du canvas
    canvas1.create_window((0,0),window=fenetre2, anchor="nw")
    #on créer des bouton executant les fonctions de requêtes sql fait plus tôt. les argument text représente ce qu'il y a d'écrit sur les bouton, command représente la fonction a executé, et font la police choisi.
    Titre = ttk.Label(fenetre2, text=str(TableAscii10),font="Courier 16")#on créer un label sur lequel on écrit le titre dans la première fenêtre, avec un police Courier 18
    Titre.pack() #on pack le Titre pour lui permettre de s'afficher sur la page
    Close=Button(root,text="fermer la fenêtre",command=root.destroy,font="Calibri 18")
    Close.pack()
    root.mainloop() #permet de lancer tout les événement de la page, soit la démarrer.

TableAscii11=PrettyTable()#on créer une variable tableAscii11 avec comme valeur PrettyTable() permettant d'afficher les tableau sous une plus belle forme, en ASCII.
def sql12():#fonction représentant la requête n°12
    c.execute(req12["Quelle sont les 5 comédies romantiques les mieux notées ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on parcour les résultats
        TableAscii11.add_rows([list(row)])#on prend le résultat de la requête que l'on met dans un tableau ASCII    
    TableAscii11.field_names = ["numVotes","primaryTitle","genres"]
    root = Tk() #on créer une fenetre dans laquel va s'afficher le résultat de la requête
    Titre = ttk.Label(root, text=str(TableAscii11),font="Courier 18")#on créer une zone de texte où vas s'afficher le résultat avec une police Courier 18
    Titre.pack()#on pack la zone de texte pour lui permettre de s'afficher sur la page 
    Close=Button(root,text="fermer la fenêtre",command=root.destroy,font="Calibri 18")
    Close.pack()

TableAscii12=PrettyTable()#on créer une variable tableAscii12 avec comme valeur PrettyTable() permettant d'afficher les tableau sous une plus belle forme, en ASCII.
def sql13():#fonction représentant la requête n°13
    c.execute(req13["Quels sont les 10 films d’animation ayant reçu plus de 1000 votes les mieux notés ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on parcour les résultats
        TableAscii12.add_rows([list(row)])#on prend le résultat de la requête que l'on met dans un tableau ASCII    
    TableAscii12.field_names = ["numVotes","primaryTitle","genres"]
    root = Tk() #on créer une fenetre dans laquel va s'afficher le résultat de la requête
    Titre = ttk.Label(root, text=str(TableAscii12),font="Courier 18")#on créer une zone de texte où vas s'afficher le résultat avec une police Courier 18
    Titre.pack()#on pack la zone de texte pour lui permettre de s'afficher sur la page 
    Close=Button(root,text="fermer la fenêtre",command=root.destroy,font="Calibri 18")
    Close.pack()

TableAscii13=PrettyTable()#on créer une variable tableAscii13 avec comme valeur PrettyTable() permettant d'afficher les tableau sous une plus belle forme, en ASCII.
def sql14():#fonction représentant la requête n°14
    c.execute(req14["Combien de films durent plus de 3 heures ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on parcour les résultats
        TableAscii13.add_rows([list(row)])#on prend le résultat de la requête que l'on met dans un tableau ASCII    
    TableAscii13.field_names = ["COUNT(primaryTitle)"]
    root = Tk() #on créer une fenetre dans laquel va s'afficher le résultat de la requête
    Titre = ttk.Label(root, text=str(TableAscii13),font="Courier 18")#on créer une zone de texte où vas s'afficher le résultat avec une police Courier 18
    Titre.pack()#on pack la zone de texte pour lui permettre de s'afficher sur la page 
    Close=Button(root,text="fermer la fenêtre",command=root.destroy,font="Calibri 18")
    Close.pack()

TableAscii14=PrettyTable()#on créer une variable tableAscii14 avec comme valeur PrettyTable() permettant d'afficher les tableau sous une plus belle forme, en ASCII.
def sql15():#fonction représentant la requête n°15
    c.execute(req15["Quelle est la durée moyenne d’un film ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on parcour les résultats
        TableAscii14.add_rows([list(row)])#on prend le résultat de la requête que l'on met dans un tableau ASCII    
    TableAscii14.field_names = ["AVG(runtimeMinutes) "]
    root = Tk() #on créer une fenetre dans laquel va s'afficher le résultat de la requête
    Titre = ttk.Label(root, text=str(TableAscii14),font="Courier 18")#on créer une zone de texte où vas s'afficher le résultat avec une police Courier 18
    Titre.pack()#on pack la zone de texte pour lui permettre de s'afficher sur la page 
    Close=Button(root,text="fermer la fenêtre",command=root.destroy,font="Calibri 18")
    Close.pack()

TableAscii15=PrettyTable()#on créer une variable tableAscii15 avec comme valeur PrettyTable() permettant d'afficher les tableau sous une plus belle forme, en ASCII.
def sql16():#fonction représentant la requête n°16
    c.execute(req16["Quel est le film le plus long ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on parcour les résultats
        TableAscii15.add_rows([list(row)])#on prend le résultat de la requête que l'on met dans un tableau ASCII    
    TableAscii15.field_names = ["primaryTitle","MAX(runtimeMinutes)"]
    root = Tk() #on créer une fenetre dans laquel va s'afficher le résultat de la requête
    Titre = ttk.Label(root, text=str(TableAscii15),font="Courier 18")#on créer une zone de texte où vas s'afficher le résultat avec une police Courier 18
    Titre.pack()#on pack la zone de texte pour lui permettre de s'afficher sur la page 
    Close=Button(root,text="fermer la fenêtre",command=root.destroy,font="Calibri 18")
    Close.pack()

TableAscii16=PrettyTable()#on créer une variable tableAscii16 avec comme valeur PrettyTable() permettant d'afficher les tableau sous une plus belle forme, en ASCII.
def sql17():#fonction représentant la requête n°17
    c.execute(req17["Quels sont les 5 films les plus longs ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on parcour les résultats
        TableAscii16.add_rows([list(row)])#on prend le résultat de la requête que l'on met dans un tableau ASCII    
    TableAscii16.field_names = ["originalTitle"]
    root = Tk() #on créer une fenetre dans laquel va s'afficher le résultat de la requête
    Titre = ttk.Label(root, text=str(TableAscii16),font="Courier 18")#on créer une zone de texte où vas s'afficher le résultat avec une police Courier 18
    Titre.pack()#on pack la zone de texte pour lui permettre de s'afficher sur la page 
    Close=Button(root,text="fermer la fenêtre",command=root.destroy,font="Calibri 18")
    Close.pack()

TableAscii17=PrettyTable()#on créer une variable tableAscii17 avec comme valeur PrettyTable() permettant d'afficher les tableau sous une plus belle forme, en ASCII.
def sql18():#fonction représentant la requête n°18
    c.execute(req18["Quels sont les titres des films les plus connus de Sean Connery ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on parcour les résultats
        TableAscii17.add_rows([list(row)])#on prend le résultat de la requête que l'on met dans un tableau ASCII    
    TableAscii17.field_names = ["originalTitle"]
    root = Tk() #on créer une fenetre dans laquel va s'afficher le résultat de la requête
    Titre = ttk.Label(root, text=str(TableAscii17),font="Courier 18")#on créer une zone de texte où vas s'afficher le résultat avec une police Courier 18
    Titre.pack()#on pack la zone de texte pour lui permettre de s'afficher sur la page 
    Close=Button(root,text="fermer la fenêtre",command=root.destroy,font="Calibri 18")
    Close.pack()

TableAscii18=PrettyTable()#on créer une variable tableAscii18 avec comme valeur PrettyTable() permettant d'afficher les tableau sous une plus belle forme, en ASCII.
def sql19():#fonction représentant la requête n°19
    c.execute(req19["Quels sont les acteurs ayant joué le rôle de James Bond, et dans quels films ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on parcour les résultats
        TableAscii18.add_rows([list(row)])#on prend le résultat de la requête que l'on met dans un tableau ASCII    
    TableAscii18.field_names = ["primaryName","originalTitle"]
    root = Tk() #on créer la racine de l'affichage tkinter
    root.geometry("1000x800")#on défini la taille de la page
    #on créer la fenêtre principal
    fenetre1=Frame(root)#on créer une variable fenetre1 avec comme valeur une fenetre
    fenetre1.pack(side=TOP,fill=BOTH,expand=1) #On défini la position du widget fill="both" remplir à la fois horizontalement et verticalement tout espace supplémentaire qui lui est alloué par le parent. Et enfin expand=True fait que le widget utilise tout espace non utilisé.
    #on créer un "canvas"  qui nous permettra de créer notre scrollbar.
    canvas1=Canvas(fenetre1) #on créer la variable canvas1 avec comme valeur un canvas de la fenêtre1
    canvas1.pack(side=LEFT,fill=BOTH,expand=1)#on pack le canvas pour l'afficher dans la fenêtre
    #On créer notre scrollbar
    scrollbarVertical=ttk.Scrollbar(fenetre1, orient=VERTICAL, command=canvas1.yview)#on créer une variable scrollbarVertical avec comme valeur la fenetre1, avec comme orientation vertical pour défiler la page de haute en bas, avec comme commande l'axe y du cavas1 
    scrollbarVertical.pack(side=RIGHT, fill=Y)#on pack notre scrollbar pour l'afficher sur la page.
    #configure canvas
    canvas1.configure(yscrollcommand=scrollbarVertical.set)
    canvas1.bind('<Configure>', lambda e: canvas1.configure(scrollregion=canvas1.bbox("all")))
    #seconde fenetre
    fenetre2=Frame(canvas1)
    #ajouter seconde fenetre and la page du canvas
    canvas1.create_window((0,0),window=fenetre2, anchor="nw")
    #on créer des bouton executant les fonctions de requêtes sql fait plus tôt. les argument text représente ce qu'il y a d'écrit sur les bouton, command représente la fonction a executé, et font la police choisi.
    Titre = ttk.Label(fenetre2, text=str(TableAscii18),font="Courier 18")#on créer un label sur lequel on écrit le titre dans la première fenêtre, avec un police Courier 18
    Titre.pack() #on pack le Titre pour lui permettre de s'afficher sur la page
    Close=Button(root,text="fermer la fenêtre",command=root.destroy,font="Calibri 18")
    Close.pack()
    root.mainloop() #permet de lancer tout les événement de la page, soit la démarrer.


TableAscii19=PrettyTable()#on créer une variable tableAscii19 avec comme valeur PrettyTable() permettant d'afficher les tableau sous une plus belle forme, en ASCII.
def sql20():#fonction représentant la requête n°20
    c.execute(req20["Quel sont les réalisateurs ayant fait les cinq film les mieux notés ? Indiquer les noms des films correspondants."])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on parcour les résultats
        TableAscii19.add_rows([list(row)])#on prend le résultat de la requête que l'on met dans un tableau ASCII    
    TableAscii19.field_names = ["primaryName","primaryTitle"]
    root = Tk() #on créer une fenetre dans laquel va s'afficher le résultat de la requête
    Titre = ttk.Label(root, text=str(TableAscii19),font="Courier 18")#on créer une zone de texte où vas s'afficher le résultat avec une police Courier 18
    Titre.pack()#on pack la zone de texte pour lui permettre de s'afficher sur la page 
    Close=Button(root,text="fermer la fenêtre",command=root.destroy,font="Calibri 18")
    Close.pack()

TableAscii20=PrettyTable()#on créer une variable tableAscii20 avec comme valeur PrettyTable() permettant d'afficher les tableau sous une plus belle forme, en ASCII.
def sql21():#fonction représentant la requête n°21
    c.execute(req21["Quels sont les noms des épisodes de Game of Thrones ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on parcour les résultats
        TableAscii20.add_rows([list(row)])#on prend le résultat de la requête que l'on met dans un tableau ASCII    
    TableAscii20.field_names = ["primaryTitle"]
    root = Tk() #on créer la racine de l'affichage tkinter
    root.geometry("1000x800")#on défini la taille de la page
    #on créer la fenêtre principal
    fenetre1=Frame(root)#on créer une variable fenetre1 avec comme valeur une fenetre
    fenetre1.pack(side=TOP,fill=BOTH,expand=1) #On défini la position du widget fill="both" remplir à la fois horizontalement et verticalement tout espace supplémentaire qui lui est alloué par le parent. Et enfin expand=True fait que le widget utilise tout espace non utilisé.
    #on créer un "canvas"  qui nous permettra de créer notre scrollbar.
    canvas1=Canvas(fenetre1) #on créer la variable canvas1 avec comme valeur un canvas de la fenêtre1
    canvas1.pack(side=LEFT,fill=BOTH,expand=1)#on pack le canvas pour l'afficher dans la fenêtre
    #On créer notre scrollbar
    scrollbarVertical=ttk.Scrollbar(fenetre1, orient=VERTICAL, command=canvas1.yview)#on créer une variable scrollbarVertical avec comme valeur la fenetre1, avec comme orientation vertical pour défiler la page de haute en bas, avec comme commande l'axe y du cavas1 
    scrollbarVertical.pack(side=RIGHT, fill=Y)#on pack notre scrollbar pour l'afficher sur la page.
    #configure canvas
    canvas1.configure(yscrollcommand=scrollbarVertical.set)
    canvas1.bind('<Configure>', lambda e: canvas1.configure(scrollregion=canvas1.bbox("all")))
    #seconde fenetre
    fenetre2=Frame(canvas1)
    #ajouter seconde fenetre and la page du canvas
    canvas1.create_window((0,0),window=fenetre2, anchor="nw")
    #on créer des bouton executant les fonctions de requêtes sql fait plus tôt. les argument text représente ce qu'il y a d'écrit sur les bouton, command représente la fonction a executé, et font la police choisi.
    Titre = ttk.Label(fenetre2, text=str(TableAscii20),font="Courier 18")#on créer un label sur lequel on écrit le titre dans la première fenêtre, avec un police Courier 18
    Titre.pack() #on pack le Titre pour lui permettre de s'afficher sur la page
    Close=Button(root,text="fermer la fenêtre",command=root.destroy,font="Calibri 18")
    Close.pack()
    root.mainloop() #permet de lancer tout les événement de la page, soit la démarrer.



#on créer la fonction afficher qui nous permet de créer l'interface avec tkinter
def afficher():
    root = Tk() #on créer la racine de l'affichage tkinter
    root.geometry("1000x600")#on défini la taille de la page
    #on créer la fenêtre principal
    fenetre1=Frame(root)#on créer une variable fenetre1 avec comme valeur une fenetre
    fenetre1.pack(side=TOP,fill=BOTH,expand=1) #On défini la position du widget fill="both" remplir à la fois horizontalement et verticalement tout espace supplémentaire qui lui est alloué par le parent. Et enfin expand=True fait que le widget utilise tout espace non utilisé.
    Titre = ttk.Label(fenetre1, text="requêtes SQL",font="Calibri 18")#on créer un label sur lequel on écrit le titre dans la première fenêtre, avec un police calibri 18
    Titre.pack() #on pack le Titre pour lui permettre de s'afficher sur la page

    #on créer un "canvas"  qui nous permettra de créer notre scrollbar.
    canvas1=Canvas(fenetre1) #on créer la variable canvas1 avec comme valeur un canvas de la fenêtre1
    canvas1.pack(side=LEFT,fill=BOTH,expand=1)#on pack le canvas pour l'afficher dans la fenêtre

    #On créer notre scrollbar
    scrollbarVertical=ttk.Scrollbar(fenetre1, orient=VERTICAL, command=canvas1.yview)#on créer une variable scrollbarVertical avec comme valeur la fenetre1, avec comme orientation vertical pour défiler la page de haute en bas, avec comme commande l'axe y du cavas1
    scrollbarVertical.pack(side=RIGHT, fill=Y)#on pack notre scrollbar pour l'afficher sur la page.

    #configurer canvas
    canvas1.configure(yscrollcommand=scrollbarVertical.set)
    canvas1.bind('<Configure>', lambda e: canvas1.configure(scrollregion=canvas1.bbox("all")))

    #seconde fenetre
    fenetre2=Frame(canvas1)

    #ajouter seconde fenetre and la page du canvas
    canvas1.create_window((0,0),window=fenetre2, anchor="nw")

    #on créer des bouton executant les fonctions de requêtes sql fait plus tôt. les argument text représente ce qu'il y a d'écrit sur les bouton, command représente la fonction a executé, et font la police choisi.
    boutton1=Button(fenetre2,text="Question 1:\n\n Quels sont les différents types de titres dans cette base de données ?",width=80,command=sql1, font="Calibri, 12")
    boutton2=Button(fenetre2,text="Question 2:\n\n Combien y a-t-il de titres dans cette base de données ?",width=80, command=sql2, font="Calibri, 12")
    boutton3=Button(fenetre2,text="Question 3:\n\n En quelle année est sortie le film The Godfather ?",width=80, command=sql3, font="Calibri, 12")
    boutton4=Button(fenetre2,text="Question 4:\n\n En quelle année est sortie le premier film Superman ?",width=80, command=sql4, font="Calibri, 12")
    boutton5=Button(fenetre2,text="Question 5:\n\n Quel est le titre original du film 'Les dents de la mer' ?",width=80, command=sql5, font="Calibri, 12")
    boutton6=Button(fenetre2,text="Question 6:\n\n Quel est le métier d’Olivier Nakache ?",width=80, command=sql6, font="Calibri, 12")
    boutton7=Button(fenetre2,text="Question 7:\n\n Quels sont les films d’Olivier Nakache ?",width=80, command=sql7, font="Calibri, 12")
    boutton8=Button(fenetre2,text="Question 8:\n\n Quel est le film ayant recueilli le plus de votes ?",width=80, command=sql8, font="Calibri, 12")
    boutton9=Button(fenetre2,text="Question 9:\n\n Qui a écrit le scénario du film Taxi sorti en 1998 ?",width=80, command=sql9, font="Calibri, 12")
    boutton10=Button(fenetre2,text="Question 10:\n\n Quelles sont les noms et rôles (category et job) des personnes intervenant dans la production du film Return of the Jedi ?",width=95, command=sql10, font="Calibri, 12")
    boutton11=Button(fenetre2,text="Question 11:\n\n Quels sont les titres des films notés plus de 9 sur 10 avec plus de 10 000 votes ?",width=80, command=sql11, font="Calibri, 12")
    boutton12=Button(fenetre2,text="Question 12:\n\n Quelle sont les 5 comédies romantiques les mieux notées ?",width=80, command=sql12, font="Calibri, 12")
    boutton13=Button(fenetre2,text="Question 13:\n\n Quels sont les 10 films d’animation ayant reçu plus de 1000 votes les mieux notés ?",width=80, command=sql13, font="Calibri, 12")
    boutton14=Button(fenetre2,text="Question 14:\n\n Combien de films durent plus de 3 heures ?",width=80, command=sql14, font="Calibri, 12")
    boutton15=Button(fenetre2,text="Question 15:\n\n Quelle est la durée moyenne d’un film ?",width=80, command=sql15, font="Calibri, 12")
    boutton16=Button(fenetre2,text="Question 16:\n\n Quel est le film le plus long ?",width=80, command=sql16, font="Calibri, 12")
    boutton17=Button(fenetre2,text="Question 17:\n\n Quels sont les 5 films les plus longs ?",width=80, command=sql17, font="Calibri, 12")
    boutton18=Button(fenetre2,text="Question 18:\n\n Quels sont les titres des films les plus connus de Sean Connery ?",width=80, command=sql18, font="Calibri, 12")
    boutton19=Button(fenetre2,text="Question 19:\n\n Quels sont les acteurs ayant joué le rôle de James Bond, et dans quels films ?",width=80, command=sql19, font="Calibri, 12")
    boutton20=Button(fenetre2,text="Question 20:\n\n Quel sont les réalisateurs ayant fait les cinq film les mieux notés ?",width=80, command=sql20, font="Calibri, 12")
    boutton21=Button(fenetre2,text="Question 21:\n\n Quels sont les noms des épisodes de Game of Thrones ?",width=80, command=sql21, font="Calibri, 12")
    Fermer=Button(root,text="Fermer la fenêtre",command=root.destroy,font="Calibri 18")
    Fermer.pack()

    #on pack les boutton avec une marge de 10px en hauteur pour les espacer les uns des autres.
    boutton1.pack(pady=10)
    boutton2.pack(pady=10)
    boutton2.pack(pady=10)
    boutton3.pack(pady=10)
    boutton4.pack(pady=10)
    boutton5.pack(pady=10)
    boutton6.pack(pady=10)
    boutton7.pack(pady=10)
    boutton8.pack(pady=10)
    boutton9.pack(pady=10)
    boutton10.pack(pady=10)
    boutton11.pack(pady=10)
    boutton12.pack(pady=10)
    boutton13.pack(pady=10)
    boutton14.pack(pady=10)
    boutton15.pack(pady=10)
    boutton16.pack(pady=10)
    boutton17.pack(pady=10)
    boutton18.pack(pady=10)
    boutton19.pack(pady=10)
    boutton20.pack(pady=10)
    boutton21.pack(pady=10)

    root.mainloop() #permet de lancer tout les événement de la page, soit la démarrer.

afficher()#on appel la fonction affichage pour l'executer.
