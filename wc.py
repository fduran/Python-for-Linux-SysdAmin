def wc(afile):
    ''' implements word count '''
    with open(afile) as fd:
        all = fd.read()
        chars = len(all)
        lines = len(all.split('\n')) # os.linesep
        wordlist = all.split(None)
        words = len(wordlist)
        return lines, words, chars

print wc('scores.txt')
