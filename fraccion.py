
class Fraccion():
    pass


def main():
    a = Fraccion(2, 6)
    b = Fraccion(7, 9)
    print(f'Fraccion a : {a}')
    print(f'Fraccion b : {b}')
    print(f'a+b : {a.suma(b)}')
    print(f'a*b : {a.mult(b)}')


print(__name__)
if __name__ == "__main__":
    main()
