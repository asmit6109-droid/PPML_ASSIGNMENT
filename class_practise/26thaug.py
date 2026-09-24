s = "a4b3c2"
output = ""
for i in range(0,len(s),2):
    char = s[i]
    count = int(s[i+1])
    output += char * count
print(output)