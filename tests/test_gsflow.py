#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `gsflow` package."""
from gsflow import Gsflow
import unittest
from gsflow import gsflow


class TestGsflow(unittest.TestCase):
    """Tests for `gsflow` package."""
    def test_load_data_set(self):
        control_file = r"D:\Workspace\bin\gsflowv1_2_1\GSFLOW_1.2.1\data\sagehen\windows\gsflow.control"
        gs = Gsflow(control_file=control_file)

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

if __name__ == "__main__":
    unittest.main()
