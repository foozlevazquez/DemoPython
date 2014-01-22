#!/usr/bin/python3.3-sp

import fileinput

FIELD_NAMES = []
FIELD_NAMES_LINE = ''

def process(line, count, stats_dict):
    global FIELD_NAMES
    global FIELD_NAMES_LINE

    # snarf the col headers
    if count == 4:
        FIELD_NAMES = line.split()
        FIELD_NAMES_LINE = line
    # Start noting data after line 4
    if count > 4:
        stats_part = line[:46]
        desc_part = line[46:]
        stats_dict[desc_part] = dict(zip(FIELD_NAMES, stats_part.split()))
        stats_dict[desc_part]['line'] = line



if __name__ == '__main__':
    count = 0
    stats_dict = {}
    for line in fileinput.input():
        process(line, count, stats_dict)
        count += 1
    # Sort by tottime
    sorted_keys = sorted(stats_dict.keys(), key=lambda k: float(stats_dict[k]['cumtime']))
    print(FIELD_NAMES_LINE)
    for key in sorted_keys:
        print(stats_dict[key]['line'])
