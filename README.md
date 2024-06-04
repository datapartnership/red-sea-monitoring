# Monitoring the Red Sea Shipping Crisis

## Assignment

The Red Sea shipping crisis is a global crisis that began in October 2023, when missile attacks on ships and tankers traversing the Red Sea caused hundreds of vessels to avoid the Suez Canal. The attacks are concentrated near the Bab al-Mandab Strait, a 20-mile-wide chokepoint for maritime traffic.

The World Bank Country Economics teams in Egypt, Yemen, and Djibouti seek to monitor the status and impacts of the crisis on their respective and regional economies. To support these efforts, a Bank team comprised of colleagues from the Data Lab and the Geospatial Operations Support Team (GOST) are using a combinat

## Data

Most of the data science products in thie repository are derived using maritime Automatic Identification System (AIS) data pulled from the [IMF PortWatch](https://portwatch.imf.org/) system and from the [UN Committee of Experts on Big Data and Data Science for Official Statistics](https://unstats.un.org/bigdata/task-teams/ais/index.cshtml), as well as conflict statistics provided by the [Armed Conflict Location and Event Data project](https://acleddata.com/).

## Reusable Data Science Products

The following data products have been prepared:

* **Maritime Choke Point Trends Monitor** for the Suez Canal, Bab el-Mandreb Straight, and the Cape of Good Hope

* **Port Call Trends Monitor** for the following ports: Aden, Al Ahmadi, Al Aqabah, Al Mukalla, As Suways, Djibouti, Duba. Duba Bulk Plant Tanker Terminal, El-Adabiya, Jiddah, Jiddah Oil, King Fahd Port, North Ain Sukhna Port, Rabigh, Safaga, and Yanbu

* **Spillover Monitor** for trade arriving in ports in Egypt, Djibouti, and Yemen

* **Missing Ships Estimator** for ships that may have disabled their transponders (forthcoming)

* **Conflict Location and Trends Monitor** derived from ACLED data

* [](notebooks/mobility/README.md) for Egypt's Red Sea Riviera through OpenStreetMap point of interest visits using GPS mobility data

Time and resources pending, the team may also investigate datasets and methods for monitoring ancillary air cargo trends.

## Insights and Indicators

The team is combining these data products to prepare high-level analytics and indicators, such as:

* Combined conflict and maritime traffic diversion trends analysis
* Combined maritime traffic diversion and global shipping price trends analysis


## License

This projects is licensed under the [**Mozilla Public License**](https://opensource.org/license/mpl-2-0/) - see the [LICENSE](LICENSE) file for details.
