def main():
    N = int(input())
    numbers = list(map(int, input().split()))
    num = tuple(numbers)
    print(hash(num))

main()

    '''for num in numbers:
        result = result * 31 + num'''