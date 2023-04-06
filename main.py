import json

import requests

from scenario import Scenario




def make_get_request(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text


# the data parameter in this function is used to send data to the server in the body of the request.
# This can be used, for example, to submit form data to the server, or to send JSON data in an API request.

def make_post_request(url, data):
    response = requests.post(url, data=data)
    if response.status_code == 200:
        return response.text


def make_dynamic_request(url, scenario):
    print(f"url: {url}, \n\n\nscenario: {scenario}")
    # Get the number of times to repeat the request
    num_repetitions = scenario.num_repetitions

    # Loop through the number of repetitions and make the request each time
    for i in range(num_repetitions):
        # Get the request type and information from the scenario
        request_type = scenario.request_type
        information = scenario.information
        print(information, type(information))

        # Make the request
        if request_type.lower() == 'get':
            response = requests.get(url, params=json.dumps(information))
        elif request_type.lower() == 'post':
            response = requests.post(url, data=json.dumps(information))
        else:
            raise ValueError('Invalid request type')

        print(f"response.text: {response.text}")
        print(f"scenario.answer: {scenario.answer}")

        # Check if we expect a certain answer
        if scenario.expected_answer:
            if response.text != scenario.answer:
                raise ValueError('Received unexpected answer')
        # Return the response instead of printing it
        scenario.answer = response.text

    return scenario if scenario.expected_answer else None


# This function ask the user to enter a number of key-value pairs,
# and then creates a list of JSON strings based on the input provided.
# It then returns a list of dictionaries created by parsing the JSON strings using json.loads().

# numData is the number of key-value pairs that the user will enter
# for the JSON data.

def inputOfDataJson(numData):

    # TODO Check if new version works

    print(f"numData: {numData}")
    json_strings = []
    # data = {}
    for i in range(numData):
        print("json number " + str(i) + ":")
        key = input("Enter key:")
        value = input("Enter value:")
        json_string = '{"' + key + '":"' + value + '"}'
        json_strings.append(json_string)

        # data[key] = value


    # { "KEY1": "VALUE", "key2": "VALUE" }

    # the function uses the json.loads() method
    # to parse each JSON string in the json_strings list
    # into a Python dictionary.

    data_json = [json.loads(s) for s in json_strings]
    print(data_json)
    return data_json

    # return data


# this main ask the user to enter a URL, request method (GET or POST),
# and number of key-value pairs to include in the JSON data.
# It then creates a list of JSON strings based on user input,
# and passes the JSON data to the make_dynamic_request() function to send the HTTP request.
# The response from the server is then printed to the console.

if __name__ == '__main__':
    while True:
        url = input("Enter url: ")
        # use http://localhost:8000 for loclhost connection, testing
        #  http://localhost:8000?name=Noy&age=19
        method = input("Enter method of request (GET/POST): ").upper()
        numData = int(input("Enter number of keys and values in json: "))
        info: str = inputOfDataJson(numData)
        print(f"info: {info}")
        data = json.dumps(info)
        scenario = Scenario(1, method, info, 1, url, expected_answer=True, answer="Received your request!")
        response = make_dynamic_request(url, scenario)
        print(response)
