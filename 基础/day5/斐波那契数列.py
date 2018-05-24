def fibo(n):
    before = 0
    after = 1
    for i in range(n - 1):
        ret = before + after
        before = after
        after = ret
    return ret
print(fibo(7))


# **************递归*********************
def fibo_new(n):  # n可以为零，数列有［0］
    if n <= 1:
        return n
    return (fibo_new(n - 1) + fibo_new(n - 2))
print(fibo_new(4))