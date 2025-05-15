s = input("Enter a string:")
vowels = "aeiouAEIOU"
vowel_count = { c for c in s if c in vowels}
consonant_count = {c for c in s if c.isalphabet() and c not in vowels}
print("Vowels:", vowel_count, "Consonants:", consonant_count)
