"""code for encoding and decoding using caesar cipher technique.
The code works for the alphabets."""
choice=input("enter your choice:encrypt=0 or decrypt=1\n")
if choice=="0":
    text=input("enter the text\n")
    text=text.lower()
    key=int(input("enter the key between 1-26\n"))
    if key > 26 or key < 1:
        print("invalid key")
    for i in text:
        i=ord(i)
        if i+key not in range(97,122):
            i=((i+key)-122)+96
        else:
            i=(i+key)
        i=chr(i)
        print(i,end="")
elif choice=="1":
    text=input("enter the text\n")
    text=text.lower()
    key=int(input("enter the key between 1-26\n"))
    if key > 26 or key < 1:
        print("invalid key")
    for i in text:
        i=ord(i)
        if i-key not in range(97,122):
            i=(i-key)+26
        else:
            i=(i-key)
        i=chr(i)
        print(i,end="")
else:
    print("not a valid choice")
