text=input("Enter a string:")
vowels="aeiouAEIOU"
vowel_count={}

for char in text:
    if char in vowels:
        if char in vowel_count:
            vowel_count[char]+=1
        else:
            vowel_count[char]=1

sorted_vowels=sorted(vowel_count.items(),key=lambda x:x[1],reverse=True)

for vowel,count in sorted_vowels:
    print(f"'{vowel}': {count}")
 
