# Demonstrates pip-installed package

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.ghostbusters("hello, " + sys.argv[1])
