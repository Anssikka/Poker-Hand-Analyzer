## Pokerhand analyzer
Analyses 5 card poker hands for up to 10 player and optionally generates a frequency table to see hand value distribution.
Look at the analysis.txt and frequencies.txt for what the output will look like. The example frequencies.txt has been generated for one billion hands.

## How to install and run

### Running tests

On Windows, run:
```
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```
On Unix or MacOS, run:
```
python3 -m venv tutorial-env
source tutorial-env/bin/activate
pip install -r requirements.txt
```

In the folder run:
```
pytest
```

### Running the program

On Windows, run:
```
python run.py
```

On Unix or MacOS, run:

```
python3 run.py
```

Which generates analysis.txt and prints hands for 3 players on default.
On line 6 in the run.py change the Dealer parameter to any number between 1-10 to generate hands for x players.
```
dealer = Dealer(3)
```

### Generating a frequency table for hand distribution.

Run the program with commandline argument generate to generate a frequencies.txt in the folder you run it from.
The default parameter is 10 which generates 10 million hands. It should take about 2 minutes +- 30 seconds depending on your machine. You can speed it up by running the program with [PyPy - Welcome to PyPy](https://pypy.org/) which cuts the time to about one third of standard library python.


```
python run.py generate
```

### Improvements

- Change the code to follow pep8 coding style standards.
- Implement Player class and numerical hand value so you could play out actual pokerhands with 2-10 players and keep track of the wins and losses. Could be used as your own rock paper scissors or random.org replacement.


### Possible Features

- Do the above but, give each player chance to discard and pick 0-5 cards once. Simulate random discards for x(10 billion?) rounds and keep track of the discards categorized by your starting hand and how it affects the expected value and what your strategy should be depending on what your starting hand is.