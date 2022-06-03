# this is our Servser!!! not main

from encryptor_bob import encryptor
from decryptor_alice import decryptor
from colorama import Fore, Style

print(Fore.LIGHTBLUE_EX + "Hello, Welcome to our email security service:" + Style.RESET_ALL)
print("\nLet's say that Bob want to sent an email to Alice;")

print("First, Bob request from Alice the Elgamal public variables")
p, g, e = decryptor.elgamal_publicVriables(decryptor)
print(Fore.LIGHTBLUE_EX +"  Public elgamal variables that Alice send to bob are: \n   - p =", p ,"\n   - g =", g, "\n   - e =", e,"" + Style.RESET_ALL)

nonce = 0xccc6f855277127780000000000000000
ciphertext, len_plaintext = encryptor.encryptor_salsa20(encryptor, "Email_message.txt", nonce)
print("=> The ciphertext is:")
print(ciphertext)

y1, y2 = encryptor.encrypt_secret_key_Salsa20(encryptor, e, g, p)
print(Fore.LIGHTBLUE_EX +"=> The Elgamal public variabels are: \n - y1 =",y1, "\n - y2 =",y2, "" + Style.RESET_ALL)

DS = encryptor.RSA_sign_request(encryptor)
print("=> The RSA digital signature are: ", DS)

print(Fore.MAGENTA + "\n\nSending messege...\n\n" + Style.RESET_ALL)

print("Alice received the encrypted message, now she checks the message with RSA signature public variables (e, n), and decodes it with the key she received from elgmal(Y1, Y2).")

RSA_public_e, RSA_modulus_n = encryptor.RSA_publicVriables(encryptor)

decryptedMsg = decryptor.decrypt_salsa20(decryptor, ciphertext, y1, y2, DS, RSA_public_e, RSA_modulus_n, len_plaintext)
print()
print(Fore.LIGHTWHITE_EX + "=> The decrypted message is:")
print(decryptedMsg, "" + Style.RESET_ALL)
