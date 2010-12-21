from vsgui import zenity

_call = zenity.Zenity()

def notice(text):
    _call.notification(text=text)

def info(text):
    _call.info(text=text)

def error(text):
    _call.error(text=text)

def die(text):
    _call.error(text=text)
    exit()

def warning(text):
    _call.warning(text=text)

def pulsate_progress(text, auto_close=False, auto_kill=False):
    return _call.progress(text=text,
                          auto_close=auto_close,
                          auto_kill=auto_kill, pulsate=True)

def progress(text, auto_close=False, auto_kill=False):
    return _call.progress(text=text,
                          auto_close=auto_close,
                          auto_kill=auto_kill)

def input_text(text, initial=None):
    kdws = {
        'text':text,
    }
    if initial:
        kdws['entry-text'] = initial
    _call.subcmd = 'entry'
    return _call(**kdws)

def input_passwd(text):
    kdws = {
        'text':'please input password: '+ '\n' + text,
        'hide-text':True
    }
    _call.subcmd = 'entry'
    return _call(**kdws)

def input_yesno(text, y=None, n=None):
    kdws = {'text':text}
    if y:
        kdws['ok-label'] = y
    if n:
        kdws['cancel-label'] = n
    return _call.question(**kdws)

def input_radiolist(columns, data, **kwargs):
    #@FIXME add a new row and fill zero into data array.
    args = [['']+columns , data]
    return _call.list(*args, radiolist=True, **kwargs)

def input_checklist(columns, data, **kwargs):
    """
    @example
        print input_checklist(['name','list'],[1,2,3,4,5,6,7,8], hide_column=1)
    """
    #@FIXME add a new row and fill zero into data array.
    args = [['']+columns , data]
    return _call.list(*args, checklist=True, **kwargs)

def input_ab(text, a, b):
    if input_yesno(text, y=a,n=b):
        return a
    return b

def check_passwd(wanted, count=3, text='', errmsg='wrong password, try again!'):
    for i in range(0, count):
        if (input_passwd(text) != wanted):
            die(errmsg) if i == 2 else error(errmsg)
        else:
            return True

if __name__ == '__main__':
    print input_checklist(['name','list'],[1,2,3,4,5,6,7,8])#, hide_column=1)
   # check_passwd('h', 2)
