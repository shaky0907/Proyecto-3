import json

class AnswerGenerator:
    """
    Generates response objects for success and error cases.
    """

    def generate_success_response(self, status_code, input_data):
        """
        Generates a success response object for the given input JSON.

        Parameters:
            status_code (int): The status code for the response.
            input_data (str): The JSON input.

        Returns:
            tuple: A tuple containing the response body, status code, and headers.
        """
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type, Authorization',
            'Access-Control-Max-Age': '3600'
        }

        response = {
            "status_code": status_code,
            "status": "success",
            "data": input_data
        }

        return (response, status_code, headers)


    def generate_error_response(self, status_code, message):
        """
        Generates an error response object.

        Parameters:
            status_code (int): The status code for the response.
            message (str): The error message.

        Returns:
            dict: An error response object.
        """
        response = {
            "status_code": status_code,
            "status": "error",
            "message": message
        }

        return response
