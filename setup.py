from setuptools import setup, find_packages

setup(
    name='NCSA_Manhattan_Plot',
    version='0.1',
    author='NCSA Visual Analytics',
    url='https://github.com/thihanmoekyaw/NCSA_Manhattan_Plot',
    packages=find_packages(),
    python_requires='>=3.9',
    install_requires=[
        'numpy >= 1.22.4',
        'pandas == 1.3.5',
        'plotly.express ==0.4.1',
        'dash >= 2.11',
        'dash_bio',
        'Jupyterlab',
    ],
)