def main():
    n = int(input())
    students = []
    
    for _ in range(n):
        name = input().strip()
        rating = int(input())
        students.append([name, rating])
    
    min_rating = min(student[1] for student in students)
    lowest_rated_students = [student[0] for student in students if student[1] == min_rating]
    lowest_rated_students.sort()
    
    for name in lowest_rated_students:
        print(name)

main()