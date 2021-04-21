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
    lib_name = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'lib.*.so')
    lib_path = glob.glob(lib_name)
    if not lib_path:
        return None
    return ctypes.cdll[lib_path[0]]

lsdlib = load_lsd_library()
if lsdlib == None:
    raise ImportError('Cannot load dynamic library. Did you compile LSD?')
