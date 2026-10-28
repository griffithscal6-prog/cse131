
def factorial_loop(n):
    factorial = 1
    for i in range(1, n + 1):
        
        factorial *= i
        

    return factorial

def factorial_recursion(n):
    if n == 1:
        
        return n
    else:
        return n * factorial_recursion(n-1)
    

    
    
# def function_2(y):
#     y += 20
#     return y

# def function_1(x):
#     x += function_2(x)
#     return x

def main():
    n = 990    
    # total = function_1(a)
    # print(total)
    total = factorial_loop(n)
    print(total)
    total_recursion = factorial_recursion(n)
    print(total_recursion)
    print(factorial_recursion(n))

main()