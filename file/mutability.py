filenames = ["1.Raw Data.txt" , "2.Reports.txt", "3.Presentations.txt"]
for data in filenames:
    new_file = data.replace(".", "-", 1)
    print(new_file)