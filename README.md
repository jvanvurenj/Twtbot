### Twitter Bot Detection via LSTM
-- N/A --
### Setting up database
To run a local instance of a database, ensure you have the dependencies installed:
	- pip3 install peewee
	- pip3 install sqlite3

When you want to create the database (one time thing), just run
``` python3 create.py ``` 

See Controller.py for methods involving the addition of users and tweets to the database.
Note: retrieving tweets is currently not implemented, and id systems need to be put into place to properly retrieve the tweets.
