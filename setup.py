from setuptools import setup, find_packages

setup(
    name='desktop-cleanup',
    version='1.0.0',
    description='Automatically organize desktop files by type, date, and size',
    author='wodesha',
    author_email='wodesha@example.com',
    url='https://github.com/wodesha/python-tools',
    packages=find_packages(),
    install_requires=[
        'Pillow>=9.0',
        'watchdog>=2.0',
        'schedule>=1.0',
        'requests>=2.28'
    ],
    entry_points={
        'console_scripts': [
            'desktop-cleanup=cleanup:main',
        ],
    },
)
