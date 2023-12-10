import re
str="This is python Program Portal"
match=re.search('Portal',str)
print("start index",match.start())
print("End index",match.end())
print(match)
