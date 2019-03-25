# Created by Miguecrack4800
database = []       #  put here your incial database
line = 2            #  put the line where is the database
def saveDatabase():
    arch = open("Main.py", "r")     #  open(NameOfTheFile, "r")
    x = arch.readlines()            #  first we read all lines of this file
    arch.close()
    x[line-1] = "database = " + str(database) + "\n"    #  then we change the line of the database to insert a new one
    arch = open("Main.py", "w")     #  open(NameOfTheFile, "w")
    arch.writelines()               #  and finally we rewrite the file
    arch.close()
