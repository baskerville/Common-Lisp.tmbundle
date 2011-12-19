#!/usr/bin/env python
#Common Lisp tooltip documentation

from sys import argv
import commands
from re import findall


def main():
    symbol = str(argv[1])
    cmd = 'curl http://lispdoc.com/?q=%s&search=Basic+search' % (symbol)
    html = commands.getoutput(cmd)

    doc = findall('<tr class="result1">.*',html)[0] + "</span><br></td></tr>"
    doc = "<table>" + doc + "</table>"

    print doc
    
    
if __name__ == '__main__':
    main()

