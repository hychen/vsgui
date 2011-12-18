# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#!/usr/bin/env python
# -*- encoding=utf8 -*-
#
# Author 2011 Hsin-Yi Chen
#
# This is a free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or (at your
# option) any later version.
#
# This software is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this software; if not, write to the Free Software Foundation, Inc., 59 Temple
# Place, Suite 330, Boston, MA 02111-1307 USA
from vsgui.api import *
# the backed is zenity by default

info("this is a information dialog")
warning("this is a warning dialog")
error("this is a error dialog")

ret=ask_text("This is a input dialog", "please input some thing")
while not ask_yesno("Do you input {0}".format(ret), 'sure', 'not this one'):
    pass

update=progress("processing text....")

import time
update(20, "setp 1")
time.sleep(1)
update(40, "setp 2")
time.sleep(1)
update(60, "setp 3")
time.sleep(1)
update(80, "setp 4")
time.sleep(1)
update(100, "Done")

ask_scalevalue('scale')

# file
info(ask_filepath())
ask_filepaths()
ask_dirpath()
ask_dirpaths()
