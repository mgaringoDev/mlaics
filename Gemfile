source "https://rubygems.org"

# to publish on github page
gem 'github-pages', group: :jekyll_plugins

# to publich without github page
#gem "jekyll"

# don't forget to tun bundle install before placing it the plugins
# in the _config file.
gem "jekyll-jupyter-notebook"

# scholar stuff 5.16.0 is the version the is working with the current jekyll installed
# in the past I tried to update and install for dependencies but that took way too long
# this is currently the working version
gem 'jekyll-scholar', '5.16.0',  group: :jekyll_plugins

# A liquid tag for Jekyll to indicate the last time a file was modified.
# This plugin determines a page's last modified date by checking the last Git commit 
# date of source files. In the event Git is not available, the file's mtime is used.
# It can be found here:https://github.com/gjtorikian/jekyll-last-modified-at
group :jekyll_plugins do
  gem "jekyll-last-modified-at"
end