#!/usr/bin/env python

# Daniel Standage (2016-03-19)
# Prerequisites
#   - ImageMagick (convert command)
#   - Poppler (pdfunite command)
# Installation on Mac OS X: `brew install imagemagick poppler`

# The subprocess module's `check_call` command is similar to Perl's `system`
# command, except that it will abort the script immediately on a non-zero
# return status.
import subprocess

# Figure numbering is inferred from the order here.
# This way we can give the files descriptive names instead of having to be
# constantly renaming the files when figures are added or removed.
# This doesn't free us from ensuring that these filenames stay in sync with
# the figure captions in the LaTeX document, though.
figures = [
    ['ilocus-designations.png'],
    ['ilocus-demo.pdf'],
    ['modorg-silocus-length.png'],
    ['modorg-pilocus-exoncount.png'],
    ['modorg-intron-length.png'],
    ['modorg-exon-length.png'],
    ['modorg-milocus-length.png'],
    ['modorg-compactness.png'],
    ['modorg-iilocus-length.png'],
    ['atha-stable.png', 'amel-stable.png'],
    ['atha-stable-scatter.png', 'amel-stable-scatter.png'],
    ['algae-bd-counts.png', 'algae-bd-bp.png'],
    ['crei-breakdown-scatter.png'],
]

pdfs = list()
for i, fig in enumerate(figures):
    outfilename = 'figure-{}.pdf'.format(i + 1)
    pdfs.append(outfilename)
    if len(fig) > 1:
        command = ['convert'] + fig + ['-adjoin', outfilename]
    else:
        infile = fig[0]
        if infile.endswith('.png'):
            command = ['convert', infile, outfilename]
        else:
            command = ['cp', infile, outfilename]
    subprocess.check_call(command)

command = ['pdfunite'] + pdfs + ['figures.pdf']
subprocess.check_call(command)
