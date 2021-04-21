# Filmweb Netflix recommendations mailing

Python script which capture filmweb.pl recommendations of movies on Netflix and send as a formatted mailing to declared receivers.

## Features

Script captures:
- name of movie
- poster
- rating (with number of votes)
- description
- link to movie's site on Filmweb

Then script format content to simply and aesthetic form with movies sorted by rating.

## Using

To use it automatically set the config.ini file and set crontab to run the script whenever you want. For independent use, you can use your own gmail mail. 


## Example config.ini
```
[sender]
mail=abc@gmail.com
password=qwerty
[receivers]
mail=def@gmail.com
```
