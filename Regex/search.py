import re
with open('mbox-short.txt') as file:
    for line in file:
        # print(line)
        line = line.rstrip()
        #Using Search method
        # if re.search('^From:', line): 
        #     print(line)

        # Using Findall and \S ()
        # email = re.findall('^From (\S+@\S+)',line) # \S : non-blank char; + : one or more occurance
        # if email != [] :
        #     print(email)
            

        #Using Findall and non-space opeartion
        y = re.findall('^From .*@([^ ]*)',line) # .: any char; *: zero or more occurance
        print(y)
        email = re.findall('^From (\S+@\S+)',line)
