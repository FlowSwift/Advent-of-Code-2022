"""
https://adventofcode.com/2022/day/1
Day 01 ex.1 - Sum up the total calories for each elf and return the highest amount.
"""

with open("day_01/input_01.txt") as file_hnd:
    elves = file_hnd.read().split("\n\n")

for elf in elves:
    print(f"elf -----------\n{elf}")