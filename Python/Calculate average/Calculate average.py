def find_average(numbers):
    n = numbers
    
    if len(n) == 0:
        return 0 
    
    soma = 0
    for x in n:
        soma += x
    media = soma / len(n)
    return media