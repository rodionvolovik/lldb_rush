#!/usr/bin/python

import lldb

def open_read(name):
    f = open(name)
    str = f.read()
    f.close()
    return (str)

def correct(debugger, command, result, internal_dict):
    # string = str(debugger.GetSelectedTarget())    # return printable representation of a given object.
    if debugger.GetSelectedTarget():            # call fanction in case the object if exist
        str = open_read('commandes')
        list = str.split('\n')
        for line in list:
            debugger.HandleCommand(line)

def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand('command script add -f correct.correct correct')         # initialization to add commands
    print('The correct python command has been installed and is ready for use.')    # print "usage"
