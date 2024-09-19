from string import ascii_letters 

correspondency = {} 
for letter, i in zip(ascii_letters, range(len(ascii_letters))): 
	correspondency[letter] = i 
	#print(f"{letter} - {i}") 


correspondency[" "] = len(ascii_letters) 

#print(correspondency) 


def to_cypher(x, a, n): 
	return ((x + a) % n) 


def to_text(c, a, n): 
	return ((c - a) % n) 



def encrypt(msg: str, a: int, chartype ): 
	cypher_arr = [] 
	cyphertext = [] 
	for i in msg: 
		#print(chartype[i]) 
		cypher_letter = to_cypher(chartype[i], a, len(chartype)) 
		cypher_arr.append(cypher_letter) 
		#print("----") 
		cyphertext.append(list(chartype.keys())[list(chartype.values()).index(cypher_letter)]) 


	return "".join(cyphertext) 


def decrypt(cypher, a, chartype ): 
	char_arr = [] 
	text = [] 
	for i in cypher: 
		char = to_text(chartype[i], a, len(chartype)) 
		char_arr.append(char) 
		text.append(list(chartype.keys())[list(chartype.values()).index(char)]) 

	#print(text) 
	return "".join(text) 



teste = encrypt("hoje", a = 4, chartype = correspondency) 
#print(teste) 

correspondency = {} 
for letter, i in zip(ascii_letters, range(len(ascii_letters))): 
	correspondency[letter] = i 
	#print(f"{letter} - {i}") 


correspondency[" "] = len(ascii_letters) 

#print(correspondency) 


def to_cypher(x, a, n): 
	return ((x + a) % n) 


def to_text(c, a, n): 
	return ((c - a) % n) 



def encrypt(msg: str, a: int, chartype ): 
	cypher_arr = [] 
	cyphertext = [] 
	for i in msg: 
		#print(chartype[i]) 
		cypher_letter = to_cypher(chartype[i], a, len(chartype)) 
		cypher_arr.append(cypher_letter) 
		#print("----") 
		cyphertext.append(list(chartype.keys())[list(chartype.values()).index(cypher_letter)]) 


	return "".join(cyphertext) 


def decrypt(cypher, a, chartype ): 
	char_arr = [] 
	text = [] 
	for i in cypher: 
		char = to_text(chartype[i], a, len(chartype)) 
		char_arr.append(char) 
		text.append(list(chartype.keys())[list(chartype.values()).index(char)]) 

	#print(text) 
	return "".join(text) 


rounds = 6

for i in range(rounds):
    my_str = "LIPPS SVPH"
    if len(my_str) < 50:
        res = decrypt(my_str, 4, correspondency)
        print(res)
