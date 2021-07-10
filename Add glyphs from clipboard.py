#MenuTitle: Add glyphs from clipboard
# -*- coding: utf-8 -*-

__doc__="""
Copy any text and “paste” them into your character set with this script. `pip install pyperclip` from Terminal to enable the script to access the macOS clipboard.
"""

import subprocess

Glyphs.clearLog()

# Get clipboard text
p = subprocess.Popen(['pbpaste', 'r'],
	stdout=subprocess.PIPE, close_fds=True)
stdout, stderr = p.communicate()
paste = stdout.decode('utf-8', errors='ignore')

# Make a sorted list of all characters present in clipboard text
chars = sorted(list(set(paste)))

# Control characters to skip
omitCodes = list(range(0x0000, 0x001f+1)) + list(range(0x007f, 0x009f+1))

glyphCountBefore = len(Glyphs.font.glyphs)
report = "Added {} glyphs from clipboard:\n"
for char in chars:

	# Skip control characters
	if ord(char) in omitCodes:
		continue

	# Add characters not already present in font
	if char not in Glyphs.font.glyphs:
		newGlyph = GSGlyph(char)
		if newGlyph.name not in Glyphs.font.glyphs:
			Glyphs.font.glyphs.append(newGlyph)
			report += newGlyph.name + " "

# Print report
glyphCountAfter = len(Glyphs.font.glyphs)
print(report.format(glyphCountAfter - glyphCountBefore))