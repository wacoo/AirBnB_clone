#!/usr/bin/python3
""" Defines the HBNBCommand class """
import cmd
import sys
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
    """ This class is a child of the cmd class that
    prvides customisable cmd interpreter. This class
    is commnadline console to create show and update
    our AirBnB application
    Attributes:
        clses (list): contains list of all classes created
        prompt (str): provides the prompt text
    """

    intro = ''
    prompt = '(hbnb)'
    # names of classes
    clses = ["BaseModel", "User", "Place", "State",
             "City", "Amenity", "Review"]
    # Support commands

    def help_EOF(self):
        """ provides help text to EOF command"""
        print("EOF command to exit the program")

    def help_quit(self):
        """ provides help text to quit command"""
        print("Quit command to exit the program")

    def help_update(self):
        """ provides help text to update command"""
        print('update <class name> <id> <attribute name> "<attribute value>"')

    def do_EOF(self, line):
        """ this method quits the cmd """
        return True

    def do_quit(self, line):
        """ this method quits the cmd """
        return True

    def emptyline(self):
        """ prevents the repeatition of previous result when empty input"""
        pass

    # Functional commands
    def default(self, line):
        """ Class.command type commands"""
        cnt = 0
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
                # show()
                pat_show = re.compile(r"show\(.+\)$")
                # destroy()
                pat_dest = re.compile(r"destroy\(.+\)$")
                pat_update = re.compile(r"update\(([a-z0-9A-Z])+\)$")
                pat_upd_dict = re.compile(\
                        r"update\((.+)\,( )?\{([a-z0-9A-Z])+\:( )?.+\)$")
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
                elif s[0] == HBNBCommand.clses[i] and pat_update.match(s[1]):
                    striped = s[1].strip('update(').strip(')')
                    striped_comma = striped.replace(',', ' ')
                    self.do_update(s[0] + " " + striped_comma.strip('\"').strip("\'"))
                    break
                elif s[0] == HBNBCommand.clses[i] and pat_upd_dict.match(s[1]):
                    striped = s[1].strip('update(').strip(')')
                    striped_comma = striped.replace(',', ' ')
                    col_rm = striped_comma.replace(':', ' ')
                    st_par = col_rm.replace('\"', '').replace("\'", "")
                    br_rem_par = st_par.replace('{', '').replace('}', '')
                    param = br_rem_par.split()
                    i = 0
                    while i + 2 < len(param):
                        self.do_update(s[0] + " " + param[0] + " "+ param[i + 1] + " " + param[i + 2])
                        i += 2
                    break

    def do_create(self, line):
        """ Creates a object from a class """
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
        """ shows the instance with id given"""
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
        """ removes the instance with the id given"""
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
        """ displays all the instances of a class given"""
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
        """ add new or changes exsiting attributes of an instace give by id"""
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




if __name__ == '__main__':
    HBNBCommand().cmdloop()
