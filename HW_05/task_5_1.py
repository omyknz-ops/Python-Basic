# Complete the function caching_fibonacci so that it returns a function that computes Fibonacci numbers using memoization.
def caching_fibonacci():
    cache = {} # Dictionary to store previously computed Fibonacci numbers

    # Inner function to compute Fibonacci numbers with memoization
    def fibonacci(n):
        if n <=0: # Base case for Fibonacci sequence
            return 0 
        if n == 1: # Base case for Fibonacci sequence
            return 1
        if n in cache: # Check if the value is already computed
            return cache[n] 
        else: # Compute the Fibonacci number recursively
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2) # Compute and store in cache
            return cache[n]
        
    
    return fibonacci # Return the inner function

# Example usage:
fib = caching_fibonacci()
print(fib(10))  # Output: 55
print(fib(50))  # Output: 12586269025