<script lang="ts">
	import { onMount } from 'svelte';

	let activeSection = $state('');

	const sections = [
		{ id: 'description', num: '01', label: 'Project Description' },
		{ id: 'data', num: '02', label: 'Data Sources' },
		{ id: 'methods', num: '03', label: 'Methods Plan' },
		{ id: 'experimental', num: '04', label: 'Experimental Design' },
		{ id: 'evaluation', num: '05', label: 'Evaluation Plan' },
		{ id: 'bias', num: '06', label: 'Bias & Limitations' },
		{ id: 'outcomes', num: '07', label: 'Expected Outcomes' },
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

		gsap.from('.proposal-section', {
			opacity: 0,
			y: 60,
			stagger: 0.15,
			duration: 0.7,
			ease: 'power2.out',
			scrollTrigger: { trigger: '.content', start: 'top 80%' }
		});

		// Track active section
		document.querySelectorAll('.proposal-section').forEach((el) => {
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
	<h1>Project <span class="gradient-text">Proposal</span></h1>
	<div class="doc-meta">
		<span class="meta-pill">CSCI 5502 — Data Mining</span>
		<span class="meta-pill">Group 16</span>
		<span class="meta-pill">CU Boulder</span>
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
	<section class="proposal-section" id="description">
		<div class="section-num-wrap"><span class="section-num">01</span></div>
		<h2>Project Description</h2>
		<p>
			The goal of this project is to evaluate and compare supervised and unsupervised approaches
			for detecting fraudulent financial transactions under extreme class imbalance, while keeping
			the focus on data mining tasks: discovering patterns, identifying unusual behavior, and
			understanding trade-offs in detection systems.
		</p>
		<p>Our central research question is:</p>
		<p class="highlight-text">
			How do supervised fraud detection models compare to unsupervised anomaly-based
			methods in identifying rare fraudulent transactions, and how does performance change
			under different fraud rates (imbalance levels) and different alert thresholds (false positive
			cost)?
		</p>
		<p>
			Fraud detection matters because missed fraud can lead to direct financial loss, while excessive
			false positives create real harm through blocked transactions, customer frustration, and wasted
			investigation time. This makes fraud detection a natural setting for studying trade-offs between:
		</p>
		<ul>
			<li>Detection coverage (catching fraud)</li>
			<li>False alarm burden (how many legitimate transactions get flagged)</li>
			<li>Interpretability / pattern discovery (what the data is telling us, even when labels are limited)</li>
		</ul>

		<h3>Data mining lens (not "just model training")</h3>
		<p>Rather than treating this as only a model leaderboard problem, the project emphasizes:</p>
		<ul>
			<li>Anomaly detection: ranking transactions by "how unusual" they are</li>
			<li>Feature exploration: identifying which variables shift most around fraud cases</li>
			<li>Clustering: discovering groups of transaction behaviors and which clusters attract fraud</li>
			<li>Association rules: discovering frequent "co-occurrence" patterns that can describe suspicious profiles</li>
			<li>Threshold/alert trade-offs: showing that the "best" detector depends on operational constraints</li>
		</ul>
		<p>
			Supervised methods (e.g., logistic regression, random forests) will be used as benchmarks
			because they represent what you can do when labels exist. Unsupervised methods will
			represent what you can do when labels are scarce, delayed, or unreliable.
		</p>
	</section>

	<section class="proposal-section" id="data">
		<div class="section-num-wrap"><span class="section-num">02</span></div>
		<h2>Data Sources</h2>
		
		<h3>Dataset A: Credit Card Fraud Detection (transaction-level)</h3>
		<p>Source: Kaggle</p>
		<p>Dataset: Credit Card Fraud Detection (2013 European card transactions)</p>
		<ul>
			<li>~284,807 transactions</li>
			<li>30 features (mostly anonymized / PCA-transformed)</li>
			<li>Binary target label: fraud vs non-fraud</li>
			<li>Strong class imbalance: 492 fraud cases (~0.17%)</li>
		</ul>
		<p>
			This dataset is useful for controlled benchmarking because it is widely used, clean, and has a
			clear fraud label that enables supervised baselines.
		</p>

		<h3>Dataset B: Fraud Dataset Benchmark (FDB)</h3>
		<p>Source: Amazon Science benchmark repo hosted on GitHub</p>
		<p>
			FDB is a collection of fraud-related datasets. We will select 1–2 transaction-like tabular
			datasets from this benchmark to broaden the project beyond a single, older dataset. Selection
			criteria will include:
		</p>
		<ul>
			<li>tabular structure compatible with our pipeline</li>
			<li>availability of a fraud label (for benchmarking)</li>
			<li>ideally variation in fraud prevalence and feature structure (to test robustness)</li>
		</ul>

		<h3>How we will use both datasets</h3>
		<p>
			We will run the same overall mining pipeline separately on the Kaggle dataset and on the
			selected FDB dataset(s) and compare:
		</p>
		<ul>
			<li>how stable fraud-related patterns are across datasets</li>
			<li>whether unsupervised methods behave consistently when the feature space changes</li>
			<li>whether threshold/alert trade-offs look similar or dataset-specific</li>
		</ul>
		<p>
			This avoids high-risk feature alignment/merging while still allowing meaningful cross-dataset
			conclusions.
		</p>
	</section>

	<section class="proposal-section" id="methods">
		<div class="section-num-wrap"><span class="section-num">03</span></div>
		<h2>Methods Plan</h2>

		<h3>3.1 Data preparation and basic exploration</h3>
		<p>For each dataset, we will:</p>
		<ul>
			<li>verify shape, data types, missingness, and duplicates</li>
			<li>review label distribution and quantify imbalance</li>
			<li>check basic distributions for key numeric variables (e.g., amount if available)</li>
			<li>examine correlations / redundancy (especially important if features are PCA-like)</li>
		</ul>
		<p>
			Output artifacts (proposal-level): we will describe these steps and the planned visualizations; in
			the final project we will include summary tables and representative plots.
		</p>

		<h3>3.2 Feature exploration focused on "fraud signals"</h3>
		<p>Even when features are anonymized (PCA-style), we can still do meaningful mining:</p>
		<ul>
			<li>Compare feature distributions for fraud vs non-fraud (histograms/boxplots or summary statistics)</li>
			<li>Rank features by how differently they behave in fraud vs normal (examples: mean difference, effect size, mutual information, or simple separability scores)</li>
			<li>Identify "tripwire features": variables that consistently spike or shift during fraud</li>
		</ul>
		<p>
			This provides interpretability in a "behavioral" sense even if we cannot assign real-world names
			to the variables.
		</p>

		<h3>3.3 Unsupervised / anomaly-focused detection (planned, final method TBD)</h3>
		<p>
			We will include at least two unsupervised/anomaly detection approaches drawn from what we
			learn in class. The project will frame them as ranking systems: each transaction receives an
			anomaly score, and we evaluate how well the top-ranked transactions capture fraud.
		</p>
		<p>
			Possible unsupervised families we expect to consider (exact methods depend on course
			coverage):
		</p>
		<ul>
			<li>distance-based or density-based outlier scoring</li>
			<li>clustering-based outlier detection (e.g., far-from-centroid behavior)</li>
			<li>neighbor-based anomaly scoring</li>
			<li>isolation-style scoring methods</li>
		</ul>
		<p>
			Even if we haven't chosen the exact algorithms yet, our proposal commits to the evaluation
			structure: unsupervised approaches output a score/ranking, which is then evaluated under
			different alert thresholds.
		</p>

		<h3>3.4 Clustering for behavioral structure discovery</h3>
		<p>Clustering will be used to uncover transaction "types" and relate them to fraud concentration.</p>
		<p>Planned clustering steps:</p>
		<ul>
			<li>Apply clustering (e.g., k-means or density-based clustering depending on feature space)</li>
			<li>Analyze cluster composition (size, feature profiles, variability)</li>
			<li>Measure fraud concentration by cluster (fraud rate within each cluster)</li>
			<li>Interpret clusters as behavioral segments (even if features are anonymized)</li>
		</ul>
		<p>This can reveal whether fraud tends to appear as:</p>
		<ul>
			<li>a distinct cluster ("fraud mode")</li>
			<li>boundary behavior (fraud near edges of normal clusters)</li>
			<li>scattered anomalies (fraud distributed, not clusterable)</li>
		</ul>

		<h3>3.5 Association rules for interpretable pattern mining</h3>
		<p>Association rules require categorical/binned inputs, so we will:</p>
		<ul>
			<li>discretize selected numeric features into bins (e.g., low/medium/high or quantiles)</li>
			<li>optionally include transaction metadata if available (type/currency/etc. in FDB datasets)</li>
		</ul>
		<p>We will mine rules such as:</p>
		<ul>
			<li>feature-bin combinations that frequently co-occur in fraudulent cases</li>
			<li>rules that are rare overall but enriched among fraud</li>
		</ul>
		<p>
			This gives human-readable "if-then"-style patterns, which complements black-box anomaly
			scores.
		</p>

		<h3>3.6 Supervised benchmarks (kept simple on purpose)</h3>
		<p>We will use supervised learning models mainly as a comparison point:</p>
		<ul>
			<li>Logistic Regression (interpretable baseline)</li>
			<li>Random Forest (nonlinear baseline)</li>
		</ul>
		<p>
			These models will not be presented as the whole project; they are "what you get when labels
			exist," used to compare against anomaly and mining approaches.
		</p>
	</section>

	<section class="proposal-section" id="experimental">
		<div class="section-num-wrap"><span class="section-num">04</span></div>
		<h2>Experimental Design</h2>

		<h3>Condition 1: Varying fraud rate (imbalance levels)</h3>
		<p>
			To test robustness under different imbalance levels, we will simulate multiple conditions where
			feasible by adjusting the dataset composition. For example:
		</p>
		<ul>
			<li>keep fraud fixed and vary the number of non-fraud samples</li>
			<li>or create multiple subsets representing different fraud prevalence regimes</li>
		</ul>
		<p>
			The goal is not to "fix" imbalance, but to observe how detection strategies break or hold when
			fraud becomes rarer or less rare.
		</p>

		<h3>Condition 2: Threshold choice / cost of false positives</h3>
		<p>
			Fraud detection is operational. A real system cannot flag everything. We will evaluate methods
			under different alert thresholds, such as:
		</p>
		<ul>
			<li>flag top 0.1%, 0.5%, 1% of transactions by anomaly score / predicted probability</li>
			<li>compare how many fraud cases are captured under each alert budget</li>
		</ul>
		<p>
			This directly expresses "cost of false positives" as how many people you bother to catch
			fraud.
		</p>
	</section>

	<section class="proposal-section" id="evaluation">
		<div class="section-num-wrap"><span class="section-num">05</span></div>
		<h2>Evaluation Plan (designed for imbalance)</h2>
		<p>
			We will explicitly avoid raw accuracy as a primary metric, because accuracy can be misleading
			when fraud is &lt;1%.
		</p>
		<p>We plan to report metrics aligned to imbalance and operational constraints, such as:</p>
		<ul>
			<li>Recall / True Positive Rate (TPR): fraction of fraud caught</li>
			<li>Precision: fraction of flagged transactions that are actually fraud</li>
			<li>PR-AUC (Precision–Recall AUC): a stronger summary metric than ROC-AUC for rare events</li>
			<li>False positives per N transactions (alert burden)</li>
			<li>Top-K / alert-budget capture rate: fraud captured when only investigating K alerts</li>
		</ul>
		<p>
			Unsupervised methods will be evaluated through their ranking: how concentrated fraud is near
			the top of the anomaly list. Supervised methods will be evaluated both by probability thresholds
			and by top-K.
		</p>
	</section>

	<section class="proposal-section" id="bias">
		<div class="section-num-wrap"><span class="section-num">06</span></div>
		<h2>Potential Bias / Limitations</h2>

		<h3>Extreme class imbalance</h3>
		<p>
			In the Kaggle dataset, only 492 of ~285,000 transactions are fraud (&lt;1%). A trivial classifier that
			predicts "not fraud" for everything can achieve ~99.8% accuracy while detecting zero fraud. To
			address this, we will avoid accuracy as a headline metric and instead emphasize recall/TPR,
			precision, PR-AUC, and alert-budget evaluations that measure meaningful detection under
			imbalance.
		</p>

		<h3>Feature anonymization limits interpretability</h3>
		<p>
			The Kaggle dataset uses PCA-transformed feature columns rather than real transaction
			attributes. This removes human interpretability and blocks "person-in-the-loop" reasoning about
			obvious edge cases. A human might immediately question an unusually large purchase in a
			specific context, but anonymized features prevent that kind of direct semantic judgment. To
			mitigate this, we will focus on behavioral interpretability: ranking which features are most
			associated with fraud behavior, identifying "tripwire" variables, and comparing fraud vs non-fraud
			distributions to extract usable insights even without real feature names.
		</p>

		<h3>Temporal relevance and concept drift</h3>
		<p>
			The Kaggle dataset is from 2013. Fraud tactics evolve rapidly, and patterns that mattered then
			may not reflect modern fraud. This risks building a detector that is tuned to "2013-style fraud."
			To mitigate, we will treat the Kaggle dataset as a proof-of-concept benchmark and include at
			least one additional dataset from the Fraud Dataset Benchmark to test whether mined patterns
			and detection trade-offs generalize beyond a single historical snapshot. Our final report will
			explicitly note that real-world deployment would require evaluation on more recent, operational
			datasets.
		</p>

		<h3>Dataset heterogeneity across FDB</h3>
		<p>
			FDB datasets may differ in schema, feature meaning, and fraud definition. This limits direct
			comparability and makes full merging risky. We will mitigate by running a consistent pipeline and
			comparing results at the level of patterns and trade-offs (e.g., stability of anomaly ranking
			behavior and threshold trade-off curves), rather than assuming features are identical across
			datasets.
		</p>
	</section>

	<section class="proposal-section" id="outcomes">
		<div class="section-num-wrap"><span class="section-num">07</span></div>
		<h2>Expected Outcomes</h2>
		<p>By the end of the project we expect to produce:</p>
		<ul>
			<li>A clear comparison of supervised vs unsupervised detection under extreme imbalance</li>
			<li>Evidence that the "best" approach depends on alert threshold and fraud prevalence</li>
			<li>Clustering and association-rule outputs that provide interpretable descriptions of suspicious patterns</li>
			<li>Cross-dataset comparison showing which findings appear stable vs dataset-specific</li>
		</ul>
		<p class="highlight-text">
			How do supervised fraud detection models compare to unsupervised anomaly-based methods
			in identifying rare fraudulent transactions, and how does performance change under different
			fraud rates (imbalance levels) and different alert thresholds (false positive cost)?
		</p>
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

	/* === Document Meta Pills === */
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

	.proposal-section {
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

	.proposal-section::before {
		content: '';
		position: absolute;
		top: 0;
		left: 0;
		width: 4px;
		height: 100%;
		background: linear-gradient(180deg, #ec4899, #a855f7, #7c3aed);
		border-radius: 4px 0 0 4px;
	}

	.proposal-section:hover {
		border-color: rgba(236, 72, 153, 0.2);
		box-shadow: 0 12px 48px rgba(124, 58, 237, 0.08);
	}

	/* === Section Number === */
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

	.highlight-text {
		background: linear-gradient(135deg, rgba(236, 72, 153, 0.06), rgba(124, 58, 237, 0.06));
		border-left: 3px solid #ec4899;
		padding: 1.25rem 1.5rem;
		border-radius: 0 12px 12px 0;
		font-style: italic;
		color: #4a3660;
		font-weight: 500;
	}

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
		.proposal-section {
			padding: 2rem 1.5rem 1.5rem;
		}
	}
</style>
