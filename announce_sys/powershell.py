def __main__():
    import os
    from pylogger.operators import cls
    import subprocess
    from colorama import init, Fore, Back

    cls()
    init()
    hf = 'history.log'
    def run(cmd):
        os.system(cmd)
    history = open(hf, 'r').read()
    print(Fore.RESET+history)
    if history == '':
        pass
    else:
        print(Back.WHITE+Fore.BLACK+' * '+Back.LIGHTBLUE_EX+Fore.BLACK+' History Restored '+Fore.RESET+Back.RESET+'\n\n')
        open(hf, 'w').write('')
    print('Opened shell instance')
    while True:
        cmd = input(Fore.RESET+f"PS {__file__.replace(r'\powershell.py', '> ')}"+Fore.YELLOW)
        print(Fore.RESET)
        if cmd == 'reload':
            os.system(f'python {__file__}')
        elif cmd == 'exit':
            cls()
            return None
        else:
            run(cmd)
            output = subprocess.run(cmd, capture_output=True, text=True, shell=True)
            if not cmd == 'cls':
                open(hf, 'a').write(f'{output.stdout}\n')
