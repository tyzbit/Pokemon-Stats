Pokemon-Stats
=============

A Web application that pulls Pokemon stats on-the-fly from Bulbapedia

Requirements
------------

CGI-capable web server (I use Apache)
Python (any version should work as long as it has jsontool)
recode (sudo apt-get install recode)

Installation
------------

Copy the files in webroot/ to the directory you want to serve the application from.

Copy the pokemon.cgi script to your CGI scripts directory. Ensure executable (chmod +x pokemon.cgi) is set.

Edit index.html and change "CHANGEMETOYOURCGIDIRECTORY" to the path to your CGI scripts directory.

Technical Details
-----------------

The CGI script pulls the pokemon stats from bulbapedia using MediaWiki's API.  Currently, the information is hard-coded, but eventually it will allow for specifying specific stats.
Using jquery and some very basic javascripting, we replace the DOM with the pure HTML from Bulbapedia, which preserves formatting.  We then clean it up, removing links and headers.

To Do
-----

[ ] Add additional stats it can pull

[ ] Implement API for other sites, possible (serebii?)

[ ] Clean up UI (maybe checkboxes for selecting what information should be pulled)

[ ] Rewrite pokemon.cgi to separate the API calls and what type of stat it gets, or break the script apart
