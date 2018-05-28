'''
Install script for macOS
'''

import os

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))

ROOT_DIR = f'{SCRIPT_DIR}/..'

BUILD_DIR = f'{ROOT_DIR}/build'

OPENSSL_ROOT_DIR = '/usr/local/Cellar/openssl/1.0.2o_1'

OPENSSL_INCLUDE_DIR = f'{OPENSSL_ROOT_DIR}/include'

os.system(f'rm -r {BUILD_DIR} && '
    f'mkdir {BUILD_DIR} && '
    f'cd {BUILD_DIR} && '
    f'cmake -DOPENSSL_ROOT_DIR={OPENSSL_ROOT_DIR} -DOPENSSL_INCLUDE_DIR={OPENSSL_INCLUDE_DIR} .. && '
    'make && make install'
    )
