#!/usr/bin/env python3

def print_fibonacci(n):
    # Initialize the Fibonacci sequence with the first two elements
    fib = [0, 1] if n > 1 else [0] * n  # Handle n = 0 or 1 cases
    
    # Generate the Fibonacci sequence up to the length n
    for i in range(2, n):
        # Add the sum of the last two elements to the sequence
        fib.append(fib[i-1] + fib[i-2])
    
    # Print the Fibonacci sequence as a list
    print(fib[:n])

# Example usage:
print_fibonacci(9)  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21]

