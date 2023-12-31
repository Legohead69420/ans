def __main__():
    import os
    import keyboard
    from time import sleep
    from pylogger.operators import cls
    import subprocess
    from colorama import init, Fore, Back

    cls()
    hf = 'history.log'
    def run(cmd):
        os.system(cmd)
    history = open(hf, 'r').read()
    na = ['reload', 'exit', 'donut']
    print(history)
    if history == '':
        pass
    else:
        print(Back.WHITE+Fore.BLACK+' * '+Back.LIGHTBLUE_EX+Fore.BLACK+' History Restored '+Fore.RESET+Back.RESET+'\n\n')
        open(hf, 'w').write('')
    while True:
        cmd = input(f"PS {__file__.replace(r'\powershell.py', '> ')}")
        if cmd == 'reload':
            os.system(f'python {__file__}')
        elif cmd == 'exit':
            return None
        else:
            run(cmd)
            output = subprocess.run(cmd, capture_output=True, text=True, shell=True)
            if not cmd == 'cls':
                open(hf, 'a').write(f'{output.stdout}\n')
