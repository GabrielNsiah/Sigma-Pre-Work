def max_min(numbers):
    try:
        max = numbers[0]
        min = numbers[0]
        for num in numbers:
            if num > max:
                max = num
            if num < min:
                min = num
        return [min, max]
    except:
        return "One or more values in your array are not integers."


done = ""
numbers = []
while True:
    try:
        number = int(input("Please enter a number to add to the list:\n"))
        numbers.append(number)
        print(numbers)
        while done.lower() != "yes" and done.lower() != "no":
            done = input(
                "Is this the final list of numbers, please type Yes or No to confirm:\n")
            if done.lower() == "yes":
                print(max_min(numbers))
                break
            elif done.lower() == "no":
                break
            else:
                print(
                    f'{str(done)} is an invalid answer, please enter Yes or No to continue:/n')
                continue

    except:
        print("That was not an integer, please try again")
        continue
