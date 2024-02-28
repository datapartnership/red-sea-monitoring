import os
import requests
import pandas as pd


def acled_api(
    email_address=None,
    access_key=None,
    country=None,
    region=None,
    start_date=None,
    end_date=None,
    add_variables=None,
    all_variables=False,
    dyadic=False,
    interaction=None,
    other_query=None,
):
    # Access key
    access_key = access_key or os.getenv("ACLED_ACCESS_KEY")
    if not access_key:
        raise ValueError(
            "ACLED requires an access key, which needs to be supplied. You can request an access key by registering on https://developer.acleddata.com/."
        )

    # Email address
    email_address = email_address or os.getenv("ACLED_EMAIL_ADDRESS")
    if not email_address:
        raise ValueError(
            "ACLED requires an email address for access. Use the email address you provided when registering on https://developer.acleddata.com/."
        )

    # Building the URL
    url = "https://api.acleddata.com/acled/read/?key={}&email={}".format(
        access_key, email_address
    )

    if country:
        url += "&iso=" + "|".join(str(iso) for iso in country)

    if region:
        url += "&region=" + "|".join(str(region) for region in region)
    if start_date and end_date:
        url += "&event_date={}|{}&event_date_where=BETWEEN".format(start_date, end_date)

    fields = "region|country|year|event_date|source|admin1|admin2|admin3|location|event_type|sub_event_type|interaction|fatalities|timestamp|latitude|longitude"
    if all_variables:
        fields = ""
    elif add_variables:
        fields += "|" + "|".join(add_variables)
    url += "&fields=" + fields

    # if dyadic:
    #     url += "&export_type=dyadic"
    # else:
    #     url += "&export_type=monadic"

    if interaction:
        url += "&interaction=" + ":".join(str(i) for i in interaction)

    if other_query:
        url += "&" + "&".join(other_query)

    # Making the GET request
    response = requests.get(url)
    if not response.ok:
        raise Exception(
            "GET request was unsuccessful. Status code: {}".format(response.status_code)
        )

    # Parsing JSON response
    data = response.json()
    if not data.get("success", False):
        raise Exception(
            "GET request wasn't successful. Error: {}".format(data.get("error", ""))
        )

    return pd.DataFrame(data["data"])


# Example usage:
# data = acled_api(email_address="your_email_here", access_key="your_access_key_here", country=["Kenya", "Uganda"], start_date="2020-01-01", end_date="2020-12-31")
# print(data)
