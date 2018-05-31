import hashlib

def kgrams(text, k=5):
    text = list(text)
    n = len(text)
    if n < k:
        yield text
    else:
        for i in range(n - k + 1):
            yield text[i:i+k]


def winnowing_hash(kgram):
    kgram = zip(*kgram)
    kgram = list(kgram)
    text = ''.join(kgram[1]) if len(kgram) > 1 else ''
    hs = hashing(text)
    return (kgram[0][0] if len(kgram) > 1 else -1, hs)


def hashing(text):
    hs = hashlib.sha1(text.encode('utf-8'))
    hs = hs.hexdigest()[-4:]
    hs = int(hs, 16)
    return hs


def select_min(window):
    return min(window, key = lambda x: x[1])


def winnow(text, k=5):
    n = len(list(text))
    text = zip(range(n), text)
    hashes = map(lambda x: winnowing_hash(x), kgrams(text, k))
    windows = kgrams(hashes, 4)
    return set(map(select_min, windows))