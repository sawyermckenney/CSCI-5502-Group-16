<script lang="ts">
	import { onMount } from 'svelte';

	onMount(async () => {
		const { gsap } = await import('gsap');
		const { ScrollTrigger } = await import('gsap/ScrollTrigger');
		gsap.registerPlugin(ScrollTrigger);

		// Hero entrance
		const tl = gsap.timeline();
		tl.from('.hero-label', { opacity: 0, y: 20, duration: 0.6, delay: 0.2 })
			.from('.hero h1', { opacity: 0, y: 40, duration: 0.8 }, '-=0.3')
			.from('.hero-desc', { opacity: 0, y: 20, duration: 0.6 }, '-=0.4')
			.from('.hero-line', { scaleX: 0, duration: 0.8, ease: 'power2.out' }, '-=0.3');

		// Stats counter animation
		document.querySelectorAll('.stat-number').forEach((el) => {
			const target = parseInt(el.getAttribute('data-value') || '0');
			gsap.from(el, {
				textContent: 0,
				duration: 2,
				ease: 'power1.out',
				snap: { textContent: 1 },
				scrollTrigger: { trigger: el, start: 'top 85%' },
				onUpdate: function () {
					el.textContent = Math.ceil(parseFloat(el.textContent || '0')).toString();
				}
			});
		});

		// Section reveals
		gsap.utils.toArray('.reveal').forEach((el: any) => {
			gsap.from(el, {
				opacity: 0,
				y: 60,
				duration: 0.8,
				ease: 'power2.out',
				scrollTrigger: { trigger: el, start: 'top 85%' }
			});
		});
	});
</script>

<!-- Hero -->
<section class="hero">
	<span class="hero-label">CSCI 5502 &middot; University of Colorado Boulder</span>
	<h1>Data Mining<br /><span class="gradient-text">Group 16</span></h1>
	<p class="hero-desc">
		Uncovering patterns. Building models. Extracting knowledge from data.
	</p>
	<div class="hero-line"></div>
</section>

<!-- Content panel that scrolls over the video -->
<div class="content-panel">
	<div class="panel-edge" aria-hidden="true"></div>
	<div class="panel-inner">

		<!-- Stats -->
		<section class="stats reveal">
			<div class="stat">
				<span class="stat-number" data-value="4">4</span>
				<span class="stat-label">Team Members</span>
			</div>
			<div class="stat">
				<span class="stat-number" data-value="3">1</span>
				<span class="stat-label">Research Questions</span>
			</div>
			<div class="stat">
				<span class="stat-number" data-value="5">4</span>
				<span class="stat-label">Mining Techniques</span>
			</div>
		</section>

		<!-- Section 1: Research Topic & Significance -->
		<section class="intro-section reveal">
			<div class="section-header">
				<span class="section-number">01</span>
				<div class="section-label">
					<span class="intro-icon">◆</span>
					<span>Research Topic & Significance</span>
				</div>
			</div>
			<h2><span class="text-pop">Research Topic & Significance</span></h2>
			<div class="section-body">
				<p>Financial fraud detection is a serious problem in our modern economies
					 due to the volume of online transactions and the fact that they will
					  only continue to increase. Electronic payment systems also contribute 
					  to this. As transaction volumes increase, so does the opportunity for 
					  fraud to take place, so it is imperative to find methods to prevent and 
					  detect these behaviors. A key challenge in fraud detection is extreme class 
					  imbalance, where fraudulent transactions represent only a very small fraction 
					  of all activity. This imbalance complicates traditional machine learning 
					  approaches and makes naïve performance metrics misleading. Many fraud 
					  detection systems must identify a handful of malicious cases among 
					  hundreds of thousands of legitimate transactions. Missing fraudulent 
					  activity can result in substantial financial losses, while overly aggressive 
					  detection can disrupt normal customers. Beyond the immediate monetary loss, 
					  the persistence of undetected fraud is one of the key factors in the erosion 
					  of trust in any digital banking infrastructure. As those perpetuating this
					   fraud are becoming more sophisticated with the increases in technology, 
					   “rule-based systems” are starting to become increasingly more out of touch 
					   with reality. This now requires programmers and security professionals to move 
					   toward dynamic, data-driven mining techniques that can adapt to evolving patterns. 
					    As a result, designing effective fraud detection systems requires careful trade-offs.
						 This project focuses on comparing supervised fraud detection models with 
						 unsupervised anomaly detection techniques under severe class imbalance. 
						 We will look at how these approaches fluctuate in their ability to detect 
						 fraud transactions. Understanding these differences is required for building 
						 real-world fraud detection that is both practical and scalable.  </p>
			</div>
			<div class="section-visual">
				<img src="/graphs/research_topic_vis_chart.png" alt="Distribution of Transactions in Credit Card Dataset — 284,315 non-fraud vs 492 fraud" />
				<p class="visual-caption">Figure 1 illustrates the extreme imbalance in the Kaggle Credit Card Fraud dataset, where only 492 out of 284,807 transactions (~0.17%) are labeled as fraud. This highlights the challenges for detection systems, as naïve models could achieve over 99% accuracy simply by predicting “non-fraud” for every transaction. </p>
			</div>
		</section>

		<!-- Section 2: Stakeholders & Real-World Impact -->
		<section class="intro-section reveal">
			<div class="section-header">
				<span class="section-number">02</span>
				<div class="section-label">
					<span class="intro-icon">◆</span>
					<span>Stakeholders & Real-World Impact</span>
				</div>
			</div>
			<h2><span class="text-pop">Stakeholders & Real-World Impact</span></h2>
			<div class="section-body">
				<p>Fraud detection impacts a very wide range of stakeholders across the 
					financial world, covering categories such as individual users all the way to 
					global institutions. Financial institutions such as banks and credit card 
					companies are heavily dependent on fraud detection systems that are reliably 
					accurate to minimize losses to self and customers as well as maintain customer 
					trust. Payment processors and online merchants are also affected, as undetected 
					fraud can lead to chargebacks and significant reputational damage. Consumers 
					experience the consequences of fraud detection directly through declined transactions 
					or account freezes caused by false positives. These inconveniences can lead to
					 "customer turnover,” where users switch to competitors after a negative security 
					 experience. Regulatory bodies also have a vested interest in ensuring that 
					 institutions implement effective safeguards against financial crime and money 
					 laundering. Fraud analysts and data scientists must balance model complexity 
					 with interpretability and operational constraints within these organizations. 
					 Poorly designed detection systems can overload analysts with alerts, reducing 
					 overall effectiveness and leading to a sort of “alert fatigue”. At the same time,
					  overly conservative systems may fail to stop sophisticated fraud schemes that 
					  target high value assets. Comparing supervised detection with unsupervised detection
					   methods is how this project intends to provide insights that are relevant to both 
					   technical teams and high-level decision-makers. The findings can inform the 
					   target audience on how organizations deploy data-driven algorithms for fraud 
					   detection to protect their bottom line. Ultimately, improved fraud detection
					    benefits institutions, consumers, and the greater stability of the financial system. </p>
			</div>
		</section>

		<!-- Section 3: Existing Solutions & Gaps -->
		<section class="intro-section reveal">
			<div class="section-header">
				<span class="section-number">03</span>
				<div class="section-label">
					<span class="intro-icon">◆</span>
					<span>Existing Solutions & Gaps</span>
				</div>
			</div>
			<h2><span class="text-pop">Existing Solutions & Gaps</span></h2>
			<div class="section-body">
				<p>Existing fraud detection solutions typically rely on supervised machine
					 learning models trained on labeled historical data. These models can 
					 achieve strong performance when sufficient labeled examples are 
					 available for the algorithm to learn patterns. However, in fraud 
					 detection, labeled fraud cases are extremely rare and often costly 
					 or time-consuming to obtain accurately. This limitation makes 
					 supervised models vulnerable to overfitting and poor generalization 
					 when they encounter “zero-day” fraud types. Unsupervised anomaly 
					 detection methods offer an alternative by identifying unusual 
					 transaction patterns without requiring pre-existing labels. While
					  these approaches can surface novel or emerging fraud behaviors, 
					  they may also flag many benign outliers as suspicious. Both approaches
					   face significant challenges related to evaluation under class 
					   imbalance, where standard accuracy is a misleading metric. While we
					    know that metrics like precision and AUPRC are vital for catching 
						rare events, the reality of managing these systems is often much 
						messier. Most organizations rely on a mix of hard-coded rules and
						 machine learning, which adds a lot of moving parts to the process.
						  Even with all the research available, we still don't have a clear 
						  answer on whether supervised or unsupervised models perform better 
						  at different scales. This study aims to fill that gap by putting 
						  both methods to the test under controlled conditions. By citing established
						   benchmarks, we aim to clarify the boundaries between these two distinct
						    detection paradigms.  </p>
			</div>
			<div class="section-citations">
				<p class="citation">Dal Pozzolo, A., Caelen, O., Johnson, R. A., &amp; Bontempi, G. (2013). Credit Card Fraud Detection Dataset. <em>Kaggle</em>. <a href="https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud" target="_blank" rel="noopener noreferrer">https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud</a></p>
				<p class="citation">Phua, C., Lee, V., Smith, K., &amp; Gayler, R. (2010). A Comprehensive Survey of Data Mining-based Fraud Detection Research. <em>Artificial Intelligence Review</em>, 34(1), 1&ndash;14. <a href="https://arxiv.org/abs/1009.6119" target="_blank" rel="noopener noreferrer">https://arxiv.org/abs/1009.6119</a></p>
			</div>
		</section>

		<!-- Section 4: Blueprint for Your Project -->
		<section class="intro-section reveal">
			<div class="section-header">
				<span class="section-number">04</span>
				<div class="section-label">
					<span class="intro-icon">◆</span>
					<span>Project Blueprint</span>
				</div>
			</div>
			<h2><span class="text-pop">Blueprint for Our Project</span></h2>
			<div class="section-body">
				<p>This project follows a structured analytical pipeline to evaluate fraud
					 detection approaches. Before diving into modeling, we’ll start with an 
					 exploratory look at the data to see how transactions are distributed and 
					 how severe the class imbalance really is. Our primary focus is the Credit
					  Card Fraud Detection dataset, which covers about 284,000 labeled transactions.
					   To make sure our conclusions aren’t just a fluke of this specific data, 
					   we’re also pulling in benchmarks from the Fraud Dataset Benchmark to validate 
					   our results across different environments. Supervised models such as logistic 
					   regression, random forests, and gradient boosting will be trained using labeled 
					   data to establish a performance baseline. In parallel, unsupervised anomaly 
					   detection techniques such as Isolation Forests or Local Outlier Factors will 
					   be applied to identify unusual transaction patterns. Model outputs will then be 
					   compared across different fraud prevalence levels and various alert thresholds 
					   to simulate real-world conditions. Evaluation will focus strictly on metrics 
					   appropriate for imbalanced data, such as recall and precision, and the area under
					    the PR curve. The analysis is designed specifically to highlight the critical 
						trade-offs between detection effectiveness and false positive rates. This 
						comprehensive blueprint ensures a fair and systematic comparison of modeling
						 approaches across different algorithmic families. The results will provide 
						 practical guidance for fraud detection system design in highly imbalanced 
						 environments. </p>
			</div>
		</section>

		<!-- Section 5: Research Questions Overview -->
		<section class="intro-section reveal">
			<div class="section-header">
				<span class="section-number">05</span>
				<div class="section-label">
					<span class="intro-icon">◆</span>
					<span>Research Questions</span>
				</div>
			</div>
			<h2><span class="text-pop">Research Questions Overview</span></h2>
			<div class="section-body">
				<p>Detecting fraud in an imbalanced environment is never straightforward.
					 Relying on just one metric will hardly ever give you the full picture. 
					 Every team has different priorities, whether that is cutting down on 
					 financial losses or making sure legitimate customers aren't constantly 
					 getting blocked. Because of these competing goals, we’ve developed a series of 
					 research questions that focus on the actual trade-offs between different 
					 modeling styles. Instead of just looking at high-level totals, we’re digging
					  into transaction-level data to see how these systems hold up under real pressure.
					   We want to understand exactly how the choice of an evaluation metric can 
					   change, or even mess up, how we perceive a model's success. By tackling these 
					   issues head-on, we hope to clarify when a supervised or unsupervised approach 
					   actually makes the most sense. Our analysis also includes a deep dive into specific
					    features to see which ones are truly the best indicators of a fraudulent hit.
						 These questions aren't just theoretical; they serve as a practical guide to
						  keep the entire project grounded in real-world data science. We’ve designed 
						  this framework to ensure the findings are actually useful for people working 
						  in the field. Ultimately, this approach builds a solid foundation for 
						  understanding the messy reality of financial crime.  </p>
			</div>
		</section>
	</div>
</div>

<style>
	/* Styles generated/assisted by AI (Claude, Anthropic) */

	/* === Hero === */
	.hero {
		text-align: center;
		position: relative;
		min-height: 100vh;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}

	/* === Content Panel (scrolls over video) === */
	.content-panel {
		position: relative;
		z-index: 2;
		background: #0a0a0f;
	}

	.panel-edge {
		position: absolute;
		top: -60px;
		left: 0;
		right: 0;
		height: 60px;
		background: linear-gradient(to bottom, transparent, #0a0a0f);
		pointer-events: none;
	}

	.panel-inner {
		max-width: 1200px;
		margin: 0 auto;
		padding: 4rem 2rem 2rem;
	}

	.hero-label {
		display: inline-block;
		font-size: 0.8rem;
		font-weight: 500;
		letter-spacing: 0.15em;
		text-transform: uppercase;
		color: rgba(255, 255, 255, 0.5);
		margin-bottom: 1.5rem;
	}

	h1 {
		font-size: clamp(2.5rem, 6vw, 4.5rem);
		font-weight: 800;
		line-height: 1.1;
		letter-spacing: -0.03em;
		color: #ffffff;
		margin-bottom: 1.5rem;
		text-shadow: 0 2px 20px rgba(0, 0, 0, 0.3);
	}

	.gradient-text {
		background: linear-gradient(90deg, #fe7ac6 20%, #ff4665 50%, #a855f7 80%);
		background-clip: text;
		-webkit-background-clip: text;
		-webkit-text-fill-color: transparent;
	}

	.hero-desc {
		font-size: 1.15rem;
		color: rgba(255, 255, 255, 0.6);
		max-width: 480px;
		margin: 0 auto 3rem;
		font-weight: 400;
	}

	.hero-line {
		width: 80px;
		height: 2px;
		background: linear-gradient(90deg, #ec4899, #a855f7);
		margin: 0 auto;
		transform-origin: center;
	}

	/* === Stats === */
	.stats {
		display: flex;
		justify-content: center;
		gap: 4rem;
		padding: 3rem 0 4rem;
		border-bottom: 1px solid rgba(255, 255, 255, 0.06);
		margin-bottom: 4rem;
	}

	.stat {
		text-align: center;
	}

	.stat-number {
		display: block;
		font-size: 3rem;
		font-weight: 800;
		letter-spacing: -0.03em;
		background: linear-gradient(135deg, #ec4899, #a855f7);
		background-clip: text;
		-webkit-background-clip: text;
		-webkit-text-fill-color: transparent;
	}

	.stat-label {
		font-size: 0.85rem;
		color: rgba(255, 255, 255, 0.35);
		font-weight: 500;
		text-transform: uppercase;
		letter-spacing: 0.08em;
	}

	/* === Introduction Sections === */
	.intro-section {
		margin-bottom: 4rem;
		padding-bottom: 4rem;
		border-bottom: 1px solid rgba(255, 255, 255, 0.06);
	}

	.intro-section:last-child {
		border-bottom: none;
		margin-bottom: 2rem;
	}

	.section-header {
		display: flex;
		align-items: center;
		gap: 1rem;
		margin-bottom: 1.25rem;
	}

	.section-number {
		font-size: 0.75rem;
		font-weight: 700;
		color: rgba(236, 72, 153, 0.4);
		letter-spacing: 0.05em;
		font-variant-numeric: tabular-nums;
	}

	.section-label {
		display: inline-flex;
		align-items: center;
		gap: 0.5rem;
		font-size: 0.75rem;
		font-weight: 600;
		text-transform: uppercase;
		letter-spacing: 0.1em;
		color: #ec4899;
	}

	.intro-icon {
		font-size: 0.6rem;
	}

	.intro-section h2 {
		font-size: 2rem;
		font-weight: 700;
		color: #ffffff;
		margin-bottom: 1rem;
		line-height: 1.2;
	}

	.text-pop {
		background: linear-gradient(90deg, #ec4899, #f97316);
		background-clip: text;
		-webkit-background-clip: text;
		-webkit-text-fill-color: transparent;
	}

	.section-body p {
		color: rgba(255, 255, 255, 0.6);
		line-height: 1.8;
		margin-bottom: 1.25rem;
		font-size: 1.05rem;
	}

	.section-visual {
		margin-top: 2rem;
		text-align: center;
	}

	.section-visual img {
		max-width: 100%;
		border-radius: 12px;
		border: 1px solid rgba(255, 255, 255, 0.08);
	}

	.visual-caption {
		font-size: 0.8rem;
		color: rgba(255, 255, 255, 0.35);
		line-height: 1.5;
		font-style: italic;
		margin-top: 0.75rem;
	}

	.section-citations {
		margin-top: 2rem;
		padding: 1.25rem 1.5rem;
		background: rgba(255, 255, 255, 0.03);
		border: 1px solid rgba(255, 255, 255, 0.08);
		border-radius: 12px;
	}

	.citation {
		font-size: 0.85rem;
		color: rgba(255, 255, 255, 0.45);
		line-height: 1.7;
		margin-bottom: 0.75rem;
	}

	.citation:last-child {
		margin-bottom: 0;
	}

	.citation em {
		font-style: italic;
		color: rgba(255, 255, 255, 0.55);
	}

	.citation a {
		color: rgba(236, 72, 153, 0.6);
		text-decoration: none;
		transition: color 0.3s;
	}

	.citation a:hover {
		color: #ec4899;
	}

	/* === Mobile Responsive === */
	@media (max-width: 768px) {
		.hero {
			min-height: 80vh;
			padding: 0 1rem;
		}

		.hero-desc {
			font-size: 1rem;
			padding: 0 0.5rem;
		}

		.panel-inner {
			padding: 3rem 1.25rem 2rem;
		}

		.stats {
			gap: 1.5rem;
			padding: 2rem 0 3rem;
			margin-bottom: 3rem;
		}

		.stat-number {
			font-size: 2.25rem;
		}

		.stat-label {
			font-size: 0.7rem;
		}

		.intro-section {
			margin-bottom: 2.5rem;
			padding-bottom: 2.5rem;
		}

		.intro-section h2 {
			font-size: 1.5rem;
		}

		.section-body p {
			font-size: 0.95rem;
			line-height: 1.7;
		}

		.section-citations {
			padding: 1rem;
		}

		.citation {
			font-size: 0.78rem;
			word-break: break-word;
		}

		.visual-caption {
			font-size: 0.75rem;
		}
	}

	@media (max-width: 480px) {
		.stats {
			flex-direction: column;
			gap: 1.25rem;
			align-items: center;
		}

		.panel-inner {
			padding: 2rem 1rem 1.5rem;
		}

		.intro-section h2 {
			font-size: 1.3rem;
		}

		.section-label {
			font-size: 0.65rem;
		}
	}
</style>
