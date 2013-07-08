import unittest

import formatdata


class TestFormatData(unittest.TestCase):

    def test_feature(self):
        ctx = {'name': 'Mr. Foo Bar', 'age': '100'}
        tmpl = 'my name is {name} and I am {age} years old'
        fd = formatdata.FormatData(tmpl)
        data = fd.parse(tmpl.format(**ctx))
        self.assertEqual(data, ctx)


if __name__ == '__main__':
    unittest.main()
