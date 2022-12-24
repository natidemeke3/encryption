from sympy import *
class Sub:
    def __init__(self,file):
        self.file = file
    def sub(self,old, new):
        if old in self.file:
            file = self.file.replace(old,new)
            self.file = file          
print("""                                                                    88                          
 ,adPPYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba, 8b       d8 8b,dPPYba, MM88MMM ,adPPYba, 8b,dPPYba,  
a8P_____88 88P'   `"8a a8"     "" 88P'   "Y8 `8b     d8' 88P'    "8a  88   a8P_____88 88P'   "Y8  
8PP""""""" 88       88 8b         88          `8b   d8'  88       d8  88   8PP""""""" 88          
"8b,   ,aa 88       88 "8a,   ,aa 88           `8b,d8'   88b,   ,a8"  88,  "8b,   ,aa 88          
 `"Ybbd8"' 88       88  `"Ybbd8"' 88             Y88'    88`YbbdP"'   "Y888 `"Ybbd8"' 88          
                                                 d8'     88                                       
                                                d8'      88                                       """)
print("""[1]Encrypt
[2]Decrypt""")
command = input("your option: ")
if command == '1':
 try:
  file_location = input("enter your file location: ")
  source = open(f"{file_location}", "r")
  files = Sub(source.read())
  files.sub("a", "67152")
  files.sub("b", "8917498")
  files.sub("c", "19847189")
  files.sub("d", "0871113")
  files.sub("e", "314523")
  files.sub("f", "654543")
  files.sub("g", "21141")
  files.sub("h", "97643")
  files.sub("i", "241515")
  files.sub("j", "63773")
  files.sub("k", "97891698")
  files.sub("l", "197419")
  files.sub("m", "1047195")
  files.sub("n", "10571")
  files.sub("o", "91081")
  files.sub("p", "0101001")
  files.sub("q", "5198751")
  files.sub("r", "9719715c")
  files.sub("s", "987151023")
  files.sub("t", "0175119")
  files.sub("u", "2019857")
  files.sub("v", "018j89")
  files.sub("w", "1999819")
  files.sub("x", "096611")
  files.sub("y", "09101")
  files.sub("z", "108104")
  edit_files = open(file_location, "w")
  edit_files.write(str(files.file))
 except FileNotFoundError:
    print("file not found")
elif command == '2':
  file_location = input("enter your file location: ")
  source = open(f"{file_location}", "r")
  files = Sub(source.read())
  files.sub("67152", "a")
  files.sub("8917498", "b")
  files.sub("19847189", "c")
  files.sub("0871113", "d")
  files.sub("314523", "e")
  files.sub("654543", "f")
  files.sub("21141", "g")
  files.sub("97643", "h")
  files.sub("241515", "i")
  files.sub("63773", "j")
  files.sub("97891698", "k")
  files.sub("197419", "l")
  files.sub("1047195", "m")
  files.sub("10571", "n")
  files.sub("91081", "o")
  files.sub("0101001", "p")
  files.sub("5198751", "q")
  files.sub("9719715c", "r")
  files.sub("987151023", "s")
  files.sub("0175119", "t")
  files.sub("2019857", "u")
  files.sub("018j89", "v")
  files.sub("1999819", "w")
  files.sub("096611", "x")
  files.sub("09101", "y")
  files.sub("108104", "z")
try:
 edit_files = open(file_location, "w")
 edit_files.write(str(files.file))
except TypeError:
    pass
except NameError:
    pass