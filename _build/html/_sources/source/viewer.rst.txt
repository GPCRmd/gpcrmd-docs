=============
GPCRmd Viewer
=============


General features
================

Mouse controls:
---------------

* **Left button hold and move**: rotate camera around center.

* **Middle button hold and move**: zoom camera in and out.
* **Middle button click**: center camera on atom.
* **Right button hold and move**: translate camera in screen plane.
* **Left button click**: pick atom or distance.
    * *On click show distance* mode:

        * When an atom is clicked, a label with information about it appears. Click at the background to deselect it, the label will disappear. To maintain a label, double-click on an atom. Double-click on a label to remove it.

        * To draw a distance line between two atoms just single-click one atom after the other. Distances can be removed by double-clicking on one of the atoms at the edges.

        * It is also possible to remove all the atom labels and distances at once, with the **Clear dists. button**.

    * *On click show variants* mode:
        Click on the blue dots to obtain information on known natural variants of a residue. Data obtained from the `ExAC database`_.

    * *On click show mutations* mode:
        Click on the blue dots to obtain information on mutational experiments done on a residue. Data obtained from GPCRdb_.

If you wish to use more complex visualization options, you can open the structure and trajectories in MDsrv_ just by clicking at the gear button.



Selection tools
===============

Quick selection
---------------

Quick-selection buttons allow to rapidly display the molecules present at the dynamics. Hover the buttons with your mouse to see the abbreviated name of these molecules, which can be used to create your own selections.

In the case of Structure selections, It is also possible to select the residues or molecules that are found **within a certain distance of a ligand**. It is only necessary to:

1. Indicate what you want to visualize (residues or molecules found at the simulation).
2. Input the wanted threshold distance (in angstroms).
3. Indicate the molecule type around which the selection is made. Apart from predefined molecules, it is also possible to show the residues/molecules that are close to a personalized selection which, again, can include generic GPCR residue numbering.

If the selection is correct, a green checkmark will appear at the left. More than one distance selection can be displayed at the same time. Selections made with this tool will appear in coral red. The distance selection will be updated for each trajectory frame, as the disposition of the atoms may change.

Custom selection
----------------

Use the text input field to specify your personalized representations. You can choose a representation type (licorice, cartoon, etc.) and a coloring scheme (color by element, by chain, etc.).

Selections must be expressed using the `NGL selection language`_. Moreover, to indicate protein residues it is also possible to use **generic GPCR residue numbering**: Ballesteros-Weinstein (ex. 1.50), GPCRdb structure-based numbering (ex. 1x50) or a combination of both (ex. 1.50x50).

For example, if you input ``40-70:P or CLZ``, residues numbered from 40 to 70 at the PDB belonging to chain P and Clozapine will be displayed. Another example, this time using a combination of different generic GPCR numbering styles, could be ``1.50 - 2x48 or 3.35x35 or SOD``.

Sequence selection
------------------

The GPCR Workbench also provides the option to select a protein segment from its sequence. Set your selection by clicking at the desired range or ranges of residues, selected segments will appear at the sequence in green. To deselect a residue range from the sequence, just click on it. Finally, click at **Confirm selection**: the residue range(s) will be added to a text input field, which you can modify to adjust the selection to what you want to display. If you want to add new sequence selections, click at the plus button.

GPCR conserved positions
------------------------

The **GPCR conserved positions** selection provides the possibility to rapidly select positions or domains conserved in the different GPCR family classes. The GPCR class of the protein being represented will be selected by default, and therefore the conserved positions/domains corresponding to that GPCR class will be available to visualize.

It is also possible to visualize the positions that correspond to conserved positions from other GPCR classes. For example, if your protein belongs to class A, you can represent the residue that corresponds to class B *2.50 (2.50b)*. Hover the buttons with your mouse for more information about the conserved positions and motifs, if available.

.. _MDsrv: http://arose.github.io/mdsrv/
.. _ExAC database: http://exac.broadinstitute.org/
.. _GPCRdb: https://www.gpcrdb.org/
.. _NGL selection language: http://proteinformatics.charite.de/ngl/doc/index.html#User_manual/Usage/Selection_language



.. |more| image:: /_static/more.png
          :align: middle
          :alt: more info