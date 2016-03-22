# Read a log file with contents like collapse.log file:
# Jan 20 03:25:08 message
# and print out the minute and number of messages in that minute, for ex:
# Jan 20 03:25 2
# ...


def collapse(afile):
    with open(afile) as fd:
        last_minute = "xxxxxxxxxxx"
        freq = 0
        for line in fd:
            minute = line[:12] #Jan 20 03:25
            if minute == last_minute:
                freq += 1
            else:
                print minute, freq
                freq = 0
                last_minute = minute
        print minute, freq # last minute not printed above
    

collapse('collapse.log')
