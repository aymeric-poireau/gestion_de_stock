import mysql.connector
from tkinter import *
from tkinter import ttk

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="xngixq973",
    database="boutique"
)

# Exécution d'une requête SQL
cursor = db.cursor()
cursor.execute("SELECT * FROM produit")
resultats = cursor.fetchall()
root = Tk()

# Créez les éléments nécessaires pour collecter les données
label = ttk.Label(root, text="Entrez la valeur à ajouter :")
entry = ttk.Entry(root)
entry_nom = ttk.Entry(root)
entry_description = ttk.Entry(root)
entry_prix = ttk.Entry(root)
entry_quantite = ttk.Entry(root)
button = ttk.Button(root, text="Ajouter")

# Placez les éléments dans la fenêtre Tkinter avec grid()
label.grid(column=0, row=0, sticky=W)
entry.grid(column=1, row=0)
button.grid(column=2, row=0)

def add_value():
    # Récupérez la valeur entrée
    nom = entry_nom.get()
    description = entry_description.get()
    prix = entry_prix.get()
    quantite = entry_quantite.get()

    # Exécutez la requête SQL pour ajouter la valeur dans la table de la base de données
    mycursor = db.cursor()
    sql = "INSERT INTO produit (nom, description, prix, quantite) VALUES (%s, %s, %s, %s)" 
    val = (nom, description, prix, quantite)
    mycursor.execute(sql, val)

    # Enregistrez les modifications dans la base de données et fermez le curseur
    db.commit()
    mycursor.close()

# Associez la fonction "add_value" au bouton "Ajouter"
button.config(command=add_value)

l = Listbox(root, height=20, width=80)
l.grid(column=0, row=1, columnspan=3, sticky=(N,W,E,S))
s = ttk.Scrollbar(root, orient=VERTICAL, command=l.yview)
s.grid(column=3, row=1, sticky=(N,S))
l['yscrollcommand'] = s.set
ttk.Label(root, text="Statut:", anchor=(W)).grid(column=0, columnspan=3, row=2, sticky=(W,E))

root.grid_columnconfigure(0, weight=10)
root.grid_rowconfigure(1, weight=10)
for resultat in resultats:
    l.insert(END, resultat)
    
root.mainloop()
