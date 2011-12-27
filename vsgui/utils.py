import os
import warnings
import functools

# enable to show warring
warnings.simplefilter('default')

def deprecated(replacement=None):
    """This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emitted
    when the function is used.

    ref:
        - recipe-391367-1 on active stack code
        - recipe-577819-1 on active stack code

    @replacement function replacement function
    """
    def wrapper(old_func):
        wrapped_func = replacement and replacement or old_func
        @functools.wraps(wrapped_func)
        def new_func(*args, **kwargs):
            msg = "Call to deprecated function %(funcname)s." % {
                    'funcname': old_func.__name__}
            if replacement:
                msg += "; use {} instead".format(replacement.__name__)
            warnings.warn_explicit(msg,
                category=DeprecationWarning,
                filename=old_func.func_code.co_filename,
                lineno=old_func.func_code.co_firstlineno + 1
            )
            return wrapped_func(*args, **kwargs)
        return new_func
    return wrapper

def parse_kwds(kwds, extra):
    """parse options from kwds

    @return filtered kwds, options
    """
    opts = {}
    for k in extra:
        opts[k] = kwds.get(k)
        try:
            del(kwds[k])
        except KeyError:
            pass
    return kwds, opts

def savefile(filename, content, backup='.bak'):
    """save file

    @param filename path of filename
    @param content content of file
    @param backup extention of backup filename, default is .bak (optional)
    """
    if backup:
        os.system("cp %s %s%s" % (filename, filename, backup))

    with open(filename, 'r') as old:
        oldstr = old.read()
    with open(filename, 'w') as new:
        newstr = content
        if newstr != oldstr:
            new.write(newstr)

if __name__ == '__main__':
    kwds = {'save':True,'nono':'oo'}
    print parse_kwds(kwds, ['save'])
