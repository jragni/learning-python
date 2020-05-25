#!/usr/bin/env python3
# author: Jhensen Ray Agni


guestList = ["tom","jerry","phil","rob","kevin","dale","jim"]
guestList = guestList
for guests in guestList:
    print(guests.title())
print('---------------------')
# adding to end of the list
guestList.append("ronald")
for guests in guestList:
    print(guests)
# removing from list using del statement
print('---------------------')

del guestList[-1]
for guests in guestList:
    print(guests)
print('---------------------')

# replacing from list
guestList[5] = "Jeremy"
for guests in guestList:
    print(guests)
print('---------------------')

# inserting from list
guestList.insert(1,"Jenny")
for guests in guestList:
    print( guests)
print('---------------------')

# removing from list using pop  // removes last item on the list 
blackListed=guestList.pop()
blackListed=guestList.pop(4)
print(blackListed)
print('---------------------')

# removing items by value
guestList.remove("kevin")

for guests in guestList:
    print(guests)

print('---------------------')

