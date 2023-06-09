# GallWaspsDiscreteTraitEvolution
EBIO 4290/5290 Final Project: Evolution of Number of Gall Chambers in Association to Gall Location

Author: Shukla, Sarthak

Intro:

What are gall wasps? Insects, Cynipidae, that inject their eggs into plant tissues resulting in the host plant forming an external structure around the larvae, known as a gall. The gall acts as a protective layer for the larvae and is their source of nutrients. Moreover, the gall is created from the plant tissue itself. Gall structure varies across all Cynipidae and some of these differences include: complexity, number of chambers, attachment form, and location of the galls. Due to the fact that the larvae are extremely dependent on the gall for nutrition, it seems that the location of the gall will influence the the nutritional value of the gall and therefore influence the gall structure. Thus, I hypothesize that galls located on reproductive areas of the plant will present as mutli-chambered galls and locations on vegetative areas will present as single-chambered galls.

Methods & Materials: 

a) Phylogenetic Inference: 
 - Convert existing morphological nexus data on gall wasps to be executable in MrBayes: this required taking 41 character sequences for 41 taxa with each sequence containing 175 morphological characters and converting character encodings to be compatiable with MrBayes software
 - MrBayes software used to generate Baysesian consensus tree and generate 1000 Baysesian trees from the highest likelihood scored MCMC run: used an equal rates model with gamma distribution parameter estimation along with MCMC analysis over 2 runs with with 100,000 generations each and sampling 100 generations at a time and discarding the first 25% of runs. 
 - Taxa Selection: ![Screenshot](ReadME_images/TaxaSelection.png)
 
b) Comparative Biology Methods:
 - Created character data matrix using the data collected in a study by Ronquist et al
 -  Trait Data matrix: Transcribed the data attributes described in paper to Mesquite software character Matrix ![Screenshot](ReadME_images/TraitMatrix.png)
 -  Built a mirror tree: Used a mirror tree to map correlated traits with respective colors in Mesquite using parsimony-based ancestral state mapping and the previously created character matrix
 -  Running Pagel Tests: Pagel tests are means of measuring correlation between discrete traits and I specifically used Omnibus, Contingent Changes, and Temporal Order Tests in the software BayesTraitsV4 with the 1000 Bayesian trees, the Bayesian consensus tree along with the trait data matrix created in Mesquite ![Screenshot](ReadME_images/Illustrated8RateDependentModel.png)

Results:

- Baysesian Consensus Tree: ![Screenshot](ReadME_images/ConTree.png)
- Corrrelated Traits Visualized on Mirror Tree: ![Screenshot](ReadME_images/MirrorTree.png)
- Table of Pagel Tests results using trait data matrix and Bayesian consensus tree: ![Screenshot](ReadME_images/ConTreeTable.png)
- Table of Pagel Tests results using trait data matrix and 1000B Bayesian tree: ![Screenshot](ReadME_images/1000TreesTable.png)

Discussion:

Please read the paper in the root directory for a full brief on the study!




 
