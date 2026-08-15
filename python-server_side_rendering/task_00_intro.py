#!/usr/bin/python3
"""Module that generates personalized invitation files from a template."""
import logging

logging.basicConfig(level=logging.INFO)


def generate_invitations(template, attendees):
    """Generate invitation files from a template and a list of attendees."""
    if not isinstance(template, str):
        logging.error("Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(
            isinstance(a, dict) for a in attendees):
        logging.error("Attendees must be a list of dictionaries.")
        return

    if template == "":
        logging.error("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        logging.error("No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    for index, attendee in enumerate(attendees, start=1):
        output = template
        for placeholder in placeholders:
            value = attendee.get(placeholder)
            if value is None:
                value = "N/A"
            output = output.replace("{" + placeholder + "}", str(value))

        filename = f"output_{index}.txt"
        with open(filename, "w") as file:
            file.write(output)
