SHELL:=bash

FrontMatter=Text/Preface/abstract.tex \
            Text/Preface/acknowl.tex \
            Text/Preface/dedication.tex \
            Text/Preface/titlepage.tex

Chapters=Text/Body/chapter1.tex \
         Text/Body/chapter2.tex \
         Text/Body/chapter3.tex \
         Text/Body/chapter4.tex \
         Text/Body/chapter5.tex \
         Text/Body/chapter6.tex

Appendices=Text/Appendix/appendix1.tex \
           Text/Appendix/appendix2.tex

Bibliography=Reference/bibtex.tex \
             Reference/mybib.bib

Graphics=Assets/Graphics/dc5.jpg

all: thesis.pdf

thesis.pdf: thesis.tex $(FrontMatter) $(Chapters) $(Appendices) $(Bibliography)
	pdflatex thesis
	bibtex thesis
	pdflatex thesis
	pdflatex thesis

clean:
	rm -f $$(cat .gitignore)
