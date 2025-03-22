def count_sheep(n)
    teste = ''
    if n == 0
        return ''
    else
        for x in range(1,n+1)
            teste += f'{x} sheep...'
        return teste