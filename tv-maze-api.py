import requests

class Season():
    def __init__(self, name):
        self.name = name
        self.seasons = None
        self.seasons_api_call(name)
        
    def seasons_api_call(self, query = ''):
        #api call for the query of which show to pull up
        data = None
        while not data:
            if not query:
                query = input('What is the name of the series?')
            r = requests.get(f'https://api.tvmaze.com/singlesearch/shows?q={query}')
            if r.status_code == 200:
                data = r.json()
#                print(data)
            else:
                print(f"Series error: status code {r.status_code}")

        # api call for the episodes
        r = requests.get(f'https://api.tvmaze.com/shows/{self.name}/seasons')
        if r.status_code == 200:
            data = r.json()
        else:
            print(f"Season Error: Status Code {r.status_code}")
                
        self.seasons = []
        for season in data:
            self.seasons.append(season['name']) 

first_show = Season()
first_show.seasons_api_call()
        