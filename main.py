# this is our Servser!!! not main


# import RSA_signiture
# import math
# import sympy
# import random
# from Crypto.PublicKey import ElGamal
# from os import urandom


from encryptor_bob import encryptor
from decryptor_alice import decryptor

print("Hello welcame our email:")

print("Bob want to sent the masseg to Alice")

print("Bob ask from Alice the Elgamal public variables")
p, g, e = decryptor.elgamal_publicVriables(decryptor)
print("Public variables that Alice send to bob are: \n - p =",p ,"\n - g =",g, "\n - e =",e)

nonce = 0xccc6f855277127780000000000000000
ciphertext = encryptor.encryptor_salsa20(encryptor, "Email_message.txt", nonce)
print("the ciphertext is:")
print(ciphertext)

y1, y2 = encryptor.encrypt_secret_key_Salsa20(encryptor, e, g, p)
print("The Elgamal public variabels are: \n - y1 =",y1, "\n - y2 =",y2 )

print("\n Sent to Alice the ciphrtext, nonce, Y1, Y2, ***DS***:")
decryptedMsg = decryptor.decrypt_salsa20(decryptor, ciphertext, y1, y2, 'DS')
print("the decrypted message is:")
print(decryptedMsg)













# #
# elgamal = ElGamal.generate(144, urandom)
# elgamal_key = elgamal.publickey
# # prime number p:
# p = elgamal_key.__self__.p

# # g when gcd(g,p)=1
# g = elgamal_key.__self__.g

# # generate random integer d between 2 to p-1
# __d = random.randint(2, p - 1)

# # calculate e = g^d mod p
# e = pow(g, __d, p)

# print("El gamal variables:")
# print("p =", p, "\n g =", g, "\n d =", __d, "\n e =", e, "\n")

# def primitiveRoot(p_val: int) -> int:
#     print("Generating primitive root of p")
#     while True:
#         g = random.randrange(3, p_val)
#         if pow(g, 2, p_val) == 1:
#             continue
#         if pow(g, p_val, p_val) == 1:
#             continue
#         return g
#

# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # private_key = 0x165ecc9b4689fc6ceb9c3658977686f8083fc2e5ed75644bb8540766a9a2884d1d82edac9bb5d312353e63e4ee68b913f264589f98833459a7a547e0b2900a33e71023c4dedb42875b2dfdf412881199a990dfb77c097ce71b9c8b8811480f1637b85900137231ab47a7e0cbecc0b011c2c341b6de2b2e9c24d455ccd1fc0c21
    # modulo_n = 0xf51518d30754430e4b89f828fd4f1a8e8f44dd10e0635c0e93b7c01802729a37e1dfc8848d7fbbdf2599830268d544c1ecab4f2b19b6164a4ac29c8b1a4ec6930047397d0bb93aa77ed0c2f5d5c90ff3d458755b2367b46cc5c0d83f8f8673ec85b0575b9d1cea2c35a0b881a6d007d95c1cc94892bec61c2e9ed1599c1e605f
    # public_key = 0x10001
    # sign = RSA_signiture.create_rsa_signature(b'testing', private_key, modulo_n)
    # print(RSA_signiture.verify_rsa_signature(sign, public_key, b'testing', modulo_n))

    # find the generator of p.
    # p = 20988936657440586486151264256610222593863921
    # print(primitiveRoot(p))
    # if primitiveRoot(p) < 20988936657440586486151264256610222593863921:




# Driver Code


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
