#!/usr/bin/env python
# -*- encoding=utf8 -*-
#
# Author 2011 Hsin-Yi Chen
import os
import unittest
import ucltip
from vsgui import zenity

# setup test env
def setup_testenv():
    testbinpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),'bin')
    os.environ['PATH'] = "{0}:{1}".format(os.getenv('PATH'), testbinpath)

def getwid(winname):
    cmd = "wininfo -root -children | grep %s | awk '{print $1}'".format(winname)
    return commands.getoutput(cmd)

class ZenityTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_info(self):
        # get window id
        z = zenity.Zenity()
        p = z.info(text='hi', as_process=True)
        # send clik
        pass

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ZenityTestCase, 'test'))
    return suite

if __name__ == '__main__':
    setup_testenv()
    unittest.main(defaultTest='suite')
