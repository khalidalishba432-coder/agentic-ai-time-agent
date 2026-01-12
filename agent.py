import requests

def get_time(city):
    city_timezones = {
        "lahore": "Asia/Karachi",
        "peshawar": "Asia/Karachi",
        "new york": "America/New_York"
    }

    city = city.lower()

    if city not in city_timezones:
        return "Sorry, I don't know this city."

    timezone = city_timezones[city]
    url = f"https://worldtimeapi.org/api/timezone/{timezone}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        datetime = data["datetime"]
        time = datetime.split("T")[1].split(".")[0]
        return f"Current time in {city.title()} is {time}"
    else:
        return "Error fetching time."

print("🤖 Time AI Agent Started")
print("Type city name or 'exit' to quit")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Agent stopped.")
        break

    print("Agent:", get_time(user_input))