def TEXT2ASCII():
    text = input("Enter Text To Convert into ASCII Code: ")
    textlen = len(text)
    print("Charecter", "\t", "ASCII")
    for i in text:
        value = ord(i)
        print(i, "           \t", value)


TEXT2ASCII()
