# CSCI-5502-Group-16
This repository is used to store and manage all work related to our group project, including code, documentation, and supporting files.

## Research Topic Summary

We examine financial fraud detection in large data sets
This project evaluates and compare supervised and unsupervised fraud detection methods
The goal with this project is to identify patterns and understand the trade-offs with different approaches
Model performance will be compared to understand the strengths and limitations of each approach in real-world fraud detection scenarios

## Scope & Boundaries

### What is in scope?
Transaction data from various datasets
Evaluation of model performance across different cases
Tradeoff analysis between accuracy and detection

### What is out of scope?
Real time fraud detection
Integration with other systems
Scalability across millions of transactions

## Research Questions
This project explores ten core research questions spanning descriptive, comparative, and predictive analysis to evaluate the efficacy of fraud detection methodologies.

1. Model Comparison: How do supervised models and unsupervised anomaly detectors compare at catching rare fraud as we vary the fraud rates and the "cost" of false alarms?

2. Impact of Class Imbalance: How exactly does the severity of class imbalance (meaning how rare the fraud actually is) impact the performance of supervised models?

3. Prevalence Sensitivity: Does changing the fraud prevalence have a different effect on the success of unsupervised detection methods?

4. Operational Constraints: If we assume a fixed "alert budget" where a team can only check the top-K transactions, which of these two methods actually performs better?

5. Precision-Recall Trade-offs: What do the real-world trade-offs between precision and recall look like for each approach as we shift our alert thresholds?

6. Feature Significance: Which specific transaction features show the biggest "red flags" that allow us to separate fraud from legitimate activity?

7. Ranking Performance: Do unsupervised scores do a better job of putting real fraud at the very top of the rankings compared to supervised probabilities?

8. Generalizability: Are these fraud patterns and trade-offs stable enough to hold up across different datasets with varying structures?

9. Cluster Identification: Can we use clustering techniques to find specific "pockets" of transactions where fraud is much more likely to hide?

10. Optimization Conditions: Under what specific conditions balancing the rarity of the fraud and the cost of an alert does one of these approaches finally outperform the other?

## Our Team

### Data Lead
Kayo Abdi is in charge of data collection, preprocessing the data, ensuring quality. He maintains the datasets for analysis, while also deleivering a foundation for modeling and evaluation.

### Modeling Lead
David Savić spearheads on the development of machine learning models for fraud detection, focusing on supervised and unsupervised approaches. His work emphasizes evaluating model performance.

### Evaluation Metrics and Lead
Sawyer McKenney designs the framework for evaluating the models and examining model performance using appropriate metrics. His role focuses on comparing trade-offs and ensuring accurate results.

### Vizualization Lead
Sam Meaux heads the design of data visualizations for the project. He focuses on moving complex results into clear, interpretable visuals and effective communication of our findings.

## Milestone Outline

### Milestone 1: Project Framing & Website Launch
Due: Mon Feb 9, 2026

### Milestone 2: Data Preparation/Collection & Cleaning
Due: Fri Mar 6, 2026

### Milestone 3: Model Implementation
Due: Fri Apr 3, 2026

### Milestone 4: Conclusion, Results & Project Report
Due: Fri Apr 17, 2026

## Project Website

Built with [SvelteKit](https://svelte.dev/docs/kit). Three pages:

- **/** — Introduction and project overview
- **/team** — Team member profiles
- **/proposal** — Research proposal summary

### Getting Started

```bash
npm install
npm run dev
```

Open [http://localhost:5173](http://localhost:5173) to view the site.

### Build for Production

```bash
npm run build
npm run preview
```

## AI Attribution

CSS styles in this project were generated and/or assisted by AI (Claude, Anthropic). Each `<style>` block in the Svelte components contains a comment noting this. The site layout, structure, and page scaffolding were also created with AI assistance.
