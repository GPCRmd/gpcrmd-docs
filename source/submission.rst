=====================
Simulation submission
=====================

.. contents:: The simulation submission process consists in 4 steps:
    :depth: 2

Protein information
===================

Please provide relevant data for GPCRs as well as other proteins (e.g. G protein, arrestin, nanobodies, peptide ligands etc.) that are included in the simulation.

**(A)** Protein information is automatically retrieved by its UniProtKB accession number (AC). In case no AC exist, fill in manually the requested information in **(B)**.

**(B)** Automatically retrieved protein details. In case the protein is not available in UniProtKB the user has to manually provide this information.

By clicking the "**+ Add protein**" button information about another proteins in the system can be provided. Several proteins can be added in a single submission but at least one must be a GPCR whose sequence must have been deposited to the GPCRdb.

Small molecule information
==========================

Please, provide a detailed chemical description of all non-protein molecules in your system. This extensive information will help to provide a platform of well-characterized molecules for screening purposes to medicinal chemists and chemoinformaticians.

**(A)** Upload for each small molecule (non-protein) a '.sdf' or '.mol' file. A 2D chemical structure will be automatically displayed.

**(B)** Indicate if the uploaded structure is a co-crystalised molecule or if it belongs to bulk.

**(C)** Revise chemoinformatics data retrieved from the upload structure.

**(D)** Obtain molecule information from PubChem and ChEMBL databases.

Click the "**+ Add molecule**" button on the bottom of the pannel corresponding to the last uploaded molecule to add information about another molecule in your system.

Molecule data submission can be made individually by clicking the "**Submit molecule**" button on the bottom of every molecule pannel or simultaneously by clicking the "**Submit all molecules**" button on the bottom of the form.


Complex information
===================

**(A)** Fill in the form with general information about the crystalized part of the simulated system.

**(B)** Fill the "Curated protein data". As the coordinates of a protein may have different sources (X-ray, homology modeling...), the table must be filled in a protein segment-wise fashion. A segment stands for a continuum fragment of the protein whose coordinates come from the same source. In cases where the coordinates of the whole protein come from the same source, only one row in the table is needed for that protein. Importantly, information about the segments of all the proteins submitted in the step 1 must be provided. Every segment must be labeled with the "**Prot #**" number of the protein to which it belongs (the "**Submitted proteins summary**" table shows the "**Prot #**" number for each submitted protein). In order to assign correctly the canonical GPCR numbering to your simulation system, please indicate the starting ("**From res**" field) and ending ("**To res**") residue numbers for each protein segment. After clicking the "Autocomplete resid" button, the Uniprot numbering will be later automatically assigned. In addition, indicate the source for coordinates of each crystalized or modeled protein segment, e.g. 'threading' for a modeled loop. Note that the "**PDB ID**" field in the table must be filled when the segment source is "X-ray" or "NMR".

**(C)** Indicate the "**Resname**" in the retrieved list of co-crystalized small molecules. Extra rows can be added to the table after clicking the "**+ Add molecule**" if molecules with more than one "Resname" exist in the set of crystalized molecules. Then, click the "**Validate**" button and the "**Num of mol**" will be automatically filled.

Dynamics information
====================

Please, fill in the following form concerning specific details on the MD simulation protocol.

**(A)** Upload simulation files including coordinate file, topology file, trajectory files, simulation parameters, other files. In case of replicated, you can upload all files simultaneously (e.g. 20 to 100 replicates). After the file upload, please click the validate button in to order to ensure correct upload.

**(B)** Please complete the table of all simulation components by adding non-crystallized bulk molecules (e.g. waters, ions and lipids). For this, you only need to assign the corresponding residue name (resname) to the bulk molecules which are part of your simulation system. Then, click the "**Validate**" button to automatically fill the number of molecules (Num of mol) based on your uploaded simulation files

**(C)** Specify the simulation setup including information of Method, software, etc.