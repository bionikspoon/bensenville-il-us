#!/usr/bin/env python
# coding=utf-8

"""
test_bensenville-il-us
----------------------------------

Tests for `bensenville-il-us` module.
"""
import pytest


@pytest.fixture
def bensenville-il-us():
    from bensenville-il-us import bensenville-il-us

    mock_bensenville-il-us = bensenville-il-us()
    return mock_bensenville-il-us

def test_bensenville-il-us_properly_mocked(bensenville-il-us):

    assert str(bensenville-il-us) == "Success"