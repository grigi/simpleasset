"Tests for simpleasset"

import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'simpleasset.dj_test_settings'

import simpleasset
from simpleasset.compat import * # pylint: disable=W0401
from simpleasset.match import process_ext

if PYVER < 2.7:
    import unittest2 as unittest
else:
    import unittest

def assertProccesedFile(self, res, oname, nname, fail=False, text=None):
    val = [val for val in res if val[1] == oname]
    self.assertEqual(len(val), 1)
    self.assertEqual(val[0][2], nname)
    self.assertEqual(val[0][0], not fail)

    if text:
        ifl = open(nname)
        self.assertEqual(ifl.read(), text)
        ifl.close()


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
        except OSError:
            pass

        (fname, text, clas) = simpleasset.process_file("samples/hello.txt.tmpl", "samples", "samples/out")
        self.assertEqual(fname, "samples/out/hello.txt")
        self.assertEqual(text, "Hello John Doe!")
        self.assertEqual(clas, "")

        ifl = open("samples/out/hello.txt")
        self.assertEqual(text, ifl.read())
        ifl.close()

    @unittest.expectedFailure
    def test_file_baddir_template(self):
        "Test file loader - bad source directory"
        with self.assertRaises(simpleasset.AssetException):
            simpleasset.process_file("simpleasset/default_config.json", "samples", "samples/out")

    def test_file_badfile_template(self):
        "Test file loader - file doesn't exist"
        with self.assertRaises(simpleasset.AssetException):
            simpleasset.process_file("samples/file_not_here", "samples", "samples/out")

    def test_piped_template(self):
        "Test piped processing"
        (fname, text, clas) = simpleasset.process("something.txt.pipetest", "1:2:3\na:b\n")
        self.assertEqual(fname, "something.txt")
        self.assertEqual(text, "1\na\n")
        self.assertEqual(clas, "")

    def test_process_dir(self):
        "Test directory processing"
        try:
            os.unlink("samples/out/hello.txt")
        except OSError:
            pass

        res = simpleasset.process_dir("samples", "samples/out")
        assertProccesedFile(self, res, "samples/hello.txt.tmpl", "samples/out/hello.txt", text="Hello John Doe!")
        assertProccesedFile(self, res, "samples/one.js", "samples/out/one.js")
        assertProccesedFile(self, res, "samples/two.js.tmpl", "samples/out/two.js")
        assertProccesedFile(self, res, "samples/three.tmpl.renamejs", "samples/out/three.js")

    def test_generic_template_filter(self):
        "Test generic_template_filter"

        (ext, text, clas) = process_ext({"mime": "text/generictemplate"}, None, "Hello {{ name }}!", "")
        self.assertEqual(ext, None)
        self.assertEqual(text, "Hello John Doe!")
        self.assertEqual(clas, "")

    def test_jinja2_filter(self):
        "Test jinja2_filter"

        (ext, text, clas) = process_ext({"mime": "text/jinja2"}, None, "Hello {{ name }}!", "")
        self.assertEqual(ext, None)
        self.assertEqual(text, "Hello John Doe!")
        self.assertEqual(clas, "")

    def test_django_template_filter(self):
        "Test django_template_filter"

        (ext, text, clas) = process_ext({"mime": "text/django"}, None, "Hello {{ name }}!", "")
        self.assertEqual(ext, None)
        self.assertEqual(text, "Hello John Doe!")
        self.assertEqual(clas, "")

if __name__ == '__main__':
    unittest.main()
