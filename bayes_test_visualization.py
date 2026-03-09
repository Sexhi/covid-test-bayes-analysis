import numpy as np
import matplotlib.pyplot as plt

# Fixed sensitivity
sensitivity = 0.99

# Specificity values to compare
specificities = [0.99, 0.999, 0.9999, 0.99999]

# Prevalence from 0.001% to 50%
prevalences = np.linspace(0.00001, 0.5, 1000)

def posterior_prob(prevalence, sensitivity, specificity):
    """
    Computes P(infected | positive) using Bayes' theorem
    """
    true_positive = sensitivity * prevalence
    false_positive = (1 - specificity) * (1 - prevalence)
    return true_positive / (true_positive + false_positive)

# Plot
plt.figure(figsize=(9, 6))

for spec in specificities:
    ppv = posterior_prob(prevalences, sensitivity, spec)
    plt.plot(prevalences * 100, ppv * 100, label=f"Specificity = {spec*100:.3f}%")

plt.xlabel("Infection prevalence (%)")
plt.ylabel("P(infected | positive) (%)")
plt.title("Probability that Fred is infected given a positive test")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Integer examples for explanation
population = 100000
example_prevalences = [0.00001, 0.001, 0.01, 0.05, 0.5]

print("Integer examples with population =", population)
for prev in example_prevalences:
    for spec in specificities:
        infected = int(round(population * prev))
        not_infected = population - infected

        true_positives = int(round(infected * sensitivity))
        false_positives = int(round(not_infected * (1 - spec)))

        if true_positives + false_positives > 0:
            prob = true_positives / (true_positives + false_positives)
        else:
            prob = float("nan")

        print(
            f"Prevalence={prev*100:.3f}%, Specificity={spec*100:.3f}% "
            f"=> TP={true_positives}, FP={false_positives}, "
            f"P(infected|positive)={prob*100:.2f}%"
        )
