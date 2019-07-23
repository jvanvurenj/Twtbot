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

Problems/Possible Improvements:

Twitter's free API limits hits per ~10 minutes to a rather lower number. This causes problems when training the neural network.
Solutions:
Load a database with all the info over a long time and train from there
Pay for a higher rate API

It's hard to find confirmed bot accounts to train the neural network with. Right now, we don't have any bots that could be considered harmful to train with, just bots that are obviously meant to be bots (such as a weather bot).
Solutions:
):

Training with people I'm following on Twitter - there could 1. Potentially be bots there, 2. Inconsistent as I follow new people relatively often, 3. Might not be an accurate representation of all of the users of Twitter, but rather only an accurate representation of my experience on Twitter.
Solutions: Take a random sample from a variety of users and somehow filter or manually check bots? It would be hard to mass train a neural network with verified users because someone needs to manually verify them while keeping them random.

