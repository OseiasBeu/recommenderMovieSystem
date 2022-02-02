import subprocess
import platform

def limpar():
    ambiente  = platform.system()
    limpa_code = ''
    if ambiente == 'Windows':
        limpa_code = 'cls'

    else:
        limpa_code = 'clear'
        
    subprocess.call(limpa_code, shell = True)