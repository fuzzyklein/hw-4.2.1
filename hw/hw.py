from program import Program

class HelloWorld(Program):
    def process_file(self, p):
        super().process_file(p)

    def run(self):
        print('Hello world')
