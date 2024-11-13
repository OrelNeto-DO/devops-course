# student = {"name" : "orel", "age" : 25, "grade" : 100}
# print(student["name"])
# student["school"] = "sela"
# print(student["school"])
# #""just tryna access the key and not the value"""
# print(list(student.keys())[0])

#same code just wanna make changes without affecting what is working:
student = {"name" : "orel", "age" : 25, "grade" : 100}

print(student["name"])

student["school"] = "sela"
print(student["school"])

student["age"] += 1
print("updated age", student["age"])

del student["grade"]
print("dictionary after removing 'grade' from student", student)

if "grade" in student:
    print("the grade is", student["grade"]) 
else:
    print("the student dictionary does not contain a value for 'grade'")