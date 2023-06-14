"""
Exercícios de list comprehension do site
https://bbookman.github.io/Python-list-comprehension1/
"""

# ex1: find all the numbers from 1-1000 that are divisible by 7
lista = [n for n in range(1, 1001) if n % 7 == 0]
print('=' * 25, '\n', lista)

# ex2: find all the numbers from 1-1000 that have a 3 in them
lista = [n for n in range(1, 1001) if "3" in str(n)]
print('=' * 25, '\n', lista)


# ex3: create a list of all the consonantes in the string "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"

def is_consonant(word):
	if "a" in word or "e" in word or "i" in word or "o" in word or "u" in word:
		return False
	return True


string = "yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
lista = [letra for letra in string if is_consonant(letra) if letra.strip() != '']
print('=' * 25, '\n', lista)
