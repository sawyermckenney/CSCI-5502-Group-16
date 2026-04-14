<script lang="ts">
	import { onMount } from 'svelte';

	interface ContentBlock {
		type: 'text' | 'image';
		value: string;
		caption?: string;
	}

	interface CardData {
		id: string;
		title: string;
		label: string;
		color: string;
		preview: string;
		content: ContentBlock[];
	}

	function text(value: string): ContentBlock {
		return { type: 'text', value };
	}

	function image(src: string, caption: string): ContentBlock {
		return { type: 'image', value: src, caption };
	}

	const cards: CardData[] = [
		{
			id: 'intro',
			title: 'Introduction',
			label: 'Overview',
			color: '#ec4899',
			preview: 'The challenge of our selected project was creating models that were able to detect fraud in a dataset where only 1.1% of all transactions were fraudulent.',
			content: [
				text(`The challenge of our selected project was creating models that were able to detect fraud in a dataset where only 1.1% of all transactions were fraudulent. In a dataset of nearly 1 million transactions, a model that ignored all fraud and labeled all transactions as non-fraudulent would perform with 98.9% accuracy. The shared goal for this assignment, the goal was to prioritize "recall" (catching fraud) over "accuracy." For our Milestone 3 approach, our team implemented four distinct model combinations, leveraging various methods and combinations to detect fraud bank account applications within the Bank Account Fraud (BAF) dataset by Feedzai. Each member of the team implemented their own algorithm and technique. By doing this, we were able to compare supervised classification, along with unsupervised clustering and ensemble methods. Our approach includes Decision Trees, Support Vector Machines (SVM), Logistic Regression, K-Nearest Neighbor (KNN), K-Means Clustering, Apriori Association Rule Mining, and combination methods such as stacking and soft voting. This has allowed our team to evaluate which approaches are more effective at handling class imbalances.`),
				text(`We chose to use Decision Trees because they give clear, rule-based splits that help us understand what features might contribute to fraud predictions. This method also does not require as much preprocessing and is simpler to use with mixed feature types.`),
				text(`Support Vector Machines (SVM) were chosen to separate data into groups methodically where there are a lot of features. In this case, our raw data set had over 30 features (both quantitate and categorical). The SVM method helps to catch fraudulent transactions in certain cases where a straight-line method might miss them.`),
				text(`K-Nearest Neighbors (KNN) was used as a distance-based approach. This model does not really "learn" one big model ahead of time. Instead, it compares the new tuple to the stored data and decides based on similar cases which group it belongs to. This allowed us to test if local patterns were capable of identifying fraud.`),
				text(`Stacking and Ensemble Methods were used to combine the different strengths of individual models into a single model. Soft voting along with stacking was used to intelligently determine the weight of model outputs. Both of these models aimed to improve the overall robustness of the model.`),
				text(`K-Means Clustering was an unsupervised learning approach we decided to test out, not expecting it to provide very much information because of the nature of the data we are dealing with. It was used to see if fraud appears in identifiable segments.`),
				text(`Apriori Association Rule Mining was used because it helps identify easy to understand patterns in data instead of predicting. For example, we were curious to see if it was able to show if parameters like high credit risk and foreign requests appear together or not. This method helps provide very valuable insights into fraud analysis.`),
				image('/models/fig1_preprocessed_snapshot.png', 'Figure 1: Preprocessed Data Snapshot'),
				image('/models/fig2_postprocessed_snapshot.png', 'Figure 2: Post-Processed Data Snapshot'),
			]
		},
		{
			id: 'model1',
			title: 'Model 1 (Samuel Meaux)',
			label: 'Samuel Meaux',
			color: '#a855f7',
			preview: 'Class Imbalance Handling using Decision Tree, Support Vector Machine, Ensemble and Stacking',
			content: [
				text(`For this analysis, nine modeling architectures were tested but ultimately only 5 were kept: Decision Tree, Support Vector Machine (SVM), Logistic Regression, Ensemble (Soft Voting), and Stacking. These models were selected to determining the ultimate method for determining fraudulent account creation methods in an imbalanced dataset utilizing an artificially balanced training set.`),
				text(`Missing Data Signals: At the beginning of the preprocessing pipeline, placeholder values of "-1" were replaced with NaN and "missingness" indicator flags were created for the features "prev_address_months_count" and "bank_months_count." This method took the data and treated all the missing values as a feature that is behavioral in nature rather than just plain noise.`),
				text(`Feature Selection: Using the LassoCV function, the data was streamlined to the most significant features. This, however, only tailored down the total number of features from 49 to 47, which was surprising. Even though it wasn't tailored much, this method was able to ensure that all future computations and all future and model implementations were conducted efficiently.`),
				text(`Class Imbalance Handling: Only 1.1% of the entire dataset were fraudulent transactions. To manage this, Random Undersampling (RUS) was utilized to build a balanced training set (11,029 samples per class). This was critical in preventing the models from ignoring the examples of fraud. Initially, Oversampling was attempted but caused extremely lengthy model run times and was subsequently removed from our handling methods.`),
				text(`Decision Tree: A max depth of 12 was found to provide the highest accuracy and provided a clear and rule-based baseline, while at the same time, was capable of preventing overfitting.`),
				text(`SVM: It was assumed that the "separability" was none linear for this SVM model. Due to the complexity associated with this large amount of features and such limited examples of fraud, it was determined that a standard linear hyperplane would not be adequate for this model. In order to distinguish classes, a radial basis function (RBF) kernel was used in combination with a balanced class weight standard to capture any non-linear fraud patterns. The features were scaled using the "StandardScaler" function to ensure the SVM was capable of accurately calculating all of the distance boundaries present in the data.`),
				text(`Logistic Regression (Linear Model): It was assumed that the independent variables and the "log-odds" of the target class had a linear relationshiop for this model. In order to meet standalone linear model requirements, LR was done using a StandardScaler with a max iterations of 1,000 in order to ensure a convergence was observed.`),
				text(`Aggregations: A Soft Voting Ensemble (voting based on probabilities) was implemented based on the assumption of model variety. By choosing to utilize three different model types (Decision Tree, SVM, and LR models) this aggregation method effectively determined from the accuracy/well-calibrated probabilities which result was the ultimate correct choice. Additionally, a Stacking Classifier was developed using a Logistic Regression component as a "meta-learner" to smartly collect the outputs of the primary models and weigh them accordingly.`),
				image('/models/fig3_stacking_confusion_matrix_balanced.png', 'Figure 3: Stacking Confusion Matrix (Balanced Test Set)'),
				image('/models/fig4_model_comparison_balanced.png', 'Figure 4: Model Comparison of Performance (Balanced Test Set)'),
				image('/models/fig5_lr_confusion_matrix_full.png', 'Figure 5: Logistic Regression Confusion Matrix (Full/Imbalanced Test Set)'),
				image('/models/fig6_model_comparison_full_imbalanced.png', 'Figure 6: Model Comparison (Balanced-Tested Models on Full Imbalanced Dataset)'),
				text(`Issues and Improvements: The first issued occurred while training SVMs on a large dataset. When attempting to train on a Random Oversampled data set, the model did not finish and was ultimately not usable. Because of this, in the rest of the models, RUS was implemented. This ended up providing a high recall of 79% (Stacking) while maintaining manageable training times. Similar results were found in the full testing (high recall) yet there were low F1-Scores in the full testing. Future models will seek to improve F1-Scores and reduce the amount of "false alarms" that were so heavily prevalent in these models.`),
				text(`Class Imbalance Handling Conclusion: Through the combination of feature optimization, ensemble methods and stacking methods of Logistic Regression, SVM models and decision tree models, there was a significant improvement in fraud identification in the balanced test data. The final "Stacking Model" in the balanced testing set was able to effectively capture almost 80% of the fraudulent activity. This provided a reliable and balanced tool for detection in this dataset. However, in the unbalanced/full testing set, it was found that the Logistic Regression model performed subjectively better than the other three models with the highest accuracy (over 80%) and highest F1-Score (8%). That said, there was still a large portion of non-fraudulent bank account initiations that were flagged as fraudulent; something that needs to be addressed in further optimization of these models.`),
			]
		},
		{
			id: 'model2',
			title: 'Model 2 (Kayo Abdi)',
			label: 'Kayo Abdi',
			color: '#f97316',
			preview: 'Fraud Detection using Decision Tree, K-Means Clustering, and Apriori',
			content: [
				text(`Implementation and Preprocessing: For this set of models, the dataset was preprocessed by replacing values -1 with NaN to represent data that was missing. For numerical features, median imputation was applied. For key attributes such as bank account durations and previous addresses, however, missing values were treated as meaningful indications rather than just noise. One-hot encoding was used on categorical variables, which gave a total of 47 features and the final dataset contained just 1,000,000 observations.`),
				text(`Model Selection: Three different modeling methods were used including, Decision Tree classification, K-means clustering, and Apriori association rule mining. Each model was selected to capture different aspects of fraud detection. Thus including behavioral grouping, predictions, and pattern discovery.`),
				text(`Decision Tree: The decision tree model was chosen due to its easy interpretability and suitability for classification. This model assumes that the data can be partitioned into different decision regions based on feature thresholds. To reduce overfitting, the maximum tree depth was limited to 5. Also, due to the severe class imbalance of about 1.1% fraud, class weighting was applied to highlight the minority class (aka fraud). The model achieved a recall of around 74% for fraud cases, thus representing effective detection of fraudulent activity. But precision was low by around 3%, reflecting a high number of false positives. The confusion matrix shows that most non-fraud cases are correctly classified, but a large number are incorrectly predicted as fraud, while only a smaller portion of fraud cases are missed. But after some research it was discovered, that this trade-off is expected in fraud detection scenarios where minimizing missed fraud cases is prioritized. This suggests that the model is more focused on capturing as many fraud cases as possible, even if it means incorrectly flagging legitimate users, which aligns with the goal of reducing financial risk.`),
				image('/models/fig7_dt_confusion_matrix_m2.png', 'Figure 7: Decision Tree Confusion Matrix'),
				image('/models/fig8_dt_classification_report_m2.png', 'Figure 8: Decision Tree Classification Report'),
				image('/models/fig8b_dt_visualization_m2.png', 'Figure 8: Decision Tree Visualization'),
				text(`K-Means Clustering: K-means clustering was applied to find natural groups in customer behavior. The model assumed that clusters are formed based on distance in feature space and that groups are approximately spherical. Prior to clustering, numerical features were standardized, and a subset of the data was used to improve computational effectiveness. The results showed distinct clusters with varying fraud rates. One cluster showed a much higher fraud rate about 2.24% compared to others that were around 0.63%\u20130.98%, thus suggesting that fraud is grouped in specific behavioral segments. The silhouette score of 0.076 indicates that while clusters are present, there is notable overlap between them and the separation is relatively weak. The Davies-Bouldin index (3.02) also supports this, indicating that the clusters are not very compact and show some overlap with each other.`),
				image('/models/fig9_fraud_rates_by_cluster.png', 'Figure 9: Fraud Rates by Cluster'),
				text(`Apriori: Apriori association rule mining was used to show frequently co-occurring feature association. This method assumes that frequent itemsets indicate meaningful relationships, and relies on the anti-monotone property where infrequent itemsets are pruned from further expansion. Due to the computational constraints and dataset size, the model was applied to a sampled and discretized subset of the data. Numerical features were transformed into categorical bins to support transaction-based analysis, since Apriori requires categorical input and treats each record as an independent transaction. But, due to the rarity of fraud cases, many rules involving fraud did not satisfy the minimum threshold.`),
				text(`Conclusion: Overall, the Decision Tree model was the best at predicting fraud and K-Means helped us understand the structure of the data. Apriori analysis demonstrated the importance of feature interactions. The visualizations show that there are clear patterns in how fraud appears within the data. The confusion matrix indicates that the model is able to capture a decent amount of fraud cases, but it also captures a large number of non-fraud cases as fraud. This shows a tradeoff between catching fraud and making incorrect predictions. The Decision Tree visualization shows that splits are based on both behavioral and financial features, which suggests fraud isn't driven by just one factor. This suggests that fraud is influenced by more than just one type of variable. The clustering results kind of show this in the PCA plot, where the data breaks into three groups, even though there's still some overlap. When we look at the rate of fraud in each group, we see that one group commits more fraud than the others. So it is not random. It seems that fraud is more common in certain parts of the data.`),
			]
		},
		{
			id: 'model3',
			title: 'Model 3 (David Savi\u0107)',
			label: 'David Savi\u0107',
			color: '#06b6d4',
			preview: 'Fraud Detection using Decision Tree, Na\u00efve Bayes, Apriori, and Logistic Regression',
			content: [
				text(`Model Selection and Preprocessing: Four models were implemented on the Feedzai Bank Account Fraud dataset (999,999 rows, 1.10% fraud rate). Similar to the models above, the same preprocessing pipeline was used throughout: placeholder "-1" values replaced with "NaN", median imputation on numeric columns, most-frequent imputation and OneHotEncoding on categorical columns, and StandardScaler on numeric features \u2014 yielding 51 features after encoding. An 80/20 stratified split was applied across all models.`),
				text(`Decision Tree: The Decision Tree was the first choice because of the simplicity of output interpretation and explanation. Every prediction can be traced back to a specific split on a specific feature, which is extremely important when trying to justify a fraud flag. Decision Trees also handle the mix of numeric and encoded categorical features without much extra setup. Additionally, "class_weight" lets you penalize the model directly for missing fraud cases.`),
				text(`Decision Tree Model Assumptions and Tuning: Trees split data into rectangular regions using single-feature thresholds. The big risk here is overfitting across 51 features, especially the sparse one-hot columns. After using "GridSearchCV" with 3-fold CV and F1 scoring across 96 combinations of "max_depth," "min_samples_leaf," "criterion," and "class_weight," the best outcome was "max_depth=5," "min_samples_leaf=10," "entropy," and "class_weight={0:1, 1:10}." The custom 10x fraud weight beat the "balanced" option. The balanced setting auto-calculated to roughly 90x on this dataset, which pushed recall up but created a large amount of false positives that reduced the final F1-Score.`),
				text(`The baseline model predicted "not fraud" for almost everything and hit 97.96% accuracy anyway \u2014 which is exactly why accuracy is the wrong metric here. After tuning, recall went to 26.25% and F1 to 0.1426. Out of 2,206 fraud cases in the test set, the model caught 579, missed 1,627, and threw 5,333 false positives.`),
				image('/models/fig10_dt_confusion_matrix_m3.png', 'Figure 10: Decision Tree confusion matrix (tuned model)'),
				image('/models/fig11_dt_feature_importances.png', 'Figure 11: Top 10 feature importances'),
				text(`Na\u00efve Bayes was included mainly because it gives a fraud probability score rather than just a binary label. That is useful in practice \u2014 a fraud team can lower the threshold to catch more fraud at the cost of more false alarms, or raise the threshold to reduce noise. Retraining is not necessary, just shift the cutoff.`),
				text(`Model assumptions and tuning: GaussianNB assumes features are independent given the class and normally distributed within each class. The independence assumption is definitely violated since velocity_6h and velocity_24h are correlated, but the model still works well enough as a probabilistic baseline. Since GaussianNB does not support "class_weight," the imbalance was handled by adjusting the decision threshold after prediction.`),
				image('/models/fig12_nb_confusion_matrix.png', 'Figure 12: Na\u00efve Bayes confusion matrix'),
				text(`This tuned model got the best F1 of the three classifiers at 0.1810, with a ROC-AUC of 0.8309. 425 out of 2,206 fraud cases were caught with 0.5 threshold as default. Dropping the threshold to 0.10 raises that to 1,104 caught \u2014 but also adds around 12,000 more false alarms. Whether that tradeoff makes sense depends on how the bank weighs the cost of a missed fraud versus an incorrectly flagged application.`),
				text(`Apriori is not a predictive model \u2014 it does not output a fraud label or score. The point of including it is to find which feature combinations tend to appear together in fraudulent applications and express them as readable rules. That is actually more useful for analysts than a black-box classifier in some cases.`),
				text(`Logistic Regression was included as the linear baseline and also because it is used as the meta-learner in our stacking ensemble. It outputs well-calibrated probabilities across the full range, which is what makes it a good choice for combining base model outputs. L1 regularization can also zero out irrelevant features automatically across the 51 columns.`),
				image('/models/fig13_lr_confusion_matrix_m3.png', 'Figure 13: Logistic Regression Confusion Matrix (tuned, C=0.01)'),
				image('/models/fig14_lr_feature_coefficients.png', 'Figure 14: Top 15 Feature Coefficients (red = increases fraud risk, blue = decreases)'),
				text(`The tuned model caught 1,737 of 2,206 fraud cases (78.7% recall) with 38,221 false positives. The high false positive count is a direct result of "class_weight=balanced" on a 90:1 dataset \u2014 the model is heavily penalized for missing fraud, so it over-flags legitimate applications. The coefficient chart shows "housing_status_BA" and "device_os_windows" as the strongest positive predictors of fraud, consistent with what the Decision Tree found. On the negative side, "employment_status_CE" and "device_os_linux" are associated with lower fraud risk.`),
				text(`Ensemble (Soft Voting & Stacking): Both ensemble methods combined all eight models from the team: the three above plus the Linear SVC and KNN from Model 4, and the Random Forest and Gradient Boosting from Model 1. The training set was resampled to balance the classes first (RandomUnderSampler, 8,823 samples per class). KNN and RBF SVM were trained on a 20% subsample of the balanced set because full training was too slow.`),
				image('/models/fig15_all_models_comparison.png', 'Figure 15: Recall / Precision / F1 across all models (ensemble columns highlighted)'),
				image('/models/fig16_voting_stacking_confusion.png', 'Figure 16: Soft Voting and Stacking confusion matrices'),
				text(`Model 3 Conclusion: The highest F1 of 0.0897 along with highest ROC-AUC of 0.8955, and highest recall of 81.78% are because of Stacking. Gradient Boosting and Logistic Regression outputs were weighed more heavily from the meta learner, as the two had strongest individual performance. Not too far behind is soft voting with recall of 81.37% and ROC-AUC of 0.8846. Both ensemble methods outperformed every individual model on every metric, and that is confirmation that merging the approaches is far better than relying on any of the ones as single method.`),
			]
		},
		{
			id: 'model4',
			title: 'Model 4 (Sawyer McKenney)',
			label: 'Sawyer McKenney',
			color: '#7c3aed',
			preview: 'Fraud Detection using SVM, KNN, and Stacking',
			content: [
				text(`Model Selection: Linear SVM was chosen because after one-hot encoding, 51 dimensions were present. SVMs are designed to find decisions boundaries in high dimensional amounts of data. Since this project is dealing with a large amount of class imbalance, and because it penalizes misclassifying the minority more, SVM was assumed to be great for this purpose. As a result, SVM was able to achieve a high recall of 0.78.`),
				text(`KNN was chosen because it does not make assumptions based on the distributions of the data it focuses on localized irregularities that SVM might have missed. So as a result, it was assumed that if these methods were stacked, it would be possible to leverage the strengths of both SVM and KNN. When it was observed that stacking provided the highest F1 score, these assumptions were proven to be correct.`),
				text(`Model assumptions: For SVM, LinearSVC was used, assuming that fraud and not fraud can be separated by a hyperplane that has a 51-feature dimensional space. It is also assumed that missing a fraud case is more costly than a false alarm, so "class_weight" was set to be "balanced."`),
				text(`For KNN it was assumed that similar transactions are near each other. In other words, it was believed that the fraud transactions will have similar fraud neighbors. It was also assumed that all 51 features are equally informative.`),
				text(`Hyperparameter Tuning: For SVM, "class_weight" was adjusted to be "balanced" so that the model did not predict "non-fraud" for everything. The max iterations was also adjusted to be 5000 instead of 1000 to give the optimizer enough iterations to converge on the large dataset.`),
				text(`For KNN, the only hyperparameter change that was made consisted of using all available CPU cores for faster computation by running in parallel.`),
				text(`During the preprocessing of this model, the "\u20131" value was replaced with "NaN" for the features with large amounts of missing data. "-1" and "NaN" were the values that represented missing values. Secondly, median imputation and normalization were applied in other features. One-hot encoding was also used on categorical features, and we resulted in 51 features after encoding.`),
				text(`The techniques applied in this model include Normalization and Bagging. Normalization was required for a distance-based model approach to apply to SVM and KNN. Bootstrapping was used to try and reduce variances through aggregation, and it was applied to both SVM and KNN. For training, a 20/80 split was implemented, training by randomly selecting 80% of the data and then testing on the 20%.`),
				text(`As a result, it was found that SVM had achieved the highest recall with 77% but very low precision of about 4%. This means that the model was catching a large amount of fraud but also generating a lot of false alarms. On the other hand, KNN struggled with class imbalance and presented a 41% recall and 4% precision.`),
				text(`After stacking precision was able to be improved by 7% over the individual models and, was able to balance recall to 60%. Stacking also provided the best F1 score for this model at 0.13.`),
				text(`The observed takeaways from this model were that SVM and KNN are both distance-based models that struggle with high imbalance. With this in mind, the assumption is that tree-based methods like random forest would likely perform better for this problem but were outside the scope of this model.`),
				image('/models/fig17_m4_performance_comparison.png', 'Figure 17: Model Performance Comparison'),
				image('/models/fig18_m4_accuracy_comparison.png', 'Figure 18: Model Accuracy Comparison'),
			]
		},
		{
			id: 'conclusion',
			title: 'Conclusion',
			label: 'All Models',
			color: '#10b981',
			preview: 'The stacking model from all eight base models performed the best with a recall of 81.78% and an F-1 score of 0.0897.',
			content: [
				text(`Based on the four model implementations in this milestone. It is clear that the stacking model from all eight base models (Model 3) preformed the best. With a recall of 81.78% and a F-1 score of 0.0897. This goes to show that combining different types of learners through a meta-learning process produces a better fraud detection than any single algorithm. The best standalone model was gradient boosting. This achieved a F-1 score of 0.0903 and a ROC-AUC of 0.8955 telling how well the model separates the two classes. This was followed by Logistic Regression and Linear SVC that achieved 78% recall. Another thing worth noting is that in Model 1, the imbalanced test set Logistic regression provided the be the most reliable model on full imbalanced sets because it was able to achieve a F1-Score of 8% while still maintaining 80% recall. The other balanced training models achieved very high recall but as a result precisions dropped to 2%, thus driving the F1-scores down to 4-5%. Logistic regression was able to hold a better recall/precision balance on the imbalanced data set makis it the most practical model base.`),
				text(`KNN was the weakest predictive model in Model 4's implementation, failing significantly with class imbalance and producing poor recall and uncertain performance overall. The standalone Decision Tree was also a consistent underperformer compared to other models, especially in terms of maintaining a balance between precision and recall.`),
				text(`From Model 2, additional insights were attained beyond pure predictions. The DT model shows that fraud detection is heavily influenced by a mix of behavioral features such as transaction velocity and session activity, along with financial attributes like credit risk score and proposed credit limit. The model achieved a high recall (~74%), meaning it was able to capture a large portion of fraud cases, but precision remained extremely low (~3%), resulting in a low F1-score (~0.06). This shows the impact of class imbalance, where the model prioritizes catching the fraud at the cost of a higher number of false positives. In comparison to Model 2's DT results, Model 3 showed a more balanced improvement after tuning, particularly in terms of F1-score and precision. Model 2 prioritized recalls (~74%) but suffered from extremely low precision (~3%), leading to a much lower F1-score (~.065), whereas Model 3 increased the recall to around 26% while improving precision, resulting in a higher F1-score (~.14). This contrast shows the two different modeling trade-offs. Model 3's approach aimed for a more balanced classifier whilst Model 2 focused more heavily on capturing as much fraud as possible, even if false positive rates were high. Despite the difference, both models show similar important features such as housing status and device type, reinforcing that fraud is driven by a mix of behavioral and identity-related factors.`),
			]
		}
	];

	let activeIndex = $state(0);
	let expandedCard = $state<string | null>(null);
	let isDragging = $state(false);
	let didDrag = $state(false);
	let dragStartX = 0;
	let dragDelta = $state(0);

	function goTo(index: number) {
		activeIndex = Math.max(0, Math.min(cards.length - 1, index));
		dragDelta = 0;
	}

	function toggleExpand(id: string) {
		expandedCard = expandedCard === id ? null : id;
	}

	function closeExpand() {
		expandedCard = null;
	}

	function handleKeydown(e: KeyboardEvent) {
		if (expandedCard) {
			if (e.key === 'Escape') closeExpand();
			return;
		}
		if (e.key === 'ArrowLeft') goTo(activeIndex - 1);
		if (e.key === 'ArrowRight') goTo(activeIndex + 1);
	}

	function handlePointerDown(e: PointerEvent) {
		if (expandedCard) return;
		isDragging = true;
		didDrag = false;
		dragStartX = e.clientX;
		dragDelta = 0;
	}

	function handlePointerMove(e: PointerEvent) {
		if (!isDragging) return;
		dragDelta = e.clientX - dragStartX;
		if (Math.abs(dragDelta) > 8) {
			didDrag = true;
		}
	}

	function handlePointerUp(e: PointerEvent) {
		if (!isDragging) return;
		isDragging = false;

		if (didDrag) {
			if (dragDelta < -60) goTo(activeIndex + 1);
			else if (dragDelta > 60) goTo(activeIndex - 1);
			dragDelta = 0;
			return;
		}
		dragDelta = 0;

		// It was a tap/click, not a drag — find which card was tapped
		const target = e.target as HTMLElement;
		const cardEl = target.closest('.model-card') as HTMLElement | null;
		if (!cardEl) return;

		const cardIndex = Array.from(cardEl.parentElement?.children ?? []).indexOf(cardEl);
		if (cardIndex === activeIndex) {
			toggleExpand(cards[cardIndex].id);
		} else {
			goTo(cardIndex);
		}
	}

	function getCardStyle(index: number): string {
		const offset = index - activeIndex;
		const dragInfluence = isDragging ? dragDelta * 0.15 : 0;

		const translateX = offset * 300 + dragInfluence;
		const translateZ = offset === 0 ? 0 : -200 - Math.abs(offset) * 80;
		const rotateY = offset * -40 + (isDragging ? dragDelta * 0.02 : 0);
		const scale = offset === 0 ? 1 : 0.78 - Math.abs(offset) * 0.06;
		const opacity = Math.abs(offset) > 2 ? 0 : 1 - Math.abs(offset) * 0.25;
		const zIndex = 10 - Math.abs(offset);

		return `
			transform: translateX(${translateX}px) translateZ(${translateZ}px) rotateY(${rotateY}deg) scale(${scale});
			opacity: ${opacity};
			z-index: ${zIndex};
			filter: brightness(${offset === 0 ? 1 : 0.65 + 0.05 / (Math.abs(offset) + 1)});
		`;
	}

	onMount(async () => {
		const { gsap } = await import('gsap');
		gsap.from('.page-header h1', { opacity: 0, y: 40, duration: 0.8, delay: 0.2 });
		gsap.from('.page-header p', { opacity: 0, y: 20, duration: 0.6, delay: 0.35 });
		gsap.from('.carousel-scene', { opacity: 0, scale: 0.9, duration: 0.8, delay: 0.5, ease: 'power2.out' });
		gsap.from('.scroll-controls', { opacity: 0, y: 20, duration: 0.5, delay: 0.9 });
	});
</script>

<svelte:window onkeydown={handleKeydown} />

<div class="models-page">
	<div class="page-header">
		<span class="header-label">Milestone 3</span>
		<h1>Model <span class="gradient-text">Implementation</span></h1>
		<p>Four distinct model combinations leveraging supervised classification, unsupervised clustering, ensemble methods, and association rule mining to detect fraud in the BAF dataset.</p>
	</div>

	<!-- svelte-ignore a11y_no_static_element_interactions -->
	<div
		class="carousel-scene"
		onpointerdown={handlePointerDown}
		onpointermove={handlePointerMove}
		onpointerup={handlePointerUp}
		onpointercancel={handlePointerUp}
	>
		<div class="carousel-stage">
			{#each cards as card, i}
				<article
					class="model-card"
					class:active={i === activeIndex}
					style="{getCardStyle(i)} --accent: {card.color}"
					role="button"
					tabindex={i === activeIndex ? 0 : -1}
				>
					{#if i === activeIndex}
						<div class="card-glow" style="background: radial-gradient(ellipse, {card.color}33, transparent 70%)"></div>
					{/if}

					<div class="card-inner">
						<div class="card-header">
							<div class="card-badge" style="background: {card.color}">{card.title}</div>
						</div>

						<h2 class="card-title">{card.preview}</h2>

						{#if i === activeIndex}
							<span class="click-hint">Click to read full details</span>
						{/if}
					</div>

					<div class="card-shine"></div>
				</article>
			{/each}
		</div>
	</div>

	<div class="scroll-controls">
		<div class="nav-row">
			<button class="nav-btn" onclick={() => goTo(activeIndex - 1)} disabled={activeIndex === 0} aria-label="Previous">
				<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" width="18" height="18"><path d="M15 18l-6-6 6-6" /></svg>
			</button>
			<div class="dots">
				{#each cards as _, i}
					<button class="dot" class:active={i === activeIndex} onclick={() => goTo(i)} aria-label="Go to card {i + 1}"></button>
				{/each}
			</div>
			<button class="nav-btn" onclick={() => goTo(activeIndex + 1)} disabled={activeIndex === cards.length - 1} aria-label="Next">
				<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" width="18" height="18"><path d="M9 18l6-6-6-6" /></svg>
			</button>
		</div>
		<span class="scroll-hint">Drag, swipe, or use arrow keys to browse &mdash; click the front card to expand</span>
	</div>
</div>

<!-- Expanded overlay -->
{#if expandedCard}
	<!-- svelte-ignore a11y_no_static_element_interactions -->
	<div class="overlay" onclick={closeExpand} onkeydown={(e) => { if (e.key === 'Escape') closeExpand(); }}>
		<!-- svelte-ignore a11y_no_static_element_interactions -->
		<div class="expanded-card" onclick={(e) => e.stopPropagation()} style="--accent: {cards.find(c => c.id === expandedCard)?.color}">
			<button class="close-btn" onclick={closeExpand} aria-label="Close">
				<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="22" height="22">
					<path d="M18 6L6 18M6 6l12 12" />
				</svg>
			</button>

			{#each cards as card}
				{#if card.id === expandedCard}
					<div class="expanded-header">
						<div class="card-badge" style="background: {card.color}">{card.title}</div>
					</div>
					<h2 class="expanded-title">{card.preview}</h2>
					<div class="expanded-body">
						{#each card.content as block}
							{#if block.type === 'text'}
								<p>{block.value}</p>
							{:else if block.type === 'image'}
								<figure class="content-figure">
									<img src={block.value} alt={block.caption ?? ''} />
									{#if block.caption}
										<figcaption>{block.caption}</figcaption>
									{/if}
								</figure>
							{/if}
						{/each}
					</div>
				{/if}
			{/each}
		</div>
	</div>
{/if}

<style>
	/* Styles generated/assisted by AI (Claude, Anthropic) */

	.models-page {
		min-height: 100vh;
		padding: 6rem 2rem 4rem;
		max-width: 1400px;
		margin: 0 auto;
		overflow: hidden;
	}

	/* === Header === */
	.page-header {
		text-align: center;
		margin-bottom: 2rem;
		padding: 0 1rem;
	}

	.header-label {
		display: inline-block;
		font-size: 0.75rem;
		font-weight: 600;
		letter-spacing: 0.15em;
		text-transform: uppercase;
		color: #7c3aed;
		margin-bottom: 0.75rem;
	}

	.page-header h1 {
		font-size: clamp(2rem, 5vw, 3.5rem);
		font-weight: 800;
		color: #1a0a2e;
		line-height: 1.15;
		margin-bottom: 1rem;
	}

	.gradient-text {
		background: linear-gradient(90deg, #ec4899, #a855f7);
		background-clip: text;
		-webkit-background-clip: text;
		-webkit-text-fill-color: transparent;
	}

	.page-header p {
		font-size: 1.05rem;
		color: #6b5585;
		max-width: 640px;
		margin: 0 auto;
		line-height: 1.7;
	}

	/* === 3D Carousel === */
	.carousel-scene {
		perspective: 1200px;
		perspective-origin: 50% 50%;
		width: 100%;
		height: 380px;
		display: flex;
		align-items: center;
		justify-content: center;
		cursor: grab;
		user-select: none;
		touch-action: pan-y;
	}

	.carousel-scene:active {
		cursor: grabbing;
	}

	.carousel-stage {
		position: relative;
		width: 440px;
		height: 100%;
		transform-style: preserve-3d;
	}

	/* === Card (preview) === */
	.model-card {
		position: absolute;
		top: 0;
		left: 0;
		width: 440px;
		height: 100%;
		transform-style: preserve-3d;
		transition: transform 0.6s cubic-bezier(0.23, 1, 0.32, 1),
					opacity 0.6s ease,
					filter 0.6s ease;
		cursor: pointer;
		border-radius: 24px;
		overflow: hidden;
	}

	.model-card.active {
		cursor: pointer;
	}

	.card-inner {
		position: relative;
		z-index: 2;
		height: 100%;
		background: rgba(255, 255, 255, 0.72);
		backdrop-filter: blur(20px);
		border: 1px solid rgba(255, 255, 255, 0.8);
		border-radius: 24px;
		padding: 2.5rem 2rem;
		display: flex;
		flex-direction: column;
		gap: 1.25rem;
		box-shadow:
			0 20px 60px rgba(0, 0, 0, 0.08),
			0 4px 16px rgba(0, 0, 0, 0.04),
			inset 0 1px 0 rgba(255, 255, 255, 0.9),
			inset 0 -1px 0 rgba(255, 255, 255, 0.3);
	}

	.card-glow {
		position: absolute;
		inset: -40px;
		z-index: 0;
		border-radius: 40px;
		pointer-events: none;
		animation: glowPulse 3s ease-in-out infinite alternate;
	}

	@keyframes glowPulse {
		0% { opacity: 0.4; transform: scale(1); }
		100% { opacity: 0.7; transform: scale(1.05); }
	}

	.card-shine {
		position: absolute;
		inset: 0;
		z-index: 3;
		border-radius: 24px;
		pointer-events: none;
		background: linear-gradient(
			135deg,
			rgba(255, 255, 255, 0.4) 0%,
			rgba(255, 255, 255, 0.1) 30%,
			transparent 50%,
			rgba(255, 255, 255, 0.05) 70%,
			rgba(255, 255, 255, 0.15) 100%
		);
	}

	.card-header {
		display: flex;
		align-items: center;
		justify-content: space-between;
		gap: 0.75rem;
	}

	.card-badge {
		font-size: 0.7rem;
		font-weight: 700;
		letter-spacing: 0.08em;
		text-transform: uppercase;
		color: #ffffff;
		padding: 0.3rem 0.8rem;
		border-radius: 20px;
		box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
	}

	.card-author {
		font-size: 0.78rem;
		color: #8b6aaf;
		font-weight: 500;
	}

	.card-title {
		font-size: 1.1rem;
		font-weight: 600;
		color: #1a0a2e;
		line-height: 1.5;
		flex: 1;
	}

	.click-hint {
		font-size: 0.72rem;
		color: var(--accent);
		font-weight: 500;
		text-align: center;
		opacity: 0.7;
		animation: hintPulse 2s ease-in-out infinite;
	}

	@keyframes hintPulse {
		0%, 100% { opacity: 0.5; }
		50% { opacity: 0.9; }
	}

	/* === Controls === */
	.scroll-controls {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 0.75rem;
		margin-top: 1.5rem;
	}

	.nav-row {
		display: flex;
		align-items: center;
		gap: 1.25rem;
	}

	.nav-btn {
		width: 40px;
		height: 40px;
		border-radius: 50%;
		border: none;
		background: rgba(255, 255, 255, 0.6);
		backdrop-filter: blur(12px);
		box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
		color: #2d1b4e;
		cursor: pointer;
		display: flex;
		align-items: center;
		justify-content: center;
		transition: all 0.25s ease;
	}

	.nav-btn:hover:not(:disabled) {
		background: #ffffff;
		box-shadow: 0 6px 24px rgba(124, 58, 237, 0.15);
		transform: scale(1.1);
	}

	.nav-btn:disabled {
		opacity: 0.25;
		cursor: default;
	}

	.dots {
		display: flex;
		gap: 0.5rem;
	}

	.dot {
		width: 10px;
		height: 10px;
		border-radius: 50%;
		border: none;
		background: rgba(124, 58, 237, 0.2);
		cursor: pointer;
		transition: all 0.3s ease;
		padding: 0;
	}

	.dot.active {
		background: #7c3aed;
		transform: scale(1.3);
		box-shadow: 0 0 12px rgba(124, 58, 237, 0.4);
	}

	.dot:hover:not(.active) {
		background: rgba(124, 58, 237, 0.4);
	}

	.scroll-hint {
		font-size: 0.75rem;
		color: #8b6aaf;
		font-weight: 400;
	}

	/* === Expanded Overlay === */
	.overlay {
		position: fixed;
		inset: 0;
		z-index: 1000;
		background: rgba(10, 0, 20, 0.6);
		backdrop-filter: blur(8px);
		display: flex;
		align-items: center;
		justify-content: center;
		padding: 2rem;
		animation: fadeIn 0.3s ease;
	}

	@keyframes fadeIn {
		from { opacity: 0; }
		to { opacity: 1; }
	}

	.expanded-card {
		position: relative;
		width: 100%;
		max-width: 720px;
		max-height: 85vh;
		background: rgba(255, 255, 255, 0.92);
		backdrop-filter: blur(24px);
		border: 1px solid rgba(255, 255, 255, 0.8);
		border-radius: 24px;
		padding: 2.5rem;
		overflow-y: auto;
		box-shadow:
			0 32px 80px rgba(0, 0, 0, 0.2),
			0 8px 24px rgba(0, 0, 0, 0.08),
			inset 0 1px 0 rgba(255, 255, 255, 0.9);
		animation: cardIn 0.4s cubic-bezier(0.23, 1, 0.32, 1);
	}

	@keyframes cardIn {
		from { opacity: 0; transform: scale(0.92) translateY(20px); }
		to { opacity: 1; transform: scale(1) translateY(0); }
	}

	.close-btn {
		position: absolute;
		top: 1.25rem;
		right: 1.25rem;
		width: 36px;
		height: 36px;
		border-radius: 50%;
		border: none;
		background: rgba(0, 0, 0, 0.06);
		color: #4a3663;
		cursor: pointer;
		display: flex;
		align-items: center;
		justify-content: center;
		transition: all 0.2s ease;
	}

	.close-btn:hover {
		background: rgba(0, 0, 0, 0.1);
		color: #1a0a2e;
	}

	.expanded-header {
		display: flex;
		align-items: center;
		gap: 0.75rem;
		margin-bottom: 1rem;
	}

	.expanded-author {
		font-size: 0.85rem;
		color: #8b6aaf;
		font-weight: 500;
	}

	.expanded-title {
		font-size: 1.3rem;
		font-weight: 700;
		color: #1a0a2e;
		line-height: 1.4;
		margin-bottom: 1.5rem;
		padding-bottom: 1.25rem;
		border-bottom: 2px solid color-mix(in srgb, var(--accent) 20%, transparent);
	}

	.expanded-body p {
		font-size: 0.92rem;
		color: #3a2855;
		line-height: 1.75;
		margin-bottom: 1.25rem;
	}

	.expanded-body p:last-child {
		margin-bottom: 0;
	}

	/* === Figures / Images === */
	.content-figure {
		margin: 1.5rem 0;
		text-align: center;
	}

	.content-figure img {
		max-width: 100%;
		border-radius: 12px;
		border: 1px solid rgba(124, 58, 237, 0.12);
		box-shadow: 0 4px 16px rgba(0, 0, 0, 0.06);
	}

	.content-figure figcaption {
		font-size: 0.78rem;
		color: #8b6aaf;
		font-style: italic;
		margin-top: 0.6rem;
		line-height: 1.4;
	}

	/* === Responsive === */
	@media (max-width: 768px) {
		.models-page {
			padding: 5rem 1rem 3rem;
		}

		.carousel-scene {
			height: 340px;
		}

		.carousel-stage {
			width: 320px;
		}

		.model-card {
			width: 320px;
		}

		.card-inner {
			padding: 1.75rem 1.5rem;
		}

		.card-title {
			font-size: 0.95rem;
		}

		.expanded-card {
			padding: 1.75rem;
			max-height: 90vh;
		}

		.expanded-title {
			font-size: 1.1rem;
		}
	}

	@media (max-width: 480px) {
		.carousel-scene {
			height: 320px;
		}

		.carousel-stage {
			width: 280px;
		}

		.model-card {
			width: 280px;
		}

		.card-inner {
			padding: 1.25rem;
		}

		.expanded-card {
			padding: 1.25rem;
			border-radius: 16px;
		}

		.expanded-body p {
			font-size: 0.85rem;
		}
	}
</style>
