import numpy as np
# Visualiser les tableaux 3D
# Imagine plusieux tableaux 2D empilés les uns en dessous des autres.

# Exemple 1
arr_1 = np.array([
    [
        [1, 2, 3],           # Tableau 1
        [4, 5, 6]
    ],
    [
        [7, 8, 9],           # Tableau 2
        [10, 11, 12]
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