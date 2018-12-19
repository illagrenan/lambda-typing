================================
λ :snake: :rocket: Lambda Typing
================================

.. image:: https://img.shields.io/pypi/v/lambda-typing.svg
    :target: https://pypi.python.org/pypi/lambda-typing
    :alt: PyPi

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://pypi.python.org/pypi/lambda-typing/
    :alt: MIT

.. image:: https://img.shields.io/travis/illagrenan/lambda-typing.svg
    :target: https://travis-ci.org/illagrenan/lambda-typing
    :alt: TravisCI

.. image:: https://img.shields.io/coveralls/illagrenan/lambda-typing.svg
    :target: https://coveralls.io/github/illagrenan/lambda-typing?branch=master
    :alt: Coverage

.. image:: https://img.shields.io/pypi/implementation/lambda-typing.svg
    :target: https://pypi.python.org/pypi/django_brotli/
    :alt: Supported Python implementations

.. image:: https://img.shields.io/pypi/pyversions/lambda-typing.svg
    :target: https://pypi.python.org/pypi/django_brotli/
    :alt: Supported Python versions

Introduction
------------

This package contains ``LambdaDict`` and ``LambdaContext`` types for AWS Lambda handler parameters.

Credits: https://gist.github.com/alexcasalboni/a545b68ee164b165a74a20a5fee9d13 :sparkling_heart:

Installation
------------

- Supported Python versions are:  ``3.6`` and ``3.7``.

.. code:: shell

    pip install --upgrade lambda-typing

Usage
-----

.. code:: python

    from lambda_typing.types import LambdaDict, LambdaContext


    def handle_event(event: LambdaDict, context: LambdaContext) -> LambdaDict:
        ...

        return {
            "message": "Foo bar",
            "event": event
        }


License
-------

The MIT License (MIT)
