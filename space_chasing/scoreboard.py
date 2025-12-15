import json


class Score:
    """
    Define a score with filename
    """

    def __init__(self, filename):
        """
        initialize new score
        :param filename: string
        """
        self.filename = filename

    def insert(self, name, score):
        """
        insert new score with player name to scoreboard.json
        :param name: Player name(string)
        :param score: int
        """
        new_data = {name: score}
        try:
            with open(f"{self.filename}.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open(f"{self.filename}.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # check player name in data file or not if not add new and
            # check new score that player can do is greater than last time or not
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
        """
        sort all score in scoreboard.json from highest to lowest
        :return: list of sorted score
        """
        with open(f"{self.filename}.json", "r") as data_file:
            data = json.load(data_file)
        scoreboard = sorted(data.items(), key=lambda x: x[1], reverse=True)
        # lambda use for create short func in this code use for get values
        return scoreboard
