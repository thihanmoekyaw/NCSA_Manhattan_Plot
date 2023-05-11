from setuptools import setup, find_packages

setup(
    name='NCSAManhattanPlot',
    version='0.1',
    author='NCSA Visual Analytics',
    url='https://github.com/thihanmoekyaw/NCSA_Manhattan_Plot',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'plotly'
    ],
)