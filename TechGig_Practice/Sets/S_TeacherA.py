#There are two sets A and B. The set A consists of students rated by teacher A. The set B consists of students rated by teacher B. Some of the students were rated by both. The Principal  wants to find the students who were rated by teacher A only.
def main():
    a = int(input())
    arate = set(map(int, input().split()))
    b = int(input())
    brate = set(map(int, input().split()))
    only_a = arate - brate#(a.difference(b))
    print(len(only_a))

main()