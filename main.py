upper = ""
while upper.lower() != "true" and upper.lower() != "false":
	upper = input("Upper case != lower case? (True or False): ")
while True:
	alphabet = input("Alphabet: ")
	if upper == "false":
		alphabet = alphabet.lower()
	valid = True
	for letter in alphabet:
		if alphabet.count(letter) > 1:
			valid = False
	if valid:
		break
	else:
		print("The alphabet must not contain duplicate characters.")

text = input("Text: ")
if upper == "false":
	text = text.lower()
key = input("Key: ")
table = {}

new_key = ""
for letter_number in range(len(text)):
	if text[letter_number] == " ":
		new_key += " "
	else:
		while letter_number >= len(key):
			letter_number -= len(key)
		new_key += key[letter_number]

print("="*30)
print("KEY     :",new_key)
print("TEXT    :",text)
print("ALPHABET:",alphabet)

for row in alphabet:
	table[row] = alphabet
	last_letter = alphabet[0]
	alphabet = alphabet[1:len(alphabet)]
	alphabet += last_letter

decoded = ""
for letter in text:
	if not letter == " ":
		if letter in alphabet:
			decoded += table[letter][alphabet.index(new_key[text.index(letter)])]
		else:
			print("Invalid text for the alphabet.")	
			quit()

print("="*30)
print("DECODED :",decoded)
print("="*30)