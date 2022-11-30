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
    shier = ""
    for i in range(len(plaintext)):
        if plaintext[i].isupper():
            shier += chr((ord(plaintext[i]) - 2 * 65 + ord(keyword[i % len(keyword)])) % 26 + 65)
        elif plaintext[i].islower():
            shier += chr((ord(plaintext[i]) - 2 * 97 + ord(keyword[i % len(keyword)])) % 26 + 97)
        else:
            shier += plaintext[i]
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
    shier = ""
    for i in range(len(ciphertext)):
        if ciphertext[i].isupper():
            shier += chr((ord(ciphertext[i]) - ord(keyword[i % len(keyword)])) % 26 + 65)
        elif ciphertext[i].islower():
            shier += chr((ord(ciphertext[i]) - ord(keyword[i % len(keyword)])) % 26 + 97)
        else:
            shier += ciphertext[i]
    return shier
