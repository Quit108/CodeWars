s="bitcoin take over the world maybe who knows perhaps"

def find_short(s):
    words = s.split()
    l=min(len(word)for word in words)
    return l

print(find_short(s))