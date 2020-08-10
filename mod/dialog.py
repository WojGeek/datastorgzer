def accept_choice():
     
    choice = 'wrong'
    options = ['A','a','C','c']
    
    while choice not in options:
        
        choice = input("Accept or Cancel (A or C): ")
        if choice not in options:
            print("Sorry, please choose A or C")

    if choice in ['A','a']:
        return True
    else:
        return False