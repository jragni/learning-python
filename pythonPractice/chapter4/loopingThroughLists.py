#!/usr/bin/env python3
# author: Jhensen Ray Agni

# working with for loop
magicians = ["alice", "david","carolina"]
praise = "Wow {}, that was a great trick!"

for magician in magicians:
    print(praise.format(magician.title()))
print('\n Thank you everyone, that was a great show!')  
