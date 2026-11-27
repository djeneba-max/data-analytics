import numpy as np

# Avec np.array:
# [] → 1D array
# [[]] → 2D array
# [[[]]] → 3D array 



# 1D array
arr = np.array([1, 2, 3])  # ← One row of elements
print(arr)
print()


# 2D array
arr2 = np.array([
    [1, 2, 3],  # ← Row 1
    [4, 5, 6]   # ← Row 2
])
print(arr2)
print()

# Visualiser les tableaux 3D


# Imagine plusieux tableaux 2D empilés les uns en dessous des autres, selon l'axis = 0.

# Exemple 1
arr_1 = np.array([
    [
        [1, 2, 3],    # ← Row 1        # Tableau 1
        [4, 5, 6]     # ← Row 2
    ],
    [
        [7, 8, 9],    # ← Row 1        # Tableau 2
        [10, 11, 12]  # ← Row 2
    ]
])

# shape : (layers, rows, columns)
# shape : (2,2,3)



# Exemple 2
arr_2 = np.array([
    [
        [1, 2],                # Tableau 1
        [3, 4],
        [5, 6]
    ],
    [
        [7, 8],                # Tableau 2
        [9, 10],
        [11, 12]
    ],
    [
        [13, 14],              # Tableau 3
        [15, 16],
        [17, 18]
    ]
])

# shape: (3,3,2)



# Exemple 3
arr_3 = np.array([
    [
        [1, 2, 3, 4],          # Tableau 1
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ],
    [
        [13, 14, 15, 16],      # Tableau 2
        [17, 18, 19, 20],
        [21, 22, 23, 24]
    ]
])

# shape: (2,3,4)
print(arr_3.shape)


# To identify the number of rows and columns in these examples,
# look at each 2D array (layer) individually, or just the top 2D array as if viewing the stack from above.


#==================================================================
# 2D/1D

# ([1, 2, 3]) → 1D  (3,)
# ([[1, 2, 3]]) → 2D (1, 3)  We can have a 2D array with only one row.

#==================================================================

# CONCATENATE

# With concatenate(), arrays must have the same number of dimensions (all 1D, all 2D, etc.).
# The result keeps the same number of dimensions.

# We only extend an existing axis (the other dimensions must have the same size).
# If there are multiple existing axes, we can specify which axis we want to extend.
# Otherwise, the default axis is 0.
# (2, 3) → size of each dimension  
# 2 → number of dimensions



# STACK
# With stack(), arrays must have exactly the same shape.
# A new dimension is added to the original shape.
# The new dimension's size corresponds to the number of arrays being stacked.
# The axis parameter determines where this new dimension is inserted in the shape.
# The result has one additional dimension.
# We don't extend an existing axis; we create a new one.


# AXIS
# 1D array: axis=0 ("columns")
# 2D array: axis=0 (rows), axis=1 (columns)
# 3D array: axis=0 (depth), axis=1 (rows), axis=2 (columns)
# Each dimension adds one possible axis, starting from axis=0.

# AXIS ERROR
# AxisError occurs when we specify an axis that does not exist in the array's dimensions.
# Example:  AxisError: axis 1 is out of bounds for array of dimension 1


#=========================================================================
# EXAMPLES

# Example 1
# images = liste de 10 tableaux de shape (28, 28)   2D
# np.stack(images, axis=0).shape   # (10, 28, 28)   3D (one big array)


# Example 2 
a = np.array([1, 2, 3])   # shape (3,)
b = np.array([4, 5, 6])   # shape (3,)

S = np.stack([a, b], axis=0)    # shape (2, 3)
# [[1, 2, 3],
#  [4, 5, 6]]        → S[0] = a, S[1] = b

S2 = np.stack([a, b], axis=1)   # shape (3, 2)
# [[1, 4],
#  [2, 5],
#  [3, 6]]           → S2[:, 0] = a, S2[:, 1] = b

# S2[:, 0] means: all rows, but only the column at position 0.


# Example 3
a = [1, 2, 3]    #(3, )
b = [4, 5, 6]    #(3, )
S = np.concatenate([a, b])   # [1, 2, 3, 4, 5, 6]   #(6, )

S[:3]   # → [1, 2, 3]  = a
S[3:]   # → [4, 5, 6]  = b


# Q8
S = np.concatenate([A, D], axis=1)   # A: (2, 3), D: (2, 5)

# Shape de S : (2, 8)   → axis=1 : 3 + 5 = 8, les lignes (2) sont identiques
# A = S[:, :3]          → colonnes 0 à 2
# D = S[:, 3:]          → colonnes 3 à 7



# Q10
S = np.stack([A, B], axis=0)         # A et B : (2, 3)

# Shape de S : (2, 2, 3)   → nouvel axe de taille 2 en position 0
# A = S[0]
# B = S[1]



# Q11
S = np.stack([A, B], axis=2)         # A et B : (2, 3)

# Shape de S : (2, 3, 2)   → nouvel axe de taille 2 en position 2
# A = S[:, :, 0]
# B = S[:, :, 1]


# Q15
# images : liste de 10 tableaux de shape (28, 28)
S = np.stack(images, axis=0)

# Shape de S : (10, 28, 28)   → nouvel axe de taille 10 en position 0
# 4e image (indice 3) = S[3]  → shape (28, 28)



# Q16
# A et B ont la shape (2, 3), on veut un résultat S de shape (2, 6).
# 1. Quelle fonction utiliser, et avec quel axis ?
# 2. Comment retrouver A et B dans S ?

S = np.concatenate([A, B], axis=1)  

# Shape de S : (2, 6)   → pas de dimension en plus, donc concatenate (pas stack)
# A = S[:, :3]          → la limite est la taille de A sur l'axe 1 (3)
# B = S[:, 3:]