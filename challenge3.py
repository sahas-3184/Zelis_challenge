def finding_six_letter_word(pieces, dictionary):
    dictionary_set = set(dictionary)
    words_found = [] 
    attempts = []  
    
    
    # Iterate over all pieces
    for i in range(len(pieces)):
        for j in range(len(pieces)):
            if i != j:
                word_attempt = pieces[i] + pieces[j]
                attempts.append(f"{pieces[i]} + {pieces[j]} = {word_attempt}")
                if word_attempt in dictionary_set:
                    # adding the word
                    words_found.append(word_attempt)

    return words_found, attempts

pieces = [
    "al", "bums", "bar", "ely", "be", "foul", "con", "vex", 
    "here", "by", "jig", "saw", "tail", "or", "we", "aver"
]

dictionary = [
    "albums", "barely", "befoul", "convex", 
    "hereby", "jigsaw", "tailor", "weaver"
]


found_words, all_attempts = finding_six_letter_word(pieces, dictionary)



print("\nAttempts:")
for attempt in all_attempts:
    print(attempt)

print("Words found:")
print(found_words)