from setuptools import setup, find_packages

setup(
    name='my_minipack',
    version='1.0.0',
    description='Howto create a package in python.',
    url='None',
    author='tsannie',
    author_email="tsannie@student.42.fr",
    license='GPLv3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Students',
        'Topic :: Education',
        'Topic :: HowTo',
        'Topic :: Package',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only'
    ],
    packages=find_packages(),
    install_requires=[],
)
