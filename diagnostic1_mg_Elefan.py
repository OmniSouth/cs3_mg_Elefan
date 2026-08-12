
def calculate_space_weight(earth_weight, destination):
    if destination == "Mars" or destination == "mars":
        return earth_weight*0.38
    elif destination == "Jupiter" or destination == "jupiter":
        return earth_weight*2.34
    elif destination == "Moon" or destination == "moon":
        return earth_weight*0.16
    else:
         print("Error: We don't know where that is")
         return 0

print(f"{calculate_space_weight(65,"Mars")}")