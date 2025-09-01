'''You are given a dataset of N students belonging to the same class.
The data contains name of the student followed by marks they scored in five subjects which are Physics, Chemsistry, Maths, English, Hindi.
Your task is find the average marks of the class for each individual subject.
ip:2
arpit 100 75 40 56 53
anushka 100 100 76 100 100
op:100.00 87.50 58.00 78.00 76.50'''

def main():
    num=int(input())
    subject_totals = [0] * 5  # Initialize totals for 5 subjects
    for _ in range(num):
        data=input().split()
        marks = list(map(int, data[1:])) #ignores name 
        for i in range(5):
            subject_totals[i] += marks[i]
    averages = [total / num for total in subject_totals]
    # Print each average formatted to 2 decimal places
    for avg in averages:
        print(f"{avg:.2f}", end=" ")


 # Write code here 

main()

