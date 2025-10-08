year = int(input('Enter a year: '))

def century(year):
    return (year + 99) // 100

print(century(year))