import base64

# Example message (like email data or API request)
message = "User login: bablu@example.com"

# Encode using Base64
encoded = base64.b64encode(message.encode())

print("Original Message:")
print(message)

print("\nBase64 Encoded:")
print(encoded.decode())

# Decode again
decoded = base64.b64decode(encoded)

print("\nDecoded Message:")
print(decoded.decode())
