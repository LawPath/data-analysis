# data-analysis

To run this app:

Step 1: Download the project
Step 2: Install project dependencies by the following sequence of commands:
  2.1 pipenv install
  2.1 npm init, then take all defaults. At the end answer "yes"
  2.1 npm install --save serverless-python-requirements
Step 3: Open up a pipenv environment by running the command:
  pipenv shell
Step 4: Deploy the app to Lambda by running the command:
  sls deploy
  Note: It will be necessary to re-deploy this app as it has been removed from lambda due to the Glue Table issue.
Step 5: To test the program locally, run:
  sls invoke local -f getCustomers
Step 6: To test the program on lambda, run:
  sls invoke -f getCustomers
