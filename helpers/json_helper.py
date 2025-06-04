import json


class JsonHelper:
    """
    Helper class to get the json data from the file
    """

    @staticmethod
    def get_json_data(file_path):
        """
        Get the json data from the file
        """
        try:
            with open(file_path, encoding="utf-8") as f:
                json_data = json.load(f)
            return json_data
        except FileNotFoundError:
            # handel all json errors
            print(f"Error loading JSON file: {file_path}")
            return None
