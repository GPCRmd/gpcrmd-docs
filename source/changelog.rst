==================
Changelog
==================
.. toctree::
    :maxdepth: 1

2.0.3 (08-02-2024)
******************

**Added**   

* New function on GPCRmd API to get information about the compounds elements simulated in GPCRmd grouped by type.
  
**Changed**  

* Update of the receptor-meta-analysis and pharmacophores documentation. 
* Update of the publication page.
  
**Fixed**  

* Error on cms format when is loaded in the step 4. 
* Style of the numbers of the sliders of the water volume distribution tool.
* Button Tool > Simulation tools not working at the home page.
* Publication page do not show the table of submissions. 
* Bugs of the Pockets tool. 
* On some paramaters the whitespaces causes errors. 
* Sdf file image in png not showing at report page. 

2.0.2 (27-10-2023, postponed to 03-11-2023)
******************

**Added**   

* New topology file format accepted: .cms. 
* New batch of published simulations from January 2023 to October 2023. 
* New graph on the statistics homepage section about the accumulated time of simulation in GPCRmd, grouped by GPCRmd community or individual contributions. 
* New two functions on GPCRmd API to get all the dynamics id by class or by ligand type (Apoform / Complex). 
* New filtering mode by field using text and download modes to get the data filtered on the search tool.

**Changed**  

* Limited the delta values from 0 to 20 nanoseconds in the step 1 of the submission form due to confusions on the units. 
* New style of graphs on the statistics section at the homepage. 

**Fixed**  

* Error access to the summary of a submission using the button "See summary" in the submission list. 
* Bug on meta-analysis tool NGL viewers that not showing the structure correctly. 
* Error numbering on generic number association with structures with fusion protein in the middle of the pdb (like 5TVN).

2.0.1 (31-08-2023)
******************

**Added**   

* Publication page link in the reference section of the simulation report (e.g. https://gpcrmd.org/dynadb/dynamics/id/90/). 
* API can accept multiple inputs.
* Documentation menu button with detailed information for the users related with GPCRmd.
  
**Changed**  

* GPCRmd workbench documentation updated. 
* Organization of the top bar menu.

**Fixed**  

* Pockets tool bug not showing data in the table if the user access from the selection tool.
* Description empties on the submission forms cause an error before the step 5 in the submission summary.
* Minor bugs. 

2.0.0 (11-08-2023)
******************

**Added**   

* Search tool selector with a dynamic table to select a specific dynamic. 
* New front-end style of the web. 
* New GPCRmd API. 
* Instructions to follow before start the submission process as pre-submission step.  
* Option on step 4 to upload the simulation protocol in the submission form. 
* Option on step 5 to retrieve the information of the article using the DOI.
* Guide to create and manage the GPCRmd account `Link <https://gpcrmd-docs.readthedocs.io/en/latest/accounts.html>`_. 
* Step-by-step guide to submit a submission into GPCRmd `Link <https://gpcrmd-docs.readthedocs.io/en/latest/submissions.html>`_. 
* Secret key account parameter for the non-published simulations to give the option to share them using the link and this key.
* Trr trajectory file format added to replace the trj format. 
* GitHub community of GPCRmd (https://github.com/GPCRmd) if some users wants to collaborate. 
  
**Changed**  

* GPCRmd Tree Map elements resize and add zoom & drag utilities.
* Search table with a compact table and options to hide or show columns.

**Fixed**  

* Workbench Viewer bugs with table sizes. 

**Removed**

* Trj trajectory file format removed due to conflicts. 

