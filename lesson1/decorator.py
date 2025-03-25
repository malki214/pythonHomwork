import datetime


#ex1
def time_of_run(func):
    def inner(*args, **kwargs):
        time1 = datetime.datetime.now()
        result = func(*args, **kwargs)
        time2 = datetime.datetime.now()
        print(f'time of run {time2 - time1}')
        return result
    return inner


@time_of_run
def f(num):
    for _ in range(num):
        pass


#f(10000000)

#EX2
@time_of_run
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

results = {}

def cache(func):
    def inner(num):
        if num not in results:
            print('in not exists')
            results[num] = func(num)
        return results[num]
    return inner

@time_of_run
@cache
def fibonacci_with_cache(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b



print(f"fib 10000: {fibonacci(10000)}")
print(f"fib with cache  - 10000: {fibonacci_with_cache(10000)}")
print(f"fib with cache  - 10000: {fibonacci_with_cache(10000)}")


