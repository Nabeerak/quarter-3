def prime(no):
    if no%2==0:
         return False
    if no <=1:
          return False
    if no== 2:
          return True
    
    for j in range(3, int(no**0.5)+1, 2):
     if no%i ==0:
          return False
    return True
def for_reveal():
    name = str(input("enter your name:"))
    numbers = []
    for i in range(3):
        num= int(input("Enter your favourite number:"))
        numbers.append(num)

    print(f"\nHello, {name}! Let's explore your favorite numbers:")

    even_or_odd = [(num, "even" if num % 2 == 0 else "odd") for num in numbers]
    for num, real in even_or_odd:
        print(f"The number {num} is {real}.")

    for num in numbers:
     print(f"the numbers {num} and its square: ({num}, {num**2})")

    totalSum = sum(numbers)
    print(f"\nAmazing! the sum of your favourite numbers is: {totalSum}")


    if prime(totalSum):
     print(f"Wow, {totalSum} is a prime number!")
    else:
     print(f"The sum {totalSum} is not a prime number, but it's still great!")
for_reveal()
