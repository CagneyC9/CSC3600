import hashlib
import hmac

def main():
    w = "helloworld"
    w2 = w.encode()
    w3 = w2 + b'apple'
    # print (hashlib.sha256("Hello").hexdigest())
    print(f"SHA-256: {hashlib.sha256(w2).hexdigest()}")
    print(f"SHA3-256: {hashlib.sha3_256(w2).hexdigest()}")
    print(f"SHAKE-256: {hashlib.shake_256(w2).hexdigest(64)}")
    # print(hashlib.algorithms_available)
    print(f"cShakeLike: {hashlib.shake_256(w3).hexdigest(64)}")
    print(f"MycShakeLike: {hashlib.shake_256(w2 + 'Hello'.encode()).hexdigest(64)}")
    cstr = 'apple'
    # Problem with this cstr
    # Should be a random string not hard coded
    # print(f"SHAKE-256: {hashlib.shake_256(w2).hexdigest(32)}")

    print(f"Tuple yay")
    acct = '500'
    amt = '150'
    inputstring = str(len(acct)) + acct + str(len(amt)) + amt
    print(f"Tuple Hash: {hashlib.shake_256(inputstring.encode()).hexdigest(32)}")

    print(inputstring)

    acct2 = len(acct)
    amt2 = len(amt)
    print("-----------")
    print("HMAC")
    secret = b'secret'
    print(f"HMAC authN tag: {hmac.new(secret, w2, hashlib.sha256).hexdigest()}")
    print(f"No HMAC: {hashlib.sha256(w2).hexdigest()}")

    x1 = "Hello world"
    x2 = "Salt"
    x3 = x1 + x2
    kmac = hmac.new(secret, x3.encode(), hashlib.sha256).hexdigest()
    print(kmac)

#     w3 had a customization string added
    kmac = hmac.new(secret, w3, hashlib.Cshake).hexdigest(16)
    print(f"KMAC: {kmac}")


main()
