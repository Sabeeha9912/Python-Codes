# Task 2 (269)
money=int(input("Enter money:"))
candy_prize=2
candies=money//candy_prize   #// for iteger division.
wrapers=candies
while wrapers>=3:   # used when user return 3 or more wrappers.
    extra=wrapers//3   # gives free candies
    candies+=extra    
    wrapers=wrapers%3+extra
print(candies)



    





