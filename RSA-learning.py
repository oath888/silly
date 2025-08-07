from cryptography.hazmat.primitives import serialization

path = "misc\id_rsa"
password = None
try:
    with open(path,"rb") as f:
        private_key = serialization.load_pem_private_key(f.read(),password,)
    numbers = private_key.private_numbers()
    print(numbers.p, numbers.q, numbers.d, numbers.dmp1, numbers.dmq1, numbers.iqmp)
except:
    with open(path,"rb") as f:
        private_key = serialization.load_ssh_private_key(f.read(),password)
    numbers = private_key.private_numbers()
    print(numbers.p, numbers.q, numbers.d, numbers.dmp1, numbers.dmq1, numbers.iqmp)
    print("This is an SSH key, not a PEM key.")
else:
    print("This is a PEM key, not an SSH key.")
