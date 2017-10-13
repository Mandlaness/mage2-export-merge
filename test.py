import re

text = '''package_contents=<p>The basic Super&nbsp;1050 machine includes the following:</p>
<p>&nbsp;</p>
<table style="" height: 567px;"" border=""1"">
<tbody>
<tr>
<td style=""width: 200px;"">
<ul>
<li>uper 1150 machine</li>
</ul>
</td>
<td>&nbsp;With dies fitted.
<ul>
<li>The Super 1050</li>
</ul>
</td>
</tr>
</tbody>
<table>,second_attribute=something else'''

split_up_pattern = re.compile(r'([^,]{1}[\w_^=]+)=([^=]+)(?:,|$)', re.X|re.M)
    
matches = split_up_pattern.findall(text)

print(matches)

# Start of the string or our ,WORD= pattern.
rgx_spans = re.compile(r'(\A|,)\w+=')

# Get the start-end positions of all matches.
spans = [m.span() for m in rgx_spans.finditer(text)]

# Use those positions to break up the string into parsable chunks.
for i, pos1 in enumerate(spans):
    try:
        pos2 = spans[i + 1]
    except IndexError:
        pos2 = (None, None)

    start = pos1[0]
    end = pos2[0]
    key, val = text[start:end].lstrip(',').split('=', 1)

    print()
    print(pos1, pos2)
    print((key, val))

