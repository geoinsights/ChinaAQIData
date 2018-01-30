#!/usr/bin/env python2
# vim: set ts=4 sw=4 tw=79 fileencoding=utf-8:

from __future__ import absolute_import, with_statement

from wcf.xml2records import XMLParser
from wcf.records import dump_records

import sys
import logging

if __name__ == '__main__':
    fp = sys.stdin

    if len(sys.argv) > 1:
        fp = open(sys.argv[1], 'r')

    logging.basicConfig(level=logging.INFO)

    with fp:
        r = XMLParser.parse(fp)
        data = dump_records(r)

    if sys.version_info >= (3, 0, 0):
        sys.stdout.buffer.write(data)
    else:
        sys.stdout.write(data)
