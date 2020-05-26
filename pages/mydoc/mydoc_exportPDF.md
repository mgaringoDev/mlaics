---
title: Exporting Project to PDF
tags: [formatting]
summary: "Exporting project to pdf"
sidebar: mydoc_sidebar
permalink: mydoc_exportPDF.html
folder: mydoc
---

{{site.data.alerts.warning}}

This was migrated from old project pages.  Need to modify this in the future for this project page. I think this is simple enough.  Just loop through the sites with specific project sidebars.  Each project should have unique sidebars.

{{site.data.alerts.end}}

You can export all the notes located in the ***_site\project1\*** directory.  To do so go to the parent directory of the project.  There should only be 4 files:

- **_PDF:** Location of the resultant pdf files.
- git_projectCodes: Location of the codes to be backed up by github
- local_projectNotes: Local directory of the notes 
- exportToPDF.py: A python file to create the pdf files.

Once in this directory, open a terminal and activate any python 3 environment.  Then run the **exportToPDF.py** file with the command:

```python
python exportToPDF.py
```

This will run the code:

```python
import os,sys
from glob import glob
import pdfkit
from tqdm import tqdm


def getHTMLFiles(searchDirectiory):
    result = [y for x in os.walk(searchDirectiory) for y in glob(os.path.join(x[0], '*.html'))]
    return result

def main():
	# I/O
	cwd = os.getcwd()
	pagesLocation = cwd + '\\local_projectNotes\\_site\\project1\\' 
	pdfOutDir = cwd+'\\_PDF\\'

	# Get all HTML Files
	htmlFiles = getHTMLFiles(pagesLocation)

	# Loop through and generate all the PDF Files
	for htmlFile in tqdm(htmlFiles):	    
	    pdfFileName = htmlFile.split('\\')[-2]+'.pdf'
	    pdfkit.from_file(htmlFile,pdfOutDir+pdfFileName)  
	    os.system( 'cls' )


if __name__ == "__main__":
    main()
    print('Finished publishing notes in PDF')

```