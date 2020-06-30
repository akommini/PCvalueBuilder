# PCvalueBuilder
### A recommender system that helps customers with identifying PC replacement parts with optimal value and performance.
PC market in the United States is estimated to be worth $20 billion in 2019. 40% of PCs bought experience hardware failures in the second year of use. Selecting the  replacement parts is a tedious task for novice customers due to the range of parts available in the market. For value conscious buyers, return on the investment is an important factor in making the purchase decisions. For example, the performance of hard drives(calculated using DiskMark) for the price does not scale linearly as seen below.
![HarddriveValue](/src/EDA/HDD_perf_price_fin.png)

This points out the need to optimize the value and performance to maximize the returns. Also, identifying the parts with resonable performance boost to the existing PC parts requires the extensive technical knowledge.

### Recommender system
To solve this problem, a recommender system is designed to assist customers with making these decisions. Users can select the existing PC configuration and the part they want to replace/upgrade. Our randomforest regression model calculates the PC system score for each available replacement part by pairing them with the existing PC. Users can give their preference on whether they need a part with maximum performance or maximum value (performance for the price). Also, users can input their budget constraints. Taking into consideration the user preferences and system score, 5 best available replacement part are recommended for user to choose from.

![ModelArch](/src/EDA/Architecture.png)

### Data
The performance benchmarks

### Model


### WebApp
The Web app is implemented using Streamlit and deployed on a AWS EC2 instance. The WebApp can be accessed at: https://akommini.me

### Value returns

### External Links
[Slides](https://docs.google.com/presentation/d/1LHpEzARqDha4KzdbR8knts1USW-q8ZNy6Wm3gi-RkPI/edit?usp=sharing)<br/>
[WebApp](https://akommini.me)
