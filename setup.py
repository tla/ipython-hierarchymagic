from setuptools import setup

setup(name='ipython-hierarchymagic',
      version='0.1',
      description='Magic extensions for Jupyter notebooks',
      url='https://github.com/tkf/ipython-hierarchymagic/',
      author='Takafumi Arakaki',
      author_email='aka.tkf@gmail.com',
      license='BSD',
      packages=['hierarchymagic'],
      install_requires=['sphinx'])