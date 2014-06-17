#!/usr/bin/env python3.3-sp

import os
import datetime
import shutil
import sys
import stat
import errno

def walk(path, report_fn):
    for (this_dir, sub_dir, files) in os.walk(path):
        for file_path in files:
            full_file_path = os.path.join(this_dir, file_path)
            abs_file_path = os.path.realpath(full_file_path)

            try:
                st = os.stat(abs_file_path)
            except EnvironmentError as err:
                if err.errno != errno.ENOENT:
                    raise
            else:
                if stat.S_ISREG(st.st_mode):
                    report_fn(full_file_path, abs_file_path, st)

import pprint
def print_report(*args):
    pprint.pprint("{}".format(args))
