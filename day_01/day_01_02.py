"""
https://adventofcode.com/2022/day/1
Day 01 ex.1 - Sum up the total calories for each elf and return the highest amount.
Day 01 ex.2 - Sum the total calories of the 3 elves carrying most calories
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

def highestCaloriesCalc(totalCalories, elvesCount):
    """Return a list with the highest elvesCount carrying elves"""

    highest = sorted(totalCalories, reverse=True)[0:elvesCount]

    return highest


totalCalories = sumCalories(elves)
highestCalories = highestCaloriesCalc(totalCalories, 3) # getting top 3 carrying elves
for i, elf in enumerate(elves, 0):
    print(f"elf -----------\n{elf}")
    print(f"Total calories : {totalCalories[i]}")
print(f"Highest calories carried: {max(totalCalories)}")
print(f"Top 3 carrying elves are carrying : {sum(highestCalories)} calories together")