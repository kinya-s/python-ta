import sys
import os


def prime(s):
    #take input from user
    s=int(input("Enter the number: "))
    #prime numbers are greater than 1
    if (s==1):
    return False
    elif(s==2):
        return True
    else :
        for x in range(2,s) 
        if(s % x==0):
    return False
   return True  

            
               


def solution(s):
    return prime(s)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argument required"))

    print(solution(sys.argv[1]))
