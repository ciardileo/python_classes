"""
chatbot baseado em GPT
"""

import openai 

# chave da api
key = "key"

# função de mandar texto
def prompt(text):

	client = openai.OpenAI(api_key=key)

	completion = client.chat.completions.create(
		model="gpt-3.5-turbo",
		messages=[
			{"role": "system", "content": "You are a helpful assistant."},
			{
				"role": "user",
				"content": text
			}
		]
	)

	print(completion.choices[0].message)
	
# menu
opc = 0
while opc != 2:
	opc = int(input("> "))
	
	match opc:
		case 1:
			texto = input("Input: ")
			prompt(texto)
			
		case 2:
			print("Saindo...")
