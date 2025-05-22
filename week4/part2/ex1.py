try:
    with open("file_2.txt", "x") as f:
        f.write("This file was created exclusively.\n")
except FileExistsError:
    print("file_2.txt already exists.")
