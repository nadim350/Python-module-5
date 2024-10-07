
import random
num_dice = int(input("How many dice would you like to roll? "))

rolls = [random.randint(1, 6) for _ in range(num_dice)]

print(f"The sum of the dice rolls is: {sum(rolls)}")
