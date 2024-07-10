import re

s1 = "Micheal Jackson is the best"
pattern = r"jack"

result = re.search(pattern,s1)

if result:
    print("Match found")
else:
    print("Match not found")