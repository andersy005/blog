---
date: 2021-02-21
category: todayilearned, cryptography
---

# Freedom of Cryptography

Today I learned that if you could travel back to the early 1990s with the contents of this [git repository](https://github.com/pyca/cryptography), you would have had to become a licensed arms dealer 😮 —the govt certainly would have denied you an export license— before you could post the source code (or any work that featured the source code) on the internet.

Publicly sharing the following code snippet would have landed you in prison for arms trafficking because export of cryptography from the United States was regulated at the same level as missiles, tanks, etc...😮.

```python
In [1]: from cryptography.fernet import Fernet

In [2]: key = Fernet.generate_key()

In [3]: f = Fernet(key)

In [4]: plain_text = b'Hello Alice'

In [5]: cipher_text = f.encrypt(plain_text)

In [6]: cipher_text
Out[6]: b'gAAAAABgMjSru96WoOLHq3ygBw93ZICzyu5aKjYQqw0MQ7G44Ch77-xqCVNmYSbB4j6Kz_Ipol3hyPWx5Ti5rui1SdRc_D7LfA=='

In [7]: f.decrypt(cipher_text)
Out[7]: b'Hello Alice'
```

**Resources with more deailed history of the legal battles for freedom of cryptography**:

- [Bernstein v. United States](https://en.wikipedia.org/wiki/Bernstein_v._United_States)
- [Crypto: How the Code Rebels Beat the Government Saving Privacy in the Digital Age](https://www.amazon.com/Crypto-Rebels-Government-Privacy-Digital/dp/0140244328)
- [The Case against Regulating
  Encryption Technology](https://people.csail.mit.edu/rivest/pubs/Riv98e.pdf)
