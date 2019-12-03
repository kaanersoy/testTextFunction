def dosyaYazi(text):
    file = open("testFile.txt", "a", encoding="utf-8")
    file.write(str(text))
    file.write("\n")
    file.close()
    print("'{}' text was added on your file.".format(str(text)))
    return text