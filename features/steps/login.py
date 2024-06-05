from behave import given, when, then
import requests
import json

base_url = "https://reqres.in/api/login"

headers = {
  'Content-Type': 'application/json'
}

@given('Login page')
def step_given_login_page(context):
    context.url = base_url

@when('User logs in with email:{email} password:{password}')
def step_when_user_logs_in(context, email, password):
    data = {
        "email": email,
        "password": password
    }
    context.response = requests.post(context.url, headers=headers, data=json.dumps(data))

@then('Login is successful')
def step_then_login_is_successful(context):
    assert context.response.status_code == 200, "Login was not successful"

@then('The response contains the field token')
def step_then_response_contains_field_token(context):
    response_data = context.response.json()
    assert 'token' in response_data, "Response does not contain 'token'"

@then('Token is a string')
def step_then_token_is_string(context):
    response_data = context.response.json()
    assert isinstance(response_data['token'], str), "Token is not a string"

@then('Token is not empty')
def step_then_token_is_not_empty(context):
    response_data = context.response.json()
    assert response_data['token'], "Token is empty"

@then('The response contains the field user_id')
def step_then_response_contains_field_user_id(context):
    response_data = context.response.json()
    assert 'user_id' in response_data, "Response does not contain 'user_id'"

@then('User ID is an integer')
def step_then_user_id_is_integer(context):
    response_data = context.response.json()
    assert isinstance(response_data['user_id'], int), "User ID is not an integer"

@then('User ID is not negative')
def step_then_user_id_is_not_negative(context):
    response_data = context.response.json()
    assert response_data['user_id'] >= 0, "User ID is negative"
