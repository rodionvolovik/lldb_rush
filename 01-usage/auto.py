try:
    import lldb
    import time
except:
    pass;

def auto(debugger, command, result, internal_dict):
    debugger.SetAsync(True)
    if debugger.GetSelectedTarget():
        try:
            file = open('commandes')
            read = (file.read()).split('\n')
        except:
            print('\x1b[31mCommand file doesn\'t exist or has wrong name\nUse filename: \'commandes\' \x1b[0m')
            return
        for r in read:
            debugger.HandleCommand(r)
            time.sleep(10)
        file.close()
    else:
        print('\x1b[31mTarget value is not indicated\x1b[0m')

def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand('command script add -f auto.auto autodebug')
    print('\x1b[34mType \'autodebug\' to debug target\x1b[0m')
