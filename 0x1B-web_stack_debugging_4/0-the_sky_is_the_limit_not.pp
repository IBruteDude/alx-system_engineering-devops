# enable disabled multi_accept option in nginx
exec { 'enable multi_accept':
  path    => '/bin',
  command => 'sed -i "s/# multi_accept/multi_accept/" /etc/nginx/nginx.conf',
}
mkdir "0x16-api_advanced" && cd "0x16-api_advanced" && touch README.md && touch 0-subs.py 1-top_ten.py 2-recurse.py 100-count.py  && echo "Scraping to advance the web exp" > README.md && find . -name "*.py" -exec sh -c 'echo "#
!/usr/bin/python3" > "{}" && chmod u+x "{}"' \;
git restore ../0x14-javascript-web_scraping/0-readme.js ../0x14-javascript-web_scraping/1-writeme.js ../0x14-javascript-web_scraping/100-starwars_characters.js ../0x14-javascript-web_scraping/101-starwars_characters.js ../0x14-javascript-web_scraping/2-statuscode.js ../0x14-javascript-web_scraping/3-starwars_title.js ../0x14-javascript-web_scraping/4-starwars_count.js ../0x14-javascript-web_scraping/5-request_store.js ../0x14-javascript-web_scraping/6-completed_tasks.js ../0x14-javascript-web_scraping/README.md
