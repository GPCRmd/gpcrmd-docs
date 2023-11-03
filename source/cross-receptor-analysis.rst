=============================
Receptor meta-analysis
=============================

This tool compares frequencies of non-covalent interactions occurring between GPCR residues or GPCRs and their ligands in all available simulated systems. Interaction frequencies have been calculated using GetContacts_, created by Rasmus Fonseca (fonseca.rasmus@gmail.com) and Anthony Ma (anthonyma27@gmail.com). Interaction frequencies are considered as the percentage of simulated time in which a residue pair is interacting, according to the `GetContacts interaction criteria`_. For simulations consisting of more than one trajectory file, the value displayed represents the average across all available trajectories. In addition, simulations have been hierarchically clustered according to their interaction frequency values.

.. contents::
    :depth: 2

Heatmaps and dendrograms
========================

These heatmaps display pre-calculated, non-covalent interaction frequencies (heatmap colour) between pairs of GPCR residues or ligand-residue (columns) in all available simulated systems (rows). To ensure comparability across systems, protein residues are labelled and aligned using `_generic GPCR residue numbers` (GPCRdb structure-based numbering). This numbering system differs for each GPCR class, so a multi-class index has been used on the heatmap's axis. Only interacting pairs with a minimum of 50% interaction frequency in at least one simulation in the dataset are displayed. Same-helix interactions are not displayed. More information from a specific interaction can be displayed by clicking on its cell.

.. image:: _static/heatmap_dend.png

The accompanying dendrogram represents the results of the precomputed hierarchical clustering, with colours identifying the cluster each simulation has been assigned. Dendrograms are generated and displayed using the _plotly python library.

Full dataset options
********************

.. image:: _static/full_dataset_options.png

1. **Simulation datasets**: Include or exclude interactions of simulations submitted by individual contributors, not belonging to GPCRmd.
2. **Interaction type**: Select the type of non-covalent interaction whose frequencies will be displayed in the heatmap.
3. **Interaction partners**: Include interaction frequencies between GPCR residues, residue and ligand or both in the displayed results.
4. **N clusters**: The number of clusters the systems will be classified into and displayed in the dendrogram 
5. **Show reversed residue pairs**: Display each interaction twice in the heatmap, with the order of interacting residue pairs reversed (e.g.: 1x24-7x27 and 7x27-1x24).

After selecting your preferred options, click **Apply** to refresh the page with the new parameters.

Customized dataset
******************

.. image:: _static/custom_dataset.png

Make a new heatmap with only the selected simulations in it. Use the **Select simulations** dropdown to specify your simulation subset, or click their name in the dendrogram. Finally, click apply to reload the metanalysis with only your specified systems. 
Clustering options are not available for customized selections 


About the Top representative interactions in clusters:
======================================================

These plots show the *n* most frequent interactions (on average) in each of the clusters. Interactions are coloured based on the average frequency of the interaction within the cluster, according to the same colour scale as the heatmap.

Such plots were created using FlarePlots_, by Rasmus Fonseca (fonseca.rasmus@gmail.com) and Anthony Ma (anthonyma27@gmail.com).

How to use them:

1. To select a cluster to display, use the dropup on top of each flareplot. Cluster 1 and Cluster 2 are shown by default.
2. To select a position on the flareplot, click on it. If available, this position will be displayed on the structure viewer below.
3. Press "show in structure" to disable or re-enable the visualization of selected positions.

The viewers at the bottom of the page (based on `NGL viewer`_) display each of the simulations present in the cluster selected in the flareplot.

How to use them:

1. Use the top-right dropdown to select the simulation to display. Notice only simulations of the selected cluster are available.
2. Use the top-left dropdown to select the trajectory file of this simulation to display.
3. Press play to reproduce the simulation on the viewer.
4. Click on any position in the flareplot to display it on the corresponding viewer.
5. For a more detailed visualization of this simulation, click on "open with GPCRmd Workbench".


Customized heatmaps
====================
It is possible to analyze only a specified set of simulations using the Customized heatmaps. For that, use the "Select simulations" dropdown to specify the simulations of interest. Simulations can also be selected by clicking on their dendrogram labels. Once the selection is done, click on "Apply".

New plots showing the interactions of the simulations selected are generated. This allows for a more detailed one-to-one comparison of the interaction pattern of such simulations. 

Please consider that a large simulation selection may require a long time to load. 


.. _GetContacts: https://github.com/getcontacts/getcontacts
.. _GetContacts interaction criteria: https://|URLDomain|/contmaps/contmaps/interaction_types
.. _plotly: https://github.com/plotly/plotly.py
.. _Generic GPCR residue numbers: http://docs.gpcrdb.org/generic_numbering.html
.. _FlarePlots: https://github.com/GPCRviz/flareplot
.. _NGL viewer: https://github.com/arose/ngl
