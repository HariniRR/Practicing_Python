#You will have to create a dictionary and output the average score of the player asked upto 2 decimal places.

def main():
    n = int(input())
    play_score = {}
    for _ in range(n):
        data = input().split()
        name = data[0]
        score = list(map(int, data[1:]))
        play_score[name] = score
    player = input()
    a = play_score.get(player)
    avg = sum(a) / len(a)
    print(f"{avg:.2f}")  
 # Write code here 

main()


