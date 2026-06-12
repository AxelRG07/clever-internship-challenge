def digitsSum(n):
    suma = 0
    n = abs(n)

    while n > 0:
        suma += n % 10
        n = n // 10

    return suma

if __name__ == '__main__':
    inputInt = int(input())
    print(digitsSum(inputInt))