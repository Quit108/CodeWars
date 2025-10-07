word = input('Enter an Item: ')
n=int(input('How many items?: '))

# Function to determine if plural or singular
def plural(n):
    if n != 1:
        return True
    if True:
        n = n+'s'
        return n
    else:
        return n

print(plural(n), word)