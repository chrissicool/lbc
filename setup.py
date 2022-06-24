from setuptools import setup, find_packages

setup(
    name='lbc',
    version='1.0.0',
    url='https://github.com/chrissicool/lbc',
    author='Christian Ludwig',
    author_email='cludwig@genua.de',
    description='A static lock balancing checker for the OpenBSD kernel',
    license='ISC',
    packages=find_packages(),
    install_requires=['pycparserext'],
    scripts=['lbc'],
)
