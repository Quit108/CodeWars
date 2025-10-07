name="Edoardo Montingelli"

def abbrev_name(name):
    return '.'.join([n[0].upper() for n in name.split()])

print(abbrev_name(name))