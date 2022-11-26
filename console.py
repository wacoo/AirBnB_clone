#!/usr/bin/python3
#Todo
import cmd, sys
from models.base_model import BaseModel
from models.user import User
from models.state import State 
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
import re

class HBNBCommand(cmd.Cmd):
    intro = ''
    prompt = '(hbnb)'
    #names of classes
    clses = ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]
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
    def emptyline(self):
        pass
    #Functional commands
    def default(self, line):
        cnt = 0
        #l1 = line
        #l2 = l1.strip('\"').strip("\'")
        #print("ST1:" + l2)
        s = line.split('.')
        t = s[1].split()
        if s[1] == "count" or s[1] == "count()":
            objs = storage.all()
            for i in range(len(HBNBCommand.clses)):
                if s[0] == HBNBCommand.clses[i]:
                    for k in objs.keys():
                        s = k.split('.')
                        if s[0] == HBNBCommand.clses[i]:
                            cnt += 1
                    print(cnt)
                    return
            print("** class doesn't exist **")
        else:
            for i in range(len(HBNBCommand.clses)):
                #show()
                pat_show = re.compile("show\(.+\)$")
                #destroy()
                pat_dest = re.compile("destroy\(.+\)$")
                if s[0] == HBNBCommand.clses[i] and t[0] == "all()":
                    self.do_all(HBNBCommand.clses[i])
                    break
                elif s[0] == HBNBCommand.clses[i] and pat_show.match(t[0]):
                    striped = t[0].strip('show(').strip(')')
                    self.do_show(s[0] + " " + striped.strip('\"').strip("\'"))
                    break
                elif s[0] == HBNBCommand.clses[i] and pat_dest.match(t[0]):
                    striped = t[0].strip('destroy(').strip(')')
                    self.do_destroy(s[0] + " " + striped.strip('\"').strip("\'"))
                    break

    def do_create(self, line):
        if line == None or line == "":
            print("** class name missing **")
        else:
            if line in HBNBCommand.clses:
                new_obj = None
                if line == "BaseModel":
                    new_obj = BaseModel()
                elif line == "User":
                    new_obj = User()
                elif line == "State":
                     new_obj = State()
                elif line == "City":
                    new_obj = City()
                elif line == "Amenity":
                    new_obj = Amenity()
                elif line == "Place":
                    new_obj = Place()
                elif line == "Review":
                    new_obj = Review()
                storage.save()
                print(new_obj.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, line):
        args = line.split()
        if len(args) == 0 or args == None:
            print("** class name missing **")
        elif len(args) < 2 and args[0] in HBNBCommand.clses:
            print ("** instance id missing **")
        else:
            if args[0] in HBNBCommand.clses:
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
        elif len(args) < 2 and args[0] in HBNBCommand.clses:
            print("** instance id missing **")
        else:
            if args[0] in HBNBCommand.clses:
                objs = storage.all()
                for k in objs.keys():
                    if k == args[0] + "." + args[1]:
                        objs.pop(k)
                        storage.save()
                        return
                print("** no instance found **")

    def do_all(self, line):
        objs = storage.all()
        lst = []
        for i in range(len(HBNBCommand.clses)):
            if line == HBNBCommand.clses[i]:
                for k in objs.keys():
                    s = k.split('.')
                    if s[0] == HBNBCommand.clses[i]:
                        lst.append(str(objs[k]))
                print(lst)
                return
        print("** class doesn't exist **")

    def do_update(self, line):
        args = line.split()
        objs = storage.all()
        if len(args) == 0 or args == None:
            print("** class name missing **")
        elif len(args) < 2 and args[0] in HBNBCommand.clses:
            print("** instance id missing **")
        elif len(args) == 2 and args[0] in HBNBCommand.clses:
            for k in objs.keys():
                if k == args[0] + "." + args[1]:
                    print("** attribute name missing **")
                    return
            print("** no instance found **")
        elif len(args) == 3 and args[0] in HBNBCommand.clses:
            print("** value missing **")
        else:
            if args[0] in HBNBCommand.clses:
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
    
    def dd(self):
        pass





if __name__ == '__main__':
    HBNBCommand().cmdloop()
