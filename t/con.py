#!/usr/bin/python3
# Comment here
import cmd, sys
from turtle import *

class tshell(cmd.Cmd):
    intro = 'Welcome to the turtle shell. Type help or ? to list commands.\n'
    prompt = '(turtle)'
    file = None

    #------basic turtle commands--------
    def do_forward(self, arg):
        'Move the turtle forward by the specified distance: FORWARD 10'
        forward(*parse(arg))
    def do_right(self, arg):
        'Turn turtle right by given number of degrees: RIGHT 20'
        right(*parse(arg))
    def do_left(self, arg):
        'Turn turtle right by number of degrees: LEFT 90'
        left(*parse(arg))
    def do_goto(self, arg):
        'Move turtle to an absolute position with changing orientation. GOTO 100 200'
        goto(*parse(arg))
    def do_home(self, arg):
        'Return turtule to the home position: HOME'
        home()
    def do_circle(self, arg):
        'Draw circle with given radius an options extent and steps: CIRCLE 50'
        circle(*parse(arg))
    def do_position(self, arg):
        'Print the current turtle position: POSITION'
        print('Current position is %d %d\n' % position())
    def do_heading(self, arg):
        'Print the current turtle heading in degrees: HEADING'
        print('Current heading is %d\n' % (heading(),))
    def do_color(self, arg):
        'Set the color: COLOR BLUE'
        color(arg.lower())
    def do_undo(self, arg):
        'Undo (repeatedly) the last turtle action(s): UNDO'
    def do_reset(self, arg):
        'Clear the screen and return turtle to center: RESET'
        reset()
    def do_wac(self, arg):
        'Do wac things for the things themselves: WAC'
        wac(arg)
    def do_bye(self, arg):
        print('THank you for using Turtle')
        self.close()
        bye()
        return True
    #-----record and playback----
    def do_record(self, arg):
        'Save future command to filename: RECORD rose.cmd'
        self.file = open(arg, 'w')
    def do_playback(self, arg):
        'Playback commands from a file: PLAYBACK rose.cmd'
        self.close()
        with open(arg) as f:
            self.cmdqueue.extend(f.read().splitlines())
    def precmd(self, line):
        line = line.lower()
        if self.file and 'playback' not in line:
            print(line, file = self.file)
        return line
    def close(self):
        if self.file:
            self.file.close()
            self.file = None
def parse(*arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))
def wac(arg):
    #for i in ar:
     #   print(i)
    print(*parse(arg))
if __name__ == '__main__':
    tshell().cmdloop()
