from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from base64 import b64decode, b64encode
from Crypto.Cipher import AES

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