# 1. Créer une class

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# class Product: → crée une class appelée Product.
# __init__() → une méthode spéciale qui s'exécute lorsqu'on crée un nouvel objet. Elle initialise l'objet avec les informations reçues lors de sa création.
# self → représente l'objet lui-même.
# self.name, instance variable → stocke le nom du produit.
# self.price, instance variable → stocke le prix du produit.

# optional : '''...''' → docstring qui décrit le rôle de la classe. Il doit etre a l'interieur de la classe.

#====================================================================
# 2. Créer des objets à partir de la class

product1 = Product("Laptop", 800)
product2 = Product("Keyboard", 50)

# Product est la classe (le modèle).
# product1 est un objet créé à partir de cette classe.
# product2 est un autre objet créé à partir de cette classe

#====================================================================
# 3. Accéder aux informations des objets

print(product1.name)        # Laptop
print(product1.price)       # 800

# self.attribut → à l'intérieur des méthodes de la classe.
# nom_objet.attribut → à l'extérieur de la classe, pour accéder aux informations d'un objet.
# En réalité, self représente l'objet lui-même. C'est pourquoi les deux syntaxes permettent d'accéder au même attribut, mais dans des contextes différents.

#====================================================================
# 4. Ajouter une action (method)

# Une classe peut également contenir des fonctions appelées methods.
# Une fonction définie dans une classe est appelée une méthode lorsqu'elle appartient à cette classe.
# When I create objects from this class, I can apply the methods defined in the class to those objects.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        print(self.name, self.price)


# On peut maintenant appeler cette méthode :
product1 = Product("Laptop", 800)

product1.display_info()   #Laptop 800

#====================================================================
# 5. Pass

# En Python, pass signifie : ne rien faire.
# C'est une instruction qui indique à Python que le bloc de code est volontairement vide pour le moment.

class Car:
    pass

# class Car: → crée une classe appelée Car.
# pass → indique qu'il n'y a pas encore de code à exécuter dans cette classe.
# Sans pass, Python signalerait une erreur, car une classe ne peut pas avoir un bloc vide.

# Exemple avec une fonction

def calculate_price():
    pass

# Tu définis une fonction, mais tu n'as pas encore écrit ce qu'elle doit faire.

#====================================================================
# Une fonction (def) permet de regrouper des instructions pour effectuer une tâche.

# En Pythom, le rôle principal d'une class est de créer un modèle pour fabriquer des objets.
# Elle definit une structure commune à partir de laquelle on peut créer plusieurs objets.
# Une même classe peut servir à créer autant d'objets que nécessaire, avec des informations différentes.
# C'est une notion fondamentale en programmation orientée objet (Object-Oriented Programming ou OOP).
#====================================================================

# Une petite analogie :

# Imagine une usine qui fabrique des produits.
# - La classe = le modèle de fabrication.
# - Les objets = les produits fabriqués.
# - Les attributs = les caractéristiques de chaque produit.
# - Les méthodes = les actions que chaque produit peut effectuer.


# Une classe permet de créer plusieurs objets qui partagent les mêmes méthodes, mais qui peuvent avoir des attributs différents.
