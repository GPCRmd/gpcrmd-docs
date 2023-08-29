==================
Simulation Browser
==================

.. contents::
    :depth: 2

The simulation browser system is found on the `Simulations` option:

* Family tree
* GPCRmd simulations
* Search

.. image:: _static/search_option.png
  :width: 600
  :alt: GPCRmd search option

-----------
Family tree
-----------

The Family tree is a visual representation of each GPCR family and subfamily ending on a pdb identifier. 

.. image:: _static/family_tree.png
  :width: 600
  :alt: GPCRmd family tree

The user can zoom in/out and drag around the tree. If the user hover on each pdb identifier the graph will display a box with all the simulations related to this code: 

.. image:: _static/family_tree_display.png
  :width: 600
  :alt: GPCRmd family tree display

Clicking in the blue link the user will be redirected to the GPCRmd viewer. In case that the user wants to restore the position, only need to click on the button "Reset view" on the box next to the tree:

.. image:: _static/family_tree_reset.png
  :width: 600
  :alt: GPCRmd family tree display

------------------
GPCRmd simulations
------------------

Here, the user can identify all simulations included into GPCRmd divided into two datasets: GPCRmd community contributions and individual contributions.

.. image:: _static/dataset.png
  :width: 600
  :alt: GPCRmd dataset

Each simulation is classified into each class, family and subfamily. Similar than the Family tree but grouped. The user can expand each of these groups until get the simulations related to a specific family. To view the simulation the user can click on the red text link (e.g. ID 90).

.. image:: _static/dataset_display.png
  :width: 600
  :alt: GPCRmd dataset display

------
Search
------

The `Search` tool is divided into 3 parts: 

* Filter 
* Browser
* List of simulated systems

.. image:: _static/search.png
  :width: 600
  :alt: GPCRmd search

Filter                  
======

This part of the Search contains the name of all the columns available to be displayed in the search table. The user can select or deselect the columns that it wants to be displayed into the table. In the next example the user select the columns: Uniprot id, Class, PDB id, State, Species, Model type and Num. of atoms.

.. image:: _static/search_filter.png
  :width: 600
  :alt: GPCRmd search filter

Browser
=======

The Browser provides to the user filter everything that it is written in the cell.

.. image:: _static/search_browser.png
  :width: 600
  :alt: GPCRmd search browser

List of simulated systems
=========================

The table rows contain a summary of the most important features of the simulations. This includes links o further details of the receptor and molecules present in the simulated system. 

* Clicking on "View" to visualize and analyze the simulation. 
* Clicking on "Report", you will access the details of the system setup and simulation protocol, as well as links to download the simulation data.

.. image:: _static/search.png
  :width: 600
  :alt: GPCRmd search list