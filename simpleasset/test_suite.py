"Tests for simpleasset"

import os
import unittest

import simpleasset
from simpleasset.compat import * # pylint: disable=W0401

class AssetIntegration(unittest.TestCase):
    "Basic Integration tests for simpleasset"

    def test_simple_process_template(self):
        "Test processing simple processing"
        (fname, text, clas) = simpleasset.process("hello.txt.tmpl", "Hello {{ name }}!")
        self.assertEqual(fname, "hello.txt")
        self.assertEqual(text, "Hello John Doe!")
        self.assertEqual(clas, "")

    def test_chained_process_template(self):
        "Test processing chained processing"
        (fname, text, clas) = simpleasset.process("hello.txt.tmpl.tmpl", "Hello {{ chain_name }}!")
        self.assertEqual(fname, "hello.txt")
        self.assertEqual(text, "Hello John Doe!")
        self.assertEqual(clas, "")

    def test_file_template(self):
        "Test file loader"
        try:
            os.unlink("samples/out/hello.txt")
        except FileNotFoundError:
            pass

        (fname, text, clas) = simpleasset.process_file("samples/hello.txt.tmpl")
        self.assertEqual(fname, "samples/out/hello.txt")
        self.assertEqual(text, "Hello John Doe!")
        self.assertEqual(clas, "")

        ifl = open("samples/out/hello.txt")
        self.assertEqual(text, ifl.read())
        ifl.close()

    def test_file_baddir_template(self):
        "Test file loader - bad source directory"
        self.assertRaises(simpleasset.AssetException, simpleasset.process_file, "verybadsamples/hello.txt.tmpl")

    def test_file_badfile_template(self):
        "Test file loader - file doesn't exist"
        self.assertRaises(simpleasset.AssetException, simpleasset.process_file, "samples/file_not_here")

    def test_piped_template(self):
        "Test piped processing"
        (fname, text, clas) = simpleasset.process("something.txt.pipetest", "1:2:3\na:b\n")
        self.assertEqual(fname, "something.txt")
        self.assertEqual(text, "1\na\n")
        self.assertEqual(clas, "")

if __name__ == '__main__':
    unittest.main()


