text = "The quick brown fox jumps over the lazy dog"

print("fox" in text)
print("cat" in text)

if "fox" in text: 
    print(True)
else: 
    print(False)

if "cat" in text:
    print(True)
else:
    print(False)
  
print(bool("fox" in text))
print(bool("cat" in text))