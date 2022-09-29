# ask what text needs to be incrypted

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']

cript = ['@', '#', '$', '%', '&', '*', '>', '<', '}', '{', 'Δ', '∧', '|', ';', 'Ω', '∴', '¥', '⋈', '£', '=', '+', 'æ',
         '∑', '∃', '∈', '∋']


def encrypt(text: str):
    encrypted_text = text.lower()

    for word in alpha:
        encrypted_text = encrypted_text.replace(word, cript[alpha.index(word)])
    print(encrypted_text)
    return encrypted_text


def decrypt(text: str):
    normal_text = text.lower()

    for signal in cript:
        normal_text = normal_text.replace(signal, alpha[cript.index(signal)])

    print(normal_text)
    return normal_text

while True:
    choice = input("1 para encriptar, 2 para desincriptar: ").strip()

    if choice == '1':
        text = input("Texto para encriptar: ").strip()
        encrypt(text)
    elif choice == '2':
        text = input("Texto para desincriptar: ").strip()
        decrypt(text)
    else:
        break