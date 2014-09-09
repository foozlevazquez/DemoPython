import argparse

ap = argparse.ArgumentParser()
ap.add_argument('--log_level=', default='debug')
sp = ap.add_subparsers(help='commands', dest='command_name')

dp = sp.add_parser('hcf')
dp.add_argument('myarg', action='store')

print("command = ", vars(ap.parse_args()).get('command_name'))
