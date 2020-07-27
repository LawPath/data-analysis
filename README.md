# data-analysis
This project contains all projects Andrea created between 1-27 Jul for the Analytics team.

## Projects
The key project folders are:
1. stripe-customers
2. segment-logs-events

Each project must be downloaded separately.

## Prerequisites
All projects in these folder require the following as prerequisites. Please download and follow installation instructions in the links given.
1. Python3
https://www.python.org/downloads/

2. NPM
https://www.npmjs.com/get-npm

3. Pipenv
https://pypi.org/project/pipenv/

4. Serverless
https://www.serverless.com/framework/docs/getting-started/

## stripe-customers
Stripe customers is a lambda function that collects, cleans, and stores Stripe Customer data in the Lawpath Data Lake. 
Note: The intial deployment was removed due to a bug. Before testing or running stripe-customers, please ensure that the app is deployed.

### Set-up
1. Clone the repository stripe-customers folder in a suitable local directory
2. Use pipenv to download all dependencies:
```
pipenv install
```
3. Open a pipenv environment:
```
pipenv shell
 ```
4. Use NPM to generate a Pipfile.lock file to manage dependencies. To do so, use the following steps:
Step 4.1: Run:
```
npm init 
```
Step 4.2: Accept all default configurations when running npm init, and enter "yes" at the end when prompted.
Step 4.3: Run:
```
npm install --save serverless-python-requirements
```
5. Deploy the app by running:
```
sls deploy
```
### Running the app
1. Ensure that you are in the correct folder (stripe-customers, containing handler.py)
2. To run the app locally:
```
sls invoke local -f getStripeCustomers
```
3. To run the app through lambda:

```
sls invoke -f getStripeCustomers
```

## segment-logs-events
Stripe customers is a lambda function that updates segment-logs-events data set (lawpath-data-lake-raw/segment-logs-events).
This may only be run after the segment-logs-events data set has been pre-populated with a separate function.

### Set-up
1. Clone the repository stripe-customers folder in a suitable local directory
2. Use pipenv to download all dependencies:
```
pipenv install
```
3. Open a pipenv environment:
```
pipenv shell
 ```
4. Use NPM to generate a Pipfile.lock file to manage dependencies. To do so, use the following steps:
Step 4.1: Run:
```
npm init 
```
Step 4.2: Accept all default configurations when running npm init, and enter "yes" at the end when prompted.
Step 4.3: Run:
```
npm install --save serverless-python-requirements
```
5. Deploy the app by running:
```
sls deploy
```
### Running the app
1. Ensure that you are in the correct folder (stripe-customers, containing handler.py)
2. To run the app locally:
```
sls invoke local -f getData
```
3. To run the app through lambda:
```
sls invoke -f getData
```
