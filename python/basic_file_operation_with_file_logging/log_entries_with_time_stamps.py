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
        another_entries = input("what is the entry purpose?: ") #how to make it that after break it doenst print another "what is the purpose..."
        if not another_entries:
            break      
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        j_file.write(f"{timestamp}  entry number: {entry}\n")

with open("journal.txt", "r") as j_file:

    total_entries = 0
    total_words = 0

    for line in j_file:
        total_entries += 1
        words = line.split()
        total_words += len(words[2:])
print(f"the number of entries to the log file: {total_entries} and the number of words it holds in entries are: {total_words}")