from os import listdir, rename

directory = input("Directory: ")
path = "./project1_birds/parrots/" + directory + "/"

for i, file in enumerate(listdir(path)):
    new = path + f"{directory} ({i})"
    rename(path + file, new)