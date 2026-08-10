# ----------------TOPICS NAME-------------------
# 1. use of list comprehension
# 2. use of lambda
# 3. use of map()
# 4. use of filter()
# --------------- 1. USE OF LIST  COMPREHENSION---------------
# NORMAL LIST
for i in range(1,20):
    if i%3==0:
        print("number divided by 3 :", i)
# lst comprehension
division = [i for i in range(1,20) if i%3==0]
print(division)
# normal lst
for i in range(1,50):
    if i%7==0:
        print("division of 7:",i)
# lst comprehension
division = [i for i in range(1,50) if i%7==0]
print(division)
#  lst comprehension
fruits = ["apple","kiwi","banana","fig"]
size = [i for i in fruits if len(i)>4]
print(size)
# lst comprehension
num = [1,2,3,4,5]
new_num = [i*i for i in num ]
print(new_num)
# lambda
num = "424"
new_num = num[::-1]
palindrome = lambda x:  num == new_num 
print("num is palindrome",palindrome)
#map
word = ["pineapple"]
big = list(map(lambda x : x.upper(),word))
print(big)
# map
celcius = [0,20,37,100]
fahrenheit = list(map(lambda x : x*9/5+32,celcius))
print(fahrenheit)
# filter
num = [1,-2,3,4,-5,-7]
positive = list(filter(lambda x: x>0,num))
print(positive)
# filter
fruits = ["apple","banana","kiwi","orange"]
vowels = list(filter(lambda x : x and x[0] in "aeiou",fruits))
print(vowels)
# filter and map
num = [12,7,5,25,3,18,41]
odd = list(filter(lambda x : x%2 != 0,num))
print(odd)
square = list(map(lambda x : x*x,odd))
print(square)



