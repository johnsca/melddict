# Copyright 2016 Canonical Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.

from pathlib import Path
from setuptools import setup, find_packages

here = Path(__file__).absolute().parent
readme = here / 'docs' / 'readme.rst'
changelog = here / 'docs' / 'changelog.rst'
long_description = '{}\n\n{}'.format(
    readme.read_text(),
    changelog.read_text()
)
version = here / 'VERSION'

setup(
    name='melddict',
    version=version.read_text().strip(),
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=[],
    include_package_data=True,
    maintainer='Cory Johns',
    maintainer_email='johnsca@gmail.com',
    description=('Dictionary with recursive additive and subtractive merging'),
    long_description=long_description,
    url='https://github.com/johnsca/melddict',
    license='Apache 2',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
    ],
)
