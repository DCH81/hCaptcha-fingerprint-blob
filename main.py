from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from base64 import b64decode, b64encode
from Crypto.Cipher import AES
from json import dumps

class BlobEncryption:
    def __init__(self, key: list) -> None:
        self.key = bytearray(key)

    def decrypt(self, data: str) -> str:
        iv, ciphertext = map(b64decode, data.split('.'))
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
        return decrypted.decode('utf-8')

    def encrypt(self, data: str) -> str:
        iv = get_random_bytes(16)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        encrypted = cipher.encrypt(pad(data.encode(), AES.block_size))
        return b64encode(iv).decode() + '.' + b64encode(encrypted).decode()
    
if __name__ == "__main__":
    key = [8, 222, 242, 86, 199, 243, 49, 222, 144, 30, 250, 234, 173, 117, 227, 53] # hsw version : cc9cbcc44893d9601186ed793b76ac72a56a3e176be51252819b38f7d2f1f97c
    
    
    blob = BlobEncryption(key)
    
    data = dumps([
        [100, "test"],
        [200, "test"]
    ], separators=(",", ":"))
    
    fingerprint_blob = blob.encrypt(data)
    
    print(fingerprint_blob)