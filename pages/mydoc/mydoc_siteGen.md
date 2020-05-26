---
title: Site Generation
tags: [formatting]
summary: "Template for exporting the site to gitHub pages."
sidebar: mydoc_sidebar
permalink: mydoc_siteGen.html
folder: mydoc
---

Run the following code in the command line.

```ruby
jekyll build --config "_configPublish.yml"
```

{{site.data.alerts.warning}}

When running this the first time you need to change the _configPublish.yml file
- **destination:** change the project folder in github folder.
- **baseurl:** change the project page github pages website location.

{{site.data.alerts.end}}
