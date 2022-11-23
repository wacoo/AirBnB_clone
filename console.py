#!/usr/bin/python3
#Todo
import cmd, sys
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    intro = ''
    prompt = '(hbnb)'

    #Support commands
    def help_EOF(self):
        print("EOF command to exit the program")
    def help_quit(self):
        print("Quit command to exit the program")
    def do_EOF(self, line):
        return True
    def do_quit(self, line):
        return True
    #Functional commands
    def do_create(self, line):
        try:
            if line == None or line == "":
                print("** class name missing **")
            else:
                if line == "BaseModel":
                    new_obj = BaseModel()
                    storage.save()
                print(new_obj.id)
        except UnboundLocalError:
            print("** class doesn't exist **")



if __name__ == '__main__':
    HBNBCommand().cmdloop()
