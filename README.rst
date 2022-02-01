========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |coveralls| |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/pybtipay/badge/?style=flat
    :target: https://pybtipay.readthedocs.io/
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.com/rolisz/pybtipay.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.com/github/rolisz/pybtipay

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/rolisz/pybtipay?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/rolisz/pybtipay

.. |requires| image:: https://requires.io/github/rolisz/pybtipay/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/rolisz/pybtipay/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/rolisz/pybtipay/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/rolisz/pybtipay

.. |codecov| image:: https://codecov.io/gh/rolisz/pybtipay/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/rolisz/pybtipay

.. |version| image:: https://img.shields.io/pypi/v/btipay.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/btipay

.. |wheel| image:: https://img.shields.io/pypi/wheel/btipay.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/btipay

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/btipay.svg
    :alt: Supported versions
    :target: https://pypi.org/project/btipay

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/btipay.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/btipay

.. |commits-since| image:: https://img.shields.io/github/commits-since/rolisz/pybtipay/v0.0.4.svg
    :alt: Commits since latest release
    :target: https://github.com/rolisz/pybtipay/compare/v0.0.4...master



.. end-badges

Python package for using the Banca Transilvania iPay API.

* Free software: MIT license

Installation
============

::

    pip install btipay

You can also install the in-development version with::

    pip install https://github.com/rolisz/pybtipay/archive/master.zip


Documentation
=============


https://pybtipay.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox


Deployment to Pypi
==================
Run `tbump new_version`, `python -m build`, `twine check` and then `twine upload dist/*`.
