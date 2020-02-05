#review1_print Triangles_20190605

def triangle():
    p = [1]
    for i in range(10):
        print(p)
        p = [1] + [p[n]+p[n+1] for n in range(len(p)-1)] + [1]
def main():
    triangle()
if __name__ == "__main__":
    main()
