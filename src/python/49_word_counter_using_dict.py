def word_counter(s):
    counter = {}
    for char in s:
        counter[char] = s.count(char)
    return counter

inp_str = input("Enter a string :- ").strip()
print(word_counter(inp_str))
