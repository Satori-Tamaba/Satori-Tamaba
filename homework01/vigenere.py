def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    keyword *= len(plaintext) // len(keyword) + 1
    shier = ""
    for i, j in enumerate(plaintext):
        if keyword[i] == "a" or keyword[i] == "A":
            shier += j
        else:
            pooch_bukakke = ord(j) + ord(keyword[i])
            shier += chr(pooch_bukakke % 26 + 65)

    return shier


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    keyword *= len(ciphertext) // len(keyword) + 1
    shift = ""
    for i, j in enumerate(ciphertext):
        if keyword[i] == "a" or keyword[i] == "A":
            shift += j
        else:
            pooch_bukakke = ord(j) - ord(keyword[i])
            shift += chr(pooch_bukakke % 26 + 65)
    return shift
