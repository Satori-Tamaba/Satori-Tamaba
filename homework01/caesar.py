import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    # PUT YOUR CODE HERE
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
     shifr = ''
    cifr = '1234567890 .,/;[]!"№;%:?*()_+'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    leter_index_big = dict(zip(alphabet_big, range(len(alphabet_big))))
    index_leter_big = dict(zip(range(len(alphabet_big)), alphabet_big))
    leter_index = dict(zip(alphabet, range(len(alphabet))))
    index_leter = dict(zip(range(len(alphabet)), alphabet))
    for leter in plaintext:
        if (leter.isalpha()):
            if (leter.isupper()):
                index_big = (leter_index_big[leter] + shift) % 26
                shifered_leter_big = index_leter_big[index_big]
                shifr += shifered_leter_big
            else:
                index = (leter_index[leter] + shift) % 26
                shifered_leter = index_leter[index]
                shifr += shifered_leter
        else:
            if (leter in cifr):
                shifr += leter

    return shifr
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
     shifr = ''
    cifr = '1234567890 .,/;[]!"№;%:?*()_+'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    leter_index_big = dict(zip(alphabet_big, range(len(alphabet_big))))
    index_leter_big = dict(zip(range(len(alphabet_big)), alphabet_big))
    leter_index = dict(zip(alphabet, range(len(alphabet))))
    index_leter = dict(zip(range(len(alphabet)), alphabet))
    for leter in ciphertext:
        if (leter.isalpha()):
            if (leter.isupper()):
                index_big = (leter_index_big[leter] - shift) % 26
                shifered_leter_big = index_leter_big[index_big]
                shifr += shifered_leter_big
            else:
                index = (leter_index[leter] - shift) % 26
                shifered_leter = index_leter[index]
                shifr += shifered_leter
        else:
            if (leter in cifr):
                shifr += leter

    return shifr
    return best_shift
