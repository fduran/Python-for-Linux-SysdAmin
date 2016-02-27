# optparse deprecated in 2.7
import optparse

p = optparse.OptionParser()
p.add_option("-i", "--inputfile", action="store", type="string", dest="infile")
opt, args = p.parse_args()

print "in file: ", opt.infile


# use argparse instead in 2.7 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", action="store", dest="infile") # type string is default
args = parser.parse_args()

print "in file: ", args.infile
