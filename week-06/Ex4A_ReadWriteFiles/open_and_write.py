f = open("about_me.txt", "a")
f.close()
# It is a good practice to close a file after using it to free up the resources used by Python.

f = open("about_me.txt", "a")
f.write("My perfect night out would be going roller skating and then having a delicious hamburger.")
f.close()