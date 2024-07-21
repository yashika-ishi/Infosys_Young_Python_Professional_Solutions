
#Write a Python function to find all the Strong numbers in a given list of numbers.
# Write another function to find and return the factorial of a number. Use it to solve the problem.

def factorial(number):
    if number == 1:
        return (number)
    elif number == 0:
        return 1
    else:
        return (number * factorial(number-1))


def find_strong_numbers(num_list):
    answer = []
    for num in num_list:
        temp = str(num)
        sum = 0
        for t in temp:
            sum = sum + factorial(int(t))
        if num == sum:
            answer.append(num)
    return (answer)

num_list=[145,375,100,2,10]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)

