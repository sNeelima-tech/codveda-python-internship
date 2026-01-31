# Word Counter Program

try:
    filename = input("Enter file name: ")

    file = open(filename, "r")
    content = file.read()
    file.close()

    words = content.split()
    print("Total number of words:", len(words))

except FileNotFoundError:
    print("File not found. Please check the file name.")
