class FileReader:
    #method 1
    def readFile(self):
        f=None
        try:
            f = open("C:\PycharmProjects\pythonProject\MyFile","r")
            print(f.read())
        except FileNotFoundError as e:
            print("file not found lala ",e)
        finally:
            pass
     #method read using for loop
    def readLine(self):
        f=None
        try:
            f = open("C:\PycharmProjects\pythonProject\MyFile","r")
            for data in f:
                print(data)
        except FileNotFoundError as e:
            print("file not found lala ",e)
        finally:
            pass
    #method 2
    #to append something use "a" instead "w"
    def writeFile(self):
        f=None
        try:
            f=open("\PycharmProjects\pythonProject\MyData","w")
            f.write("hey there!")
        except Exception as e:
            print("exception during write ",e)
        finally:
            pass

obj = FileReader()
# obj.readFile()
# obj.writeFile()
obj.readLine()