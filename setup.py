from setuptools import setup, Extension, find_packages
from Cython.Distutils import build_ext
from Cython.Build import cythonize
import os
from distutils.sysconfig import get_python_lib

os.environ["CC"] = "g++"
os.environ["CXX"] = "g++"

if 'LDFLAGS' in os.environ.keys():
    ldfl=os.environ['LDFLAGS']
    new_ldfl=ldfl.replace('-Wl,-dead_strip_dylibs ','')
    os.environ['LDFLAGS']=new_ldfl


pathtopythonlib=get_python_lib()

extensions=Extension(name="euclidemu2",
                           sources=["src/euclidemu2.pyx","src/cosmo.cxx","src/emulator.cxx"],
                           include_dirs=["/usr/local/include","../src/"],
                           libraries=["gsl","gslcblas"],
                           extra_link_args=['-L/usr/local/lib'],
                           language="c++",
                           extra_compile_args=['-std=c++11',
                                               '-D PRINT_FLAG=0',
                                               '-D PATH_TO_EE2_DATA_FILE="'+pathtopythonlib+'/euclidemu2/ee2_bindata.dat"']
                           )


setup(name='euclidemu2',
      cmdclass={'build_ext': build_ext},
      ext_modules = cythonize(extensions,language_level = 3),
      packages=['euclidemu2'],
      package_dir={'euclidemu2': 'src'},
      package_data={'euclidemu2': ["ee2_bindata.dat","cosmo.h","emulator.h","units_and_constants.h"]},
      include_package_data=True,
      install_requires=['cython','numpy','scipy']
      )
