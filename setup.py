#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup


# https://github.com/pypa/setuptools_scm
use_scm = {"write_to": "ortho_view_napari/_version.py"}
setup(
      use_scm_version=use_scm,
      entry_points={'napari.plugin': 'OtherView = ortho_view_napari'},
)
