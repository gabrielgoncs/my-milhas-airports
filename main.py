import json

def normalize_state(state):
    return state.replace("-", " ")

def filter_and_normalize_airports(airports):
    filtered_airports = []

    for key, airport in airports.items():
        if airport["country"] == "BR":
            airport["state"] = normalize_state(airport["state"])
            filtered_airports.append(airport)

    return filtered_airports

if __name__ == "__main__":
    with open("airports.json", "r") as file:
        airports_data = json.load(file)

    filtered_airports = filter_and_normalize_airports(airports_data)

    formatted_airports = [
        {
            "icao": airport["icao"],
            "iata": airport["iata"],
            "name": airport["name"],
            "city": airport["city"],
            "state": airport["state"],
            "country": airport["country"],
            "elevation": airport["elevation"],
            "lat": airport["lat"],
            "lon": airport["lon"],
            "tz": airport["tz"]
        }
        for airport in filtered_airports
    ]

    with open("airports-br.json", "w") as output_file:
        json.dump(formatted_airports, output_file, indent=4)
