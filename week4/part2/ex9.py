import string

for idx, letter in enumerate(string.ascii_lowercase, start=1):
    with open(f"{letter}.txt", "w") as f:
        f.write("Python\n" * idx)
