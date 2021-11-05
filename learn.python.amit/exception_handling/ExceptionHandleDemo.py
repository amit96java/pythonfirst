class Demo:
    def div(self):
        try:
            a=5
            b=2
            print(a/b)
        except ZeroDivisionError as e:
            print("hey ! you can not divide a number by zero ",e)
        except ValueError as e:
            print("invalid input")
        except Exception as e:
            print("something went wrong || ",e)
        finally:
            print("resource closed")

obj=Demo()
obj.div()
print("bye")

