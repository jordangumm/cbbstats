import os

from distutils.core              import setup
from distutils.command.build_py  import build_py
from pathlib                     import Path
from setuptools.command.install  import install
from setuptools.command.develop  import develop
from setuptools.command.egg_info import egg_info
from subprocess                  import run


class my_build_py(build_py):
    def run(self):
        if not self.dry_run:
            if not os.path.exists(Path.home() / '.kaggle/kaggle.json'):
                raise OSError('Kaggle API Credentials Not Found\nhttps://github.com/Kaggle/kaggle-api')
            projectpath = Path(__file__).resolve().parent
            targetpath  = Path(os.path.join(self.build_lib, 'cbbstats/data')).resolve()

            run([f'{projectpath}/build.sh', str(targetpath)])

        build_py.run(self)


class CustomInstallCommand(install):
    def run(self):
        install.run(self)
        my_build_py()


class CustomDevelopCommand(develop):
    def run(self):
        develop.run(self)
        my_build_py()


class CustomEggInfoCommand(egg_info):
    def run(self):
        egg_info.run(self)
        my_build_py()


setup(name='cbbstats',
      description='College basketball statistics generator and interface',
      author='Jordan Gumm',
      author_email='jordan@variantanalytics.com',
      packages=['cbbstats'],
      cmdclass={'build_py': my_build_py}
)
