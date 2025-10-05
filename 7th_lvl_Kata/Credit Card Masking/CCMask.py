cc=input("Enter Your Creditcard Number: ")

def maskify(cc): 
    
    if len(cc) > 4:
        mask = "#" * (len(cc)-4) + cc[-4:]
        return(mask)
    else:
        return(cc)