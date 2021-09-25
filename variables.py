# x = 48 #(Comment out multi-line reminder: Ctrl + K + C. Uncomment: Ctrl + K + U. Highlight the lines first if commenting/uncommenting
# # multiple lines)
# y = 6
# z = 5 + x
# c = x + y

# print(z)

# Arithmetic operators: + - * / ( Self-explanatory)  ** - Power of operator (ex: 2 ** 3 = 8, aka 2 * 2 * 2), If you don't use (), then 
# calc priority from highest to lowest is: **, *, /, +, - 

x = (3 + 5) * 6
print(x)

y = ((3 + 5) * 2) ** 2/ 16 - 1 # These double () make it so that 3 + 5 is added first. Then result is * by 2. Then the power operator 
# comes into play. Finally, the result is / by 16, then - 1, which is supposed to result in 15.
print(y)


# Methods are good to know in Python. They help avoid repetition in code, especially if you want the same function to be done over and over
# again. Methods are a kind of function that are limited by data type. Some methods [put () after the method]: 
# .upper - Converts letters in a string to upper case
# .title - Converts the 1st letter in a string to upper case
# .lower - Converts letters in a string to lower case
# .split - Eliminates the space in the starting letters.
# .replace [Requires at least 2 arguments or 2 letters in () ]- 1st argument shows where you want to replace the string. 2nd argument shows 
#  what you want to replace the string with.
# .slice - Literally slices up a string according to what index you indicate in [] - 

# Why is indexing in Python important? 
# Remember, indexing starts at 0 for positive indexing. Starts at -1 if it's negative indexing.