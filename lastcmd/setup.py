from setuptools import setup

setup(
    name='lastcmd',
    version='0.1.0',
    py_modules=['lastcmd'],
    entry_points={
        'console_scripts': [
            'lastcmd=lastcmd:get_last_command',
        ],
    },
    description='Print the last command run in your shell',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
