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
    shifr = ''
    for let in plaintext:
        if (let.isupper()):
            new_let = chr(((ord(let) - 65 + shift) % 26) + 65)
            shifr += new_let
        elif (let.islower()):
            new_let = chr(((ord(let) - 97 + shift) % 26) + 97)
            shifr += new_let
        else:
            shifr += let
    return shifr


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
  shifr = ''
    for let in ciphertext:
        if (let.isupper()):
            new_let = chr(((ord(let) - 65 - shift) % 26) + 65)
            shifr += new_let
        elif (let.islower()):
            new_let = chr(((ord(let) - 97 - shift) % 26) + 97)
            shifr += new_let
        else:
            shifr += let
    return shifr

def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
    
