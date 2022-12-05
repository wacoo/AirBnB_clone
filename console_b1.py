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
    def help_update(self):
        print('update <class name> <id> <attribute name> "<attribute value>"')
    def do_EOF(self, line):
        return True
    def do_quit(self, line):
        return True
    #Functional commands
    def do_create(self, line):
        if line == None or line == "":
            print("** class name missing **")
        else:
            if line == "BaseModel":
                new_obj = BaseModel()
                storage.save()
                print(new_obj.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, line):
        args = line.split()
        if len(args) == 0 or args == None:
            print("** class name missing **")
        elif len(args) < 2 and args[0] == "BaseModel":
            print ("** instance id missing **")
        else:
            if args[0] == "BaseModel":
                objs = storage.all()
                for k in objs.keys():
                    if k == args[0] +"."+ args[1]:
                        print(objs[k])
                        return
                print("** no instance found **")
            else:
                print("** class doesn't exist **")
    def do_destroy(self, line):
        args = line.split()
        if len(args) == 0 or args == None:
            print("** class name missing **")
        elif len(args) < 2 and args[0] == "BaseModel":
            print("** instance id missing **")
        else:
            if args[0] == "BaseModel":
                objs = storage.all()
                for k in objs.keys():
                    if k == args[0] + "." + args[1]:
                        objs.pop(k)
                        storage.save()
                        return

    def do_all(self, line):
        objs = storage.all()
        lst = []
        if line == "BaseModel":
            for k in objs.keys():
                lst.append(str(objs[k]))
            print(lst)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        args = line.split()
        objs = storage.all()
        if len(args) == 0 or args == None:
            print("** class name missing **")
        elif len(args) < 2 and args[0] == "BaseModel":
            print("** instance id missing **")
        elif len(args) == 2 and args[0] == "BaseModel":
            for k in objs.keys():
                if k == args[0] + "." + args[1]:
                    print("** attribute name missing **")
                    return
            print("** no instance found **")
        elif len(args) == 3 and args[0] == "BaseModel":
            print("** value missing **")
        else:
            if args[0] == "BaseModel":
                objs = storage.all()
                nonup = ["id", "created_at", "updated_at"]
                for k in objs.keys():
                    if k == args[0] + "." + args[1]:
                        if args[2] not in nonup:
                            #TODO strip problem fin the core problem and fix
                            setattr(objs[k], args[2].strip('\"').strip("\'"), args[3].strip('\"').strip("\'"))
                            storage.save()
                            return
                #print("** no instance found **")
            else:
                print("** class doesn't exist **")





if __name__ == '__main__':
    HBNBCommand().cmdloop()
