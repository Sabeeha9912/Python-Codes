# To count vowels and constants.
sentence=(input("Enter any sentence:")) 
num_vowels=0
num_constant=0
vowels= "aeiouAEIOU"
for character in sentence:
        #if character .isalpha():
         if character in vowels:
            num_vowels=num_vowels+1
         else:
          num_constant=num_constant+1

print(f"No. of vowels is:{num_vowels}")
print(f"No. of constants is:{num_constant}")

