# data-analysis

To run this app:

Step 1: Download the project <br />
<br />
Step 2: Install project dependencies by the following sequence of commands:<br />
<br />
  2.1 pipenv install<br />
  2.1 npm init, then take all defaults. At the end answer "yes"<br />
  2.1 npm install --save serverless-python-requirements<br />
  <br />
Step 3: Open up a pipenv environment by running the command:<br />
  pipenv shell<br />
  <br />
Step 4: Deploy the app to Lambda by running the command:<br />
  sls deploy<br />
  <br />
  Note: It will be necessary to re-deploy this app as it has been removed from lambda due to the Glue Table issue.<br />
  <br />
Step 5: To test the program locally, run:<br />
  sls invoke local -f getCustomers<br />
  <br />
Step 6: To test the program on lambda, run:<br />
  sls invoke -f getCustomers<br />
