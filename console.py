#!/usr/bin/env python3
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """Implement the end-of-file prompt"""
        exit()

    def do_quit(self, line):
        """quit the command interpreter"""
        exit()

    def emptyline(self):
        pass

    def do_create(self):
        pass

    def do_show(self):
        pass

    def do_destroy(self):
        pass

    def do_all(self):
        pass

    def do_update(self):
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
