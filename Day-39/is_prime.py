import math

def is_prime(n: int) -> bool: 
    is_prime = True  
    for d in range(2, int(math.sqrt(n)) + 1):
        if n % d == 0: 
            is_prime = False 
            return is_prime 
    return is_prime

if __name__ == "__main__": 
    print(is_prime(n = 4))
    print(is_prime.__annotations__)