input_string=input("Enter the word: ")
def remove_vowels(input_string):
    vowels="aeiouAEIOU"
    result=""

    for char in input_string:
        if char not in vowels:
            result+=char
    
    return result

output_str=remove_vowels(input_string)
print(output_str)
