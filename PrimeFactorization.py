# Prime Factorization - Have the user enter a number and find all Prime Factors (if there are any) and display them.


# THIS FUNCTION WILL CHECK IF A NUMBER IF PRIME.
def prime_finder(num):
    is_prime = True
    if num == 0 or num == 1:  # Avoid dividing by 0 and 1.
        is_prime = False
    else:
        for n in range(2, num):  # Loop runs check if a number is prime.
            if n == num:
                break  # Ensures a number is not divided by itself.
            else:
                if num % n != 0:
                    is_prime = True
                    continue  # Continue until to ensure there are no factors.
                elif num % n == 0:
                    is_prime = False
                    break  # If there are factors, break immediately (not prime)
    return is_prime


# FIND ALL THE PRIME FACTORS OF A NUMBER
def all_primes(number):
    # An array to store the factors.
    prime_factors = []

    # An array to store the largest factors.
    largest_factors = []

    # Find all the factors of the number
    if number == 2:
        return [1, 2]
    elif number == 3:
        return [1, 3]
    elif prime_finder(number):
        return [1, number]
    elif number > 1:
        factors = [num for num in range(1, number) if number % num == 0]
    else:
        return "Cannot find prime factors!!!"

    # Get the first and second largest factors to factorize.
    first_largest = factors[len(factors) - 1]
    second_largest = 0

    # Remove the 1 from the list of factors since we do not need it.
    factors.remove(1)

    # Calculate the second largest factor.
    for second_factor in factors:
        if second_factor * first_largest == number:
            second_largest = second_factor

    # Append the fist and second largest in their array.
    largest_factors.append(first_largest)
    largest_factors.append(second_largest)

    factors.clear()  # Clear the factors array to append new factors.

    # Compute the factors of the largest stored factors.
    for factor in largest_factors:
        if prime_finder(factor):
            prime_factors.append(factor)

        else:
            factors = [num for num in range(1, factor) if factor % num == 0]  # Find all the factors and store them.
            first_largest = factors[len(factors) - 1]
            largest_factors.append(first_largest)

            # Remove the 1 from the list of factors since we do not need it.
            factors.remove(1)

            for second_factor in factors:  # Calculate the second largest factor.
                if second_factor * first_largest == factor:
                    second_largest = second_factor
                    largest_factors.append(second_largest)

    return prime_factors


if __name__ == '__main__':
    user_number = int(input("Enter a number to find its prime numbers? "))
    print(all_primes(user_number))

