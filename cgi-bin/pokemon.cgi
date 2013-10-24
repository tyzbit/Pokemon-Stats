#!/bin/sh
echo "Content-type: text/html; charset=\"UTF-8\"\n"
echo "<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Transitional//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd\">"
echo "<span><div class=subdiv>"
###Declarations###
apipath="http://bulbapedia.bulbagarden.net/w/api.php?"
redirects="&redirects"
both="&redirects&format=json"



if [ -z $1 ]; then
	echo "script error, arguments needed"
else
	#stats part
	index=$(curl -s $apipath"format=xml&action=parse&prop=sections&page="$1"&redirects&format=json" | python -m json.tool | grep '"Base stats"' -B3 -A3 | grep -Po '"index":.*?[^\\]",' | cut -d "\"" -f4)
	echo $(curl -s $apipath"&format=xml&action=parse&prop=text&page="$1"&section="$index"&redirects" | recode html..ISO-8859-1)
	echo "</div><div class=subdiv>"
	#weaknesses part
	index=$(curl -s $apipath"format=xml&action=parse&prop=sections&page="$1"&redirects&format=json" | python -m json.tool | grep '"Type effectiveness"' -B3 -A3 | grep -Po '"index":.*?[^\\]",' | cut -d "\"" -f4)
	echo $(curl -s $apipath"&format=xml&action=parse&prop=text&page="$1"&section="$index"&redirects" | recode html..ISO-8859-1)
	echo "</span>"
fi
