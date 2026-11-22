f = open("about_me.txt", "r")
#print(f.read())

# f.read() reads the content of the file, and print() displays that content in the terminal.


#print(f.read(50))
#print(f.read(50))
# The first read(50) reads the first 50 characters.
# The second read(50) continues reading from where the previous read stopped
# and reads the next 50 characters.

# a)
#print(f.readline(10))
#print(f.readline())

# Calling readline() reads the entire current line.
# Calling readline(10) reads only the first 10 characters of the current line.
# The next readline() continues from the current position, reading the remaining characters.
# It moves to the next line only after reaching the end of the current line.

# c) 
#for i in range(1, 5):
#    print(f.readline())


# range(1, 5) generates the values 1, 2, 3, and 4, resulting in 4 iterations.
# The for loop repeats the reading process 4 times.
# At each iteration, readline() reads the next line and print() displays it in the terminal.





# readlines() reads all the lines of the file and returns them as a list of strings.
#print(f.readlines())

# readlines(1) reads approximately 1 byte of data, returning complete lines.
#print(f.readlines(1))

# readlines(10) reads approximately 10 bytes of data, returning complete lines.
#print(f.readlines(10))

# The second readlines(10) continues reading from the current position.
#print(f.readlines(10))

# readlines(100) reads approximately 100 bytes of data, returning complete lines.
#print(f.readlines(100))

# readlines(-1) reads all remaining lines until the end of the file.
#print(f.readlines(-1))

# The size argument controls approximately how much data Python reads at each call,
# instead of loading the entire file into memory.
# Python may exceed this size to finish reading the last line.



 # Reads the first 50 characters and stores them in a variable.
content = f.read(50)  # str

# Creates an empty list to store the lines read from the file.
lines = []   # list 

# Reads up to 4 lines, starting from the current reading position,
# and appends each line to the list.
# At each iteration, readline() reads one line and append() adds that line to the list.
for i in range(1, 5):
    lines.append(f.readline())   # list

# Reads approximately 100 bytes of data from the remaining file content,
# starting from where the loop stopped, and stores the lines in a list.
remaining_lines = f.readlines(100)




print("First 50 characters:", content)
print()
print("Next four lines, as list by line:", lines)
print()
print("Next 100 characters, as list by line, rounded up to complete lines:", remaining_lines)








#============================
# PERSONAL NOTES

# f = open("about_me.txt", "r")

# f.readline()        # Reads the first line
# print(f.readline()) # Reads and displays the second line

# f.close()



# .read()	Lit tout le contenu du fichier ou un nombre précis de caractères.
# .readline()	Lit une ligne à la fois.
# .readlines()	Lit plusieurs lignes et les retourne sous forme de liste (list).
