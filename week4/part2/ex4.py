with open("file.txt", "r") as f:
    line_count = len(f.readlines())
    print("Line count:", line_count)
