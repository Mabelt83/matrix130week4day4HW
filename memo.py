#1. Write a Decorator: Create a Python decorator called `memoize` that will store already computed values for any function to which it's applied.
#Use a dictionary to store the results.
#The keys will be the arguments passed to the function, and the values will be the results.
 
#2.Apply to Fibonacci: Apply the `memoize` decorator to a recursive Fibonacci function. The function should take an integer `n` and 
#return the nth Fibonacci number.
 
#3. Test It: Test your decorated Fibonacci function with high values of `n`.
#For comparison, run the same function without the decorator and notice the speed difference.
#Use your new unittest skills we learned today!


def memoize(func):
    

    cache = {}

    def wrappers(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrappers


def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


@memoize
def fibonacci_deco(n):
    if n < 2:
        return n
    else:
        return fibonacci_deco(n - 1) + fibonacci_deco(n - 2)


def fibonacci_undeco(n):
    if n < 2:
        return n
    else:
        return fibonacci_undeco(n - 1) + fibonacci_undeco(n - 2)









   
