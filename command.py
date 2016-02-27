import shlex, subprocess


def execute(command):
    ''' Executes external command '''
    # shlex.split tokenizes command into a list
    args = shlex.split(command)
    res = subprocess.Popen(args, stdout = subprocess.PIPE)
    print res.stdout.read().strip()

execute('ls -l')
