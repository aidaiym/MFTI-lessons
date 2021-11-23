a = 239 #variable 
b = 392 # type is number 
string  = "Hello" # typ of variable is string
c = (a**2 + b**3)**0.5 
print(c)
print(string*3)

# ()	Parentheses
# **	Exponent
# +x, -x, ~x	Unary plus, Unary minus, Bitwise NOT
# *, /, //, %	Multiplication, Division, Floor division, Modulus
# +, -	Addition, Subtraction
# <<, >>	Bitwise shift operators
# &	Bitwise AND
# ^	Bitwise XOR
# |	Bitwise OR
# ==, !=, >, >=, <, <=, is, is not, in, not in	Comparisons, Identity, Membership operators
# not	Logical NOT
# and	Logical AND
# or	Logical OR


#Concationation is - Python string concatenation is the process of merging two or more strings. (A+B) (A*n)


#Conditions 
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
x = 3
if x>0:
    x = -x #Indentation refers to the spaces at the beginning of a code line. (4 whitespace)
print(x)

# Loops 
# While 
i = 1 # initial number
while i <= 10: # condition is true
    print(i)
    i += 1 # increment i, or else the loop will continue forever.

# break stop the loop even if the while condition is true
i = 1 
while i < 6:
  print(i)
  if i == 4:
    break  # stop
  i *= 2

  # Continue
i = 0
while i < 6:
  i += 1
  if i == 1:
    continue # stop the current iteration, and continue with the next
  print(i)

# For  iterating over a sequence 
books = ["Secrets of Droon", "Koran", "7 life"]
for x in books:
    print(x)