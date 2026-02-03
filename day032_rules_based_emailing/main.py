import os
import json
import smtplib
import datetime
import random
import calendar
import pandas
import re


def get_filepath(filename, root="."):
    """
    Return the absolute file path to a file.

    :param filename: Name of the file (e.g. 'filename.txt').
    :type filename: str
    :param root: Absolute parent directory path where search begins.
    :root type: str
    :return: Full file path or empty string if file not found.
    :rtype: str
    """
    for parent, _, files in os.walk(root):
        if filename in files:
            return os.path.join(parent, filename)
    return ""


def is_monday():
    """
    Return True if today is Monday; otherwise, Return False.
    """
    monday = 0
    return datetime.datetime.now().weekday() == monday


def email_monday_quote(login_file=None, to_email=None):
    """
    Send email of motivational quote if weekday is Monday.
    Original quotes: https://gist.github.com/robatron/a66acc0eed3835119817

    :param login_filename:  Name of file containing dictionary of username, password, simple mail transfer protocol.
                            For example "credentials.json"
    :type login_filename: str
    :param to_email: Recipient email address.
    :type to_email: str
    """
    if is_monday():
        quotes_path = get_filepath("quotes.txt")
        with open(quotes_path) as quote_file:
            quotes = quote_file.read().splitlines()

        login_path = (
            get_filepath("login.json") if not login_file else get_filepath(login_file)
        )
        with open(login_path, "r") as login_file:
            login_data = json.load(login_file)

        with smtplib.SMTP(host=login_data["protocol"]) as connection:
            connection.starttls()
            connection.login(
                user=login_data["username"], password=login_data["password"]
            )

            recipient = login_data["username"] if not to_email else to_email
            connection.sendmail(
                from_addr=login_data["username"],
                to_addrs=recipient,
                msg=f"""Subject:What a Beautiful Monday
                \n\nHere is some motivation: {quotes[random.randint(a=0, b=len(quotes))]}""",
            )
    else:
        print(
            f"""Motivation emails are only sent out on Monday.\n
            Enjoy your {calendar.day_name[datetime.datetime.now().weekday()]}!!!"""
        )


if __name__ == "__main__":
    ##################### Extra Hard Starting Project ######################
    def manage_birthdate(name, email, year, month, day, mode, filename=None):
        """
        Manage birthday records by adding, updating, or removing entries in a CSV file.

        :param name: Full name of the person.
        :type name: str
        :param email: Email address of the person.
        :type email: str
        :param year: Birth year.
        :type year: int
        :param month: Birth month.
        :type month: int
        :param day: Birth day.
        :type day: int
        :param mode: Operation to perform ("add", "update", "remove").
        :type mode: str
        :param filename: Optional CSV filename override.
        :type filename: str or None
        :return: None
        :rtype: None
        """
        modes = ["add", "update", "remove"]
        mode = mode.lower().strip()

        if mode in modes:
            birthdays_path = (
                get_filepath("birthdays.csv")
                if not filename
                else get_filepath(filename=filename)
            )
            birthdays = pandas.read_csv(birthdays_path)
            birthdays = birthdays.to_dict(orient="records")
            print(birthdays)

            birthdate = {
                "name": name.lower().title(),
                "email": email.lower(),
                "year": year,
                "month": month,
                "day": day,
            }
            birthdate_exist = birthdate in birthdays

            if mode == "update":
                for record in birthdays:
                    if (
                        record.get("name") == birthdate.get("name")
                        and record.get("year") == birthdate.get("year")
                        and record.get("month") == birthdate.get("month")
                        and record.get("day") == birthdate.get("day")
                    ) or record.get("email") == birthdate.get("email"):
                        birthdays.remove(record)
                        birthdays.append(birthdate)
            elif birthdate_exist:
                if mode == "remove":
                    birthdays.remove(birthdate)
            elif not birthdate_exist:
                if mode == "add":
                    birthdays.append(birthdate)

            birthdays = pandas.DataFrame(birthdays)
            birthdays.to_csv(birthdays_path, header=True, mode="w", index=False)
        else:
            print(f"Invalid mode provided. Mode options: {modes}")

    # 2. Check if today matches a birthday in the birthdays.csv
    def get_today_birthday():
        """
        Retrieve all birthday records that match today's date.

        :return: List of dictionaries containing name and email for today’s birthdays.
        :rtype: list[dict]
        """
        birthdays_path = get_filepath("birthdays.csv")
        birthdays_df = pandas.read_csv(birthdays_path)
        birthdays_dict = birthdays_df.to_dict(orient="records")
        birtdays_today = [
            {"name": record["name"], "email": record["email"]}
            for record in birthdays_dict
            if not datetime.date(
                year=record["year"], month=record["month"], day=record["day"]
            )
            == datetime.date.today()
        ]

        return birtdays_today

    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    def generate_birthday_letter(birthday_fullname, sender_firstname):
        """
        Generate a personalized birthday letter from a random template.

        :param birthday_fullname: Full name of the birthday recipient.
        :type birthday_fullname: str
        :param sender_firstname: First name of the sender.
        :type sender_firstname: str
        :return: Completed birthday letter text.
        :rtype: str
        """
        templates_path = (
            "/home/rolarrin/projects/python_100_days_code/day032/letter_templates"
        )
        letter_path = random.choice(
            [
                filepath
                for filepath in os.listdir(templates_path)
                if not filepath.upper().endswith(".IDENTIFIER")
            ]
        )

        with open(os.path.join(templates_path, letter_path), "r") as letter:
            modified_letter = letter.readlines()
            modified_letter[0] = modified_letter[0].replace("[NAME]", birthday_fullname)
            modified_letter[-1] = re.sub(
                pattern=r"\w+", repl=sender_firstname, string=modified_letter[-1]
            )
            letter_string = "".join(modified_letter)

        return letter_string

    # 4. Send the letter generated in step 3 to that person's email address.
    def email_birthday_letters():
        """
        Send birthday emails to all recipients whose birthday is today.

        :return: None
        :rtype: None
        """
        birthday_dict = get_today_birthday()
        is_birthday_today = bool(birthday_dict)
        if is_birthday_today:
            for birthday in birthday_dict:
                birthday_letter = generate_birthday_letter(
                    birthday_fullname=birthday["name"], sender_firstname="My Name"
                )

                login_path = get_filepath("login.json")
                with open(login_path, "r") as login_file:
                    login_data = json.load(login_file)

                with smtplib.SMTP(host=login_data["protocol"]) as connection:
                    connection.starttls()
                    connection.login(
                        user=login_data["username"], password=login_data["password"]
                    )

                    connection.sendmail(
                        from_addr=login_data["username"],
                        to_addrs=birthday["email"],
                        msg=f"""Subject:HAPPY HAPPY BIRTHDAY!
                        \n\n{birthday_letter}""",
                    )
