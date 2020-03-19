def switch_average(grade):
    switcher = {
        'A': 90,
        'B': 80,
        'C': 70
    }
    # Second parameter acts as our default
    average = switcher.get(grade)
    return average