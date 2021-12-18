import os

import setuptools
import pythonate._info

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", 'r') as fh:
    requirements = fh.read().splitlines()

setuptools.setup(
    # How you named your package folder (MyLib)
    name=pythonate._info.__package__,
    # Chose the same as "name"
    packages=setuptools.find_packages(),
    # Start with a small number and increase it with every change you make
    version=os.environ["TAG"],
    license='GNU General Public License v3 (GPLv3)',
    # Give a short description about your library
    description="General purpose helper functions and classes for Python3 projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # Type in your name
    author=pythonate._info.__author__,
    # Type in your E-Mail
    author_email=pythonate._info.__author_email__,
    # Provide either the link to your github or to your website
    url=f'https://github.com/{os.environ["GITHUB_REPO"]}',
    download_url=f'https://github.com/{os.environ["GITHUB_REPO"]}/archive/refs/tags/{os.environ["TAG"]}.tar.gz',
    # Keywords that define your package best
    keywords=[
        'Python',
        'Python3',
        'requests',
        'SQL',
        'Dropbox',
        'helper',
        'Google Analytics',
        'sorting',
        'unit conversion',
        'imperial',
        'metric',
        'storage',
        'temperature',
        'enum',
        'random',
        'uuid'
    ],
    install_requires=requirements,
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        # Specify which python versions that you want to support
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Multimedia :: Video',
        'Topic :: Multimedia',
        'Topic :: Internet :: WWW/HTTP',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.7'
)
