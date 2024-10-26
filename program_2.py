# Program #2: Word Separator
# Write a program that accepts as input a sentence in which all of the words are run together, 
# but the first character of each word is uppercase.  
# Convert the sentence to a string in which the words are separated by spaces, 
# and the first word starts with an uppercase.  
# For example the string "StopAndSmellTheRoses" would be converted to "Stop and smell the roses."

# Start your changes on line 13

def word_separator(sentence : str) -> str:

    new_sentence = ""
    #    Add your logic here
    first_char_found : bool = False
    for character in sentence:
        # if character is uppercase
        if character == character.upper():
            # if the first uppercase is already found, convert all others to lower case
            if first_char_found:
                new_sentence += f" {character.lower()}"
                continue # make sure there are no duplicate characters by sending back to the start of the for loop
            first_char_found = True 
        new_sentence += character

    return new_sentence.strip()

# Example usage
if __name__ == "__main__":
    sentence = "StopAndSmellTheRoses"

    new_sentence = word_separator(sentence)

    print(new_sentence)