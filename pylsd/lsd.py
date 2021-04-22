#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ctypes
import os
import sys
from tempfile import NamedTemporaryFile

import numpy as np


from .bindings.lsd_ctypes import lsdlib

def lsd(src, scale=0.8, sigma_scale=0.6, quant=2.0, ang_th=22.5, eps=0.0, density_th=0.7, n_bins=1024, max_grad=255.0):
    """Analyse image with Line Segment Detector.

    Args:
        src (Numpy object) : 2-d grayscale image array (HxW) to analyse.

    Keyword Args:
        scale (double) : Scale the image by Gaussian filter.
        sigma_scale (double) : Sigma for Gaussian filter is computed as sigma = sigma_scale/scale.
        quant (double) : Bound to the quantization error on the gradient norm.
        ang_th (double) : Gradient angle tolerance in degrees.
        eps (double) : Detection threshold, -log10(NFA).
        density_th (double) : Minimal density of region points in rectangle.
        n_bins (int) : Number of bins in pseudo-ordering of gradient modulus.
        max_grad (double) : Gradient modulus in the highest bin. The default value corresponds to the highest gradient modulus on images with gray levels in [0,255].

    Returns:
        A list of line candidates as 5-tuples of (x1, y1, x2, y2, width).
    """
    rows, cols = src.shape
    src = src.reshape(1, rows * cols).tolist()[0]

    lens = len(src)
    src = (ctypes.c_double * lens)(*src)

    with NamedTemporaryFile(prefix='pylsd-', suffix='.ntl.txt', delete=False) as fp:
        fname = fp.name
        fname_bytes = bytes(fp.name) if sys.version_info < (3, 0) else bytes(fp.name, 'utf8')

    lsdlib.lsdGet(src, ctypes.c_int(rows), ctypes.c_int(cols), fname_bytes,
                  ctypes.c_double(scale),
                  ctypes.c_double(sigma_scale),
                  ctypes.c_double(quant),
                  ctypes.c_double(ang_th),
                  ctypes.c_double(eps),
                  ctypes.c_double(density_th),
                  ctypes.c_int(n_bins),
                  ctypes.c_double(max_grad))

    with open(fname, 'r') as fp:
        output = fp.read()
        cnt = output.strip().split(' ')
        count = int(cnt[0])
        dim = int(cnt[1])
        lines = np.array([float(each) for each in cnt[2:]])
        lines = lines.reshape(count, dim)

    os.remove(fname)
    return lines
