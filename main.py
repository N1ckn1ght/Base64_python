import base64

print("Enter string to encode to Base64 format:")
s = input()
bs = base64.b64encode(s.encode("UTF-8")).decode("UTF-8")
print(bs, "\n")

print("Enter string to decode from Base64 format:")
bs = input()
s = base64.b64decode(bs.encode("UTF-8")).decode("UTF-8")
print(s)
