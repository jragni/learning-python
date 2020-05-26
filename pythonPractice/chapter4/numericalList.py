#!/usr/bin/env python3
# author: Jhensen Ray Agni

# using range 
print('This is used to print ranges 1 - 8')
for num in range(1,9):
    print(num)

# making a list of even number 2 - 30
even =list( range(2,32,2))
print(even)


# statistics 

print(min(even))
print(max(even))
print(sum(even))

# squares 
squares = []
for value in range(1,100,2):
    squares.append(value**2)

print(squares)

print('this is the same as: ')
# this is called line comprehension
squares2 = [value**2 for value in range(1,100,2)]
print(squares2)

