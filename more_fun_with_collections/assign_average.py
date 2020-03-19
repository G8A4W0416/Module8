def switch_average(grade):
    switcher = {
        'A': 90,
        'B': 80,
        'C': 70,
        'D': 60,
        'F': 0
    }
    # Second parameter acts as our default
    average = switcher.get(grade, "Invalid Grade")
    return average
