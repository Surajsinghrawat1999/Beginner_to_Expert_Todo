import glob

myfiles = glob.glob("*.txt")
print(myfiles)
for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read().upper())

#glob module is used to filter all the files available in a project