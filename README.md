# PCvalueBuilder
### A recommender system that helps customers with identifying PC replacement parts with optimal value and performance.
PC market in the United States is estimated to be worth $20 billion in 2019. 40% of PCs bought experience hardware failures in the second year of use. Selecting the  replacement parts is a tedious task for novice customers due to the range of parts available in the market. For value conscious buyers, return on the investment is an important factor in making the purchase decisions. For example, the performance of hard drives(calculated using DiskMark) for the price does not scale linearly as seen below.
![HarddriveValue](/src/EDA/HDD_perf_price_fin.png)

This points out the need to optimize the value and performance to maximize the returns. Also, identifying the parts with resonable performance boost to the existing PC parts requires the extensive technical knowledge.

## Recommender system
To solve this problem, a recommender system is designed to assist customers with making these decisions. Users can select the existing PC configuration and the part they want to replace/upgrade. Our randomforest regression model calculates the PC system score for each available replacement part by pairing them with the existing PC. Users can give their preference on whether they need a part with maximum performance or maximum value (performance for the price). Also, users can input their budget constraints. Taking into consideration the user preferences and system score, 5 best available replacement part are recommended for user to choose from.

![ModelArch](/src/EDA/Architecture.png)

## Data
Right now, the model can work with four different PC components:
- Processor
- Graphics Card (GPU)
- Hard Drive
- Memory (RAM)

Available replacement parts are suggested to one of components given the other three components in the exisitng system are selected. The performance data ont the available parts for these components are extracted from PassMark database. 
- CPU Mark - 2600 Processor options
- G3D Mark - 3000 GPU options
- Disk Mark - 1100 Hard Drive options
- Memory Mark - 1175 Memory (RAM) options

The price and technical data is extracted from PassMark database, Newegg and Manufacturer's website.

## Model


## WebApp
The Web app is implemented using Streamlit and deployed on a AWS EC2 instance. The WebApp can be accessed at: https://akommini.me

## Value returns
Part type | Value return
------------ | -------------
Processor| 1.5x - 9x
Graphics card (GPU) | 1.4x - 3x
Memory (RAM) | 1.5x - 9x
Hard disk | 1.2x - 2x
## External Links
[Slides](https://docs.google.com/presentation/d/1LHpEzARqDha4KzdbR8knts1USW-q8ZNy6Wm3gi-RkPI/edit?usp=sharing)<br/>
[WebApp](https://akommini.me)
