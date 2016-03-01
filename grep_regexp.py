import re

def grep(afile, asearch):
    ''' find asearch in afile '''
    reobj = re.compile(asearch)
    matches = 0
    with open(afile) as fd:
        for line in fd:
            if reobj.search(line):
                matches += 1
                print line.strip()
    
    print '----'
    print "%d matches found" % matches


grep("scores.txt","john")
