try:
    import lldb
except:
    pass;

def reverse(debugger, command, result, internal_dict):
    print('FT_' + (str(debugger.GetSelectedTarget()))[::-1] if debugger.GetSelectedTarget() else '\x1b[31mTarget value is not indicated\x1b[0m')

def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand('command script add -f reverse.reverse reverse')
    print('\x1b[34mType \'reverse\' command to get a reversed target name preceded with FT_\x1b[0m')
