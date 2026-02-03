# ISS Overhead Email Notifier

A small Python project that checks whether the **International Space Station (ISS)** is near your current location and sends you an **email alert** when it is overhead at night.

This project is part of a Python bootcamp and focuses on **APIs, datetime, and email automation**.

---

## What This Project Does

- Detects your approximate location using your IP address
- Fetches the current ISS position from a public API
- Checks sunrise and sunset times for your location
- Determines if:
  - The ISS is within a given distance
  - It is currently dark
- Sends you an email telling you to **look up**

---

## APIs Used

- IP location: https://ipinfo.io
- ISS position: http://api.open-notify.org
- Sunrise/Sunset times: https://sunrise-sunset.org/api

---

## File Structure

```
day033_intl_space_station_api/
│ main.py
│ config.py
```

---

## Requirements

```
python3
requests
```

Uses Python standard library modules:
- datetime
- math
- smtplib
- email
- json
- time
- os

---

## Email Setup

This project expects an existing `login.json` file containing:

```json
{
  "username": "your_email@gmail.com",
  "password": "your_app_password",
  "protocol": "smtp.gmail.com"
}
```

> Gmail requires an **App Password**, not your normal password.

---

## How It Works (High Level)

1. Get your latitude and longitude
2. Get the ISS latitude and longitude
3. Compare the distance between them
4. Check if current time is after sunset
5. If conditions match → send email
6. Repeat every 60 seconds until triggered

---

## Run

```
python main.py
```

Stop the program with:

```
Ctrl + C
```

---

## Notes

- Distance checks are approximate (degrees, not kilometers)
- Time comparisons are done in UTC
- Built for learning, not production use
