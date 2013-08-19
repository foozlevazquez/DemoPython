#! /usr/bin/python

class MyProgram:
    message = "Foo You"
    def __init__ (self):
        self.message = "Hello World"

    def print_message (self):
        print( self.message)
        print(MyProgram.message)

            
        
if __name__ == "__main__":
    program = MyProgram()
    program.print_message()
