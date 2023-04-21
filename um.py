import re
def count(s):
    # You’re welcome, but not required, to use re and/or sys.

    words = s.lower().split(" ")
    words = [word.strip("!@#$%^&*()<>,.?") for word in words]

    return words.count("um")
    
def main():
    print(count(input("Text: ")))

if __name__ == "__main__":
    main()