#!/usr/bin/env python
# author: Jhensen Ray Agni

cars = ['bmw','audi','toyota','subaru','tesla']

# sorting alphabetically
print("\t Here is the original list: \n" )
for car in cars:
    print(car)
print("here is the temporarily sorted list ")
tempSortCar = sorted(cars)
for car in tempSortCar:
    print(car)
print("here is the original again: \n")
for car in cars:
    print(car)

cars.sort()
print("here is the sorted list \n")
for car in cars:
    print(car)
# sorting reverse

cars.sort(reverse=True)
print("here is the reversed sorted list:\n" )
for car in cars:
    print(car)

print("\n The length of the list is: " + str(len(cars)))






