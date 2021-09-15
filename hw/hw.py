from program import Program

class HelloWorld(Program):
    def process_file(self, p):
        super().process_file(p)
        print()
        print("******* HELLO WORLD!!!!! ********")
        print()
