import requests

class Data:
    def __init__(self,parameters:dict):
        self.params = parameters
        self.response = requests.get(url='https://opentdb.com/api.php',params=self.params)
        self.question_json = self.response.json()
        self.question_data = self.question_json['results']


    def get_data(self):
        return self.question_data