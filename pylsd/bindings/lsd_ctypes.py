#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-19 02:09:53
# @Author  : Gefu Tang (tanggefu@gmail.com)
# @Link    : https://github.com/primetang/pylsd
# @Version : 0.0.1

import ctypes
import os
import glob

def load_lsd_library():
    # may fail if CWD (via sys.path) contains pylsd/bindings/__init__.py,
    # but otherwise contains the auto-built library for this platform/installation:
    lib_dir = os.path.dirname(os.path.dirname(__file__))
    lib_path = None
    for lib_name in ['lib.*.so', 'lib.*.dll', 'lib.*.dylib', 'lib.*.lib']:
        libs = glob.glob(os.path.join(lib_dir, lib_name))
        if libs:
            lib_path = libs[0]
            break
    if not lib_path:
        return None
    return ctypes.cdll[lib_path]

lsdlib = load_lsd_library()
if lsdlib == None:
    raise ImportError('Cannot load dynamic library. Did you compile LSD?')
