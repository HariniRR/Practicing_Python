#isdecimal
def main():
    inp = input()  # raw_input returns a string in Python 2
    print(inp.isdecimal())  
main()

#isupper
def main():
    inp = input().strip()  
    print(inp.isupper())  
main()

#istitle
def main():
    inp = input()
    print(inp.istitle())  
main()

#isnumeric
def main():
    inp = input()  
    print(inp.isnumeric())  
main()

#islower
def main():
    inp = input()  
    print(inp.islower())  
main()

#isdigit
def main():
    inp = input() 
    print(inp.isdigit())  
main()