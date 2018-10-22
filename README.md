# First task  

## Requirements  
You should have: *make*, *docker*, *docker-compose*

## Mission 1: 
```
make server
make server-python
```  
```  
from main import Parser

p = Parser()
p.print_all_categories_games()
```  

## Mission 2:  
```
make server
```  
Go to [http://0.0.0.0:8000](http://0.0.0.0:8000) to see all results.  

## Mission 3:  
```
make server
```  
Go to [http://0.0.0.0:8000/?search=yourWord](http://0.0.0.0:8000/?search=yourWord) to find games with 'yourWord' in name.  
Example: [http://0.0.0.0:8000/?search=Wordscapes](http://0.0.0.0:8000/?search=Wordscapes)