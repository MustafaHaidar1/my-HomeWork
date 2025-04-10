def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


if __name__ == "__main__":
    message = input("أدخل النص: ")
    shift = int(input("أدخل مفتاح التشفير (عدد الحروف): "))

    encrypted = caesar_encrypt(message, shift)
    print("النص المشفر:", encrypted)

    decrypted = caesar_decrypt(encrypted, shift)
    print("النص بعد فك التشفير:", decrypted)
