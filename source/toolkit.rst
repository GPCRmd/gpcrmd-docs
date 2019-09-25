=======
Toolkit
=======

Interaction network (Flare plots)
=================================

If a flare plot is available for the simulation being displayed at the viewer, the option to obtain it will be available at the GPCRmd Toolkit section. Flare Plots are a tool for the study and representation of intra-protein interactions developed at the Stanford University by Dr. Fonseca and Dr Venkatakishnan. This approach makes it possible to obtain a highly visual depiction of complex data, such as the set of interactions formed between protein residues throughout MD simulations, in the form of circular interactive networks named Flare plots. Applied to the study of GPCRs, Flare plots are capable to generate networks which group protein residues according to the helix in which they belong and differentiate interactions between residues of the same helix from inter-helix interactions. Residue-residue interactions are represented as lines connecting residue pairs. Hover or click a residue to highligh the lines representing the interactions in which it participates.

There are several options available

* **Interacion type**: Select the type of interaciton to display on the plot.
* **Display**:
    * **Interacting pairs**:Show only a subset of interactions (intra- or inter-helix) or all of them.
    * **Simulation**: It is possible to summarize the interactions formed through all the trajectory frames. The frequency of each interaction is represented by the thickness of the lines connecting residues.
* **Show in structure**: Click to display structural representations of the residues selected (clicked) at the flare plot plot. Unclick to hyde them. If there are no residues selected at the flare plot, nothing will happen.
* **Clear plot**: Click to delete all selections made on the plot.
* **Download data**: Click to download the plot data.

Hbond frequency
===============

This tool identifies Hydrogen Bonds formed in a simulation, splitting the results between protein-protein hydrogen bonds and protein-not protein bonds. We use the MDTraj module function called **"wernet_wilson"** , which basically stablishes a threshold distance of 3.3 Angstroms between the donor and acceptor atoms; more concretely, this threshold becomes progressively stricter as the angle formed by H-D-A increases (a perfect straight bond is 0 degrees, as the donor atom is central). You can select between a few options:

1. **Do not include Hbonds between neighbours**: If selected, excludes hydrogen bonds among residues which are less than 5 residues apart. These are usually the hydrogen bonds stabilizing alpha helices.
2. **Include backbone Hydrogen Bonds**: If selected, includes hydrogen bonds formed between backbone (BB) atoms or side chains (SC) atoms, in any combination (SC-SC,BB-BB,SC-BB).
3. **Only Side Chain Hydrogen Bonds**: If selected, only includes hydrogen bonds formed between side chain atoms.

Finally, you can set a frequency threshold so only those hydrogen bonds which hold the cited condition in a proportion of the frames greater than the value you have set will appear in the results. You can also define an interval of frames into which perform the analysis. 

Results have a "Show Hbond" button next to them which displays the bond in the viewer. At the end of the results table, you can find a "Show All" button, which displays all the bonds in that table at once.

Lig-prot interaction frequency
==============================

This analysis tool calculates the frequency of interaction between the protein residues and a given ligand across a trajectory. When the distance between any of their atoms and the ligand is smaller than the threshold, it is considered to be an interaction. It is possible to chose which residue atoms will be considered (heavy atoms only or all atoms). The result is presented as table and a plot, which can be downloaded as an image. The residues that are found to interact can be displayed at the viewer screen (shown in purple), which can be deactivated using the "Display interacting residues" checkbox. It is also possible to download the interaction data obtained.

Salt bridge frequency
=====================

This tool allows you to identify the salt bridges formed through a simulation. Salt bridges are defined as any combination between these two sets: {Arg-NH1, Arg-NH2, Lys-NZ, His-NE2, His-ND1} and {Glu-OE1, Glu-OE2, Asp-OD1, Asp-OD2} in which the participating atoms are closer than 4 Angstroms. Histidine atoms are only considered if the residue is protonated. As with hydrogen bond analysis, you can select a percentage threshold, and the results include a "Show Salt Bridge" button and a "Show All" button. Furthermore, you can select an interval of frames, instead of the whole trajectory.

Distance progression
====================

This tool is used to calculate the distance between atom pairs across the different frames of a trajectory, and therefore across time. To calculate a distance, you need to indicate the pair or pairs of atoms you are interested in. This can be done in different ways:

* Select a pair of atoms at the viewer screen by clicking on them and, afterwards, **importing the created distances** with the blue arrow button.
* Indicate the desired atom pairs manually, by selecting "Compute distance between" **atoms** and inputting a pair of atom indices at the text input fields.
* Indicate the desired atom pairs manually, by selecting "Compute distance between" **residues** and indicating the residue, chain and atom name you are interested in. The residue number and chain name must be indicated according to the NGL selection language (ex. 50:P), and the atom name selected from the droplist.

It is also necessary to select the trajectory that will be used for the calculation. 
Finally, just click at **Compute**. Only atom pairs which are marked with a green checkmark will be considered, since the absence of a checkmark indicates an error in the input (only numbers are allowed). The result will appear as a plot of distance by time or by frame, which can be downloaded as an image. It is also possible to download the data obtained as a csv file. Moreover, the distances calculated can be displayed at the viewer screen, in the colors indicated at the plot legend. Such distance representations can be deactivated by deselecting the "Display distance" checkbox.

RMSD progression
================

This tool computes the RMSD of all the conformations in a target trajectory to a reference conformation. It is necessary to indicate the trajectory to be used and the frames to be considered. Also, a reference frame of a given trajectory. It is possible to chose which atoms are going to be considered in the calculation: only alpha carbons, non-hydrogen protein atoms, protein C-alpha, etc. As in the case of distance analysis, the result will be shown in a plot (RMSD by time or by frame). It is possible to download the plot as an image or all the obtained data as a csv file.