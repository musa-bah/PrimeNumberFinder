# THIS TEST BENCH WILL FIND THE PRIME NUMBERS OF EACH NUMBER IN A GIVEN RANGE.
from PrimeFactorization import all_primes

#  ENTER RANGE.
rrange = int(input("Enter range? "))
mega_prime_numbers = []
for num in range(rrange):
    mega_prime_numbers.append(all_primes(num))

for item in range(len(mega_prime_numbers)):
    print(mega_prime_numbers[item])
    print("\n")
