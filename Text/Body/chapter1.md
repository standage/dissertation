# Chapter 1: Introduction

- NGS: the promise of easy genomes
    - ok, much less $ for data collection
    - new algorithms, software for handling data
    - many genomes have been sequenced that otherwise would not have been
    - NGS genomes are not the same as before, can't be treated the same
    - assembly and annotation are still hard, some basic genome informatics is
      necessary for interpreting annotated genomes
- assess changes/differences in annotations
    - during early stages of project, annotations are preliminary, may
      accumulate annotation versions during initial testing
    - RNA-Seq offers opportunity to improve existing annotations
    - need to be able to compare
        - gene-level resolution necessary to visualize and understand what is
          happening at particular loci
        - also important to summarize the overall amount of change
- assess changes in genome assemblies
    - new algorithms and/or new data --> new assemblies
    - changes may be many or few, minor or severe, depending on algorithms and
      data used; regardless, coordinates of annotations on previous assemblies
      are invalidated
    - local context of man regions will remain unchanged
    - need to identify what has remained constant between assembly versions
- assess differences between species
    - how is the genome similar/different from genomes of related species?
        - gene features (gene length, composition, so on)
        - breakdown (% occupied by conserved genes, % intergentic, so on)
    - identify conserved genes (at least get a lower bound on high-confidence
      orthologs)
- perform quality control
    - gene models within an annotation fall on a wide spectrum of quality
    - filtering by homology and support from experimental data is important
    - high quality genes, even if only a small %, sufficient; more genes is not
      better if gene models are spurious or inaccurate
- reproducibility over time
    - most projects will need continuous refinement
    - however, sometimes you need to report on what you have now
    - maintaining a versioned history of annotations critical for reproducible
      science
    - *ad hoc* conventions, manual archiving difficult to maintain
    - version control software already solves these problems, just need to
      leverage for a domain-specific solution
- organizational framework
    - all of this requires a robust organizational framework
    - genes insufficient; incomplete representation of genome, do not account
      for overlap
    - entire chr/scaff sequences insufficient; impractical computationally, and
      provide insufficient resolution
    - ideal solution:
        - granular
        - representation of the entire genome
        - capture contextual information
- thesis organization
    - chapter 1: introduction, motivation
    - chapter 2: paper wasp genome; provides motivation for principles, shows
      many of them in action
    - chapter 3: ParsEval: comparison of anntotations
    - chapter 4: iLoci: organizational framework, assessing differences between
      species
    - chapter 5: GeneAnnoLogy: quality control and version control for
      reproducibility
    - chapter 6: conclusion
