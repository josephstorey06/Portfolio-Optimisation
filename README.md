**Portfolio Optimisation made using Python** 
A Python-based portfolio optimisation project analysing past stock market data to investigate the risk and return relationship.

**Overview**
In this project, I analysed 10 years of price data for 5 S&P 500 companies, investigating the efficient frontier and identifying portfolio allocations under various risk-return objectives.

**Companies Analysed**
-NVidia Corp (NVDA)
-Tesla Inc (TSLA)
-Netflix Inc (NFLX)
-Pepsi Co (PEP)
-Walt Disney Co (DIS)

**Key Features**
Historical Stock Price Analysis, Efficient Frontier Construction, Sharpe Ratio Analysis, Data Visualisation, Optimal Asset Location, Risk-Reward Calculations

**Technology Used**
-Python 
-Pandas
-Numpy
-SciPy
-Matplotlib

**Methodology**
Processed historical price data from Yahoo finance and used Pandas to convert it into returns so that I could analyse it. Then, returns and volatility is calculated and SciPy is used to optimise the portfolio weights under different objectives. These portfolios were then plotted on to a graph to visualise the efficient frontier as well as the trade-off between risk and reward.

**Results**
The project showed how optimisation can affect a portfolio's expected returns. It also helped visualise how there is a clear trade-off between risk and reward and which investment objectives were worth the risk and which were not. 

**Limitations**
I was not able to simulate real-world investment conditions and the expected returns would have differed from reality. There was also a small sample size with only 5 companies, which again limited the accuracy. 
