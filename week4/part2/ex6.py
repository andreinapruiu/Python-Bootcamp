with open("file.txt", "r") as src, open("file_2.txt", "w") as dst:
    dst.write(src.read())
