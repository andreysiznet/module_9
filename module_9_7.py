def is_prime(func):
    def wrapper(*args):
        summ = func(*args)

        for i in range(2, summ):
            if summ % i == 0:
                return f'Составное\n {summ}'
        else:
            return f'Простое \n {summ}'

    return wrapper


@is_prime
def sum_three(*line):
    summ = sum(line)
    return summ


result = sum_three(2, 3, 6)
print(result)
