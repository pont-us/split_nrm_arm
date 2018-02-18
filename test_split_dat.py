#!/usr/bin/env python3

from unittest import TestCase
import split_dat


class TestSplitDat(TestCase):

    def test_split(self):
        lines = [
            "Line zero", "one", "two",
            "three ARM axial blah"
            "four", "five", "six"
        ]

        chunks = split_dat.split(lines)
        self.assertEquals(2, len(chunks))
        self.assertEquals(lines, chunks[0] + chunks[1][1:])
        self.assertEquals(lines[0:3], chunks[0])
        self.assertEquals([lines[0]] + lines[3:], chunks[1])
