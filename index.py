def fizz_buzz(number):
  if number % 3 == 0:
    if number % 5 == 0:
      return "fizzbuzz"
    return "fizz"
  if number % 5 != 0:
    return number
  return "buzz"


nums = 50
print(fizz_buzz(nums))
   
