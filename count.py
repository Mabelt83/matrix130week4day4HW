
#Exercise 2: Count Function Calls

#Overview:  
#Decorators can also be used to modify the behavior of functions in other ways, such as tracking how many times they have been called. 
# In this exercise, you will write a decorator that counts the number of times a function has been invoked.

 #Instructions:

#1. Create the Decorator: Write a decorator called `count_calls` that will increment a counter each time the decorated function is invoked.
# #You may want to use nonlocal variables or attributes on the function object to keep track.
 
#2. Apply to Fibonacci: Add the `count_calls` decorator to your memoized Fibonacci function from Exercise 1.
 
#3. Test the Count: Run the decorated function several times and verify that the count is accurate.



import unittest

def count_calls(func):
    count = 0

    def wrappers(*args): 
        nonlocal count
        count += 1
        return func(*args)
    wrappers.count = count
    return wrappers


@count_calls
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def test_fibonacci_count():
    assert fibonacci.count == 0
    fibonacci(10)
    assert fibonacci.count == 1
    fibonacci(10)
    assert fibonacci.count == 2


if __name__ == "__main__":
    unittest.main()
