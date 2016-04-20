# Dissertation revisions

## iLocus Chapter: Abstract

> The committee passed the defense on condition that an abstract be provided for the iLocus chapter.
> The abstract is provided below.

**Background**:
The rate at which new draft genome sequences and corresponding annotations are being produced outpaces the scientific community's capacity to refine these drafts into "finished" reference-quality data resources.
Scientists must be able to evaluate newly sequenced genomes in the context of previously published data, requiring summaries of genome content that can be quickly computed and meaningfully compared without the support of a large model organism research community.
As annotation quality will necessarily vary within and across data sets, the ability to select subsets of only those data that are well supported is critical for distinguishing technical artifacts from biological effects.

**Results:**
We introduce a new framework for genome analyses based on parsing an annotated genome assembly into distinct *interval loci (iLoci)*.
We demonstrate that iLoci provide an alternative coordinate system that is robust to changes in assemblies and annotations, and facilitates granular quality control of genome data.
We discuss how statistics computed on iLoci reflect various characteristics of genome content and organization, and illustrate how this can be used to establish a baseline context for evaluating a new genome assembly and annotation.
We also introduce a well-defined measure of relative genome compactness, and more generally show how iLoci reveal the extent of gene clustering genome wide.

**Conclusions:**
The iLocus framework, available as open source software as part of the AEGeAn Toolkit (https://brendelgroup.github.io/AEGeAn), provides a comprehensive solution to common challenges in annotation and analysis of non-model genomes.


## iLocus Chapter: Applications

> The committee passed the defense on condition that the iLocus chapter makes applications of the iLocus work more clear.
> A couple of committee members even suggested this may be as simple as adding a table listing potential applications.
> This is already in the text to some extent, and is something we'll want to be sure and highlight better for the paper submission, but for now I just need to make these applications come across more clearly.

Pending.

## iLocus Chapter: Classifications

> *From Karin.*
>
> Fig. 4.2 needs to clearly state the precise flavor of each type of iloci for each segment.
> You tell us the fiLoi, iiLoci, and giLoci, but what about siLoci vs. ciLoci.
> Statements elsewhere (possibly in your presentation) have me confused: Can a siLocus have multiple isophorms or not?

I didn't realize I had misspoken during my presentation.
A siLocus can indeed contain multiple isoforms, just not overlapping genes.
I have corrected the Figure 4.2 caption to be more specific:

**Parsing an annotated genome sequence into iLoci. The letters A to J indicate 10 adjacent iLoci on the genomic sequence (central horizontal line), separated by the long vertical bars. Gene annotations are shown underneath the genome sequence. Exons are schematized by horizontal lines, introns by the triangular thin lines below. Arrows indicate transcriptional direction. iLoci A, C, E, G, and J are without gene annotation, with A and J representing potentially incomplete genomic fragments (fiLoci), and C, E, and G representing intergenic regions (iiLoci). siLoci contain a single gene annotation each and include genes with a single annotated transcript (B, H, and I) as well as genes with alternative transcripts (D). ciLocus F contains three distinct, but overlapping genes. The boundaries of the gene-containing iLoci (giLoci) are derived from the annotation ends, extended in each direction by δ. An exception occurs between iLoci H and I, where the extension would result in an iiLocus shorter than δ: in this case, the bordering iLoci (H and I) are extended towards each other to fill the entire space.**

> *Again, from Karin.*
>
> Fig. 4.1 makes some assumptions, like a giLocus is either protein-encoding or it is not.
> What if it is a ciLocus and has both protein and non-protein coding genes?
> niLoci cannot be ciLoci?
> There is a similar problem with your definition of FF, RR, FR, and RF iiLoci much later.
> You act as if all transcripts in a giLocus agree on direction, but your examples demonstrate this may not be so for ciLoci.
> Are you ignoring iiLoci bound by ciLoci?
> I know ciLoci are rare, but a computer scientist needs to be precise on these details because you never know what complex biology lies in your program's future.

I have now clarified this in a few places in the text.
Regarding orientation of iiLocus flanks: I clarified that when an iiLocus is bounded on one or both sides by ciLoci, the orientation of gene models directly flanking the iiLocus are reported.
Regarding the non-coding vs protein-coding issue, protein-coding genes and non-coding RNA genes are not grouped together in the same iLoci.
ncRNA genes do occasionally overlap, but we have no terminology to distinguish these cases from single ncRNA genes like we do with siLoci vs ciLoci (it's easy enough to distinguish in the output data, however).
I tried to clarify this in the text as well.

## iLocus Chapter: Algorithm vs Implementation

> *From Karin.*
>
> p. 64 "Operational definition of iLoci," the algorithm, and "Implementation" seem to contradict each other somewhat.
> I now think the algorithms have only minor problems (I misunderstood something ealier), but I don't see the advantage to presenting the algorithm one way when it is implemented another...In a statistical bioinformatics paper, we often have a model section, where we set up the conceptual ideas and model, and a methods section where we discuss the gory implementation details, datasets, and how we particularly chose to implement the model.
> I think iLocus is your model, and δ and other details are you methods.

The current presentation was intentional, and was my attempt to distinguish the abstract mathematical concept of an iLocus (still operationally defined) from our particular implementation. The AEGeAn library/programs are influenced heavily by the GenomeTools library upon which they depend: GenomeTools conventions are the primary reason I went with the streaming approach. I would probably end up implementing it quite differently if I wanted to create, for example, a Python script that provides a more intuitive exposition of the concepts. I would be less concerned about memory efficiency, slurp up all the data into memory, iterate over the genes one-by-one, use overlap queries (an interval tree) to find overlapping genes, and build iLoci that way.

So I think the current algorithm/operational description does a better job of capturing what the iLoci represent, while the implementation description describes how we implemented it in a particular open source framework. Whether this matches the model/implementation pattern described is up for debate I guess, but I definitely see common elements and motivations.

> *S* is an assembled piece of genome?  (I'm not sure what you mean by "genomic sequence")

Clarified as follows. **Computing iLoci for an assembled contig/scaffold/pseudo-chromosome S depends on a set of intervals G (corresponding to gene models annotated on S) and an extension parameter δ.**

> *G* and *L* are just sets of intervals, the only difference being that *G* are genes and *L* are the union of sets of genes?

Yes. G corresponds to provided gene models, and L corresponds to our resulting parsing of the genome.

> dist(locm, locn) is a non-standard distance since locm and lon are not points.  It's a minor point, but precision is nice.

Fair point. I thought about replacing dist() with something like sep(), to avoid confusion. But I think that's unnecessary as long as I am more explicit about what dist() is.
Clarified (along with comments about additional extensions not being "marginal") as follows: **...if the number of nucleotides separating the two intervals dist(loc_m, loc_n) > 3 δ$ nucleotides, then loc_m and loc_n will be extended toward each other by δ nucleotides, each designated as a giLocus, and the remaining space between them will be designated as an iiLocus;
+if 2δ < dist(loc_m, loc_n) ≤ 3δ, then loc_m and loc_n are extended toward each other equally until they meet, with extensions potentially as long as 1.5δ, to prevent annotating an extremely short iiLocus...**

> the algorithms suggest an unordered traversal of G, but implementation states it is ordered by location along the scaffold/contig

Again this gets at the intended separation of the abstract concept vs our implementation.

> In OVERLAP(), you shouldn't bother examining marked g', right?

In the AEGeAn implementation, I don't mark and check due to the way the ordered genes are accumulated and grouped. In a generic implementation, where an unordered traversal of G is possible, you need to make sure you don't create multiple copies of each ciLocus. Some check would therefore be necessary.

> The algorithm, as written, is inefficient.  Even the implementation is inefficient.  All you need to check is whether the current rightmost position of the locus exceeds the leftmost position of the next gene.  You do not need to check all genes in the buffer for overlap.


Perfectly right here. I had a bug in an older version of the software where I simply checked the last gene in the buffer, which doesn't necessarily contain the rightmost nucleotide in the buffer. I went with the naive brute-force solution to just check all genes in the buffer, but the proposed solution is not only more efficient but more concise to describe. I've opened up a ticket to fix this in the software (although to be honest I don't expect a huge performance benefit), and I've clarified the text as follows. **Initially, the node stream will collect a single gene feature from the input and store it in a buffer. Then, as subsequent gene features are collected, they are tested for overlap with the current iLocus (buffer) and accumulated as long as their leftmost position is less than or equal to the rightmost position of the buffer. When the node stream encounters a gene feature that does not overlap with the buffer, a giLocus feature is created, all the genes in the buffer are assigned as children to the giLocus, a reference to the giLocus is stored temporarily in the node stream, and the giLocus is emitted for further processing or storage.**

> Beware, the average of two integers may not be an integer (Algorithm 2).

I updated the algorithm to make it clear that the floor of the average is taken.

## iLocus Chapter: Miscellaneous

> *From Karin.*
>
> p. 68, 3rd paragraph is not clear.  What is the problem each script is solving?  What does the user need to know about this, really?  I think I understand it, but only after several read-throughs.

This is getting into some pretty technical and scientifically uninteresting nitty-gritty.
I feel obliged to describe this in the manuscript for full disclosure, and have therefore moved discussion of these details to the supplement where I can devote a bit more space and attention to making this clear.

> I think it is important for you to define how you will use the GFF3 format to communicate iLocus information.
> Establishing some standards will be a useful contribution of this work.

A detailed description of how GFF3 is used, both in input and output, has been added to the iLocus chapter/paper supplement.

> p. 71. Why a costly simulation when you can test goodness of fit to a Geometric distribution.

We are looking into this, but it will require additional time to investigate.
For now, random arrangements of genes are clearly distinct from annotated arrangements, and I'll let this methods and results stand until such as time as we are able to model this more directly, as suggested here.
