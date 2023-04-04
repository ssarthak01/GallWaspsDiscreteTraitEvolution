# GallWaspsDiscreteTraitEvolution
EBIO 4290/5290 Final Project: Evolution of Number of Gall Chambers in Association to Gall Location


Plan of Execution:
1) reformat orginal nexus data file into MrBayes compatible nexus file
2) build trait dataset from paper (focusing on number of gall chambers and gall location)
3) build bayesian trees -> param sweeps and try to optimize the posterior probabilities of the clades to match bootstraps of paper
4) discrete trait analysis 
5) congregate results


Project Organization:

GallWaspsDiscreteTraitEvolution

  PhylogeneticsFinalProject
  
    enumerate.py (python script to convert between PAUP nexus files -> MrBayes nexus files 
    
    GallWasps_Morph.nex (this is the orginal dataset with MrBayes nexus compatibility)
    
    MrBayesManual.pdf (manual from MrBayes documentation)
    
    GallWaspsMorphologyORGINAL.nex (original PAUP compatible nexus data file)
    
    MrBayesRun.txt (initial log output of MrBayes compatible data)
    
    test.txt (contains the alphabetic character sequences for original morphology dataset)
    
