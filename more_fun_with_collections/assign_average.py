def switch_average(grade):
    switcher = {
        'A': 90
    }
    # Second parameter acts as our default
    average = switcher.get(grade)
    return average