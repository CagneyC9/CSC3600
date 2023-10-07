import hashlib


def hash(p):
    # Teacher way
    m = p.encode()
    h = hashlib.sha256(m).hexdigest()
    # Hashes the parameter (Hello World)
    # My way, just return myHash
    myHash = hashlib.sha256(p.encode('utf-8')).hexdigest()
    return h
def main():
    w = 'helloworld'
    print(w)
    print(hash(w))
    # x = hash(w)
    # print(x)


main()
