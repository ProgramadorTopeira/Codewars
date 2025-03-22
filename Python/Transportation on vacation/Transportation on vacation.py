def rental_car_cost(d):
    base = d * 40
    if d >=7:
        base -= 50
    elif d >= 3:
        base -= 20
    return base