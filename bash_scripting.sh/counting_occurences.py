count = 0
fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
for fruit in fruits: 
    if fruit == 'apple':    
        count += 1
print("the word apple appears in the list", count, "times")

#another option to make this happen is:

fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
print("the word apple appears in the list", fruits.count('apple'), "times")