#There are two sets A and B. The set A consists of students rated by teacher A. The set B consists of students rated by teacher B. Some of the students were rated by both. The Principal  wants to find the students who were rated by teacher A only and by teacher B only but not both.
def main():
    a_count = int(input())
    a_rolls = set(map(int, input().split()))
    b_count = int(input())
    b_rolls = set(map(int, input().split()))
    result = a_rolls.symmetric_difference(b_rolls)
    print(len(result))

main()