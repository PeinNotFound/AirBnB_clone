#!/usr/bin/python3
'''Coonsole module contains the entry point of the command interpreter.'''

import cmd

class HBNBCommand(cmd.Cmd):
    '''The entry point of the command interpreter.'''
    prompt = "(hbnb)"

    def do_quit(self, args):
        '''Quit the program.'''
        return True

    def  help_quit(self,arg):
        '''Quit the program.'''
        print("Quit command to exit the program")

    def do_EOF(self,arg):
        '''Quit the program.'''
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()

