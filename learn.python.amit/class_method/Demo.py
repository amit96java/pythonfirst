class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("config is ", self.cpu, self.ram)


com1 = Computer("i5", 16)
com2 = Computer("ryzen3", 8)

# Computer.config(com1)
# Computer.config(com2)

com1.config()
com2.config()
