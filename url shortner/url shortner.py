import pyshorteners

link = input("Enter link: ")

shortener = pyshorteners.Shortener()

x = shortener.tinyurl.short(link)

print("Short link:",x)