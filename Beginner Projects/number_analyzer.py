# This project evaluates a number to give us a few characteristics

'''Here we check characteristics whether odd or even number'''
def check_odd_even(number):
  if number % 2 == 0:
    print(f'{number} is an even number')
  else:
    print(f'{number} is an odd number')

''' Here we find the factors of characteristics'''
def get_factors(number):
  factors = []
  iteration_index = 1
  while iteration_index <= number:
    if number % iteration_index == 0:
      factors.append(iteration_index)
    iteration_index += 1
  print(f'The factors of {number} are: {factors}')
  return(factors)

''' Here we check whether number is a prime number'''
def check_prime(number, factors):
  if len(factors) == 2:
    print(f'{number} is a prime number')
  else:
    print(f'{number} is not a prime number')

''' Finally we create an overall function, so user doesnt have to type each one individually'''
def analyze_number(number):
  check_odd_even(number)
  factors = get_factors(number)
  check_prime(number, factors)

analyze_number(4)

# We can play around to check other characteristics
# Whether positive or negative, float or integer etc.