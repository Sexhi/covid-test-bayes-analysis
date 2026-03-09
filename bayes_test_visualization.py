import numpy as np
import matplotlib.pyplot as plt

sensitivity = 0.99
specificities = [0.99, 0.999, 0.9999, 0.99999]
prevalences = np.linspace(0.00001, 0.5, 1000)

def posterior_prob(prevalence, sensitivity, specificity):
    true_positive = sensitivity * prevalence
    false_positive = (1 - specificity) * (1 - prevalence)
    return true_positive / (true_positive + false_positive)

plt.figure(figsize=(9,6))

for spec in specificities:
    ppv = posterior_prob(prevalences, sensitivity, spec)
    plt.plot(prevalences*100, ppv*100, label=f"Specificity {spec*100:.3f}%")

plt.xlabel("Prevalence (%)")
plt.ylabel("P(Infected | Positive) (%)")
plt.title("Probability of infection given a positive test")
plt.legend()
plt.grid(True)

plt.show()
