# Part 1
from statistics import median
import math


def read_input():
    with open('input') as f:
        input = f.read().split(',')
        input = [int(i) for i in input]
        return input


def calculate_fuel_spent(crabs, goal):
    fuel = 0
    for c in crabs:
        fuel += abs(c-goal)
    return fuel


# Part 2

def calculate_increasing_fuel_spent(crabs, goal):
    fuel = 0
    for c in crabs:
        fuel += sum(range(abs(c-goal)+1))
    return fuel


data = read_input()
testcase = [16,1,2,0,4,2,7,1,2,14]
cheapest = int(median(data))
print(f'Part 1: Fuel spent to move to {cheapest}: {calculate_fuel_spent(data, cheapest)}')

cheapest2 = math.floor(sum(data)/len(data))
print(f'Part 2: Fuel spent to move to {cheapest2}: {calculate_increasing_fuel_spent(data, cheapest2)}')

