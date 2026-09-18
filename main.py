import numpy as np
import pandas as pd
import yfinance as yf
import scipy.optimize as sco
import matplotlib.pyplot as plt
 

tickers = ['NVDA', 'TSLA', 'NFLX', 'PEP', 'DIS']
data = yf.download(
	tickers,
	start='2016-01-01',
	end='2026-01-01',
	auto_adjust=False,
	progress=False,
)['Close']

if data.empty:
	raise RuntimeError('No price data was downloaded from Yahoo Finance.')

data = data.dropna(how='all').dropna(axis=1, how='all')


returns = np.log(data / data.shift(1)).dropna()


mean_returns = returns.mean()*252
cov_matrix = returns.cov() * 252

def portfolio_performance(weights):
	ret = np.sum(mean_returns * weights)
	vol = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
	return ret, vol

def min_negative_sharpe(weights, risk_free_rate=0.04):
    ret, vol = portfolio_performance(weights)
    return -(ret - risk_free_rate) / vol

num_assets = len(tickers)
init_guess = num_assets * [1.0 / num_assets]
bounds = tuple((0, 1) for _ in range(num_assets))
constraints = ({'type': 'eq', 'fun': lambda w: np.sum(w) - 1})


opt_results = sco.minimize(min_negative_sharpe, init_guess, method='SLSQP',
                           bounds=bounds, constraints=constraints)

optimal_weights = opt_results.x
opt_return, opt_volatility = portfolio_performance(optimal_weights)
opt_sharpe = (opt_return - 0.04) / opt_volatility

print(f"Optimal Weights: {dict(zip(tickers, np.round(optimal_weights, 4)))}")
print(f"Expected Return: {opt_return:.2%}, Volatility: {opt_volatility:.2%}, Sharpe: {opt_sharpe:.2f}")



portfolio_daily_returns = (returns * optimal_weights).sum(axis=1)
var_95 = np.percentile(portfolio_daily_returns, 5)
print(f"95% 1-Day Historical VaR: {var_95:.2%}")


results = np.zeros((3, 5000))
for i in range(5000):
    w = np.random.random(num_assets)
    w /= np.sum(w)
    r, v = portfolio_performance(w)
    results[0,i] = r
    results[1,i] = v
    results[2,i] = (r - 0.04) / v


plt.figure(figsize=(10, 6))
plt.scatter(results[1,:], results[0,:], c=results[2,:], cmap='viridis', marker='o', s=10, alpha=0.3)
plt.scatter(opt_volatility, opt_return, color='red', marker='*', s=200, label='Max Sharpe Ratio')
plt.colorbar(label='Sharpe Ratio')
plt.xlabel('Annualized Volatility')
plt.ylabel('Annualized Return')
plt.title('Efficient Frontier & Optimal Portfolio Weights')
plt.legend()
plt.show()