import os

import setuptools
import pythonate._info as info

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", 'r') as fh:
    requirements = fh.read().splitlines()

setuptools.setup(
    name=info.__package__,
    packages=setuptools.find_packages(),
    version=info.__version__,
    license='GNU General Public License v3 (GPLv3)',
    description="General purpose helper functions and classes for Python3 projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=info.__author__,
    author_email=info.__author_email__,
    url=f'https://github.com/{os.environ["GITHUB_REPO"]}',
    download_url=f'https://github.com/{os.environ["GITHUB_REPO"]}/archive/refs/tags/{os.environ["TAG"]}.tar.gz',
    keywords=[
        'Python',
        'Python3',
        'requests',
        'SQL',
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
