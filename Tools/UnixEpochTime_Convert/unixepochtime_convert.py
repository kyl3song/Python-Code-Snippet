# -*- coding: utf-8 -*-
# @Author: Kyle Song
# @Date:   2020-03-11 13:50
# @Last Modified by:   KyleSong

import datetime

def main():
    """ 2147483647 is the end value, just before the overflow of EpochTime"""

    UNIXEPOCH_LENGTH = 10
    UNIXEPOCH_MILLISEC_LENGTH = 13

    timestamp = [1583902425,
                 1583902426,
                 1583902576,
                 1582722273439,
                 1582714696234,
                 1582714671700,
                 1582533627849,
                 "N/A",
                 " "]

    for ts in timestamp:
        time_length = len(str(ts))
        try:
            if time_length == UNIXEPOCH_LENGTH:
                humantime = unixepoch_to_humantime(ts)
                print("Converted Time (UnixEpoch):", humantime)

            elif time_length == UNIXEPOCH_MILLISEC_LENGTH:
                humantime = unixepoch_millisec_to_humantime(ts)
                print("Converted Time (UnixEpoch_Millisecond):", humantime)

            else:
                print("Convert Error: ", ts)

        except:
            print(ts, "-> ERROR")
            pass

def unixepoch_to_humantime(unixepoch):
    """ convert unixepoch time to human-readable time """
    return datetime.datetime.fromtimestamp(unixepoch)


def unixepoch_millisec_to_humantime(unixepoch):
    """ convert unixepoch time(millisecond) to human-readable time """
    return datetime.datetime.fromtimestamp(unixepoch / 1000)


if __name__ == '__main__':
    main()
