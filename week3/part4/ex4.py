import random

def generate_sequence(length=1000):
    return ''.join(random.choices('abcdef', k=length))

def has_pattern(seq):
    for i in range(3, len(seq)):
        prev = set(seq[i-3:i])
        if len(prev) == 3 and seq[i] not in prev:
            print(f"Character '{seq[i]}' follows 3 different others at position {i}")
            return True
    return False

sequence = generate_sequence()
if not has_pattern(sequence):
    print("No such sequence found.")
