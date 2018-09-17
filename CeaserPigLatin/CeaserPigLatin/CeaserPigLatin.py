# Python CeaserPigLatin Encryption
# Trey Hall
# 9/17/18

consonants = [ 'B', 'C', 'D',  'F', 'G', 'H',  'J', 'K', 'L', 'M', 'N',  'P', 'Q', 'R', 'S', 'T',  'V', 'W', 'X', 'Y', 'Z']
vowels = ['A','E','I','O','U',]

def main ():
	str = input("Enter a word to encrypt")
	enc_str = ""

	if str != "":
		# begin encryption
		for letter in range(len(str)):
			if letterletter_is_consonant(letter) : 
				# do consonant things
			elif letter_is_vowel(letter) :
				# do vowel things
			else :
				# is this the last letter in the string?
				# if it is a consonant add '-ay'

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


