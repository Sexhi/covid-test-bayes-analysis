# COVID Test Bayesian Analysis

This project visualizes the probability that a person is actually infected given a positive test result using Bayes' theorem.

## Model assumptions

- Sensitivity fixed at 99%
- Specificity values: 99%, 99.9%, 99.99%, 99.999%
- Prevalence from 0.001% to 50%

The script plots the posterior probability

P(infected | positive)

as a function of prevalence.

## Interpretation

When prevalence is very low, specificity has a very large effect on the probability that a positive test result is a true positive. As prevalence increases, the probability that the person is truly infected also increases.

## Integer example

To explain the result with integers, consider a population of 100,000 people.

For example:

Prevalence = 5%  
Sensitivity = 99%  
Specificity = 99%

- infected people = 5,000  
- true positives = 4,950  
- non-infected people = 95,000  
- false positives = 950
  
Therefore P(infected | positive) = 4950 / (4950 + 950) ≈ 83.9%.

This shows that even with a very accurate test, false positives still matter when prevalence is not very high.

