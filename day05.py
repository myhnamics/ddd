import random
def process(number_list,f):
    for no in number_list:
        print(f(no))
def squre(n):
    """


    :param n:
    :param func:
    :return:
    """
    return n*n


numbers = [random.randint(1,100) for i in range(5)]
print(numbers)

# process(numbers,squre)

process(numbers, lambda x: x*x)