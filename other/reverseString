
from functools import lru_cache

def reverse_string_loop(sentence):
    for i in range (len(sentence)-1, -1, -1):
        print(sentence[i], end="")

def reverse_string_recursion(sentence):
    if len(sentence) == 1:
        print(sentence[0], end="")
    else:
        reverse_string_recursion(sentence[1: ])
        print(sentence[0], end="")

@lru_cache(maxsize=None)
def fibonacci_recursion(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)


    

def main():
    sentence = "The quick brown fox jumps over the lazy dog."

    reverse_string_loop(sentence)

    print()

    reverse_string_recursion(sentence)
    
    print()

    # Display Fibonacci numbers
    u = int(input("Please enter the number in the fibonacci sequence you want to calculate to? "))
    for i in range(u + 1):
        print(f"Fibonacci({i}) = {fibonacci_recursion(i)}")

main()