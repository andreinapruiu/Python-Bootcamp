def longest_common_prefix(strings):
    if not strings:
        return ""
    prefix = strings[0]
    for word in strings[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

words = ["flower", "flow", "flight"]
print("Longest common prefix:", longest_common_prefix(words))
