---
title: Embedding Files Inside Note
tags: [formatting]
keywords: datatables, tables, grids, markdown, multimarkdown, jquery plugins
last_updated: May 22, 2020
summary: "Embedding various files inside the note including files from google drive and from the web."
sidebar: mydoc_sidebar
permalink: mydoc_fileAttachment.html
folder: mydoc
---

## Files From gDrive

If you want to add gDoc, gSheet or PDF from google drive add the following parameters in the front matter.

Copy paste the following in the front matter of the new note.  Note that the random collection of numbers and letters are the sharable id of the document you are trying to link.

### Adding gDrive PDF Files

```ruby
gDrivePDFile: 1KKTAUuj8OlM03U922KJL1ZTTSuMBTK4X
```

### Adding gDrive Sheet Files

```ruby
gDriveSheets: 1WnGloeNUhf__Um0i1kSsqVUA3ZwF56yr68R4_UQyiE8
```

### Adding gDrive Doc Files

```ruby
gDriveDoc: 1iPIAVzNSf8uNbhaV56lVvxd_2lOWVywTXuGFCPPJJ9s
```

### Adding gDrive Slides Files

```ruby
gDriveSlide: 1cQyCiFMB48_0RAl83ErkJVGJe6VwIUiP5t3pIPH-nH8
```

## Files From The Web

These should be the direct link to the PDF.  I don't advise this because sometimes the PDF just disappears.  The best thing to do is download them, place them in the mfDev gDrive account and link them according to the above ways of adding them on the page.
```ruby
pdfFile: http://youeeg.net/_siteMigraineProject/assets/pdf/conferences/CSCI2017/CSCI2017Presentation.pdf
```