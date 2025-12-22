import sys
# 1
a = "text_variable"
b = 1
b1 = 1.1
c = ["a", 1, 1.25, "Word", a] 
d = {"a": "Word", "b": 1, a: b} 
e = ("a", a) 
f = {"ss", a + str(b)}  

print("Variable a:", a)
print("Variable b:", b)
print("List c:", c)
print("Dict d:", d)
print("Tuple e:", e)
print("Set f:", f)
# 2
print(f"Output like this is possible: {False}")
help("keywords")  
# 3
print(abs(-12.5), f"is equal to {abs(12.5)}", "and comparison:", abs(-12.5) == abs(12.5))
print(round(12.5678, 2))

# 4
letters = ["a", "b", "c"]
for i in range(len(letters)):
    print(f"At position {i} is letter {letters[i]}")
else:
    print("This else clause is pointless!")
# 5
from random import randint
A = randint(0, 1)
print(f"So A={A}" if A else f"But it can be A={A}")
# 6
A = 0
try:
    print("What happens if", 10 / A, "?")
except Exception as e:
    print("Is this an error >", e)
finally:
    print("Here you go!")
# 7
with open("temp.txt", "w") as f:
    f.write("This is the first line\n")
    f.write("This is the second line\n")
with open("temp.txt", "r") as f:
    for _, line in enumerate(f):
        print(f"{_})> {line.strip()}")
# 8
def a_b_func(a, b):
    return a, b

this_is_lambda = lambda first, age: f"This code was written by: {first}, I am {age} years old"

print("Just a function call:", a_b_func("a", 1))
print("And this is lambda:", this_is_lambda)
print("Calling lambda with actual data:", this_is_lambda('Vadim', 100_000))
print("Calling lambda via function output:", this_is_lambda(*a_b_func("a", 1)))

