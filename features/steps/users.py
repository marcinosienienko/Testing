import json
import requests

from behave import *

base_url = "https://reqres.in/api/users"

headers = {'Content-Type': 'application/json'}

@given(u'Im in super App')
def step_impl(context):
    pass

@when(u'User is created with name:morpheus job:leader')
def step_impl(context):
    payload = json.dumps({"name": "morpheus", "job": "leader"})
    url = base_url

    res = requests.post(url, headers=headers, data=payload)
    if res.status_code == 201:
        context.user_id = res.json()['id']
    else:
        raise AssertionError(f"Request failed with status code: {res.status_code}")

@then(u'Created user exist in the system')
def step_impl(context):

    context.user_data = {
        "id": context.user_id,
        "name": "morpheus",
        "job": "leader"
    }

@then(u'User has correct data for "name" is "morpheus"')
def step_impl(context):
    assert context.user_data['name'] == 'morpheus', f"Expected name to be 'morpheus', but got '{context.user_data['name']}'"

@then(u'User has correct data for "job" is "leader"')
def step_impl(context):
    assert context.user_data['job'] == 'leader', f"Expected job to be 'leader', but got '{context.user_data['job']}'"
