# Python CeaserPigLatin Encryption
# Trey Hall
# 9/17/18

consonants = [ 'B', 'C', 'D', 'F', 'G', 'H',  'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
vowels = ['A','E','I','O','U',]

def letter_is_vowel (letter):
	is_vowel = -1
	# begin a loop through the vowel array
	for current_letter in range(len(vowels)):

		# if the current letter is the same as the parameter letter then set is_vowel to true
		if letter.upper() == vowels[current_letter] : is_vowel = current_letter

	return is_vowel

def letter_is_consonant (letter):
	is_consonant = -1
	# begin a loop through the consonant array
	for current_letter in range(len(consonants)):

		# if the current letter is the same as the parameter letter then set is_consonant to true
		if letter.upper() == consonants[current_letter] : is_consonant = current_letter

	return is_consonant

def new_consonant (_str, i) : 
    if i < len(consonants) - 1 :
        new_str = _str + consonants[i+1]
    else :
        new_str = _str + consonants[0]
    return new_str

def new_vowel (_str, i) : 
    if i < len(vowels) - 1 :
        new_str = _str + vowels[i+1]
    else :
        new_str = _str + vowels[0]
        
    return new_str

def add_ay (word) : return word + "AY"

def encrypt_one_word (word) :
    enc_str = ""
    while word != "":
	    # begin encryption
        for i in range(len(word)):
            # if i is a space, move to next index
            if word[i] != " " :
                # get the indicies of the letter in both lists. if a letter is not in a list
                # the function will return -1
                c_index = letter_is_consonant(word[i])
                v_index = letter_is_vowel(word[i])

                # if the index is not -1 use that index
                if c_index != -1 : enc_str = new_consonant(enc_str, c_index)
                elif v_index != -1 : enc_str = new_vowel(enc_str, v_index)
            
                # is this the last letter in the string? if it is a consonant add '-ay'
                if word[i] == word[len(word)-1] :
                    if letter_is_consonant(word[i]) != -1 :
                        enc_str = add_ay(enc_str)
                    word = ""
    pass
    return enc_str

def Main () :
    again = "y"

    while again != "n" :
        if again != "y" :
            str = again
        else :
            str = input("Enter a word to encrypt: ")

        enc_str = ""

        words = str.split(" ")
        if len(words) == 0 : words = [str]

        while str != "":
	        # begin encryption
            for i in range(len(words)):
                enc_str += encrypt_one_word(words[i])

                if i == (len(words) - 1) : str = ""
                else :
                    enc_str += " "
        pass

        print("The new string is: ", enc_str)
        again = input("Again? [y/n]: ")
    pass
    print ("Goodbye")
    return 0
    
Main()


