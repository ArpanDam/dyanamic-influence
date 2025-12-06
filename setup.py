#!/usr/bin/env python
# -*- coding: utf-8 -*-
import setuptools
import os
DISTNAME = 'dynamicgem'

setuptools.setup(
    name='dynamicgem',
    description="A Python library for directional Dynamic Graph Embedding Methods with topics ",
    packages=setuptools.find_packages(exclude=['dataset', 'py-env', 'build', 'dist', 'venv','intermediate','output','dynamicgem.egg-info']),
    package_dir={DISTNAME: 'dynamicgem'},
    setup_requires=['sphinx>=2.1.2'],
    classifiers=[
        "Programming Language :: Python :: 3.6"
       
    ]
)