from chalice import Chalice
import boto3

app = Chalice(app_name='lambdaTest')

BUCKET = 'lawpath-data-lake'
s3_resource=boto3.resource("s3")


@app.lambda_function()
def hello_world(event, context):
    print("hello world!")
    return {'hello': 'world'}

@app.lambda_function()
def check_this_works(event, context):
    print("hello again!")
    return {"hello": "again"}

@app.lambda_function()
def s3PrintFunction(event,context):
    stuff = s3_resource.Bucket(BUCKET)
    for obj in stuff.objects.all():
        print(obj.key)

#@app.on_s3_event(bucket=BUCKET, events=['s3:ObjectCreated:*'])
#def prints3chalice(event,context):
#    print(event)

# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
