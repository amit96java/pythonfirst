#duck typing means it should walk like duck , talk like duck , behave like duck
#so here in this class execute method is duck behaviour

class PyCharm:
    def execute(self):
        print("compiling")
        print("running")

class MyEditor:
    def execute(self):
        print("spell checking")
        print("convention checking")
        print("compiling")
        print("running")

class Laptop:
    def code(self,ide):
        ide.execute()

ide = MyEditor()

lap1 = Laptop()

lap1.code(ide)