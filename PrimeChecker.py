import math

def main():    
    n = get_number()
    # improved output message
    if prime(n):
        print(n, 'is a prime number.')
    else:
        print(n, 'is not a prime number')

# gets the number that we want to check from the user
def get_number():
    while True:
        try:
            n = int(input('type a number: '))
            if n > 0:
                return n
            print('only positive numbers, try again')
        except ValueError:
            print('that is not a number, try again')

# verifies if a number is prime or not
def prime(n):
    if n == 1:
        return False 
    # Using sqrt(n) limits the range and makes the check faster
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

main()

    