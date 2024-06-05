import json
from behave import *
import requests

base_url = "https://reqres.in/api/register"
users = 'users'

headers = {
  'Content-Type': 'application/json'
}

@given('Register page')
def step_given_register_page(context):
  context.url = base_url


@when('User is created with email:{email} password:{password}')
def step_when_user_is_created(context, email, password):
    data = {
        "email": email,
        "password": password
    }
    context.response = requests.post(context.url, headers=headers, data=json.dumps(data))

@then('Registered account returns correct response')
def step_then_correct_response(context):
    assert context.response.status_code == 200, "Failed to create user"



@then('The response contains the fields id and token')
def step_then_response_contains_fields(context):
    response_data = context.response.json()
    assert 'id' in response_data, "Response does not contain 'id'"
    assert 'token' in response_data, "Response does not contain 'token'"

@then('User id is 4 and token is a string')
def step_then_id_and_token(context):
    response_data = context.response.json()
    print('Success',response_data)
    assert response_data['id'] == 4, "ID does not match"
    assert isinstance(response_data['token'], str), "Token is not a string"