import json

# Reads credentials from a JSON file.
def read_credentials(filename):
    try:
        with open(filename) as json_data:
            creds = json.load(json_data)
            return creds
    except IOError:
        print("Credentials file '" + filename + "' not found")

    print("Valid creds file not found")
