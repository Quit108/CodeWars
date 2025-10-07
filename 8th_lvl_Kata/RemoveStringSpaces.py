x = input('Enter a string with spaces at the beginning and end: ')

def no_space(x):
    return x.replace(" ", "")

print(no_space(x))