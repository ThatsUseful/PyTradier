#!/usr/bin/env python3

from distutils.core import setup

# requirements
with open('requirements.txt') as requirements:
    req = [i.strip() for i in requirements]

setup(name='com.thatsuseful.PyTradier',
      version='0.1.0',
      description='Tradier API wrappers',
      author='R Leonard',      
      author_email='rleonard@unknown.com',
      maintainer='Scott Rutherford',
      maintainer_email='scott@thatsuseful.com',
      url='https://github.com/thatsuseful/PyTradier',
      license='GPLv3',
      packages=['PyTradier'],
      package_dir={'PyTradier':'PyTradier'},
      install_requires=req,
      platforms=['any'],
      keywords=['tradier', 'options', 'stocks', 'thatsuseful'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: Financial and Insurance Industry',
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
          'Natural Language :: English',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Topic :: Software Development :: Libraries'
          ]
     )
