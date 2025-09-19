def count_file_stats(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            lines = text.splitlines()
            words = text.split()
            characters = len(text)
            print(f"Lines: {len(lines)}")
            print(f"Words: {len(words)}")
            print(f"Characters: {characters}")
    except FileNotFoundError:
        print("File not found. Please check the filename.")
        
filename = input("Enter the filename to analyze: ")
count_file_stats(filename)
