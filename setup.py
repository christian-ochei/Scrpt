from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

ext_modules = [
    Extension(
        r'main',
        [r'main.py']
    ),
]

setup(
    name='main',
    ext_modules=cythonize(ext_modules),
)