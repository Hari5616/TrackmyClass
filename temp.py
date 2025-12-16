import hashlib

hasher = hashlib.sha256()

hasher.update(b'pass')

hex_digest = hasher.hexdigest()
print("SHA-256 Hash:",hex_digest)