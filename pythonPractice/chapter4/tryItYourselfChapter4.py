#!/usr/bin/env python3 
# author: Jhensen Ray Agni

# for loop to print 1 to 20

for numbers in range(1,21):
    print(numbers)

#print a million numbers
print("here's a loop from 1 to 1 million")
millionNumbes = [number for number in range(1,1000001)]
print(millionNumbes)

# summing a million

print('here is the sum of a million numbers')
print(sum(millionNumbes))

# Odd numbers: make a list of odd numbers from 1 to 20. Use a for loop
odd = []
for i in range(1,20,2):
    odd.append(i)
    print(i)

# threes : make a list of multipes of 3 from 3 to 30
multiplesOfThree = [number for number in range(3,33,3)]
print(multiplesOfThree)

# cubes : make a list of cubes for the first t10 cubes
cubes = [num**2 for num in range(1,11)]
print(cubes)

