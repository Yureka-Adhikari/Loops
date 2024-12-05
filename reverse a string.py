string=input("enter a word: ")

string2= ""

for i in string:
    string2= i + string2

print(f"original string: {string}")
print(f"reversed string: {string2}")