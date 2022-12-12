from base64 import decode
import hashlib

string = input("Enter word/s to hash: ")
encode = string.encode()
result = hashlib.md5(encode)
print("String : ", end="")
print(string)
print("Hash value : ", end="")
print(result)
print("Hexadecimal equivalent: ", result.hexdigest())
