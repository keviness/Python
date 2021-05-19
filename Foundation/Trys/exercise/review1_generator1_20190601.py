#review1_generator1_20190601

def fio(n):
    a, b, s = 0, 1, 0
    while s< n:
        yield b
        a, b = b, a+b
        s += 1
if __name__ == "__main__":
    s = fio(10)
    for i in s:
        print(i)
