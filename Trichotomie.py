def trichotomie(tab:list,n:int):
    if tab == [] or tab ==  None:
        return False

    debut = 0
    fin = len(tab)-1

    if tab[debut] == n or tab[fin] == n:
        return True

    while debut < fin:
        m = (fin-debut)//3
        mid1 = debut + m
        mid2 = fin - m

        if tab[mid1] == n or tab[mid2] == n:
            return True
        elif n < tab[mid1]:
            fin = mid1 -1
        elif n > tab[mid2]:
            debut = mid2 + 1
        else:
            debut = mid1 + 1
            fin = mid2 - 1
    return False

