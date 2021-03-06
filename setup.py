#   Copyright (c) 2020 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
setup for paddle-rec.
"""

import os

from setuptools import setup, find_packages
import shutil
import tempfile

requires = ["paddlepaddle == 1.7.2", "PyYAML >= 5.1.1"]

about = {}
about["__title__"] = "paddle-rec"
about["__version__"] = "0.0.2"
about["__description__"] = "paddle-rec"
about["__author__"] = "paddle-dev"
about["__author_email__"] = "paddle-dev@baidu.com"
about["__url__"] = "https://github.com/PaddlePaddle/PaddleRec"

readme = ""


def run_cmd(command):
    assert command is not None and isinstance(command, str)
    return os.popen(command).read().strip()


def build(dirname):
    package_dir = os.path.dirname(os.path.abspath(__file__))
    run_cmd("cp -r {}/* {}".format(package_dir, dirname))
    run_cmd("mkdir {}".format(os.path.join(dirname, "paddlerec")))
    run_cmd("mv {} {}".format(
        os.path.join(dirname, "core"), os.path.join(dirname, "paddlerec")))
    run_cmd("mv {} {}".format(
        os.path.join(dirname, "doc"), os.path.join(dirname, "paddlerec")))
    run_cmd("mv {} {}".format(
        os.path.join(dirname, "models"), os.path.join(dirname, "paddlerec")))
    run_cmd("mv {} {}".format(
        os.path.join(dirname, "tests"), os.path.join(dirname, "paddlerec")))
    run_cmd("mv {} {}".format(
        os.path.join(dirname, "tools"), os.path.join(dirname, "paddlerec")))
    run_cmd("mv {} {}".format(
        os.path.join(dirname, "*.py"), os.path.join(dirname, "paddlerec")))

    packages = find_packages(dirname, include=('paddlerec.*'))
    package_dir = {'': dirname}
    package_data = {}

    models_copy = [
        'data/*.txt', 'data/*/*.txt', '*.yaml', '*.sh', 'tree/*.npy',
        'tree/*.txt', 'data/sample_data/*', 'data/sample_data/train/*',
        'data/sample_data/infer/*', 'data/*/*.csv', 'Criteo_data/*',
        'Criteo_data/sample_data/train/*'
    ]

    engine_copy = ['*/*.sh']
    for package in packages:
        if package.startswith("paddlerec.models."):
            package_data[package] = models_copy
        if package.startswith("paddlerec.core.engine"):
            package_data[package] = engine_copy

    setup(
        name=about["__title__"],
        version=about["__version__"],
        description=about["__description__"],
        long_description=readme,
        author=about["__author__"],
        author_email=about["__author_email__"],
        url=about["__url__"],
        packages=packages,
        package_dir=package_dir,
        package_data=package_data,
        python_requires=">=2.7",
        install_requires=requires,
        zip_safe=False)


dirname = tempfile.mkdtemp()
build(dirname)
shutil.rmtree(dirname)

print('''
\033[32m
  _   _   _   _   _   _   _   _   _
 / \ / \ / \ / \ / \ / \ / \ / \ / \
( P | A | D | D | L | E | - | R | E | C )
 \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/
\033[0m
\033[34m
Installation Complete. Congratulations!
How to use it ? Please visit our webside: https://github.com/PaddlePaddle/PaddleRec
\033[0m
''')
