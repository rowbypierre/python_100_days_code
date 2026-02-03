from datetime import datetime, timezone
from email.message import EmailMessage
from json import load
from os.path import exists
from math import hypot
from requests import request, get
import smtplib
import time


response = request(method="GET", url="https://ipinfo.io/json")
response.raise_for_status()
ip_data = response.json()

MY_COORDINATES = [float(point) for point in ip_data["loc"].split(",")]
MY_LATITUDE = MY_COORDINATES[0]
MY_LONGITUDE = MY_COORDINATES[1]
# print(MY_LONGITUDE, MY_LATITUDE)

response = get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
space_station_data = response.json()
# print(space_station_data)
space_station_location = [
    float(point) for point in space_station_data["iss_position"].values()
]
space_station_lat = space_station_location[1]
space_station_long = space_station_location[0]
# print(space_station_long, space_station_lat)

parameters = {
    "lat": MY_LATITUDE,
    "lng": MY_LONGITUDE,
    "formatted": 0,
}
response = get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
sun_data = response.json()
sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])
# print(sunrise, sunset)


def is_space_station_overhead(location, iss_location, degrees_apart):
    """
    Determine whether the International Space Station is within a given angular distance of a location.

    :param location: Latitude and longitude of the observer.
    :type location: tuple[float, float] or list[float]
    :param iss_location: Latitude and longitude of the ISS.
    :type iss_location: tuple[float, float] or list[float]
    :param degrees_apart: Maximum allowed distance in degrees.
    :type degrees_apart: float
    :return: True if ISS is within the threshold distance; otherwise False.
    :rtype: bool
    """
    time_now = datetime.now(timezone.utc).hour
    return (
        hypot(location[0] - iss_location[0], location[1] - iss_location[1])
        < degrees_apart
    ) and (time_now < sunrise or time_now > sunset)


def send_iss_email():
    """
    Send an email notification if ISS conditions are met and credentials are available.

    :return: True if the email was sent successfully; otherwise False.
    :rtype: bool
    """
    app_login = "ADD PATH HERE"
    if exists(app_login):
        app_file = open(app_login, "r")
        app_data = load(app_file)
        app_file.close()

        username = app_data["username"]
        password = app_data["password"]
        protocol = app_data["protocol"]
        port = 465

        message = EmailMessage()
        message["From"] = username
        message["To"] = username
        message["Subject"] = "TODAY IS YOUR LUCKY DAY, LOOK UP!"
        message.set_content("Data has the INTERNATIONAL SPACE STATION near you!")

        try:
            with smtplib.SMTP_SSL(host=protocol, port=port) as connection:
                connection.login(user=username, password=password)
                connection.send_message(message)
            return True
        except smtplib.SMTPException:
            return False
    else:
        print("Could not find json file containing Gmail application credentials.")


if __name__ == "__main__":
    while True:
        if is_space_station_overhead(
            location=(MY_LATITUDE, MY_LONGITUDE),
            iss_location=(space_station_lat, space_station_long),
            degrees_apart=5,
        ):
            send_iss_email()
            break
        else:
            print("ISS is not near you. Will check again in 60 seconds.")
            time.sleep(60)
