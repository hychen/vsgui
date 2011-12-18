# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#!/usr/bin/env python
# -*- encoding=utf8 -*-
#
# Author 2011 Hsin-Yi Chen
import ucltip
from vsgui import zenity
from vsgui.utils import deprecated

try:
    _dialoger = zenity.Zenity()
except ucltip.CommandNotFound, e:
    print e
    exit()

# Dialog
# ---------------------------------------------
def info(msg):
    _dialoger.info(text=msg)

def warning(msg):
    _dialoger.warning(text=msg)

def error(msg):
    _dialoger.error(text=msg)

def die(msg):
    error(msg)
    exit()

def notice(msg):
    _dialoger.notification(text=msg)

# Inpit text
#-------------------------------------------------------------
def ask_text(text, initial=None):
    kdws = {
        'text':text,
    }
    if initial:
        kdws['entry-text'] = initial
    return _dialoger.entry(**kdws)

@deprecated(ask_text)
def input_text(*args, **kwargs):
    pass

def ask_passwd(text):
    kdws = {
        'text':'please input password: '+ '\n' + text,
        'hide-text':True
    }
    return _dialoger.entry(**kdws)

@deprecated(ask_passwd)
def input_passwd():
    pass

# Question
#-------------------------------------------------------------
def ask_yesno(text, y=None, n=None):
    kdws = {'text':text}
    if y:
        kdws['ok-label'] = y
    if n:
        kdws['cancel-label'] = n
    return _dialoger.question(**kdws)

@deprecated(ask_yesno)
def input_yesno():
    pass

def ask_ab(text, a, b):
    if input_yesno(text, y=a,n=b):
        return a
    return b

@deprecated(ask_ab)
def input_ab(text, a, b):
    pass

def check_passwd(wanted, count=3, text='', errmsg='wrong password, try again!'):
    for i in range(1, count):
        if (ask_passwd(text) != wanted):
            die(errmsg) if i == count else error(errmsg)
        else:
            return True

# progress
#-------------------------------------------------------------
def pulsate_progress(text, auto_close=False, auto_kill=False):
    return _dialoger.progress(text=text,
                          auto_close=auto_close,
                          auto_kill=auto_kill, pulsate=True)

def progress(text, auto_close=False, auto_kill=False):
    return _dialoger.progress(text=text,
                          auto_close=auto_close,
                          auto_kill=auto_kill)

def ask_scalevalue(label, initial_value=0, **kwargs):
    return _dialoger.scale(text=label, value=initial_value, **kwargs)

# file
#-------------------------------------------------------------
def first_or_none(list):
    try:
        return list[0]
    except IndexError:
        return None

def ask_filepath(**kwargs):
    return first_or_none(ask_filepaths(**kwargs))

def ask_filepaths(**kwargs):
    kwargs['multiple'] = True
    return _dialoger.file_selection(**kwargs)

def ask_dirpath(**kwargs):
    return first_or_none(ask_dirpaths(**kwargs))

def ask_dirpaths(**kwargs):
    kwargs['directory'] = True
    kwargs['multiple'] = True
    return _dialoger.file_selection(**kwargs)
