import json


class Scenario:
    def __init__(self, num_requests: int, request_type: str, information: str, num_repetitions: int, destination: str, expected_answer: bool, answer: str):
        # the number of requests to be made
        self.num_requests = num_requests

        # the type of request to be made (get,post)
        self.request_type = request_type.upper()

        # the information to be sent with the request
        self.information = information

        # the number of times to repeat the requests
        self.num_repetitions = num_repetitions

        # the destination URL to send the requests to
        self.destination = destination

        # (optional): the expected answer to receive from the server
        self.expected_answer = expected_answer

        self.answer = answer

    # to_json- to convert an object of this class into a JSON string.
    def to_json(self):
        # convert a dictionary of the instance variables into a JSON string.
        return json.dumps({
            # defines a Python dictionary with keys and values
            # that represent attributes of the instance of the class
            "num_requests": self.num_requests,
            "request_type": self.request_type,
            "information": self.information,
            "num_repetitions": self.num_repetitions,
            "destination": self.destination,
            "expected_answer": self.expected_answer,
            "answer": self.answer
        })

    def print_scenario(self):
        print(f"Number of run requests: {self.num_requests}")
        print(f"Request type: {self.request_type}")
        print(f"Information: {self.information}")
        print(f"Number of repetitions: {self.num_repetitions}")
        print(f"destination: {self.destination}")
        print(f"expected_answer: {self.expected_answer}")



