<script lang="ts">
	import { onMount } from 'svelte';

	let activeSection = $state('');

	const sections = [
		{ id: 'data-collection', num: '01', label: 'Data Collection' },
		{ id: 'data-understanding', num: '02', label: 'Data Understanding' },
		{ id: 'cleaning', num: '03', label: 'Cleaning & Preprocessing' },
		{ id: 'quality', num: '04', label: 'Data Quality Assessment' },
		{ id: 'correlations', num: '05', label: 'Correlation Data' },
		{ id: 'normality', num: '06', label: 'Normality Checks' },
		{ id: 'velocity', num: '07', label: 'Velocity Graphs' },
		{ id: 'missing', num: '08', label: 'Data Quality, Bias & Limitations' },
	];

	function scrollToSection(id: string) {
		document.getElementById(id)?.scrollIntoView({ behavior: 'smooth', block: 'start' });
	}

	onMount(async () => {
		const { gsap } = await import('gsap');
		const { ScrollTrigger } = await import('gsap/ScrollTrigger');
		gsap.registerPlugin(ScrollTrigger);

		gsap.from('.page-header h1', { opacity: 0, y: 40, duration: 0.8, delay: 0.2 });
		gsap.from('.doc-meta', { opacity: 0, y: 20, duration: 0.6, delay: 0.35 });
		gsap.from('.toc', { opacity: 0, y: 20, duration: 0.6, delay: 0.5 });

		gsap.from('.exploration-section', {
			opacity: 0,
			y: 60,
			stagger: 0.15,
			duration: 0.7,
			ease: 'power2.out',
			scrollTrigger: { trigger: '.content', start: 'top 80%' }
		});

		document.querySelectorAll('.exploration-section').forEach((el) => {
			ScrollTrigger.create({
				trigger: el,
				start: 'top 40%',
				end: 'bottom 40%',
				onEnter: () => { activeSection = el.id; },
				onEnterBack: () => { activeSection = el.id; },
			});
		});
	});
</script>

<div class="page-bg">
<section class="page-header">
	<h1>Data <span class="gradient-text">Exploration</span></h1>
	<div class="doc-meta">
		<span class="meta-pill">CSCI 5502 — Data Mining</span>
		<span class="meta-pill">Group 16</span>
		<span class="meta-pill">Milestone 2</span>
	</div>
</section>

<nav class="toc" aria-label="Table of contents">
	{#each sections as s}
		<button
			class="toc-item"
			class:active={activeSection === s.id}
			onclick={() => scrollToSection(s.id)}
		>
			<span class="toc-num">{s.num}</span>
			<span class="toc-label">{s.label}</span>
		</button>
	{/each}
</nav>

<div class="content">
	<!-- Section 1: Data Collection -->
	<section class="exploration-section" id="data-collection">
		<div class="section-num-wrap"><span class="section-num">01</span></div>
		<h2>Data Collection</h2>
		<p>During the data collection step, we opted not to use a dynamic API to collect our data. We opted not to do this for many reasons, for starters there are latency challenges, security challenges as well as overall availability. Getting a business to agree or anyone in fact to give us real-time access to live streamed transactions is a major security risk and would cost any company money. During this we also explored the idea of using real-time crypto transactions as out data source but decided not to go this route. This came up because this gives us real time transactions feed but does not provide a fraud label and without labels, we would not be able to evaluate supervised models or fairly compare these models with unsupervised models.</p>
		<p>Even though we could not get a live API the data set we ended up choosing bank account creation fraud data that was available through a public API. The data set we ended up using was the Bank Account Fraud (BAF) dataset by Feedzai. We determined that Feedzai is an actual fraud detection tool that works with various institutions. So, this is not just so random CSV file we downloaded off the internet. The data set was introduced in a NeurlIPS 2022 paper and claims to be built using privacy preserving methods that were applied to real bank account opening fraud data. Since this data is synthetic, it does not mean it is unusable because it was modeled after real fraud behavior patterns and designed to be used specifically for training machine learning models in a financial setting.</p>
		<p>This dataset fits our research question perfectly because our whole project is about comparing supervised fraud detection models to unsupervised anomaly detection under extreme class imbalance. The BAF dataset has transaction-level features and a clear fraud label (fraud_bool), which lets us train supervised models and test anomaly detection methods side by side. The data set as expected does not have very much balance with only about 1% of the data being fraud, and this is very much mimics a real world setting. This imbalance is quite literally the core challenge we are studying in this project, so the data set supports the goals of our project without us having to manipulate the data artificially.</p>
	</section>

	<!-- Section 2: Data Understanding -->
	<section class="exploration-section" id="data-understanding">
		<div class="section-num-wrap"><span class="section-num">02</span></div>
		<h2>Data Understanding</h2>
		<p>Each row in the data set represents a single account application. Each account application was submitted by a user who was attempting to open a finical account or credit. This data set has numerical features, categorical features and binary features. The numerical features in this data set include income, custoemr_age, credit_risk_score, session_length_in_minutes and proposed_credit_limit. There are all great numerical variables that can be used in analysis and various machine learning models. Some of the categorical features include payment_type, employment_status, housing_status and device_os. These variables will require encoding methods such as one hot encoding before they can be used in machine learning algorithms. Finally, we have binary features that can only be 0 or 1. Some examples from that data include: fraud_bool, email_is_free, phone_home_valid, foreign_request and has_other_cards. Since binary variables are already numeric, we will not need to require additional encoding on these values.</p>
	</section>

	<!-- Section 3: Data Cleaning and Preprocessing -->
	<section class="exploration-section" id="cleaning">
		<div class="section-num-wrap"><span class="section-num">03</span></div>
		<h2>Data Cleaning and Preprocessing</h2>
		<p>Goal for this milestone was to get the dataset (Feedzai) to a state where it can be used prior to modeling which will take place in milestone 3. We came across a mix of numerical and categorical fields in raw file as well as columns which has a placeholder for missing values of –1. We converted those to proper missing values so that they could be handled correctly.</p>
		<p>Numeric columns were filled using the median since several features are skewed and the median is less sensitive to extreme valus. Categorical columns were filled with the most common category in each column. After that, numeric features were standardized so they are all on a similar scale and categorical featuires were one hot encoded so they can be used later in machine learning models.</p>
		<p>To save the changes, we saved the first ten rows of the dataset before and after cleaning. These snapshots show how missing values were handled and how categorical variables expanded into multiple columns after encoding. We also generated several visual checks (fraud distribution plot, correlation heatmap, payment type frequencies, velocity histograms, and QQ plots for normality). These helped confirm what we saw in the summary statistics – skewed distributions, redundant velocity features, and no single feature that strongly predicts fraud on its own.</p>
		<p>For the time being we did not do any dimentality reduction. We are proceeding with all avaiable fetaures because we believe for now keeping all the features in tact will make it easier to understand what varaibles are driving our fraud predictions. Our data also does not have an excessive number of features. So we thought that reamoving features early might lose important signals. During milestone three once we start creating our model we do beleive that there will be some demnsionalty reduction both to remove noise and to optimize our model.</p>
		<p>We have exported the final result as cleaned_feedzai.csv and will be using it in the modeling stage in milestone 3.</p>
	</section>

	<!-- Section 4: Data Quality Assessment -->
	<section class="exploration-section" id="quality">
		<div class="section-num-wrap"><span class="section-num">04</span></div>
		<h2>Data Quality Assessment</h2>

		<div class="viz-card wide">
			<img src="/figures/fraud_distribution.png" alt="Fraud vs Non-Fraud Distribution" />
			<p class="viz-caption">This summary was taken from the raw data of 1,000,000 applications for new bank accounts in which there were 11,029 instances of fraud or 1.1029%. This data will be cleaned and processed to ensure normality.</p>
		</div>

		<h3>Summary Statistics</h3>
		<div class="table-scroll">
			<table>
				<thead>
					<tr>
						<th>Feature</th>
						<th>Mean</th>
						<th>Median</th>
						<th>Variance</th>
						<th>Skewness</th>
						<th>Audit Interpretation</th>
					</tr>
				</thead>
				<tbody>
					<tr><td>Customer Age</td><td>33.69</td><td>30.00</td><td>144.62</td><td>0.48</td><td>Younger main audience; "older" outliers pulling the tail right.</td></tr>
					<tr><td>Credit Risk Score</td><td>130.99</td><td>122.00</td><td>4855.55</td><td>0.30</td><td>High variance; widely spread out data.</td></tr>
					<tr><td>Income</td><td>0.56</td><td>0.60</td><td>0.08</td><td>-0.39</td><td>Clustered data; mostly higher-end, some low-income outliers.</td></tr>
					<tr><td>Has Other Cards</td><td>0.22</td><td>0.00</td><td>0.17</td><td>1.33</td><td>Most are new customers; strong positive skew</td></tr>
					<tr><td>Name-Email Sim.</td><td>0.49</td><td>0.49</td><td>0.08</td><td>0.04</td><td>Perfectly symmetrical; very "clean" and predictable data.</td></tr>
					<tr><td>DOB Distinct Emails</td><td>9.50</td><td>9.00</td><td>25.33</td><td>0.70</td><td>High variance suggests "bursts" of bot/spam activity.</td></tr>
				</tbody>
			</table>
		</div>

		<div class="interpretations">
			<ol>
				<li>For <em>Customer Age</em>, the mean here is higher than that of the median, indicating large outliers with a younger main audience and older audience in the tails. A larger variance shows that ages are widely spread out, and its positive skew confirms that the tails are pointed toward older ages.</li>
				<li>For <em>Income</em>, the mean is very close to the median, yet smaller. It's important to note that this feature has already been normalized between 0 and 1. The variance in this feature indicates that the values are fairly well clustered. The negative skew associated with this feature indicates that outliers in the lower end of the income distribution are pulling that tail to the left.</li>
				<li>For <em>Credit Risk Score</em>, our mean and median are again very close but the variance is incredibly large. The data has a positive skew meaning that some outliers in the higher end of the score range are pulling the mean and tails to the right.</li>
				<li>For <em>Has Other Cards</em>, this data clearly points out that a majority of applicants are new customers to the bank.</li>
				<li>For <em>Name-Email Similarity</em>, this feature is, at first glance a very normally distributed with a mean and median both of 0.49 and a skew of only .04, meaning that a majority of people have an email that is similar to their actual name. However, Q-Q Plots will imply otherwise, and what we're really looking at is a symmetrical distribution, not necessarily a normal one.</li>
				<li>For <em>DOB Distinct Emails</em>, the average of 9.50 and the median of 9.00 implies that a typical day is seeing about 9-10 applications associated with the same birthday. The variance is kind of high in this feature meaning some days, the banks sees a higher amount of applications with the same birthday. The skew here indicates tails that are drawn towards much higher numbers. Instances when there is an increase in the amount of account requests tied to the same birthday are indicative of bot usage and new account fraud.</li>
			</ol>
		</div>
	</section>

	<!-- Section 5: Correlation Data -->
	<section class="exploration-section" id="correlations">
		<div class="section-num-wrap"><span class="section-num">05</span></div>
		<h2>Correlation Data</h2>

		<div class="table-scroll">
			<table>
				<thead>
					<tr>
						<th>Category</th>
						<th>Feature</th>
						<th>Correlation Value</th>
						<th>Interpretation</th>
					</tr>
				</thead>
				<tbody>
					<tr><td>Positive Corr.</td><td>Credit Risk Score</td><td>0.0706</td><td>Higher scores are correlated with higher fraud.</td></tr>
					<tr><td>Positive Corr.</td><td>Customer Age</td><td>0.0630</td><td>Older applicants in this specific dataset are correlated with higher fraud</td></tr>
					<tr><td>Positive Corr.</td><td>Income</td><td>0.0451</td><td>Higher reported income correlates slightly with fraud attempts.</td></tr>
					<tr><td>Negative Corr.</td><td>DOB Distinct Emails</td><td>-0.0432</td><td>Higher email-to-birthday variance reduces implies less fraud</td></tr>
					<tr><td>Negative Corr.</td><td>Name-Email Similarity</td><td>-0.0367</td><td>Higher similarity between names and emails implies less fraud.</td></tr>
					<tr><td>Negative Corr.</td><td>Has Other Cards</td><td>-0.0352</td><td>Existing customers are less likely to be flagged as fraudulent.</td></tr>
				</tbody>
			</table>
		</div>

		<p>Looking at correlation data, the top positive and negative correlations with fraud are: Customer Age, Credit Risk Score, Income, Has Other Cards, Name-Email Similarity, and Date of Birth Distinct Emails.</p>

		<div class="viz-card wide">
			<img src="/figures/correlation_heatmap_full.png" alt="Correlation Heatmap: Bank Account Fraud Dataset" />
		</div>

		<ul>
			<li>Here it is evident that velocity features are correlated with each other. This is likely the case since a bank account application within 6 hours of a previous one would be double counted in both the 24 hours and 4 weeks velocity count. Therefore, this feature may not provide useful insight in a future model and might need to be trimmed to only the 6-hour feature.</li>
			<li>There is also evidence of a high correlation between credit risk scores and proposed credit limits. This makes sense, as banks are likely to offer high credit limits to low risk score applicants.</li>
			<li>Our key feature though, fraud_bool, show no obvious "smoking gun." The highest correlations that are visible are those that have already been addressed in the previous section: customer_age, credit_risk_score, income, has_other_cards, name_email_similarity, and date_of_birth_distinct_emails_4w.</li>
		</ul>
	</section>

	<!-- Section 6: Normality Checks -->
	<section class="exploration-section" id="normality">
		<div class="section-num-wrap"><span class="section-num">06</span></div>
		<h2>Normality Checks</h2>

		<div class="viz-card wide">
			<img src="/figures/qq_normality_full.png" alt="QQ Plot: Normality Observations" />
		</div>

		<p>Overwhelmingly, based on these 6 features that were highly correlated (both positively and negatively) with fraudulent activity, the data is not normally distributed. This will be addressed in the cleaning stage of this milestone.</p>
	</section>

	<!-- Section 7: Velocity Graphs -->
	<section class="exploration-section" id="velocity">
		<div class="section-num-wrap"><span class="section-num">07</span></div>
		<h2>Velocity Graphs</h2>

		<div class="viz-card wide">
			<img src="/figures/velocity_distributions_full.png" alt="Velocity Feature Distributions" />
		</div>

		<p>While the velocity features were not part of the top correlated features with fraud, it is a common-sense approach that associates frequent requests with fraudulent activity. Observations of the correlation heat map and these histograms confirm that they are very similar which implies that they are providing redundant information. That said, if we look at velocity_6h in isolation, we can see a positive skew which is indicative of volatility and could be evidence of bot attacks or other fraudulent activity.</p>
	</section>

	<!-- Section 8: Data Quality, Bias and Limitations -->
	<section class="exploration-section" id="missing">
		<div class="section-num-wrap"><span class="section-num">08</span></div>
		<h2>Data Quality, Bias and Limitations</h2>

		<div class="table-scroll">
			<table>
				<thead>
					<tr>
						<th>Feature</th>
						<th>Missing Count</th>
						<th>Missing %</th>
						<th>Interpretation</th>
					</tr>
				</thead>
				<tbody>
					<tr><td>Count of Months at Previous Address</td><td>712,920</td><td>71.29%</td><td>Largest gap: Over 70% of data missing for this feature</td></tr>
					<tr><td>Count of Months with Current Bank</td><td>253,635</td><td>25.36%</td><td>Large gap: Over 25% of data missing for this feature. Is this implicative of new customers?</td></tr>
					<tr><td>Count of Months at Current Address</td><td>4,254</td><td>0.43%</td><td>Small gap: Less than 1% missing. Recently moved or just missing data?</td></tr>
					<tr><td>Length of Session in Minutes</td><td>2,015</td><td>0.20%</td><td>Small gap: Most session lengths have been logged successfully</td></tr>
					<tr><td>Credit Risk Score</td><td>488</td><td>0.05%</td><td>Practically negligible</td></tr>
					<tr><td>Device Distinct Emails (&lt;=8 weeks)</td><td>359</td><td>0.04%</td><td>Practically negligible</td></tr>
				</tbody>
			</table>
		</div>

		<h3>Completeness</h3>
		<p>The data is complete in general however fields like prev_address_months_count and bank_months_count are missing values at an extremely high percentage. This will be addressed in the cleaning phase.</p>

		<h3>Consistency/Usability</h3>
		<ul>
			<li>In general, the data is fairly consistent and very usable. However, some patterns have emerged in EDA that specifically need to be addressed in cleaning. Patterns of high correlation indicate redundant features in velocity as well as in credit_score_risk and proprosed_credit_limit. Only one of these features per correlated set should be retained moving forward.</li>
			<li>As shown in the Q-Q plots, the data is highly non-normal and that needs to be addressed. In the transformation and normalization stage, this will be addressed, specifically in the application of One-Hot-Encoding.</li>
		</ul>

		<h3>Bias and Ethics</h3>
		<div class="table-scroll">
			<table>
				<thead>
					<tr>
						<th>Feature Category</th>
						<th>Metric</th>
						<th>Legitimate Result</th>
						<th>Fraudulent Result</th>
						<th>Interpretation</th>
					</tr>
				</thead>
				<tbody>
					<tr><td>Numerical</td><td>Customer Age</td><td>33.61 (Mean)</td><td>40.86 (Mean)</td><td>Differential: +21.5% - The average age of an applicant that was deemed fraudulent was, on average, 21.5% older than "legitimate" applicants.</td></tr>
					<tr><td>Numerical</td><td>Credit Risk Score</td><td>130.47 (Mean)</td><td>177.59 (Mean)</td><td>Differential: +36.1% - The average credit risk score of an applicant that was deemed fraudulent was, on average, 36.1% higher than "legitimate" applicants.</td></tr>
					<tr><td>Numerical</td><td>Income Level</td><td>0.56 (Mean)</td><td>0.69 (Mean)</td><td>Differential: +23.2% - The average income of an applicant that was deemed fraudulent was, on average, 23.2% higher than "legitimate" applicants.</td></tr>
					<tr><td>Housing Status</td><td>BA</td><td>163,318 (Count)</td><td>6,357 (Count)</td><td>3.74% Fraud Rate: Fraud Rate larger than data set fraud rate. Potential bias against applicants in this category.</td></tr>
					<tr><td>Housing Status</td><td>BE</td><td>168,553 (Count)</td><td>582 (Count)</td><td>0.34% Fraud Rate: Baseline "stable" housing group. Similar total counts to BA, but 11x less likely to be fraud.</td></tr>
					<tr><td>Employment</td><td>CC</td><td>36,826 (Count)</td><td>932 (Count)</td><td>2.47% Fraud Rate: Potential bias: almost double the average fraud rate for the entire dataset.</td></tr>
					<tr><td>Employment</td><td>CA</td><td>721,353 (Count)</td><td>8,899 (Count)</td><td>1.22% Fraud Rate: The baseline "stable" employment group; high volume, similar fraud rate to dataset.</td></tr>
					<tr><td>Location</td><td>Foreign Request</td><td>24,687 (Count)</td><td>555 (Count)</td><td>2.20% Fraud Rate: Geographic Bias: compared to domestic requests, foreign requests are almost 2x as likely to be flagged as fraudulent.</td></tr>
					<tr><td>Payment</td><td>AC</td><td>247,862 (Count)</td><td>4,209 (Count)</td><td>1.67% Fraud Rate: Of all the fraudulent payment methods, AC was the highest.</td></tr>
					<tr><td>Bank Tenure</td><td>No Other Cards</td><td>766,914 (Count)</td><td>10,098 (Count)</td><td>1.30% Fraud Rate: Compared to existing bank cardholders, would-be first-time members carry 3x the likelihood of being fraudulent as existing customers (0.41%).</td></tr>
				</tbody>
			</table>
		</div>

		<p>In this dataset, it appears that application which were deemed as fraudulent tended to come from applications in which the individual drafted a fairly strong financial profile (older, higher income, higher credit scores, etc.). As a result:</p>
		<ul>
			<li>A model may build a profile for what is determined to be a "legitimate" applicant as somebody who is younger and has a lower income which could potentially lead to false-positives and "punish" older, wealthier, better credit score, applicants who fraudsters seem to imitate.</li>
			<li>On the flip side, a model could also develop a profile that discriminates against younger, less established people who don't fit the housing, employment status, or bank tenure categories that the system favors.</li>
		</ul>

		<p>As noted above, in terms of bias, some of the potential risks for bias application occur in categories such as Housing Status-BA, Employment Status – CC, and Foreign Requests. In these specific categories, rates of fraud were disproportionately high when compared to the dataset average of 1.1029%</p>

		<p>In conclusion for this bias and ethics section, it will be imperative that the methods that are used to develop this model reinforce the concept of being demographic-agnostic. It would be a detriment to have a model learn fraud based on any sort of demographic category. If properly implemented, these guidelines will enable the team to develop a model that is both accurate and fair.</p>

		<h3>Limitations</h3>
		<p>This data set leads one to believe that we are looking at sophisticated con-artists or competent identity thieves. Contrary to common wisdom, this model will not be able to rely on typical values such as higher income or higher credit scores.</p>
		<p>There are several redundant features that could convince a model into overfitting or just cause general confusion. These redundant features should be removed prior to implementing model training.</p>
		<p>There is at least one feature that has zero variance. Zero variance features provide no helpful information for model training so those features should also be removed.</p>
		<p>The elephant in the room is that this data set is largely imbalanced. We are looking for the needle in the haystack. A model that guesses "not fraud" for 100% of the scenarios has a 98.9% accuracy rate. The implication here is that standard accuracy metrics are a limitation and other methods will need to be implemented instead.</p>
	</section>
</div>
</div>

<style>
	/* Styles generated/assisted by AI (Claude, Anthropic) */

	.page-bg {
		position: relative;
		z-index: 2;
		min-height: 100vh;
		padding: 0 2rem;
	}

	.page-header {
		text-align: center;
		padding: 8rem 0 2rem;
	}

	h1 {
		font-size: clamp(2rem, 5vw, 3.5rem);
		font-weight: 800;
		color: #1a1a2e;
		letter-spacing: -0.03em;
		margin-bottom: 1rem;
	}

	.gradient-text {
		background: linear-gradient(90deg, #ec4899 20%, #ff4665 50%, #7c3aed 80%);
		background-clip: text;
		-webkit-background-clip: text;
		-webkit-text-fill-color: transparent;
	}

	.doc-meta {
		display: flex;
		justify-content: center;
		gap: 0.75rem;
		flex-wrap: wrap;
		margin-bottom: 2rem;
	}

	.meta-pill {
		display: inline-flex;
		align-items: center;
		gap: 0.3rem;
		font-size: 0.8rem;
		font-weight: 500;
		color: #5b4578;
		background: rgba(255, 255, 255, 0.85);
		border: 1px solid rgba(236, 72, 153, 0.15);
		padding: 0.4rem 1rem;
		border-radius: 100px;
	}

	/* === Table of Contents === */
	.toc {
		display: flex;
		justify-content: center;
		gap: 0.25rem;
		flex-wrap: wrap;
		max-width: 900px;
		margin: 0 auto 3rem;
		padding: 0.75rem;
		background: rgba(255, 255, 255, 0.7);
		border-radius: 16px;
		border: 1px solid rgba(236, 72, 153, 0.1);
	}

	.toc-item {
		display: flex;
		align-items: center;
		gap: 0.4rem;
		padding: 0.45rem 0.85rem;
		border: none;
		background: transparent;
		border-radius: 10px;
		cursor: pointer;
		transition: all 0.3s ease;
		font-family: inherit;
	}

	.toc-item:hover {
		background: rgba(236, 72, 153, 0.08);
	}

	.toc-item.active {
		background: linear-gradient(135deg, rgba(236, 72, 153, 0.12), rgba(124, 58, 237, 0.12));
	}

	.toc-item.active .toc-num {
		background: linear-gradient(135deg, #ec4899, #7c3aed);
		color: #fff;
	}

	.toc-num {
		font-size: 0.6rem;
		font-weight: 700;
		width: 22px;
		height: 22px;
		border-radius: 6px;
		display: flex;
		align-items: center;
		justify-content: center;
		background: rgba(124, 58, 237, 0.1);
		color: #7c3aed;
		transition: all 0.3s ease;
	}

	.toc-label {
		font-size: 0.72rem;
		font-weight: 500;
		color: #4a3660;
	}

	/* === Content === */
	.content {
		max-width: 900px;
		margin: 0 auto;
		padding-bottom: 5rem;
	}

	.exploration-section {
		background: rgba(255, 255, 255, 0.92);
		border: 1px solid rgba(236, 72, 153, 0.1);
		border-radius: 20px;
		padding: 2.5rem 2.5rem 2rem;
		margin-bottom: 2rem;
		position: relative;
		overflow: hidden;
		transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.4s, box-shadow 0.4s;
		scroll-margin-top: 2rem;
	}

	.exploration-section::before {
		content: '';
		position: absolute;
		top: 0;
		left: 0;
		width: 4px;
		height: 100%;
		background: linear-gradient(180deg, #ec4899, #a855f7, #7c3aed);
		border-radius: 4px 0 0 4px;
	}

	.exploration-section:hover {
		border-color: rgba(236, 72, 153, 0.2);
		box-shadow: 0 12px 48px rgba(124, 58, 237, 0.08);
	}

	.section-num-wrap {
		margin-bottom: 1rem;
	}

	.section-num {
		display: inline-flex;
		align-items: center;
		justify-content: center;
		width: 40px;
		height: 40px;
		border-radius: 12px;
		background: linear-gradient(135deg, #ec4899, #7c3aed);
		color: #fff;
		font-weight: 800;
		font-size: 0.9rem;
		letter-spacing: -0.02em;
		box-shadow: 0 4px 16px rgba(236, 72, 153, 0.25);
	}

	h2 {
		font-size: 1.5rem;
		font-weight: 700;
		color: #2d1b4e;
		margin-bottom: 1rem;
		letter-spacing: -0.01em;
	}

	h3 {
		font-size: 1.1rem;
		font-weight: 600;
		color: #3d2a5c;
		margin-top: 1.5rem;
		margin-bottom: 0.75rem;
		padding-bottom: 0.35rem;
		border-bottom: 2px solid rgba(236, 72, 153, 0.12);
		display: inline-block;
	}

	p {
		color: #5b4578;
		margin-bottom: 0.75rem;
		line-height: 1.8;
	}

	em {
		font-style: italic;
		color: #3d2a5c;
		font-weight: 500;
	}

	/* === Tables === */
	.table-scroll {
		overflow-x: auto;
		border-radius: 12px;
		border: 1px solid rgba(236, 72, 153, 0.1);
		margin: 1rem 0;
	}

	table {
		width: 100%;
		border-collapse: collapse;
		font-size: 0.82rem;
	}

	thead {
		background: linear-gradient(135deg, rgba(236, 72, 153, 0.06), rgba(124, 58, 237, 0.06));
	}

	th {
		padding: 0.75rem 1rem;
		text-align: left;
		font-weight: 600;
		color: #2d1b4e;
		border-bottom: 2px solid rgba(236, 72, 153, 0.12);
		white-space: nowrap;
	}

	td {
		padding: 0.6rem 1rem;
		color: #5b4578;
		border-bottom: 1px solid rgba(236, 72, 153, 0.06);
		line-height: 1.6;
	}

	/* === Viz Cards === */
	.viz-card {
		background: rgba(255, 255, 255, 0.6);
		border: 1px solid rgba(236, 72, 153, 0.1);
		border-radius: 14px;
		padding: 1.25rem;
		margin: 1.5rem 0;
		transition: border-color 0.3s, box-shadow 0.3s;
	}

	.viz-card:hover {
		border-color: rgba(236, 72, 153, 0.25);
		box-shadow: 0 4px 20px rgba(124, 58, 237, 0.06);
	}

	.viz-card img {
		width: 100%;
		border-radius: 8px;
		border: 1px solid rgba(236, 72, 153, 0.08);
	}

	.viz-caption {
		font-size: 0.85rem;
		color: #6b5585;
		font-style: italic;
		margin-top: 0.75rem;
		margin-bottom: 0;
		line-height: 1.6;
	}

	/* === Lists === */
	ul {
		list-style: none;
		padding-left: 0;
		margin-bottom: 1rem;
	}

	li {
		color: #5b4578;
		margin-bottom: 0.6rem;
		padding-left: 1.5rem;
		position: relative;
		line-height: 1.7;
	}

	li::before {
		content: '';
		position: absolute;
		left: 0;
		top: 0.6em;
		width: 6px;
		height: 6px;
		border-radius: 50%;
		background: linear-gradient(135deg, #ec4899, #a855f7);
		box-shadow: 0 0 4px rgba(236, 72, 153, 0.3);
	}

	ol {
		padding-left: 0;
		counter-reset: item;
		list-style: none;
		margin-bottom: 1rem;
	}

	.interpretations ol li {
		counter-increment: item;
		padding-left: 2rem;
		margin-bottom: 1rem;
		position: relative;
		color: #5b4578;
		line-height: 1.7;
	}

	.interpretations ol li::before {
		content: counter(item);
		position: absolute;
		left: 0;
		top: 0;
		width: 24px;
		height: 24px;
		border-radius: 6px;
		background: linear-gradient(135deg, rgba(236, 72, 153, 0.12), rgba(124, 58, 237, 0.12));
		color: #7c3aed;
		font-weight: 700;
		font-size: 0.7rem;
		display: flex;
		align-items: center;
		justify-content: center;
	}

	/* === Responsive === */
	@media (max-width: 700px) {
		.toc {
			gap: 0.15rem;
			padding: 0.5rem;
		}
		.toc-label {
			display: none;
		}
		.toc-item {
			padding: 0.4rem;
		}
		.exploration-section {
			padding: 2rem 1.5rem 1.5rem;
		}
	}
</style>
