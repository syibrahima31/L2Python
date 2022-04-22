def longeur(chaine) : 
    if chaine == "" : 
        return 0 
    else : 
        return 1 + longeur(chaine[1:]) 

longeur("DAKA")