#!"F:\Winpython\WPy64-3850\python-3.8.5.amd64\python.exe"

"""
Info: Cette requête utilise beaucoup de ressource et créer une erreur: "Internal Server Error" qui n'affiche pas la réponse sur la page web, cependant la reqûete est fonctionnelle si on l'execute sur l'interpreteur de code.
"""


import sqlite3 #import du module sqlite3


with open('requêtes/req19.sql') as query19: #on ouvre le ficher de la requête 19
    req19={"Quels sont les acteurs ayant joué le rôle de James Bond, et dans quels films ?": query19.read()} #on met la requête 19 dans un dictionnaire avec comme clé la question et comme valeur on lit la requête.

def database_connexion(db_file):
    """ 
    créer une connexion à une base de données SQLite spécifiée par le db_file
    : param db_file: fichier de base de données
    : return: Objet de connexion ou Aucun 
    """
    connexion = None
    try:
        connexion = sqlite3.connect(db_file)
    except Error as e:
        return e

    return connexion
conn=database_connexion("../data/imdb.db")



def debuthtml():
    """
    Fonction permettant de structurer la page avec des balises html et des instruction css.
    """
    print("Content-type: text/html")
    print("\n")
    print("<html><head>")
    print("\n")    
    print("<p id='quest'> ",''.join(req19),"</p>")
    print(" <style> table, th, td {border: 2px solid black; padding: 15px 30px; text-align: center; border-collapse: collapse;} button{border: 2px solid black; box-shadow: 5px 2px 2px #545454; color: black; padding: 15px 30px; margin-top: 50px; \
    text-align: center; display: inline-block; font-size: 16px; }button:hover{ background-color: #545454; color: whitesmoke; cursor: pointer; transition: 0.2s ease; } #quest{font-size:1.5em} </style> ")
    print("</head><body>")

def finhtml():
    """
    Fonction de fin de la page html
    """
    print("</body></html>")

def execute_sql(connexion,sql):
    """
    Fonction utilisant les résultats d'une reqûete sql pour les mettres dans un tableaux
    """
    cur = connexion.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    debuthtml()
    table = "<table>\n"     
    for row in rows:
        table += "<tr><td>\n"+str(row[0])+"</td></tr>\n"
    table +="</table>\n"
    print(table)
    finhtml()
    print('<a id="menu" href="http://localhost/python/menu.html"><button>retour</button></a>')

sql19=req19["Quels sont les acteurs ayant joué le rôle de James Bond, et dans quels films ?"] #appel de la requête 19
execute_sql(conn,sql19) #execution de la fonction execute_sql prenant en argument la requête sql appelé précédement.
