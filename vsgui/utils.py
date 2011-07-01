import os

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
