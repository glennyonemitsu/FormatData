import re
import string


class FormatData(object):

    def __init__(self, template):
        self.template = template
        self.formatter = string.Formatter()
        self.tokens = self.formatter.parse(self.template)
        regex = ''
        for t in self.tokens:
            regex += t[0]
            if t[1]:
                regex += '(?P<{}>[\w\s.]+)'.format(t[1])
        self.regex = re.compile(regex)

    def parse(self, string):
        result = self.regex.match(string)
        return {} if result is None else result.groupdict()

