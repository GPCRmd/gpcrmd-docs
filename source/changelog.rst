==================
Changelog
==================
.. toctree::
    :maxdepth: 1

2.1.0 (08-04-2025 | 10-04-2025)
*******************************

**IMPORTANT**

* Terms & conditions of GPCRmd are updated to improve the protection of the data from the users and misused of the database.  

**Added**     

* Second round of GPCRmd data published: https://doi.org/10.1038/s41467-025-57034-y.
* Two new tools to analyze **allosteric sites** and **intracellular core conformation** via lipids.
* New **State** parameter included in **Step 1** of the submission form.
* Added **AlphaFold** as a new **Source type** and **PDB ID** option in `Steps 1/3 of the submission form <https://gpcrmd-docs.readthedocs.io/en/latest/submissions.html#simulation-submission-guide>`_.
* Introduced a **Source type** filter in the search table for easier data discovery.
* Added the **GPCRmd publication code**, enabling users to create a publication page to share and link multiple submissions under the same reference.
* Added a new FAQs & guide "How to cite my submission into an article?": https://gpcrmd-docs.readthedocs.io/en/latest/citation.html

**Changed**  

* Search tables now display the **Model name** next to the receptor by default.
* The **Class** column is hidden by default in search tables.
* Submission form (https://gpcrmd-docs.readthedocs.io/en/latest/submissions.html#simulation-submission-guide) updated (step 1, 3 & 5).
* Step 4 & 5 disabled from the "Simulation Submission Index" if you do not submit correctly the step 1, 2 & 3. 

**Fixed**   

* API downloader now correctly retrieves responses from the worker after a server restart.
* Fixed missing image in the **Variants** tool caused by a broken link due to DisGeNET website style updates.
* All **Type** and **Source type** options now correctly display on saved submissions.

**Next**

* Implementation of **batch submissions via API** (production release).

2.0.9 (14-02-2025)
*******************************

**Added**     

* New storage machine to store new income data from the community.

**Changed**  

* Reference on the report page to be more clear.  
* Home style to be more fitted for mobile devices. 

**Fixed**   

* Menu dropdown on the publication page.  
* Search by submitter on the search page. 

**Next**

* Possibility to multi submit submissions using the API (testing release).  


2.0.8 (16-11-2024)
*******************************

**Added**     

* Dynamic id as parameter on the search table (https://www.gpcrmd.org/dynadb/search/).   
* Loader and cancel button on "View" button of the search tables.  
* Some new FAQs to help users (https://gpcrmd-docs.readthedocs.io/en/latest/faqs.html).  

**Changed**  

* Simulation tool search table modified to be easily use.  

**Fixed**   

* Some minor bugs on the submission form.  

2.0.7 (05-08-2024 | 09-08-2024)
*******************************

This update is mainly to improve the server performance:

* API downloader on multiple requests.
* Fluent of the viewer with multiple user requests.
* Smoothly load of the trajectories. 
* Improvements on the submission form. 
  ...

2.0.6 (10-06-2024)
******************

**Added**   

* Downloader API change to improve the following of the process of downloading. 
* Step 1 submissions with no PDB code can introduce "-" to indicate that is not PDB code related. *Note: Recommended to change it later if a PDB code is assigned to the structure.*  
* Buttons on the home page to jump into the sections: tools, news and statistics. 

**Changed**

* Due confusion the name of the download_all API function to download_id. This functions download all the files related to a dynamic not download the whole database.  
* Order of the tools in the home page following the alphabetical order. 

**Fixed** 

* Add references to some submissions avoiding non-reference indications to cite the papers. 

2.0.5 (02-05-2024)
******************

**Added**   

* Step 1 & 4 shows the files that user previously upload into the submission. 
* Step 1 & 4 do not request always the file/s if some file was uploaded previously.
* To access into non-published submission reports need the submission key like in the viewer.
* News with articles of the published submission into GPCRmd.

**Fixed** 

* Errors on the step2 & 3 related with small molecules or chains returning 'Server error message'.
* Search & Datasets tool showing non-published data that are not public available. 
* Clean of uncompleted submissions. 

2.0.4.1 (20-03-2024)
******************

**Added**   

* New API documentation to explain more in detail how the functions work.

**Changed**  

* Meta-analysis tool style. 

**Fixed** 

* Selection tool gives an error using the generic numbering nomenclature. 
* Step 3 of the submission form not showing the sdf image of the molecule, mainly basic ions like Calcium, Sodium and Water, among others. 

2.0.4 (08-03-2024)
******************

**Added**   

* New policy on the pre-submission, point 4 to avoid incomplete submissions: "Step 5 on references can be completed after publication. Please submit the full citation with the DOI once available. Failure to do so may result in automatic closure of the submission without reference completion."
* Update of the submission table style to facilitate the user to take a look into their previous submissions.
* Search tool filters can accept regular expressions to filter the data `RegEx <https://en.wikipedia.org/wiki/Regular_expression>`_ (e.g. State > Active or Inactive > ^Active, ^ means startswith, in this case only get active results).

**Changed**  

* Change of the max upload file size accepted for the server in order to incorporate bigger systems. 
* Users do not need to use the submission protection key to access into his submissions if they are the owners. To share with other people you need to continue sharing with them the dynamic id and the submission key.
  
**Fixed** 

* Error with whitespace on the field of Uniprotkbac at the submission form step3.
* Emails to notify maintenance blocked by Gmail and not reaching the users.  
* Error with distance and RMSD tool with new data (not working). 
* Data login request when the user try to download files of published submissions. 

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
* On some parameters the whitespace causes errors. 
* Sdf file image in png not showing at report page. 

2.0.2 (03-11-2023)
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

