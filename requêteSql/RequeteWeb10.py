#!"F:\Winpython\WPy64-3850\python-3.8.5.amd64\python.exe"
#Sur la ligne ci-dessus il faut mettre le chemin de l'interpréteur python pour que les requêtes puissent s'executer.

"""
Info: Cette requête utilise beaucoup de ressource et créer une erreur: "Internal Server Error" qui n'affiche pas la réponse sur la page web, cependant la reqûete est fonctionnelle.
"""


import sqlite3 #import du module sqlite3


with open('requêtes/req10.sql') as query10: #on ouvre le ficher de la requête 10
    req10={"Quelles sont les noms et rôles (category et job) des personnes intervenant dans la production du film Return of the Jedi ?": query10.read()} #on met la requête 9 dans un dictionnaire avec comme clé la question et comme valeur on lit la requête.

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
    print("Content-type: text/html")
    print("\n")
    print("<html><head>")
    print("\n")
    print(" <style> table, th, td {border: 2px solid black;  padding: 15px 30px; text-align: center; border-collapse: collapse;} button{border: 2px solid black; box-shadow: 5px 2px 2px #545454; color: black; padding: 15px 30px; margin-top: 50px; \
    text-align: center; display: inline-block; font-size: 16px; }button:hover{ background-color: #545454; color: whitesmoke; cursor: pointer; transition: 0.2s ease; } </style> ")
    print("</head><body>")

def finhtml():
    print("</body></html>")

def execute_sql(connexion,sql):
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

sql10=req10["Quelles sont les noms et rôles (category et job) des personnes intervenant dans la production du film Return of the Jedi ?"] #appel de la requête 10
execute_sql(conn,sql10) #execution de la fonction execute_sql prenant en argument la requête sql appelé précédement.
