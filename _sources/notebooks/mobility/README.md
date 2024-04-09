# Economic Impacts on Tourism

Understanding where and when population movement occurs and analyzing the frequency of visits within or near points of interest has the potential to provide insights into the economic ramifications of conflicts and disasters.

## Data

The project team acquired longitudinal human mobility data. The mobility data was provided pro-bono by [Veraset](https://veraset.com) for the proposal [Measure Activity Levels on Tourism Sites Affected by the 2023 Red Sea Crisis](https://portal.datapartnership.org/readableproposal/565) through the [Development Data Partnership](https://datapartnership.org). During the project’s implementation, [Veraset Movement](https://www.veraset.com/products/movement/)’s global daily data feed was ingested and processed by the [Development Data Partnership](https://datapartnership.org/) through the [Mobility](https://docs.datapartnership.org/collections/mobility/README.html) pipeline. For additional information, please refer to the [Mobility Documentation](https://docs.datapartnership.org/collections/mobility/README.html) accessible to all eligible [Development Partners](https://datapartnership.org/).

### Data Availability Statement

Data are available upon request through the [Development Data Partnership](https://datapartnership.org). Licensing and access information for all other datasets are included in the documentation.

## Results

```{caution}
The following working methodologies are currently under development and await review.
```

- [Estimating Activity Through Point of Interest Visits Using Mobility Data](./visits.ipynb)

After an initial exercise, we conclude that the available [mobility data](#data) is not adequate to estimate general population movement and the impact on Egypt's tourism inflicted by the crisis. Although the mobility data panel provides [billions of locations on a daily basis throughout Egypt](./visits.ipynb#mobility-data), the Red Sea and South Sinai governorates only account for a fraction of this volume, of which only a small fraction can be identified within points of interest. For example, based on the analysis, **hotels would see about 100 daily visitors**.

Additionally, it’s important to note the inherent limitations associated with using mobility data. Notably, mobility data is typically collected through convenience sampling methods and lacks the controlled methodology of randomized trials. The adoption and usage of mobile devices differ greatly among urban, suburban, and rural dwellers. Moreover, the popularity of specific mobile apps can fluctuate over time with the introduction of new apps and the decline of older ones or the exclusion of important apps in the panel.
