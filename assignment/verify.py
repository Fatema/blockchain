import ecdsa

# put the hex of your public key in the line below
vk_string="b6d85a234b19327fa7b70079cb5a1b0fb8e9ae81aa32bea5a768ea6c07bef4fbfd92a995fee5dc0db12af14fcf481d09df69e20e53e0517ed08e7cbb8715fe14"
vk = ecdsa.VerifyingKey.from_string(bytes.fromhex(vk_string),ecdsa.SECP256k1)

message = b'Hello World'

# put your signature for Hello World in the line below
sig_hex = "15c2a97b6a485ab54c931c246e7702fbf0e64afdc916e1d5461a872809666559296773397245421e335bbd3dd94e8d4f5c589d584f27ab4e41fb02856117ce57"
sig = bytes.fromhex(sig_hex)

print("Checking signature")
print("Message: "+str(message))

print("Signature: "+sig_hex)
print("Public key: "+vk_string)
try:
    vk.verify(sig, message)# True
    print('Verification passed')
except ecdsa.keys.BadSignatureError:
    print('Verification failed')