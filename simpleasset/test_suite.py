import os
import unittest

import simpleasset


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
        os.unlink("samples/out/hello.txt")

        (fname, text, clas) = simpleasset.process_file("samples/hello.txt.tmpl")
        self.assertEqual(fname, "samples/out/hello.txt")
        self.assertEqual(text, "Hello John Doe!")
        self.assertEqual(clas, "")

        f = open("samples/out/hello.txt")
        self.assertEqual(text, f.read())
        f.close()

    def test_file_baddir_template(self):
        "Test file loader - bad source directory"
        with self.assertRaises(simpleasset.AssetException):
            simpleasset.process_file("verybadsamples/hello.txt.tmpl")

    def test_file_badfile_template(self):
        "Test file loader - file doesn't exist"
        with self.assertRaises(simpleasset.AssetException):
            simpleasset.process_file("samples/file_not_here")


if __name__ == '__main__':
    unittest.main()
