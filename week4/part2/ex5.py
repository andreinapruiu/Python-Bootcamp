with open("file.txt", "r") as f:
    words = f.read().split()
    longest = max(words, key=len)
    print("Longest word:", longest)
