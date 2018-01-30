#!/usr/bin/env python2
# vim: set ts=4 sw=4 tw=79 fileencoding=utf-8:

from __future__ import absolute_import
import logging
import doctest
import unittest
import sys
from codecs import decode

sys.path.append('..')
    
from wcf.records import *

test_bin = decode(
"56020b0173040b0161065608440a1e0082993a687474703a2f2f646f6373"
"2e6f617369732d6f70656e2e6f72672f77732d73782f77732d7472757374"
"2f3230303531322f5253542f4973737565441aad5db293d4bc0ba547b9dc"
"cb2f140fd0c3442c442aab1401440c1e00829923687474703a2f2f657861"
"6d706c652e636f6d2f466f6f4261722f58797a4d6574686f6401560e4105"
"747275737414526571756573745365637572697479546f6b656e0407436f"
"6e74657874982c757569642d34393037636538322d303630372d34626330"
"2d626438612d6531633937663165323862372d3232090574727573743068"
"7474703a2f2f646f63732e6f617369732d6f70656e2e6f72672f77732d73"
"782f77732d74727573742f3230303531324105747275737409546f6b656e"
"547970659941687474703a2f2f646f63732e6f617369732d6f70656e2e6f"
"72672f77732d73782f77732d736563757265636f6e766572736174696f6e"
"2f3230303531322f736374410574727573740b5265717565737454797065"
"9936687474703a2f2f646f63732e6f617369732d6f70656e2e6f72672f77"
"732d73782f77732d74727573742f3230303531322f497373756541057472"
"757374074b657953697a658b0001410574727573740e42696e6172794578"
"6368616e67650674aaa60306d402aad8029e364e544c4d53535000010000"
"00b7b218e20a000a002d00000005000500280000000601b11d0000000f43"
"4c5753315745425345525649439f0145010101", "hex_codec")

class TransformTest(unittest.TestCase):

    def runTest(self):
        from io import BytesIO
        bio = BytesIO(test_bin)
        new = dump_records(Record.parse(bio))

        self.assertEqual(test_bin, new)

class Suite(unittest.TestSuite):

    def __init__(self, *args, **kwargs):
        super(Suite, self).__init__(*args, **kwargs)

        self.addTest(doctest.DocTestSuite(base))
        self.addTest(doctest.DocTestSuite(elements))
        self.addTest(doctest.DocTestSuite(attributes))
        self.addTest(doctest.DocTestSuite(text))
        self.addTest(TransformTest())

if __name__ == '__main__':
    #unittest.main()
    unittest.TextTestRunner(verbosity=1).run(Suite())
