#!/usr/bin/python3
'''Coonsole module contains the entry point of the command interpreter.'''

import cmd
import shlex
from models.base_model import BaseModel
from models import storage
import re
import ast

class HBNBCommand(cmd.Cmd):
    '''The entry point of the command interpreter.'''
    prompt = "(hbnb)"
    valid_classes = ["BaseModel"]

    def emptyline(self):
        '''Does nothing when an empty line is entered'''
        pass

    def do_quit(self, args):
        '''Quit the program.'''
        return True

    def do_create(self, arg):
        '''Creates a new instance of BaseModel and save it to the JSON file.
        Usage: create <class_name>
        '''
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name is missing **")
        elif commands[0] not in self.valid_classes:
            print("** class does not exist **")
        else:
            new_instance = eval(f"{commands[0]}()")
            storage.save()
            print(new_instance.id)

    def do_show(self, arg):
        '''
        Shows the string representation of an instance.
        Usage: show <class_name> <id>
        '''
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name is missing **")
        elif commands[0] not in self.valid_classes:
            print("** class does not exist **")
        elif len(commands) < 2:
            print("** instance id is missing **")
        else:
            objects = storage.all()

            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance has found **")

    def do_destroy(self, arg):
        '''
        Deletes an instance based on the class name and id.
        Usage: destroy <class_name> <id>
        '''
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name is missing **")
        elif commands[0] not in self.valid_classes:
            print("** class does not exist **")
        elif len(commands) < 2:
            print("** instance id is missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance has found **")

    def do_all(self, arg):
        '''
        Prints the string representation of all instances or a specific class.
        Usage: <User>.all() <User>.show()
        '''
        objects = storage.all()

        commands = shlex.split(arg)

        if len(commands) == 0:
            for key, value in objects.items():
                print(str(value))
        elif commands[0] not in self.valid_classes:
            print("** class does not exist **")
        else:
            for key, value in objects.items():
                if key.split('.')[0] == commands[0]:
                    print(str(value))

    def do_update(self, arg):
        '''
        Updates an instance by adding or updating an attribute.
        Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
        '''
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name is missing **")
        elif commands[0] not in self.valid_classes:
            print("** class does not exist **")
        elif len(commands) < 2:
            print("** instance id is missing **")
        else:
            objects = storage.all()

            key = "{}.{}".format(commands[0], commands[1])
            if key not in objects:
                print("** no instance has found **")
            elif len(commands) < 3:
                print("** attribute name is missing **")
            elif len(commands) < 4:
                print("** value is missing **")
            else:
                obj = objects[key]

                attr_name = commands[2]
                attr_value = commands[3]

                try:
                        attr_value = eval(attr_value)
                except Exception:
                    pass
                setattr(obj, attr_name, attr_value)

                obj.save()

    def  help_quit(self,arg):
        '''Quit the program.'''
        print("Quit command to exit the program")

    def do_EOF(self,arg):
        '''Quit the program.'''
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()

