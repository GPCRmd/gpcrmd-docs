==================
Simulation browser
==================

.. contents::
    :depth: 2

Usage
=====

Imagine that you want to cook something and you are interested in a few ingredients, it would be nice to have some website where you could look for those ingredients, and then look for a recipe which uses those elements. This is exactly what we have done...for molecular dynamics. If you are interested in a simulation containing the ingredients serotonin and the serotonine receptor, you look for the molecule serotonin in the left panel (A), results will appear and then you click "Add to Search". Now, you look for the serotonin receptor -again in the left panel-, and click "Add to Search". Finally, go to the right panel (B) and click the search button. We will show you all the simulations containing those elements.


Left Panel, searching the elements:
-----------------------------------

Use the panel in the left to search for molecules or proteins (the "elements" which constitute simulations). You can use SMILES, InChI, InChIKey, PubChem CIDs, ChEMBL id's and common names to search for molecules. In order to find proteins, Uniprot accession codes and common names can be used. You can filter the type of the results returned (All, protein, standard form, specific states). Next to every result, you will find an "Add to search" button, which will add the element to the right panel, allowing you to search a simulation using a given combination of elements. For example: standard form Clozapine AND protein P28222.

Right Panel, joining the elements:
----------------------------------

The right panel holds all the elements you have added during your elements search. You can directly click the search button  to find all simulations matching that combination or you can tune a bit your results by filtering by some parameters (time step, software used, etc.). You can select the function which the molecule performs in the system: "Orthosteric ligand", "Allosteric Ligand", "Other" or "All". "All" meaning any of the previous. For proteins, you can select if it is a GPCR or not, using the **"is GPCR" checkbox**. If it is not selected, we assume that the protein is NOT a GPCR. If you need to use boolean operators like OR, AND, NOT, switch to the `Advanced search`_.

Difference between standard form and specific state
===================================================

The difference between standard form and specific states is that a standard form represents a **set** of related molecules which only differ in the protonation state, or tautomerization state, or some other subtle features. Each of this different states is a single specific state. As the concept of specific state is more precise, when searching with it, you will only find those simulations containing exactly that specific state. However, if you search by a standard form, you will find all the simulations which have any of the related molecules belonging to that standard form set. So, if you search systems using Clozapine (standard form) you will always get more results (or the same) than if you search by Clozapine (specific state X).

Simple and Advanced Search
==========================

In the right panel, you can choose between **Simple and Advanced search**, the difference being that the second kind allows you to use "AND", "OR" and "NOT" boolean operators, as well as brackets. Simple search only allows "AND" operator (which is enough in most cases). The following is an example of how to perform a search with brackets:

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

Please, keep in mind that the results may not be composed only by the elements you have included in the search. So, when we say that the system will match "P28222 + Serotonin", it means that at least, it has those two components, but it also may have something else, like ions, water, etc. Read the `Exact match`_ section to know how to avoid this greedy behaviour.


Exact Match
===========

If you select "Exact Match", the search will return only those simulations whose composition matches exactly the one you have build in the right panel. If there is any other element in the simulation that you have not included in the search, it will not appear as a result. So, if you look for P28222 AND Serotonin, and select exact match, only those systems composed by P28222 and serotonin and nothing else will be retrieved; a system with P28222, water and serotonin will not be a result.

Search by GPCRmd ID:
====================

You also have the option to search by the identifiers used in the GPCRmd database, just check the **"Search by GPCRmd ID" checkbox**. If you select this type of search, you can return standard forms, specific states, proteins and dynamics. Below you will find the definition of these three concepts. You may find this kind of search useful to check if the simulation you have submited is available.

Empty search
============

You can search simulations without adding any elements. This will return every simulation we have in our database. You can still filter by any of the fields: Force Field, Software, etc.




.. _Advanced search: https://submission.gpcrmd.org/dynadb/search/#adv
