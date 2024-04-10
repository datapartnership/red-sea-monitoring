import requests
import pandas as pd
from datetime import datetime

def get_chokepoints():
    chokepoints_url = "https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/PortWatch_chokepoints_database/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json"
    res = requests.get(chokepoints_url)
    df_chokepoints = pd.DataFrame([d["attributes"] for d in res.json()["features"]])
    return df_chokepoints

# build function to get chokepoint data based on code above for multiple offests
def get_chokepoint_data(chokepoints):
    url_base = "https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/Daily_Chokepoints_Data/FeatureServer/0/query?where="
    for chokepoint in chokepoints:
        if chokepoint == chokepoints[-1]:
            url_base += f"portid%3D%27{chokepoint}%27&outFields=*&outSR=4326&f=json&resultOffset=0"
        else:
            url_base += f"portid%3D%27{chokepoint}%27+OR+"
    res = requests.get(url_base)
    df = pd.DataFrame([d["attributes"] for d in res.json()["features"]])
    df.loc[:, "date"] = df.date.apply(lambda x: datetime.fromtimestamp(x / 1000))
    offset = 1000
    while len(df) % 1000 == 0:
        res = requests.get(url_base.replace("resultOffset=0", f"resultOffset={offset}"))
        df2 = pd.DataFrame([d["attributes"] for d in res.json()["features"]])
        df2.loc[:, "date"] = df2.date.apply(lambda x: datetime.fromtimestamp(x / 1000))
        df = pd.concat([df, df2])
        offset += 1000
    df.reset_index(inplace=True, drop=True)
    df.sort_values(["portid", "date"], inplace=True)
    return df

def get_ports():
    base_url = "https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/PortWatch_ports_database/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json&resultOffset=0"
    res = requests.get(base_url)
    df = pd.DataFrame([d["attributes"] for d in res.json()["features"]])
    offset = 1000
    while len(df) % 1000 == 0:
        res = requests.get(base_url.replace("resultOffset=0", f"resultOffset={offset}"))
        df2 = pd.DataFrame([d["attributes"] for d in res.json()["features"]])
        df = pd.concat([df, df2])
        offset += 1000
    df.reset_index(inplace=True, drop=True)
    return df

def get_port_data(ports):
    url_base = "https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/Daily_Trade_Data/FeatureServer/0/query?where="
    for port in ports:
        if port == ports[-1]:
            url_base += (
                f"portid%3D%27{port}%27&outFields=*&outSR=4326&f=json&resultOffset=0"
            )
        else:
            url_base += f"portid%3D%27{port}%27+OR+"
    res = requests.get(url_base)
    df = pd.DataFrame([d["attributes"] for d in res.json()["features"]])
    df.loc[:, "date"] = df.date.apply(lambda x: datetime.fromtimestamp(x / 1000))
    offset = 1000
    while len(df) % 1000 == 0:
        res = requests.get(url_base.replace("resultOffset=0", f"resultOffset={offset}"))
        df2 = pd.DataFrame([d["attributes"] for d in res.json()["features"]])
        df2.loc[:, "date"] = df2.date.apply(lambda x: datetime.fromtimestamp(x / 1000))
        df = pd.concat([df, df2])
        offset += 1000
    df.reset_index(inplace=True, drop=True)
    df.sort_values(["portid", "date"], inplace=True)
    return df