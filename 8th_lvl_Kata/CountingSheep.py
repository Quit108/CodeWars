sheep=[input('Enter a list of sheep presence (True/False): ').split(',')]

def count_sheeps(sheep):
    return sum(1 for present in sheep if present.strip().lower() == 'true')

print(count_sheeps(sheep[0]))