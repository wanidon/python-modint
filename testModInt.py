from modint import ModInt,cmb
# import modint
# modint.MOD = 11

def main():
    i = ModInt(10)
    j = 2
    print(str(i))
    print(int(i))
    print(i + j)
    print(i - j)
    print(i * j)
    print(i / j)
    print(i ** j)
    print(i // j)
    print(j + i)
    print(j - i)
    print(j / i)
    print(j * i)
    print(j / i * i)
    print(i ** j)
    print(j ** i)
    print(j // i)
    print(i < j)
    print(j < i)
    print(i <= j)
    print(i == j)
    print(cmb(ModInt(6),ModInt(3)))
    print(ModInt(6) in [1,2,3,4,5,6])
if __name__ == '__main__':
    main()
