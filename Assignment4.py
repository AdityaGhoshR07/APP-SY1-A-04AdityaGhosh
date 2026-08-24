#Calculate the nth fibonacci number using techniques that optimize time complexity, ensuring that the computation is fast and scalable even for large values of n.
import time
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    try:
        n = int(input("Enter the value of n: "))
        if n < 0:
            print("Please enter a non-negative integer.")
        else:
            start_time = time.perf_counter()
            res = fib(n)
            end_time = time.perf_counter()
            
            exec_time = (end_time - start_time) * 1000
            
            print(f"The {n}th Fibonacci number is: {res}")
            print(f"Execution time: {exec_time:.6f} milliseconds")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
