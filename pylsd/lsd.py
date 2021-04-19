#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ctypes
import os
import sys
from tempfile import NamedTemporaryFile

import numpy as np


from .bindings.lsd_ctypes import lsdlib

def lsd(src):
    rows, cols = src.shape
    src = src.reshape(1, rows * cols).tolist()[0]

    lens = len(src)
    src = (ctypes.c_double * lens)(*src)

    with NamedTemporaryFile(prefix='pylsd-', suffix='.ntl.txt', delete=False) as fp:
        fname = fp.name
        fname_bytes = bytes(fp.name) if sys.version_info < (3, 0) else bytes(fp.name, 'utf8')

    lsdlib.lsdGet(src, ctypes.c_int(rows), ctypes.c_int(cols), fname_bytes)

    with open(fname, 'r') as fp:
        output = fp.read()
        cnt = output.strip().split(' ')
        count = int(cnt[0])
        dim = int(cnt[1])
        lines = np.array([float(each) for each in cnt[2:]])
        lines = lines.reshape(count, dim)

    os.remove(fname)
    return lines
