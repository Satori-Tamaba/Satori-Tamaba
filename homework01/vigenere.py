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
    shifr = ''
    for i, j in enumerate(plaintext):
        if (keyword[i] == 'a' or keyword[i] == 'A'):
            shifr += j
        else:
            pochti_bukva = (ord(j) + ord(keyword[i]))
            shifr += chr(pochti_bukva % 26 + 65)
    return shifr


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
    shif = ''
    for i, j in enumerate(ciphertext):
        if (keyword[i] == 'a' or keyword[i] =='A'):
            shif += j
        else:
            pochti_bukva = (ord(j) - ord(keyword[i]))
            shif += chr(pochti_bukva % 26 + 65)
    return shif
