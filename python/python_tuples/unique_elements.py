numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print(unique_numbers)

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
if 3 in set_a:
    print("3 is in set_a")
else:
    print("3 does not exist in set_a")

if 6 in set_b:
    print("6 is in set_b")
else:
    print("6 does not exist in set_b")

set_a.add(8)
print(set_a)

set_a.remove(8)
print(set_a)

set_a.discard(2)
print(set_a)