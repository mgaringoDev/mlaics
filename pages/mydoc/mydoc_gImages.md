---
title: Adding Google Images
tags: [formatting]
keywords: datatables, tables, grids, markdown, multimarkdown, jquery plugins
last_updated: May 22, 2020
summary: "Adding images from google drive"
sidebar: mydoc_sidebar
permalink: mydoc_gImages.html
folder: mydoc
---

Essentially do the follow:

1. Copy sharable link
	- EX: https://drive.google.com/file/d/1UifH9c8DGBMWa-UKmMAsOJx1uBzVb9Yd/view?usp=sharing
2. Remove everything after the file ID
	- EX: https://drive.google.com/file/d/1UifH9c8DGBMWa-UKmMAsOJx1uBzVb9Yd
3. Replace /file/d/ with uc?id=
	- EX: https://drive.google.com/uc?id=1UifH9c8DGBMWa-UKmMAsOJx1uBzVb9Yd
4. Copy paste this new file onto the website you want this image to be used

***
## Copy Convert
Use the input box below to copy a glink of the shared image and copy the markdown version of that image to be used to paste into a markdown compatible link image.
<form id='myForm' action="/action_page.php">
  <label for="gLink">gLink: </label>
  <input type="text" id="gLink" name="gLink"> <button onclick="myFunction()">Convert to MD</button>  
  <input type="reset" value="Reset">
</form>
***

<script>
function myFunction() {
	var glinkString;
  	glinkString = document.getElementById("myForm").elements[0].value;
  	var newglinkString = glinkString.replace('open?id=','uc?id=');
  	newglinkString = '![](' + newglinkString + ')'  	
  	document.getElementById("myForm").elements[0].value = newglinkString


  	var copyText = document.getElementById("gLink");
  	copyText.select();
	copyText.setSelectionRange(0, 99999)
	document.execCommand("copy");	
}
</script>

```ruby
![](https://drive.google.com/uc?id=___IMG_ID____)
```
Follow this [tutorial](https://www.google.ca/search?q=embed+an+image+on+google+drive&oq=embed+an+image+&aqs=chrome.3.69i57j0l2j69i59j0l2.4687j1j7&sourceid=chrome&ie=UTF-8#kpvalbx=1)

## Alternative Using Liquid

{% raw %}
```ruby
{% assign gID = '1UifH9c8DGBMWa-UKmMAsOJx1uBzVb9Yd' %}{% include addGImg %}
```
{% endraw %}

# Changing Image Size
To change the dimension of the image add **{:height="HEIGHTpx" width="WIDTHpx"}** to the end of the tag.  Note that this is for "kramdom"

```javascript
![](https://drive.google.com/uc?id=___IMG_ID____ ={:height="36px" width="36px"})
```
