# Challange 1
# integer to number representation

def fn_num_words():
    numerics_in_words = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
        "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, 
        "seventeen": 17, "eighteen": 18, "nineteen": 19,
        "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90
    }
    return numerics_in_words



def word_to_number(words):
    numerics_in_words = fn_num_words()    
    #  multipliers
    multipliers = {"hundred": 100, "thousand": 1000, "million": 1000000}
    # formating the input
    words = words.lower().replace("-", " ").split()    
    result = 0
    current_number = 0
    is_negative = False
    
    for word in words:
        if word == "negative":
            is_negative = True
        elif word in numerics_in_words:
            current_number += numerics_in_words[word]
        elif word in multipliers:
            if word == "hundred":
                current_number *= multipliers[word]
            else:
                current_number *= multipliers[word]
                result += current_number
                current_number = 0
    result += current_number    
    if is_negative:
        result = -result    
    return result


# Loop for multiple inputs
while True:
    user_input = input("Enter a number in words or type 'exit': ")
    if user_input.lower() == "exit":
        print("Taking exit")
        break
    try:
        number = word_to_number(user_input)
        print(f"The numeric representation is: {number}")
    except Exception as e:
        print(f"An error occurred: {e}. Please enter a word")