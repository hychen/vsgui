VSGUI - Very Simple Graphic Interface Library for Python
========================================================

Description
-----------

It proides a simple functions to comuunicate with `zenity` which
is a program that will display GTK+ dialogs, and return
(either in the return code, or on standard output) the users input.
This allows you to present information, and ask for information from
the user, from all manner of shell scripts.

Note: this moduels requires `ucltip` (http://pypi.python.org/pypi/ucltip)
      module, please install it.

How To Use
----------

The source code includes some examples, so you can take a qucik look before you
start coding, and thre are two part of this library as below

1. High Level API functions
---------------------------

Before start, you need to import api funcitons:

::
	from vsgui.api import *

Dialogs

::
	from vsgui.api import *

	# information dialog
	info(msg)

	# warring dialog
	warning(msg):

	# error dialog
	error(msg):

	# error dialog and terminate script
	die(msg):

	# notice dialog
	notice(msg):

Input Text

::
	# input text
	input_text(text, initial=None)

	# input password
	input_passwd(text)

Questions

::

	# ask user the anwser is yes or no
	input_yesno(text, y=None, n=None):

	# ask user select a or b
	input_ab(text, a, b):

	# ask user passowrd, and check it
	check_passwd(wanted, count=3, text='', errmsg='wrong password, try again!')

Progress
-------

::
	# launch a progress bar and create a update function
	update = progress('downloading files')

	# update progress bar message ot 'md5sum checking' and progessive number to 90
	update(90, 'md5sum checking')


2. Zenity Class
---------------

if api functions is not enough, you can use Zenity class direcly to get
more powerful feature.

::
	from vsgui.zenity import Zenity
	z = Zenity()

	# same as executing 'zenity --file-selection --filename=a.txt'
	z.file_selection(filename='a.txt')
