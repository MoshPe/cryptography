
# The decryptor - Alice:
class decryptor:
    # pre preparations: Alice choose p, g, d and calculate e and sent to the encryptor p,g,e
    elgamal = ElGamal.generate(144, urandom)
    elgamal_key = elgamal.publickey
    # prime number p:
    p = elgamal_key.__self__.p

    # g when gcd(g,p)=1
    g = elgamal_key.__self__.g

    # generate random integer d between 2 to p-1
    __d = random.randint(2, p - 1)

    # calculate e = g^d mod p
    e = pow(g, __d, p)

    print("El gamal variables:")
    print("p =",p ,"\n g =",g,"\n d =",__d, "\n e =",e,"\n")
