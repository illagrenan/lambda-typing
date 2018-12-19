# -*- encoding: utf-8 -*-
# ! python3

from unittest import TestCase

from lambda_typing.types import LambdaContext


class DummyTestCase(TestCase):
    def test_dummy(self):
        xx = LambdaContext()
        self.assertTrue(True)
