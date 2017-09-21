# Volatility Prediction

### Importance of Predicting Volatility
Volatility is up-and-down movement of the market. It's usually measured by the standard deviation from the expectation. Volatility is criticle when it comes to investment. Return isn't the only thing that matters. For most people who are risk averse, the objective for investment is to maximize the return with minimized risks. The traditional method in financial application of risk measurement is to calculate the historical standard deviation as the prediction of future volatility. However, this may not render the most accurate prediction of future volatility as historical data does not reflect information in the future.

### New Approach to Volatility Prediction
Our new approach to predict volatility is to use a combination of market, industry and company factors to shed lights on future return risk. Specifically, we want to predict the risk in Information Technology Sector.

Our input data would include:

Market Factors: S&P 500, DJI, NASDAQ, etc.
Industry Factors: Google Trend, S&P500 Information Technology, Industry specific PPI, etc.
Company Factors: Google Trend, P/E, Market Cap, EBITDA, Turnover, Liquidity ratio, etc.

Each factor category contains information that would influence equity price, and thus the volatility from each factor would influence and reflect on the volatility for specfic stock. For example, Brexit introduces global market volatility, and thus it would reflect on stock price of large cap company that has a global exposure. And, company specific factors like low liquidity ratio probably implies that the company is more vulnerable to market shock.
