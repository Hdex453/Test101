
def factorial(n):
    if n == 1:
        return n
    return n * factorial(n-1)


def exponential(x, n):
    if n == 1:
        return x
    return x * exponential(x, n-1)


if __name__ == "__main__":
    print(factorial(5))
    print(exponential(2, 4))
