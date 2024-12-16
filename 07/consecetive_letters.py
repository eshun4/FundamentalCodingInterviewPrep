"""
Given a string lik ""aabcddefgghhijjk" write a program that counts the consecutive letters in the string.
Stretch 1: Return a list of all the consecutive letters. e.g ['aa', 'bb', 'cc']
Stretch 2: Return the count of the consecutive vowel letters.
Stretch 3: Return a list of all the consecutive vowel letters.  e.g. ['aa','ee', 'ii', 'oo','uu'].

"""


def count_consecjutive_letters(str_inp):
    """This function counts the number of consecutive letters in the string input provided."""
    # Create a variable to store the count of consecutive letters
    consecutive_let_count = 0
    # Create another variable to keep track of the previous letter
    prev_letter = None
    # Iterate through each letter in the string 
    for lett in str_inp:
        if prev_letter == lett:
            consecutive_let_count += 1
        prev_letter = lett
    # Return the consecutive letter count
    return consecutive_let_count


def count_consecjutive_letters_stretch1(str_inp):
    """This function counts the number of consecutive letters in the string input provided."""
    # Create an array to store the consecutive letters
    consecutive_letters= []
    # Create another variable to keep track of the previous letter
    prev_letter = None
    # Iterate through each letter in the string 
    for lett in str_inp:
        if prev_letter == lett:
            consecutive_letters.append(prev_letter + lett)
        prev_letter = lett
    # Return the consecutive letter count
    return consecutive_letters


def count_consecjutive_letters_vowel(str_inp):
    """This function counts the number of consecutive letters in the string input provided."""
    # Create a variable to store all the vowels
    vowels = "aeiouAEIOU"
    # Create a variable to store the count of consecutive letters
    consecutive_vowel_let_count = 0
    # Create another variable to keep track of the previous letter
    prev_letter = None
    # Iterate through each letter in the string 
    for lett in str_inp:
        if prev_letter == lett and prev_letter in vowels and lett in vowels:
             consecutive_vowel_let_count += 1
        prev_letter = lett
    # Return the consecutive letter count
    return  consecutive_vowel_let_count

def count_consecjutive_letters_vowel_arr(str_inp):
    """This function counts the number of consecutive letters in the string input provided."""
    # Create a variable to store all the vowels
    vowels = "aeiouAEIOU"
    # Create a variable to store the count of consecutive letters
    consecutive_vowel_letters = []
    # Create another variable to keep track of the previous letter
    prev_letter = None
    # Iterate through each letter in the string 
    for lett in str_inp:
        if prev_letter == lett and prev_letter in vowels and lett in vowels:
             consecutive_vowel_letters.append(prev_letter + lett)
        prev_letter = lett
    # Return the consecutive letter count
    return consecutive_vowel_letters
def main():
    inp = "aabcddeefgghhiijjk"
    out1 = count_consecjutive_letters(inp)
    print(f"Count: {out1}")
    
    # Func 2 test
    out2 = count_consecjutive_letters_stretch1(inp)
    print(f"Count: {out2}")
    
    # Func test 3
    out3 = count_consecjutive_letters_vowel(inp)
    print(f"Count: {out3}")
    
    # Func test 4
    out4 = count_consecjutive_letters_vowel_arr(inp)
    print(f"Count: {out4}")

if __name__ == "__main__":
    main()