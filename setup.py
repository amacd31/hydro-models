import numpy as np
from setuptools import setup
import versioneer

from distutils.core import setup, Extension
from Cython.Distutils import build_ext
ext_modules = [Extension(
    "hydromodels.owndata",
    ["hydromodels/owndatamodule.c"],
    include_dirs=[np.get_include()]
)]

cmd_classes = {
    'build_ext': build_ext,
}
cmd_classes.update(versioneer.get_cmdclass())

setup(name='hydromodels',
    version=versioneer.get_version(),
    cmdclass=cmd_classes,
    packages=['hydromodels'],
    install_requires=['cffi>=1.0.0'],
    cffi_modules=["hydromodels/_build.py:ffi"],
    ext_modules=ext_modules,
)
