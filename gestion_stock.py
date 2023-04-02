import mysql.connector
from tkinter import *
from tkinter import ttk
from decimal import Decimal
from tkinter import messagebox

root = Tk()

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="boutique"
)


# Créer les éléments nécessaires pour collecter les données
label = ttk.Label(root, text="ID de la ligne à supprimer :")
entry = ttk.Entry(root)
button_delete = ttk.Button(root, text="Supprimer")

# Placer les éléments dans la fenêtre Tkinter avec grid()
label.grid(column=0, row=0, sticky=W)
entry.grid(column=1, row=0)
button_delete.grid(column=2, row=0)

def delete_value():
    # Récupérer le nom du produit à supprimer
    nom = entry.get()

    # Exécuter la requête SQL pour supprimer la ligne de données
    cursor = db.cursor()
    sql = "DELETE FROM produit WHERE nom = %s"
    val = (nom,)
    cursor.execute(sql, val)

    # Enregistrer les modifications dans la base de données et fermer le curseur
    db.commit()
    cursor.close()

# Associer la fonction "delete_value" au bouton "Supprimer"
button_delete.config(command=delete_value)

# Exécution d'une requête SQL
cursor = db.cursor()
cursor.execute("SELECT * FROM produit")
resultats = cursor.fetchall()


# Créez les éléments nécessaires pour collecter les données
label2 = ttk.Label(root, text="Entrez la valeur à ajouter :")
entry2 = ttk.Entry(root)
entry_nom = ttk.Entry(root)
entry_description = ttk.Entry(root)
entry_prix = ttk.Entry(root)
entry_quantite = ttk.Entry(root)
button_add = ttk.Button(root, text="Ajouter")

# Placez les éléments dans la fenêtre Tkinter avec grid()
label2.grid(column=0, row=1, sticky=W)
entry_nom.grid(column=1, row=2)
entry_description.grid(column=1, row=3)
entry_prix.grid(column=1, row=4)
entry_quantite.grid(column=1, row=5)
button_add.grid(column=2, row=6)

def add_value():
    # Récupérez la valeur entrée
    nom = entry_nom.get()
    description = entry_description.get()
    prix = Decimal(entry_prix.get())
    quantite = Decimal(entry_quantite.get())

    cursor = db.cursor()
    sql = "INSERT INTO produit (nom, description, prix, quantite) VALUES (%s, %s, %s, %s)" 
    val = (nom, description, prix, quantite)
    cursor.execute(sql, val)

    # Enregistrez les modifications dans la base de données et fermez le curseur
    db.commit()
    cursor.close()

# Créer le widget Treeview
tree = ttk.Treeview(root)
tree['columns'] = ('Nom', 'Description', 'Prix', 'Quantité')

# Configurer les colonnes
tree.column("#0", width=0, stretch=NO)
tree.column("Nom", width=100, minwidth=100)
tree.column("Description", width=200, minwidth=200)
tree.column("Prix", width=100, minwidth=100)
tree.column("Quantité", width=100, minwidth=100)

# Ajouter les en-têtes de colonne
tree.heading("#0", text="", anchor=W)
tree.heading("Nom", text="Nom", anchor=W)
tree.heading("Description", text="Description", anchor=W)
tree.heading("Prix", text="Prix", anchor=W)
tree.heading("Quantité", text="Quantité", anchor=W)

# Ajouter les données à Treeview
cursor = db.cursor()
cursor.execute("SELECT * FROM produit")
for row in cursor.fetchall():
    tree.insert('', 'end', text=row[0], values=(row[1], row[2], row[3], row[4]))

# Placer le widget Treeview dans la fenêtre Tkinter
tree.grid(column=0, row=7, columnspan=3, padx=5, pady=5)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(7, weight=1)

root.mainloop()

