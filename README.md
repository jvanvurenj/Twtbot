### Twitter Bot Detection via LSTM
*note: database currently not implemented*


To use Twtbot with python-twitter ( https://github.com/bear/python-twitter ) and Tensorflow ( tensorflow.org ) installed:
Simply run
- python3 webScraper.py
It will build the neural network, then ask for a username you would like checked.


Note:
Twitter's free API vastly limits how much you can train a neural network. Additionally, finding confirmed bots that aren't already suspended is very difficult, resulting in less accuracy than I would have liked.


### Setting up database
To run a local instance of a database, ensure you have the dependencies installed:
	- pip3 install peewee
	- pip3 install sqlite3

When you want to create the database (one time thing), just run
``` python3 create.py ``` 

See Controller.py for methods involving the addition of users and tweets to the database.
Note: retrieving tweets is currently not implemented, and id systems need to be put into place to properly retrieve the tweets.
