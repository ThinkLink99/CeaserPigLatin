# Python CeaserPigLatin Encryption
# Trey Hall
# 9/17/18

consonants = [ 'B', 'C', 'D', 'F', 'G', 'H',  'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
vowels = ['A','E','I','O','U',]

ret = main()

def main ():
    str = input("Enter a word to encrypt")
    enc_str = ""

    while str != "":
		# begin encryption
        for i in range(len(str)):
            if letter_is_consonant(str[i]) : enc_str = new_consonant(enc_str, i)
            elif letter_is_vowel(str[i]) : enc_str = new_vowel(enc_str, i)
            
            # is this the last letter in the string? if it is a consonant add '-ay'
            if letter == str[len(str)-1] :
                if letter_is_consonant(letter) :
                    enc_str = add_ay(enc_str + letter)
                    str = ""
    pass

    print("The new string is: ", enc_str)
    return 0
	
def letter_is_vowel (letter):
	is_vowel = false
	# begin a loop through the vowel array
	for current_letter in range(len(vowels)):

		# if the current letter is the same as the parameter letter then set is_vowel to true
		if letter == current_letter : is_vowel = true

	return is_vowel

def letter_is_consonant (letter):
	is_consonant = false
	# begin a loop through the consonant array
	for current_letter in range(len(consonants)):

		# if the current letter is the same as the parameter letter then set is_consonant to true
		if letter == current_letter : is_consonant = true

	return is_vowel

def new_consonant (_str, i) : 
    new_str = _str + consonants[i+1]
    return new_str

def new_vowel (_str, i) : 
    new_str = _str + vowels[i+1]
    return new_str

def add_ay (word) : return word + "ay"


