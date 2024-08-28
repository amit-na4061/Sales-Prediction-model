Step 1 Business Problem understanding
- Identify relationship between total advetizing spend and sales?
- Our Next ad-campaign will have a total of $200,000 how many unit do we expect to sell as well a result of this?

Step 2 Data Understanding

Data
- This sample data displays sales for a partivular product as a fucntion of advertizing budget (in dollars) for TV, Radio and Newspaper

Independent Variable
- TV : Advertising dollar spend on TV for a single prodcut in a given market (in dollars)
- Radio: Advertizing dollars spend on Radio- Newspapers: Advertizing dollars spend on Newspapers

Target/Dependent Variable
- Sales: Sales of a single prodcut in giver market
- Collect & Load Data
- Dataset Understanding

Step 3 - Data Preprocessing

Step 4 Modelling

Step - 5 Evaluation

Check for the Error ( Model Goodness)
Model Selection
- Checklist 1 : check wthether model is good or either having overfitting/underfitting problem
  test accuracy = train accuracy
- Cheklist 2 : whether the test accuracy = cross validation score
- Checklist 3 Check whether, it satisfies the business problem requirments
- Checklist 4 ( only for Linear Regression) Check for assumptions
1. Lenearity of Error
2. Noramlity of Error
3. Equal Variance of Errors ( Homoscandensicity)
4. Variable Significance
5. Final Model
  Sales = 0.04860551 (Total Spend) + 4231.42788361
Intercepting & Coefficient
1 unit increase in total spend is associated with an increase of 0.0486 unit in sales. This basically means that for every $10000 dollars spend on ads, we could expect 487
more unit of sold.
**Business Problem** - Use the model to predictions on a new value. for a total spend on 200K on ads, how many units could we expect to be sold?
