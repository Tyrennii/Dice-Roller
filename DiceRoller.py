import os
import random

# get the exact directory where this script lives
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "roll_history.txt")

sides = int(input("enter number of sides: "))
rolls = int(input("enter number of rolls: "))

history = []
total = 0

for i in range(rolls):
    roll = random.randint(1, sides)
    history.append(roll)
    total += roll

average = total / rolls

# results: {history} to the file write
with open(file_path, "a") as file:
    file.write(f"sides: {sides}, rolls: {rolls}, results: {history}, total: {total}, average: {average}\n")

print(f"data written to: {file_path}")
print(f"results: {history}")
print(f"total: {total}")
print(f"average: {average}")

input("\npress enter to exit...")
