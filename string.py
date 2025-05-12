
#for char in s:
#    rev=char+rev
#if rev==s:
#     print("it is palindrome string",rev)
#else:
#    print("Not",rev)
# calculate charcters in a string : 

S=input("Enter a string:")
char_count={}

for char in S:
    if char in char_count:
        char_count[char]+=1
    else:
        char_count[char]=1

sorted_char=sorted(char_count.items(),key=lambda x:x[1],reverse=True)

for char,count in sorted_char:
    print(f"'{char}':{count}")
