=============================
Comparative receptor analysis
=============================

.. contents::
    :depth: 2

About the heatmap:
==================

This plot compares residue interaction frequency among several GPCR dynamic simulations.

Interaction frequencies have been calculated with GetContacts_ scripts, created by Rasmus Fonseca (fonseca.rasmus@gmail.com) and Anthony Ma (anthonyma27@gmail.com).

This scripts consider the interaction frequency as the proportion of frames in which a residue pair is considered to be interacting, according to `GetContacts interaction criteria`_.

In base to this frequency values, a dendrogram clustering is computed and displayed using plotly_ python library.

Total interaction frequency reffers to the percentage of frames on which the residue pair is interacting in any of the previous criteria.

Protein residues are labeled using `generic GPCR residue numbers`_ (GPCRdb structure-based numbering). This numbering system differs for each GPCR class, and so a multi-class index has been used on the heatmap's axis.

Only interactions with an average of 10% frequency across all simulations are displayed in plots. Same-helix interactions are not displayed.

How to use this heatmap:

1. Select the type of interaction you want to display in the plot, and click apply to load it.
2. Select the number of clusters to display as colors on the dendrogram
3. Select the interaction partners of the interactions to be displayed by checking the checkboxes
4. Check "Show reversed residue pairs" to display interactions for the reversed residue pair. (Eg: 5x43-7x32 and 7x32-5x43)

More information from a selected interaction can be displayed by clicking uppon its cell.

About the Top5 flareplots:
==========================

On these two plots are represented the 5 most frequent interactions (on average) in each of the clusters.

Each line represents one of the top5 interactions. Its color is based on the average frequency of this interaction in the cluster. The color scale is the same as the heatmap.

All flareplots were created using FlarePlots_, by Rasmus Fonseca (fonseca.rasmus@gmail.com) and Anthony Ma (anthonyma27@gmail.com).

How to use these flareplots:

1. To select a new cluster to display, use the dropup under each flareplot. Cluster 1 and Cluster 2 are shown by default.
2. To select a position on the flareplot, click on it. If avalible, this position will be displayed on the structure visualizer below.
3. Press "show in structure" to disable or reenable the visualization of selected positions.

About the cluster simulation viewers:
=====================================

On these viewers can be visulaized each of the simulations present on the cluster selected in flareplot.

This visualizers run on `NGL viewer`_.

How to use these viewers:

1. Use the top-right dropdown to select the simulation to display. Notice only simulations of the selected cluster are avalible.
2. Use the top-left dropdown to select the trajectory file of this simulation to display.
3. Press play to reproduce the simulation on the viewer.
4. Click on any position in the flareplot to display it on the corresponding protein visualizer.
5. For a more detailed visualization of this simulation, click on "open with GPCRmd viewer".

.. _GetContacts: https://github.com/getcontacts/getcontacts
.. _GetContacts interaction criteria: http://./contmaps/interaction_types
.. _plotly: https://github.com/plotly/plotly.py
.. _Generic GPCR residue numbers: http://docs.gpcrdb.org/generic_numbering.html
.. _FlarePlots: https://github.com/GPCRviz/flareplot
.. _NGL viewer: https://github.com/arose/ngl
