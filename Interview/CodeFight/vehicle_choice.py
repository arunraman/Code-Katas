def fancyRide(l, fares):
    max_value = 0
    vehicle_choice = ""
    vehicle = ["UberX", "UberXL", "UberPlus", "UberBlack", "UberSUV"]
    for f, v in zip(fares, vehicle):
        if (l * f) <= 20 and (l * f) > max_value:
            max_value = (l * f)
            vehicle_choice = v

    return vehicle_choice
