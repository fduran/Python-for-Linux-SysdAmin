def tail(afile, last=10):
    ''' implements tail-like function (for chars, not lines) '''
    offset = last
    with open(afile) as fd:
        fd.seek(0, 2)
        len = fd.tell()
        if last > len:
            offset = len
        fd.seek(offset*(-1), 2)
        tail = fd.read(last)
        print str(tail)

tail('scores.txt')
tail('scores.txt', 5)
