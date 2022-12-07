"""
https://adventofcode.com/2022/day/1
Day 01 ex.1 - Sum up the total calories for each elf and return the highest amount.
"""

with open("day_01/input_01.txt") as file_hnd:
    elves = file_hnd.read().split("\n\n")


def sumCalories(elves):
    """Return a list of the sums of the calories each elf is carrying"""

    totalCalories = list()
    for elf in elves: # map each elf calories into a list of ints before making a sum.
        calories = map(int, elf.split())
        totalCalories.append(sum(calories))
    
    return totalCalories

totalCalories = sumCalories(elves)
for i, elf in enumerate(elves, 0):
    print(f"elf -----------\n{elf}")
    print(f"Total calories : {totalCalories[i]}")
print(f"Highest calories carried: {max(totalCalories)}")