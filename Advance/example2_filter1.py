# filter(1)删除偶数，保留奇数

def is_odd(n):
    return n % 2 == 1
list(filter(is_odd, [1, 2, 4, 5, 6, 7, 8, 9, 10, 19]))

is_odd()
