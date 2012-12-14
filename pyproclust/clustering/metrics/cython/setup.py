'''
Created on 26/07/2012

@author: victor
'''
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy as np  
setup(
    cmdclass = {'build_ext': build_ext},
    include_dirs = [np.get_include()], 
    ext_modules = [Extension("boundedCohesion", ["boundedCohesion.pyx"],extra_compile_args=["-O3"]),
    Extension("silhouette", ["silhouette.pyx"],extra_compile_args=["-O3"]),
    Extension("meanMinimumDistance", ["meanMinimumDistance.pyx"],extra_compile_args=["-O3"])])