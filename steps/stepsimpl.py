from behave import *
import requests


@given('the book details which needs to be added')
def step_impl(context):
    context.json = {
        "name": "morpheus",
        "job": "leader"
    }


@when('we execute the API')
def step_impl(context):
    context.response = requests.post('https://reqres.in/api/users', json=context.json)
    context.body = context.response.json()

@then('the book is successfully added')
def step_impl(context):
    assert context.body['name'] == "morpheus"