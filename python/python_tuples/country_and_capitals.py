capitals = {'France': 'Paris', 'Spain': 'Madrid', 'Japan': 'Tokyo'}
for countries in capitals:
    print(f"the capital of {countries} is {capitals[countries]}.")

print("--------------------------------------------------------------------------")
# and example which is more visual:

capitals = {'France': 'Paris', 'Spain': 'Madrid', 'Japan': 'Tokyo'}
for x in capitals:
    print(f"the capital of {x} is {capitals[x]}.")

print("-------------------------------------------------------------------------") 
# a methood to practive the .keys() func, .values() func and the .items() func,
# then, try the .get() func:

capitals = {'France': 'Paris', 'Spain': 'Madrid', 'Japan': 'Tokyo'}

print("the keys are:", capitals.keys())

print("the values for each key are:", capitals.values())

print("lets see what is the items() func does:", capitals.items())

the_capital_of_germany = capitals.get('germany', 'not found')
print("the capital of germany:", the_capital_of_germany)