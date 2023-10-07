import hashlib


# print(hashlib.algorithms_available)
def hash(p):
    # Teacher way
    m = p.encode()
    h = hashlib.sha256(m).hexdigest()
    return h


def hashSha3_256(p):
    # Teacher way
    m = p.encode()  # Converts text to byte code
    h = hashlib.sha3_256(m).hexdigest()
    return h


def hashShake(p):
    # Teacher way
    m = p.encode()  # Converts text to byte code
    h = hashlib.shake_256(m).hexdigest(32)
    return h


def main():
    w = 'helloworld'
    print(w)
    print(f"SHA-256: {hash(w)}")
    print(f"SHA3-256: {hashSha3_256(w)}")
    print(f"SHake: {hashShake(w)}")


main()

