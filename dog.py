import getopt
import os
import sys

import src.dogengine as engine

# Control ==================================

def setup():
    """Initial setup that should be done before running the main routines."""

    if not os.path.exists('data'):
        os.mkdir('data')

def run():
    """Runs a cycle of the bot's activity, including necessary setup."""

    setup()
    engine.run()

def test():
    """Runs a test cycle, operating without making any actual posts."""

    setup()
    engine.run(testmode=True)
    print("")

# Process command line input ================

if __name__ != '__main__':
    sys.exit(0)
    
mode = None
count = None

# Error cases

def error_mode_conflict():
    print("> Error: must choose one mode from test or publish")
    sys.exit(1)

# Get args

try:
    opts, params = getopt.getopt(sys.argv[1:], "etpc:k:", ["test", "publish"])
except getopt.GetoptError:
    print('dog.py --publish')
    sys.exit(2)

# Process args
for opt, arg in opts:
    
    if opt in ["-t", "--test"]:
        if mode != None:
            error_mode_conflict()
        mode = "test"
    elif opt in ["-p", "--publish"]:
        if mode != None:
            error_mode_conflict()
        mode = "publish"

# Assign defaults

if mode == None:
    print("> Defaulting to test mode")
    mode = "test"

if mode == "publish":
    run()
elif mode == "test":
    test()
