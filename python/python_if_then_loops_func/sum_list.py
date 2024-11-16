def sum_list(list):
    list = [10, 20, 30, 40, 50]
    total = 0
    for i in list:
        total += i
    return total

print(f"{sum_list(list)}")

def summing(lst):
    total = 0
    for i in lst:
        total += i
    return total

result = summing([10, 20, 30, 40, 100])  # קריאה לפונקציה עם רשימה
print(result)  # הדפסת התוצאה
