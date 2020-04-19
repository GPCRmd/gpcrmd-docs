==================
Search
==================

.. contents::
    :depth: 2

List of simulated systems
==========================
This table provides an easy and quick tool to search for any simulation in GPCRmd. Use the `Search` input to filter out the simulations shown at the table. It is possible to search by any of the terms included in the table (receptor name, Uniprot entry name, Uniprot ID, etc.). 

The table rows contain a summary of the most important features of the simulations. This includes links to further details of the receptor and molecules present in the simulated system. Click on "Go to the Workbench" to visualize and analyze the simulation. By clicking on "Go to the Report", you will access the details of the system setup and simulation protocol, as well as links to download the simulation data.


Browser
=======

For more complex searches, we provide our Browser, which includes more advanced browsing tools. Moreover, it has the advantage of allowing to search by synonims. 

Overall, the Browser is used to find simulations based on the elements included in it. First, use panel **1** to search the desired elements (GPCRs, other proteins, molecules, etc). Add the elements to the search by clicking "Add to Search". Then, use the panel **2** to search for simulations containing the elements added.

Usage
------------

Let's say you are looking for a simulation containing serotonin and the serotonin receptor. You should use the panel **1** to search for these elements (e.g. search by the word "serotonin"). You will obtain a list of elements related to your search (serotonin, serotonin receptors, ...). Select the elements you are interested in by clicking "Add to Search". They will appear in panel **2**. If you don not want to apply any more filters or use the advanced search, you can just click at the search button of panel **2**. A list of simulations corresponding to your search will appear.


Panel **1**, searching the elements: 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Use panel **1** to search for molecules or proteins (the "elements" which constitute simulations). You can use SMILES, InChI, InChIKey, PubChem CIDs, ChEMBL id's and common names to search for molecules. In order to find proteins, Uniprot accession codes and common names can be used. You can indicate if your search is a GPCR or another protein using the dropdown. You can also use it to search by dynamics ID. If you are not looking for a protein, just use the option "All". Then press the search button to obtain the resulting elements. Next to every result, you will find an "Add to search" button, which will add the element to the panel **2**.

Panel **2**, joining the elements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Panel **2** holds all the elements you have added. You can directly click on the search button to find all simulations matching that combination of elements, or you can tune your results by filtering by some parameters, which you will find at "See simulation filters". Such parameters include time step, software used, etc. For molecules, you can select whether your molecule is an "Orthosteric ligand", "Allosteric Ligand", "Other" or "All" (meaning any of the previous). For proteins, you can select if it is a GPCR or not, using the *"is GPCR" checkbox*. If it is not selected, we assume that the protein is NOT a GPCR. If you need to use boolean operators like OR, AND, NOT, switch to the `Advanced search`_.


Difference between standard form and specific state
---------------------------------------------------------

The difference between standard form and specific states is that a standard form represents a **set** of related molecules that only differ in the protonation state, tautomerization state, or some other subtle features. Each of these different states is a single specific state. As the concept of specific state is more precise, when searching with it, you will only find those simulations containing exactly that specific state. However, if you search by a standard form, you will find all the simulations which have any of the related molecules belonging to that standard form. Therefore, if, for example, you search systems using Clozapine (standard form) you will always get more results (or the same) than if you search by Clozapine (specific state X).

Simple and Advanced Search
-----------------------------

In panel **2**, you can choose between *Simple and Advanced search*, the difference being that the second allows you to use "AND", "OR" and "NOT" boolean operators, as well as brackets. Simple search only allows "AND" operator (which is enough in most cases). The following is an example of how to perform a search with brackets:

=============== =============
P28222	        P28222
AND ( Serotonin	AND Serotonin
OR Clozapine	OR Clozapine
OR POPC )	    OR POPC
=============== =============

The example search in the left will return the systems matching any of the following:

* P28222 + Serotonin
* P28222 + Clozapine
* P28222 + POPC
* P28222 + Serotonin + Clozapine
* P28222 + Serotonin + POPC
* P28222 + Serotonin + Clozapine + POPC
* P28222 + POPC + Clozapine

However, the example search in the right will return the systems matching any of the following:

* P28222 + Serotonin
* Every system with Clozapine
* Every system with POPC

Please, keep in mind that the results may not be composed only by the elements you have included in the search. So, when we say that the system will match "P28222 + Serotonin", it means that at least, it has these two components - it may also have something else, like ions, water, etc. Read the `Exact match`_ section to know how to avoid this greedy behaviour.


Exact Match
---------------

If you select "Exact Match", the search will return only those simulations whose composition matches exactly the one you have built in the right panel. If there is any other element in the simulation that you have not included in the search, it will not appear as a result. So, if you look for P28222 AND Serotonin, and select exact match, only those systems composed by P28222 and serotonin and nothing else will be retrieved; a system with P28222, water and serotonin will not be a result.


Empty search
-------------

You can search simulations without adding any elements. This will return every simulation we have in our database. You can still filter by any of the fields: Force Field, Software, etc. 

.. _Advanced search: https://submission.gpcrmd.org/dynadb/search/#adv
