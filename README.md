FormatData
==========

Extract data from strings based on string formats

Usage:

    from formatdata import FormatData


    tmpl = 'My name is {name}'
    fd = FormatData(tmpl)
    fd.parse('My name is Glenn') # returns {'name': 'Glenn'}
