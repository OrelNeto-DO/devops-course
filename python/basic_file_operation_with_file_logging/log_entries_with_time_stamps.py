import datetime

with open("journal.txt", "a") as j_file:
    #i = 0
    #while i < 4:
        entry = (input("journal entry: "))
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        j_file.write(f"{timestamp}  entry number: {entry}\n")
        #i += 1

with open("journal.txt", "r") as j_file:
    for line in j_file:
        print(line.strip())

with open("journal.txt", "a") as j_file:
    while True:
        another_entries = input("what is the entry purpose?: ")
        if not another_entries:
            break      
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        j_file.write(f"{timestamp}  entry number: {entry}\n")