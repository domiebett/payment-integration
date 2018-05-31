from M2Crypto import RSA, X509
from base64 import b64encode
import os


INITIATOR_PASS = b"LongPassword"
CERTIFICATE_FILE = os.path.abspath("./files/cert.cer")

def encryptInitiatorPassword():
    cert_file = open(CERTIFICATE_FILE, 'r')
    cert_data = cert_file.read()  # read certificate file
    cert_file.close()

    cert = X509.load_cert_string(cert_data)
    # pub_key = X509.load_cert_string(cert_data)
    pub_key = cert.get_pubkey()
    rsa_key = pub_key.get_rsa()
    cipher = rsa_key.public_encrypt(INITIATOR_PASS, RSA.pkcs1_padding)
    return b64encode(cipher)

print(encryptInitiatorPassword())
