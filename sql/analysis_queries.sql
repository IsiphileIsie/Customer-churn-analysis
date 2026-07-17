-- Question 1:
-- How many customers are in the dataset ?
select count(*) as total_customers from customers;

-- Question 2:
-- How many customers churned ?
select count(*) as churned_customers from customers where Churn = 'Yes';

-- Question 3:
-- Which contract type has the highest number of customers who churned ?
select Contract, count(*) as churned_customers
from customers
where Churn = 'Yes'
group by Contract
order by churned_customers desc
limit 1;

-- Question 4:
-- Which payment method has the highest number of customers who churned ?
select PaymentMethod, count(*) as churned_customers
from customers
where Churn = 'Yes'
group by PaymentMethod
order by churned_customers desc
limit 1;

-- Question 5:
-- Do senior citizens churn more than non-senior citizens ?
select SeniorCitizen, count(*) as churned_customers
from customers
where Churn = 'Yes'
group by SeniorCitizen
order by churned_customers desc;

-- Question 6:
-- Which Internet service has the highest number of churned customers ?
select InternetService, count(*) as churned_customers
from customers
where Churn = 'Yes'
group by InternetService
order by churned_customers desc;

-- Question 7:
-- What is the average monthly charge of customers who churned ?
select round(avg(MonthlyCharges),2) as average_monthly_charge
from customers
where Churn = 'Yes';

-- Question 8:
-- Which contract type has the highest average monthly charge ?
select Contract, round(avg(MonthlyCharges),2) as average_monthly_charge
from customers
where Churn = 'Yes'
group by Contract
order by average_monthly_charge;

-- Question 9:
-- What percentage of males and females churned ?
select Gender, round(sum(case when Churn = 'Yes' then 1 else 0 end) * 100.0 / count(*), 2) as churn_rate
from customers
group by Gender;

-- Question 10:
-- Which payment method generates the highest average monthly revenue ?
select PaymentMethod, round(sum(MonthlyCharges),2) as average_monthly_charge
from customers
group by PaymentMethod
order by average_monthly_charge desc;