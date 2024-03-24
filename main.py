def f(n: int) -> int:
    if (n == 0 or n == 1):
        return 1
    return f(n - 1) + f(n - 2)

if __name__ == "__main__":
    for i in range(10):
        print(f(i), end=' ')