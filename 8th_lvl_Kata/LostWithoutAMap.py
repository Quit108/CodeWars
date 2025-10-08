a=input('Enter a list of numbers separated by spaces: ').split()
a=[int(x) for x in a]

def maps(a):
    return [2*x for x in a]

print(maps(a))