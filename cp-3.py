str=input("Enter a string : ")
s=str.split()
for i in  range(0,len(s),1):
    if(s[i] != s[i][::-1]):
        s[i] = s[i]+s[i][::-1]
str=" ".join(s)
print(str)