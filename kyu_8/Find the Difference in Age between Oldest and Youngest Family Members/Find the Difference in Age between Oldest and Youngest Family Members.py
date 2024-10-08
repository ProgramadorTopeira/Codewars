def difference_in_ages(ages):
    menor = ages[0]
    maior = ages[0]
    for x in ages:
        if x <= menor:
            menor = x
        if x >= maior:
            maior = x
    
    return menor, maior, maior-menor