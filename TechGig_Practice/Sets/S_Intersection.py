#There are two sets A and B. The set A consists of students rated by teacher A. The set B consists of students rated by teacher B. Some of the students were rated by both. The Principal wants to find the total students who were rated by both. 
# Read number of students rated by A
a_count = int(input())
a_rolls = set(map(int, input().split()))
b_count = int(input())
b_rolls = set(map(int, input().split()))
common_students = a_rolls & b_rolls
print(len(common_students))