import tkinter as tk #on importe le module tkinter et on ajoute un alias: "tk"
import os #on importe le module os
import sqlite3 #on importe le module de base de donnée sqlite

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
    req8={"Quel est le film ayant recueilli le plus de votes ?":query8.read()} #requête n°8
    req9={"Qui a écrit le scénario du film Taxi sorti en 1998 ?": query9.read()} #requête n°9
    # req10={"": ""}  #requête n°10
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

#On créer une fonction ClearCmd afin de vider la console python au début de chaque résultat pour effacer les précédent:
def ClearCmd():
    clear = lambda: os.system('cls') #on nettoye la console en supprimant les résultats précédents 
    clear()

# Fonction d'execution des requête:

def sql1():#fonction représentant la requête n°3
    ClearCmd()
    c.execute(req1["Quels sont les différents types de titres dans cette base de données ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on récupére tout les résultat sous la forme d'une liste
        print(list(row))#on affiche le résultat de la requête

def sql2():#fonction représentant la requête n°3
    ClearCmd()
    c.execute(req2["Combien y a-t-il de titres dans cette base de données ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on récupére tout les résultat sous la forme d'une liste
        print(list(row))#on affiche le résultat de la requête

def sql3():#fonction représentant la requête n°4
    ClearCmd()
    c.execute(req3["En quelle année est sortie le film The Godfather ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on récupére tout les résultat sous la forme d'une liste
        print(list(row))#on affiche le résultat de la requête

def sql4():#fonction représentant la requête n°5
    ClearCmd()
    c.execute(req4["En quelle année est sortie le premier film Superman ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on récupére tout les résultat sous la forme d'une liste
        print(list(row))#on affiche le résultat de la requête

def sql5():#fonction représentant la requête n°6
    ClearCmd()
    c.execute(req5["Quel est le titre original du film 'Les dents de la mer' ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on récupére tout les résultat sous la forme d'une liste
        print(list(row))#on affiche le résultat de la requête

def sql6():#fonction représentant la requête n°7
    ClearCmd()
    c.execute(req6["Quel est le métier d’Olivier Nakache ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on récupére tout les résultat sous la forme d'une liste
        print(list(row))#on affiche le résultat de la requête

def sql7():#fonction représentant la requête n°8
    ClearCmd()
    c.execute(req7["Quels sont les films d’Olivier Nakache ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on récupére tout les résultat sous la forme d'une liste
        print(list(row))#on affiche le résultat de la requête
        
def sql8():#fonction représentant la requête n°9
    ClearCmd()
    c.execute(req8["Quel est le film ayant recueilli le plus de votes ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on récupére tout les résultat sous la forme d'une liste
        print(list(row))#on affiche le résultat de la requête

def sql9():#fonction représentant la requête n°10
    ClearCmd()
    c.execute(req9["Qui a écrit le scénario du film Taxi sorti en 1998 ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on récupére tout les résultat sous la forme d'une liste
        print(list(row))#on affiche le résultat de la requête

"""
def sql10():#fonction représentant la requête n°11
    ClearCmd()
    c.execute(req10[""])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on récupére tout les résultat sous la forme d'une liste
        print(list(row))#on affiche le résultat de la requête
"""

def sql11():#fonction représentant la requête n°12
    ClearCmd()
    c.execute(req11["Quels sont les titres des films notés plus de 9 sur 10 avec plus de 10 000 votes ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on récupére tout les résultat sous la forme d'une liste
        print(list(row))#on affiche le résultat de la requête

def sql12():#fonction représentant la requête n°13
    ClearCmd()
    c.execute(req12["Quelle sont les 5 comédies romantiques les mieux notées ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on récupére tout les résultat sous la forme d'une liste
        print(list(row))#on affiche le résultat de la requête

def sql13():#fonction représentant la requête n°14
    ClearCmd()
    c.execute(req13["Quels sont les 10 films d’animation ayant reçu plus de 1000 votes les mieux notés ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on récupére tout les résultat sous la forme d'une liste
        print(list(row))#on affiche le résultat de la requête

def sql14():#fonction représentant la requête n°15
    ClearCmd()
    c.execute(req14["Combien de films durent plus de 3 heures ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on récupére tout les résultat sous la forme d'une liste
        print(list(row))#on affiche le résultat de la requête

def sql15():#fonction représentant la requête n°16
    ClearCmd()
    c.execute(req15["Quelle est la durée moyenne d’un film ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on récupére tout les résultat sous la forme d'une liste
        print(list(row))#on affiche le résultat de la requête

def sql16():#fonction représentant la requête n°17
    ClearCmd()
    c.execute(req16["Quel est le film le plus long ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on récupére tout les résultat sous la forme d'une liste
        print(list(row))#on affiche le résultat de la requête

def sql17():#fonction représentant la requête n°18
    ClearCmd()
    c.execute(req17["Quels sont les 5 films les plus longs ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on récupére tout les résultat sous la forme d'une liste
        print(list(row))#on affiche le résultat de la requête

def sql18():#fonction représentant la requête n°18
    ClearCmd()
    c.execute(req18["Quels sont les titres des films les plus connus de Sean Connery ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on récupére tout les résultat sous la forme d'une liste
        print(list(row))#on affiche le résultat de la requête

def sql19():#fonction représentant la requête n°18
    ClearCmd()
    c.execute(req19["Quels sont les acteurs ayant joué le rôle de James Bond, et dans quels films ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on récupére tout les résultat sous la forme d'une liste
        print(list(row))#on affiche le résultat de la requête

def sql20():#fonction représentant la requête n°18
    ClearCmd()
    c.execute(req20["Quel sont les réalisateurs ayant fait les cinq film les mieux notés ? Indiquer les noms des films correspondants."])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on récupére tout les résultat sous la forme d'une liste
        print(list(row))#on affiche le résultat de la requête

def sql21():#fonction représentant la requête n°18
    ClearCmd()
    c.execute(req21["Quels sont les noms des épisodes de Game of Thrones ?"])#on execute la requête sql en utilisant sa clé dans le dictionnaire
    for row in c.fetchall():#on récupére tout les résultat sous la forme d'une liste
        print(list(row))#on affiche le résultat de la requête


#affichage de l'interface avec tkinter: 
class affichage(tk.Tk): #création de la classe affichage avec comme argument tk.Tk

    def __init__(self, *args, **kwargs): #initialisation de la classe avec une méthode __init__, et avec comme argument *args, **kwargs qui permettent de récupérer des arguments et de faire ce que l'on appel du "packing"
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self) #on créer un container avec dedans la page affiché par tkinter
        container.pack(side="top",fill="both",expand=True) # défini la position des widget, Sidé="top" détermine la position du widget parent, fill="both" remplir à la fois horizontalement et verticalement tout espace supplémentaire qui lui est alloué par le parent. Et enfin expand=True fait que le widget utilise tout espace non utilisé.
        container.grid_rowconfigure(1,weight=0) #on configure la page à la taille minimum 
        container.grid_columnconfigure(1,weight=0)
        self.fenetres={} #on créer un dictionnaire vide pour la page
        fenetre=StartPage(container, self) #frame renvoie à la classe StartPage servant à lancer la page.
        self.fenetres[StartPage]=fenetre
        fenetre.grid(row=1,column=1,sticky="nsew") # on créer une "grille" avec, pour l'instant aucune colonm ni ligne. Et sticky=nsew signifie north south east west, soit nord sud est ouest en fançais, celà permet de cadré la page selon une "boussole".
        self.afficher_fenetre(StartPage) # fait appel à la méthode qui affiche la page.

    def afficher_fenetre(self,cont):#cration de la methode qui affiche la page avec comme argument self et cont pour controller
        fenetre=self.fenetres[cont] #correspond à tout les cadres utilisé
        fenetre.tkraise() #affiche la page 


# lancement de la page:
class StartPage(tk.Frame): #création de la classe StartPage avec comme argument tk.Frame, soit tous ce qu'il y a dans la page

    def __init__(self,parent,controller): #initialisation de la classe avec une méthode __init__, et avec comme argument parent et controller
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="", font="Arial, 30") #label permet d'ajouté du texte à la page, ici, Requête SQL :, et avec font représentant la police correspondante.
        label.pack(pady=20,padx=400) #on pack le texte dans la page avec une marge de 50px en haute et 400px en largeur
        #on créer des bouton executant les fonctions de requêtes sql fait plus tôt. les argument text représente ce qu'il y a d'écrit sur les bouton, command représente la fonction a executé, et font la police choisi.
        boutton1=tk.Button(self,text="Question 1:\n\n Quels sont les différents types de titres dans cette base de données ?",width=80,command=sql1, font="Calibri, 12") 
        boutton2=tk.Button(self,text="Question 2:\n\n Combien y a-t-il de titres dans cette base de données ?",width=80, command=sql2, font="Calibri, 12")
        boutton3=tk.Button(self,text="Question 3:\n\n En quelle année est sortie le film The Godfather ?",width=80, command=sql3, font="Calibri, 12")
        boutton4=tk.Button(self,text="Question 4:\n\n En quelle année est sortie le premier film Superman ?",width=80, command=sql4, font="Calibri, 12")
        boutton5=tk.Button(self,text="Question 5:\n\n Quel est le titre original du film 'Les dents de la mer' ?",width=80, command=sql5, font="Calibri, 12")
        boutton6=tk.Button(self,text="Question 6:\n\n Quel est le métier d’Olivier Nakache ?",width=80, command=sql6, font="Calibri, 12")
        boutton7=tk.Button(self,text="Question 7:\n\n Quels sont les films d’Olivier Nakache ?",width=80, command=sql7, font="Calibri, 12")
        boutton8=tk.Button(self,text="Question 8:\n\n Quel est le film ayant recueilli le plus de votes ?",width=80, command=sql8, font="Calibri, 12")
        boutton9=tk.Button(self,text="Question 9:\n\n Qui a écrit le scénario du film Taxi sorti en 1998 ?",width=80, command=sql9, font="Calibri, 12")
        boutton10=tk.Button(self,text="Question 10:\n\n Quelles sont les noms et rôles (category et job) des personnes intervenant dans la production du film Return of the Jedi ?",width=80, command="", font="Calibri, 12")
        boutton11=tk.Button(self,text="Question 11:\n\n Quels sont les titres des films notés plus de 9 sur 10 avec plus de 10 000 votes ?",width=80, command=sql11, font="Calibri, 12")
        boutton12=tk.Button(self,text="Question 12:\n\n Quelle sont les 5 comédies romantiques les mieux notées ?",width=80, command=sql12, font="Calibri, 12")
        boutton13=tk.Button(self,text="Question 13:\n\n Quels sont les 10 films d’animation ayant reçu plus de 1000 votes les mieux notés ?",width=80, command=sql13, font="Calibri, 12")
        boutton14=tk.Button(self,text="Question 14:\n\n Combien de films durent plus de 3 heures ?",width=80, command=sql14, font="Calibri, 12")
        boutton15=tk.Button(self,text="Question 15:\n\n Quelle est la durée moyenne d’un film ?",width=80, command=sql15, font="Calibri, 12")
        boutton16=tk.Button(self,text="Question 16:\n\n Quel est le film le plus long ?",width=80, command=sql16, font="Calibri, 12")
        boutton17=tk.Button(self,text="Question 17:\n\n Quels sont les 5 films les plus longs ?",width=80, command=sql17, font="Calibri, 12")
        boutton18=tk.Button(self,text="Question 18:\n\n Quels sont les titres des films les plus connus de Sean Connery ?",width=80, command=sql18, font="Calibri, 12")
        boutton19=tk.Button(self,text="Question 19:\n\n Quels sont les acteurs ayant joué le rôle de James Bond, et dans quels films ?",width=80, command=sql19, font="Calibri, 12")
        boutton20=tk.Button(self,text="Question 20:\n\n Quel sont les réalisateurs ayant fait les cinq film les mieux notés ?",width=80, command=sql20, font="Calibri, 12")
        boutton21=tk.Button(self,text="Question 21:\n\n Quels sont les noms des épisodes de Game of Thrones ?",width=80, command=sql21, font="Calibri, 12")
        #on pack les boutton avec une marge de 10px en hauteur et 400 en largeur
        boutton1.pack(pady=10,padx=800)
        boutton1.place(x=10)#on change la position du boutton1, idem pour les autres bouttons jusqu'au 9 et le 22.

        boutton2.pack(pady=10,padx=800)
        boutton2.place(x=10,y=100)
   
        boutton3.pack(pady=10,padx=800)
        boutton3.place(x=10,y=200)
        
        boutton4.pack(pady=10,padx=800)
        boutton4.place(x=10,y=300)
        
        boutton5.pack(pady=10,padx=800)        
        boutton5.place(x=10,y=400)
        
        boutton6.pack(pady=10,padx=800)
        boutton6.place(x=10,y=500)
        
        boutton7.pack(pady=10,padx=800)
        boutton7.place(x=10,y=600)
        
        boutton8.pack(pady=10,padx=800)
        boutton8.place(x=10,y=700)        
    
        boutton9.pack(pady=10,padx=800)
        boutton9.place(x=10,y=800)

        boutton10.pack(pady=10,padx=800)
        boutton10.place(x=10,y=900)

        boutton11.pack(pady=10,padx=800)
        boutton11.place(x=800,y=0)  
        
        boutton12.pack(pady=10,padx=800)
        boutton13.pack(pady=10,padx=800)        
        boutton14.pack(pady=10,padx=800)
        boutton15.pack(pady=10,padx=800)
        boutton16.pack(pady=10,padx=800)
        boutton17.pack(pady=10,padx=800)
        boutton18.pack(pady=10,padx=800)            
        boutton19.pack(pady=10,padx=800)              
        boutton20.pack(pady=10,padx=800)  
        boutton21.pack(pady=10,padx=800)


app=affichage() #on assigne la classe principal: affichage à la variable app
app.mainloop() #permet de lancer tout les événement de la page, soit la démarrer
