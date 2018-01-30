import inspect
import sys
import os.path


sys.path.insert(0, os.path.abspath('..'))


import wcf.records

def cls_sort(a, b):
    if a.__name__ > b.__name__:
        return 1
    elif a.__name__ < b.__name__:
        return -1
    else:
        return 0

with open('record_list.rst', 'w') as fp:
    cnt = fp.tell()
    fp.write('Available Records\n')
    fp.write('-' * (fp.tell() - cnt - 1) + '\n')
    fp.write('==== =====\nType Class\n==== =====\n')
    values = wcf.records.Record.records.values()
    values.sort(cls_sort)
    for cls in values:
        func = inspect.getmembers(cls, inspect.ismethod)
        for name, f in func:
            if name == '__init__':
                fp.write('0x{0:02X} {1}('.format(cls.type, cls.__name__))
                args, varargs, keywords, defaults = \
                    inspect.getargspec(f.__func__)
               
                params = []
                if defaults and len(defaults) > 0:
                    for i in range(1, len(args)):
                        if i > len(defaults):
                            break
                        if args[-i] == 'type' and defaults[-i] == None:
                            continue

                        params.insert(0, 
                            '{0}={1}'.format(
                                args[-i],
                                defaults[-i]))
                    params = args[1:-len(defaults)] + params
                else:
                    params = args[1:]
                if varargs:
                    params.append('\*' + varargs)
                if keywords:
                    params.append('\*\*' + keywords)
                fp.write(', '.join(params) + ')\n')
        #fp.write('.. autoclass:: wcf.records.{0}\n    :members:\n'.format(cls.__name__))
    fp.write('==== =====\n')

