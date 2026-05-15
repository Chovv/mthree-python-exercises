history = [] # a list because we want to keep track of the history of conversions

while True:
    print("\n1) Temperature")
    print("2) Weight")
    print("3) Exit")

    choice = 0
    while choice < 1 or choice > 3:
        choice = int(input("What do you want to do? "))
        if choice < 1 or choice > 3:
            print("Must be 1, 2, or 3")

    if choice == 3:
        if history:
            print("\n------- History -------")
            for line in history:
                print(line)
        break

    if choice == 1:
        temp = float(input("Temperature: "))
        print("1) Celsius to Fahrenheit")
        print("2) Fahrenheit to Celsius")

        direction = 0
        while direction < 1 or direction > 2:
            direction = int(input("Pick 1 or 2: "))
            if direction < 1 or direction > 2:
                print("Must be 1 or 2")

        if direction == 1:
            converted = (temp * 9 / 5) + 32
            result = f"{temp} C = {converted:.2f} F"
        else:
            converted = (temp - 32) * 5 / 9
            result = f"{temp} F = {converted:.2f} C"

        print(result)
        history.append(result)

    else:
        weight = float(input("Weight: "))
        print("1) Kilograms to Pounds")
        print("2) Pounds to Kilograms")

        direction = 0
        while direction < 1 or direction > 2:
            direction = int(input("Pick 1 or 2: "))
            if direction < 1 or direction > 2:
                print("Must be 1 or 2")

        if direction == 1:
            converted = weight * 2.20462
            result = f"{weight} kg = {converted:.2f} lb"
        else:
            converted = weight / 2.20462
            result = f"{weight} lb = {converted:.2f} kg"

        print(result)
        history.append(result)

print("Exited")