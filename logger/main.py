try:
    import colorama
    colorama.init(autoreset=True)
except ImportError:
    import sys
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install',
                           'colorama'])
    raise ImportError('Wail to import colorama restart script')

class Logger:
    def __init__(self, colored=False):
        self.paras = 0
        self.colored = colored

    def good(self, object):
        xx = ' '
        for x in range(self.paras):
            xx += ' '
        if self.colored:
            print(xx, colorama.Fore.GREEN+'+', object)
        else:
            print(xx, '+', object)

    def bad(self, object, excepto=''):
        xx = ' '
        for x in range(self.paras):
            xx += ' '
        if self.colored:
            print(xx, colorama.Fore.RED + '-', object.__str__() + ' ' + excepto.__str__())
        else:
            print(xx, '-', object.__str__() + ' ' + excepto.__str__())


    def info(self, script, object):
        if self.colored:
            print('[{0}INFO{1}][{2}] {3}'.format(colorama.Fore.WHITE, colorama.Fore.RESET, script, object.__str__()))
        else:
            print('[INFO][{0}] {1}'.format(script, object.__str__()))


    def warning(self, script, object):
        if self.colored:
            print('[{0}WARNING{1}][{2}] {3}'.format(colorama.Fore.YELLOW, colorama.Fore.RESET, script, object.__str__()))
        else:
            print('[WARNING][{0}] {1}'.format(script, object.__str__()))

    def error(self, script, object):
        if self.colored:
            print('[{0}ERROR{1}][{2}] {3}'.format(colorama.Fore.RED, colorama.Fore.RESET, script, object.__str__()))
        else:
            print('[ERROR][{0}] {1}'.format(script, object.__str__()))

    def para(self):
        self.paras += 1

    def unpara(self):
        if self.paras != 0:
            self.paras -= 1
