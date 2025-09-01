''' bunch from strings one on each line and you need to concatenate them as shown in the sample.
ip: 
    -
    a
    b
    c
op: 
    a-b-c '''
    
def main():
    import sys
    sym = sys.stdin.readline().strip()  # Read the delimiter
    lines = [line.strip() for line in sys.stdin if line.strip()]  # Read remaining lines
    result = sym.join(lines)
    print(result)

main()