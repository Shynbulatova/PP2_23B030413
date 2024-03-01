# Python RegEx exercises

# Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re

def match_pattern(text):
    pattern = r'ab*'  
    match = re.fullmatch(pattern, text)
    if match:
        return True
    else:
        return False

test_strings = ["a", "ab", "abb", "abbb", "ac", "b", "ba", "bb"]
for string in test_strings:
    print(f"String: {string}, Matched: {match_pattern(string)}")

# Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
import re

def match_pattern(text):
    pattern = r'ab{2,3}'  
    match = re.fullmatch(pattern, text)
    if match:
        return True
    else:
        return False

test_strings = ["ab", "abb", "abbb", "abbbb", "ac", "b", "ba", "bb"]
for string in test_strings:
    print(f"String: {string}, Matched: {match_pattern(string)}")


# Write a Python program to find sequences of lowercase letters joined with a underscore.
import re

def find_sequences(text):
    pattern = r'\b[a-z]+_[a-z]+\b'  
    matches = re.findall(pattern, text)
    return matches

test_string = "This_is_a_test_string with_multiple_sequences_of_lowercase_letters_joined_with_underscore."
sequences = find_sequences(test_string)
print("Sequences found:", sequences)



# Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re

def find_sequences(text):
    pattern = r'[A-Z][a-z]+'  
    matches = re.findall(pattern, text)
    return matches

test_string = "This is a Test String With Multiple Sequences of One Uppercase Letter Followed by Lowercase Letters."
sequences = find_sequences(test_string)
print("Sequences found:", sequences)



# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re

def match_pattern(text):
    pattern = r'a.*b$'  
    match = re.fullmatch(pattern, text)
    if match:
        return True
    else:
        return False

test_strings = ["acb", "a123b", "ab", "axby", "aZb", "a\nb", "aB"]
for string in test_strings:
    print(f"String: {string}, Matched: {match_pattern(string)}")



# Write a Python program to replace all occurrences of space, comma, or dot with a colon.
import re

def replace_chars(text):
    pattern = r'[ ,.]'  
    replacement = ':'   
    replaced_text = re.sub(pattern, replacement, text)
    return replaced_text

test_string = "This is, a test. Replace spaces, commas. and dots with colons."
result = replace_chars(test_string)
print("Original:", test_string)
print("After replacement:", result)



# Write a python program to convert snake case string to camel case string.
def snake_to_camel(snake_case):
    words = snake_case.split('_')  
    camel_case = words[0] + ''.join(word.capitalize() for word in words[1:]) 
    return camel_case

snake_case_string = "snake_case_example_string"
camel_case_string = snake_to_camel(snake_case_string)
print("Snake Case:", snake_case_string)
print("Camel Case:", camel_case_string)



# Write a Python program to split a string at uppercase letters.
import re

def split_at_uppercase(text):
    pattern = r'[A-Z][a-z]*'  
    split_words = re.findall(pattern, text)
    return split_words

test_string = "SplitThisStringAtUppercaseLetters"
split_words = split_at_uppercase(test_string)
print("Original string:", test_string)
print("Split at uppercase letters:", split_words)



# Write a Python program to insert spaces between words starting with capital letters.
import re

def insert_spaces(text):
    pattern = r'(?<!^)(?=[A-Z])'
    spaced_text = re.sub(pattern, ' ', text)
    return spaced_text

test_string = "InsertSpacesBetweenWordsStartingWithCapitalLetters"
spaced_text = insert_spaces(test_string)
print("Original string:", test_string)
print("With spaces inserted:", spaced_text)


# Write a Python program to convert a given camel case string to snake case.
def camel_to_snake(camel_case):
    snake_case = ''
    for char in camel_case:
        if char.isupper():
            snake_case += '_' + char.lower()
        else:
            snake_case += char
    return snake_case.lstrip('_')

camel_case_string = "CamelCaseExampleString"
snake_case_string = camel_to_snake(camel_case_string)
print("Camel Case:", camel_case_string)
print("Snake Case:", snake_case_string)
