numbers = []
while True:
    input_number = input("Enter a number (or press Enter to quit): ")
    if input_number == "":
        break
    numbers.append(int(input_number))

if len(numbers) >= 5:
    numbers.sort(reverse=True)
    print("The five greatest numbers are:")
    for num in numbers[:5]:
        print(num)
else:
    print("Not enough numbers to find five greatest.")
