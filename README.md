# hCaptcha "fingerprint_blob" Encryption

This content is provided for educational purposes only. I am not responsible for any misuse or consequences resulting from the application of the information shared here.

If you want to study hCaptcha, join us: https://t.me/hcaptchastudy
And if you want to contact me, here is my Telegram: https://t.me/azulax1

## Usage

Local:
```python
from json import dumps

key = [8, 222, 242, 86, 199, 243, 49, 222, 144, 30, 250, 234, 173, 117, 227, 53] # hsw version : cc9cbcc44893d9601186ed793b76ac72a56a3e176be51252819b38f7d2f1f97c

blob = BlobEncryption(key)

data = dumps([
        [100, "test"],
        [200, "test"]
], separators=(",", ":"))
    
fingerprint_blob = blob.encrypt(data)

decrypted_fingerprint_blob = blob.decrypt(data)
```
 
# Credits

* **[DEXV](https://dexv.lol)**
* **[Emrovsky](https://github.com/emrovsky)** 
* **[Switch](https://github.com/Switch3301)** 
