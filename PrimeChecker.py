def main():    
    n=get_number()
    print(primary(n))

#gets the number that we want to check from the user
def get_number():
    while True:
        n=int(input('type a number'))
        if n>0:
            return n

#verifies if a number is primary or not
def primary(n):
    match n:
        case 1 :
            return False 
        case _:
            for i in range (2,n//2+1):
                if (n%i==0):
                    return False
            return True
            
main()

    