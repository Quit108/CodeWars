sq=121

def find_next_square(sq):
    if (sq**0.5).is_integer():
        return (sq**0.5+1)**2
    else:
        return -1

print(find_next_square(sq))
