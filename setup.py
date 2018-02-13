from setuptools import setup
import versioneer

setup(name='hydromodels',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=['hydromodels'],
    install_requires=['cffi>=1.0.0'],
    cffi_modules=["hydromodels/_build.py:ffi"],
)
