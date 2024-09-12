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

    shier = ""
    for let in plaintext:
        if let.isupper():
            new_let = chr(((ord(let) - 65 + shift) % 26) + 65)
            shier += new_let
        elif let.islower():
            new_let = chr(((ord(let) - 97 + shift) % 26) + 97)
            shier += new_let
        else:
            shier += let

    return shier


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
    shier = ""
    for let in ciphertext:
        if let.isupper():
            new_let = chr(((ord(let) - 65 - shift) % 26) + 65)
            shier += new_let
        elif let.islower():
            new_let = chr(((ord(let) - 97 - shift) % 26) + 97)
            shier += new_let
        else:
            shier += let

    return shier
