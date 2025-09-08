'''There are a total N students present in today's class. You are given student names and their respective height (in cms).
You have to find names of all the second highest students (according to their heights).
If there are multiple students , print each name on new line.'''
def main():
    n = int(input())
    students = []
    for _ in range(n):
        name = input().strip()
        height = int(input().strip())
        students.append((name, height))
    heights = sorted({height for _, height in students}, reverse=True)
    if len(heights) < 2:
        return
    second_highest = heights[1]
    second_highest_students = [name for name, height in students if height == second_highest]
    for name in sorted(second_highest_students):
        print(name)

main()