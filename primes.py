number=[]
primes=2
def file_writer(primes):
    pr=f"{primes}"
    if open("primes.txt",'a'):
        with open("primes.txt",'a') as f:
            f.write(pr+"\n")
    else: 
        with open("primes.txt",'w')as f:
            f.write("primes.txt")
              
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(f"{number} is a prime number.")
        prime=number
        file_writer(prime)


lower=int(input("what is the lower end of your range?\n "))
upper=int(input('what is the upper end of you range?\n'))
for n in range(lower,upper):
    number = n+1
    prime_checker(number)