import datetime
import os
import subprocess

from vsgui import utils

import ucltip

class Zenity(ucltip.CmdDispatcher):

    """
    To communicate with Zenity in Python

    Zenity  is a program that will display GTK+ dialogs, and return
    (either in the return code, or on standard output) the users input.
    This allows you to present information, and ask for information from
    the user, from all manner of shell scripts.

    Here is the concept, more method could be found in `zenity --help`

    zenity.info() maps to `zenity --info`
    zenity.info(text="hello") maps to `zenity --info --text='hello'
    """
    #{{{attrs
    cmdname = 'zenity'
    subcmd_prefix = '--'
    __DEBUG__=True
    #}}}

    #{{{def question(self, *args, **kdws):
    def question(self, *args, **kdws):
        """display question dialog

        @param  text title text
        @param  y    text of OK label
        @param  n    text of Cancel label
        @return True or False
        """
        self.subcmd='question'
        kdws['with_extend_output'] = True
        retval = self(*args, **kdws)
        return not retval[0]
    #}}}

    #{{{def calendar(self, *args, **kwds):
    def calendar(self, *args, **kwds):
        """display calendar dialog

        @param text=TEXT                                    Set the dialog text
        @param selected_day=DAY                             Set the calendar day
        @param date_format=PATTERN                          Set the format for the returned date
        @return  datetime.date
        """
        (_kwds, opts) = utils.parse_kwds(kwds, ['selected_day'])
        selected = opts.get('selected_day')
        if selected:
            _kwds['day'] = selected.day
            _kwds['month'] = selected.month
            _kwds['year'] = selected.year
        self.subcmd = 'calendar'
        retval = self(*args, **_kwds)
        (month, day, year) = map(int, retval.split('/'))
        return datetime.date(year, month, day)
    #}}}

   #{{{def text_info(self, *args, **kwds):
    def text_info(self, *args, **kwds):
        """dispaly Display text information dialog

        @param save   save the content in current file
        @param backup extenion of backup filename
        @return content content user inputed
        """
        (_kwds, opts) = utils.parse_kwds(kwds, ['save', 'backup'])
        self.subcmd = 'text-info'
        content = self(*args, **_kwds)
        if opts.get('save') and _kwds.get('filename'):
            utils.savefile(_kwds.get('filename'), content, backup=opts.get('backup'))
        return content
    #}}}

    #{{{def progress(self, *args, **kwds):
    def progress(self, *args, **kwds):
        """display progress dialog

        @param text=TEXT                                    Set the dialog text
        @param percentage=PERCENTAGE                        Set initial percentage
        @param pulsate                                      Pulsate progress bar
        @param auto_close                                   Dismiss the dialog when 100% has been reached
        @param auto_kill                                    Kill parent process if cancel button is pressed
        @return update function                             callable function to update dialog

        @example

            update = zenity.progress(text="Download Script")
            update("10", "starting")
            time.sleep(1)
            update("20", "closing")
            time.sleep(1)
        """
        kwds['stdin'] = subprocess.PIPE
        self.subcmd = 'progress'
        p = self(interact=True, *args, **kwds)

        def update(percent, message=''):
            if type(percent) == float:
                percent = int(percent * 100)
            try:
                p.stdin.write(str(percent) + '\n')
                if message:
                    p.stdin.write('# %s\n' % message)
            except IOError:
                exit()
            return p.returncode
        return update
    #}}}

    #{{{def file_selection(self, *args, **kwds):
    def file_selection(self, *args, **kwds):
        """display file or directory selection dialog

        @return list of selection path of files or directories
        """
        self.subcmd = 'file-selection'
        retstr = self(*args, **kwds)
        return [] if not retstr else retstr.strip().split('|')
    #}}}

    #{{{def list(self, columns, data=[], **kwds):
    def list(self, columns, data=[], **kwds):
        """display selection dialog

        @param columns
        @param data data of cells , its size must be equal to the number of columns
        @return list
        """
        args = []
        for col in columns:
            args.append("--column=%s" % col)

        args += data
        self.subcmd = 'list'
        retstr = self(*args, **kwds)
        if kwds.get('checklist'):
            return [] if not retstr else retstr.split('|')
        return retstr
    #}}}

    #{{{def _callProcess(self, *args, **kwargs):
    def _callProcess(self, *args, **kwargs):
        try:
            return super(Zenity, self)._callProcess(*args, **kwargs)
        except ucltip.CommandExecutedFalur:
            exit()
    #}}}
pass

if __name__ == '__main__':
    obj = Zenity()
#    print obj.text_info()
#    print obj.file_selection()
#    print obj.list(['a'],[1,2,3,4,5,6], text="hello", editable=True)
    print obj.question(text='hi')
#    up= obj.progress(text="hi")
#    import time 
#    up(10, "iii")
#    time.sleep(1)
#    up(20, "iii")
#    time.sleep(1)
#    up(30, "iii")
#    time.sleep(1)
#    up(40, "iii")
