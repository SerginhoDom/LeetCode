import numpy as np

prices = [100, 105, 102, 108, 110]

returns = [((prices[i] - prices[i - 1]) / prices[i - 1]) for i in range(1, len(prices))]

average_return = np.mean(returns)

std_dev = np.std(returns)

risk_free_rate = 0.02

sharpe_ratio = (average_return - risk_free_rate) / std_dev

print("Средняя доходность:", average_return)
print("Стандартное отклонение:", std_dev)
print("Коэффициент Шарпа:", sharpe_ratio)