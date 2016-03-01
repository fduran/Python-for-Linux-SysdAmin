def grep(afile, astring):
    ''' function implementing grep-like , with generator '''
    with open(afile) as fd:
        for line in fd:
            if astring in line:
                yield str(line).strip()

g = grep("scores.txt", "john")

print g.next() # first result
print g.next() # second result

print next(g, '- no more results -') # better, no StopIteration exception but returns default value
