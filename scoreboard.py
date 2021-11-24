import json

class Score:
    def __init__(self, filename):
        self.filename = filename

    def insert(self, name, score):
        new_data = {
            name: score
        }
        try:
            with open(f"{self.filename}.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open(f"{self.filename}.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            try:
                if score >= data[name]:
                    data.update(new_data)
                    with open(f"{self.filename}.json", "w") as data_file:
                        json.dump(data, data_file, indent=4)
            except KeyError:
                data.update(new_data)
                with open(f"{self.filename}.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

    def sort_score(self):
        with open(f"{self.filename}.json", "r") as data_file:
            data = json.load(data_file)
        scoreboard = sorted(data.items(), key=lambda x: x[1], reverse=True)
        return scoreboard

