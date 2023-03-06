import cmd
import shlex
import cowsay

class cmdline(cmd.Cmd):
    def do_list_cows(self, arg):
        """
        Lists all cow file names in the given directory
        Example: list_cows ~
        """
        if arg:
            print(cowsay.list_cows(cow_path=arg))
        else:
            print(cowsay.list_cows())
    def do_make_bubble(self, arg):
        """
        Wraps text if wrap_text is true, then pads text and sets inside a bubble.
        This is the text that appears above the cows
        Example: make_bubble "Hello, world!"
        """
        print(cowsay.make_bubble(text=shlex.split(arg)[0]))
    def do_cowsay(self, arg):
        """
        Similar to the cowsay command. Parameters are listed with their
        corresponding options in the cowsay command. Returns the resulting cowsay
        string
        """
        names, defaults = ['cow', 'eyes', 'tongue'], ['default', 'oo', '  ']
        args = shlex.split(arg)
        message, defaults[:len(args) - 1] = args[0], args[1:]
        args = dict(list(zip(names, defaults)))
        print(cowsay.cowsay(message=message, **args))
    def do_cowthink(self, arg):
        """
        Similar to the cowthink command. Parameters are listed with their
        corresponding options in the cowthink command. Returns the resulting
        cowthink string
        """
        names, defaults = ['cow', 'eyes', 'tongue'], ['default', 'oo', '  ']
        args = shlex.split(arg)
        message, defaults[:len(args) - 1] = args[0], args[1:]
        args = dict(list(zip(names, defaults)))
        print(cowsay.cowthink(message=message, **args))
    def complete_list_cows(self, prefix, line, start, end):
        pass
    def complete_make_bubble(self, prefix, line, start, end):
        pass
    def complete_cowsay(self, prefix, line, start, end):
        pass
    def complete_cowthink(self, prefix, line, start, end):
        pass

if __name__ == '__main__':
    cmdline().cmdloop()
