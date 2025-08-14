def count_occurrences(text, character):
    count = text.count(character)
    return count
ipstring = "hello world"
targetchar = "l"
result = count_occurrences(ipstring, targetchar)
print(f"The character '{targetchar}' appears {result} times in '{ipstring}'.")
#op : The character 'l' appears 3 times in 'hello world'.
