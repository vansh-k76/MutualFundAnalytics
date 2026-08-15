-- Bluestock Mutual Fund Analytics
-- SQL Analysis Queries

-- 1. Top funds by 3-year return
SELECT scheme_name,
       fund_house,
       category,
       return_3yr_pct
FROM scheme_performance
ORDER BY return_3yr_pct DESC
LIMIT 10;


-- 2. Top funds by Sharpe Ratio
SELECT scheme_name,
       fund_house,
       category,
       sharpe_ratio
FROM scheme_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;


-- 3. Funds with lowest expense ratio
SELECT scheme_name,
       fund_house,
       category,
       expense_ratio_pct
FROM scheme_performance
ORDER BY expense_ratio_pct ASC
LIMIT 10;


-- 4. Category-wise average 3-year return
SELECT category,
       ROUND(AVG(return_3yr_pct), 2) AS avg_return_3yr_pct
FROM scheme_performance
GROUP BY category
ORDER BY avg_return_3yr_pct DESC;


-- 5. Category-wise average risk
SELECT category,
       ROUND(AVG(std_dev_ann_pct), 2) AS avg_volatility_pct,
       ROUND(AVG(max_drawdown_pct), 2) AS avg_max_drawdown_pct
FROM scheme_performance
GROUP BY category
ORDER BY avg_volatility_pct DESC;


-- 6. Fund house-wise AUM
SELECT fund_house,
       ROUND(AVG(aum_crore), 2) AS avg_aum_crore
FROM scheme_performance
GROUP BY fund_house
ORDER BY avg_aum_crore DESC;


-- 7. Monthly SIP inflow trend
SELECT month,
       sip_inflow_crore,
       active_sip_accounts_crore,
       new_sip_accounts_lakh,
       yoy_growth_pct
FROM monthly_sip_inflows
ORDER BY month;


-- 8. Category-wise net inflows
SELECT category,
       ROUND(SUM(net_inflow_crore), 2) AS total_net_inflow_crore
FROM category_inflows
GROUP BY category
ORDER BY total_net_inflow_crore DESC;


-- 9. Investor transactions by state
SELECT state,
       COUNT(*) AS transaction_count,
       ROUND(SUM(amount_inr), 2) AS total_transaction_amount
FROM investor_transactions
GROUP BY state
ORDER BY total_transaction_amount DESC;


-- 10. Investor transactions by age group
SELECT age_group,
       COUNT(*) AS transaction_count,
       ROUND(SUM(amount_inr), 2) AS total_amount_inr
FROM investor_transactions
GROUP BY age_group
ORDER BY total_amount_inr DESC;


-- 11. Portfolio sector exposure
SELECT sector,
       ROUND(SUM(weight_pct), 2) AS total_weight_pct,
       ROUND(SUM(market_value_cr), 2) AS total_market_value_cr
FROM portfolio_holdings
GROUP BY sector
ORDER BY total_weight_pct DESC;


-- 12. Benchmark performance
SELECT index_name,
       MIN(close_value) AS minimum_value,
       MAX(close_value) AS maximum_value,
       ROUND(
           (MAX(close_value) - MIN(close_value))
           * 100.0 / MIN(close_value), 2
       ) AS total_change_pct
FROM benchmark_indices
GROUP BY index_name
ORDER BY total_change_pct DESC;