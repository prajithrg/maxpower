#!/usr/bin/python

import os
from fabricate import *

MAXOSDIR = os.environ['MAXELEROSDIR']
MAXCOMPILERDIR = os.environ['MAXCOMPILERDIR']

sources = ['lmem.c']
target = 'liblmem.a'
includes = [ ] 

def get_maxcompiler_inc():
    """Return the includes to be used in the compilation."""
    return ['-I.', '-I%s/include' % MAXOSDIR, '-I%s/include/slic' % MAXCOMPILERDIR]

cflags = ['-ggdb', '-O2', '-fPIC', '-std=gnu99', '-Wall', '-Werror'] + includes + get_maxcompiler_inc() 

def build():
    compile()
    link()

def compile():
    for source in sources:
        run('gcc', cflags, '-c', source, '-o', source.replace('.c', '.o'))

def link():
    objects = [s.replace('.c', '.o') for s in sources]
    run('ar', '-cq', target, objects)

def clean():
    autoclean()

main()
