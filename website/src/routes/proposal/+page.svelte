<script lang="ts">
	import { onMount } from 'svelte';

	let activeSection = $state('');

	const sections = [
		{ id: 'topic-summary', num: '01', label: 'Research Topic Summary' },
		{ id: 'scope', num: '02', label: 'Scope & Boundaries' },
		{ id: 'questions', num: '03', label: 'Research Questions' },
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
	<h1>Proposal <span class="gradient-text">Overview</span></h1>
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
	<!-- Section 1: Research Topic Summary -->
	<section class="proposal-section" id="topic-summary">
		<div class="section-num-wrap"><span class="section-num">01</span></div>
		<h2>Research Topic Summary</h2>
		<ul>
			<li>We examine financial fraud detection in large data sets</li>
			<li>This project evaluates and compare supervised and unsupervised fraud detection methods</li>
			<li>The goal with this project is to identify patterns and understand the trade-offs with different approaches</li>
			<li>Model performance will be compared to understand the strengths and limitations of each approach in real-world fraud detection scenarios</li>
		</ul>
	</section>

	<!-- Section 2: Scope & Boundaries -->
	<section class="proposal-section" id="scope">
		<div class="section-num-wrap"><span class="section-num">02</span></div>
		<h2>Scope & Boundaries</h2>

		<h3>What is in scope</h3>
		<ul>
			<li>Transaction data from various datasets</li>
			<li>Evaluation of model performance across different cases</li>
			<li>Tradeoff analysis between accuracy and detection</li>
		</ul>

		<h3>What is out of scope</h3>
		<ul>
			<li>Real time fraud detection</li>
			<li>Integration with other systems</li>
			<li>Scalability across millions of transactions</li>
		</ul>

		<!-- Optional: add a visual/diagram here -->
	</section>

	<!-- Section 3: Research Questions -->
	<section class="proposal-section" id="questions">
		<div class="section-num-wrap"><span class="section-num">03</span></div>
		<h2>Research Questions</h2>
		<p>Ten research questions spanning descriptive, comparative, and predictive types.</p>

		<div class="rq-grid">
			<div class="rq-card descriptive">
				<span class="rq-type">Descriptive</span>
				<span class="rq-number">1</span>
				<p>How do supervised models and unsupervised anomaly detectors compare at catching rare fraud as we vary the fraud rates and the "cost" of false alarms?</p>
			</div>

			<div class="rq-card descriptive">
				<span class="rq-type">Descriptive</span>
				<span class="rq-number">2</span>
				<p>How exactly does the severity of class imbalance, meaning how rare the fraud actually is impact the performance of supervised models?</p>
			</div>

			<div class="rq-card comparative">
				<span class="rq-type">Comparative</span>
				<span class="rq-number">3</span>
				<p>Does changing the fraud prevalence have a different effect on the success of unsupervised detection methods? </p>
			</div>

			<div class="rq-card comparative">
				<span class="rq-type">Comparative</span>
				<span class="rq-number">4</span>
				<p>If we assume a fixed "alert budget" where a team can only check the top-K transactions, which of these two methods actually performs better?</p>
			</div>

			<div class="rq-card descriptive">
				<span class="rq-type">Descriptive</span>
				<span class="rq-number">5</span>
				<p>What do the real world trade-offs between precision and recall look like for each approach as we shift our alert thresholds?  </p>
			</div>

			<div class="rq-card comparative">
				<span class="rq-type">Comparative</span>
				<span class="rq-number">6</span>
				<p>Which specific transaction features show the biggest "red flags" that allow us to separate fraud from legitimate activity?  </p>
			</div>

			<div class="rq-card comparative">
				<span class="rq-type">Comparative</span>
				<span class="rq-number">7</span>
				<p>Do unsupervised scores do a better job of putting real fraud at the very top of the rankings compared to supervised probabilities?  </p>
			</div>

			<div class="rq-card descriptive">
				<span class="rq-type">Descriptive</span>
				<span class="rq-number">8</span>
				<p>Are these fraud patterns and trade-offs stable enough to hold up across different datasets with varying structures?  </p>
			</div>

			<div class="rq-card descriptive">
				<span class="rq-type">Descriptive</span>
				<span class="rq-number">9</span>
				<p>Can we use clustering techniques to find specific "pockets" of transactions where fraud is much more likely to hide? </p>
			</div>

			<div class="rq-card predictive">
				<span class="rq-type">Predictive</span>
				<span class="rq-number">10</span>
				<p>Under what specific conditions balancing the rarity of the fraud and the cost of an alert does one of these approaches finally outperform the other?</p>
			</div>
		</div>
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

	/* === Research Questions Grid === */
	.rq-grid {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 1rem;
		margin-top: 1.5rem;
	}

	.rq-card {
		background: rgba(255, 255, 255, 0.6);
		border: 1px solid rgba(236, 72, 153, 0.1);
		border-radius: 14px;
		padding: 1.25rem 1.5rem;
		position: relative;
		transition: border-color 0.3s, box-shadow 0.3s;
	}

	.rq-card:hover {
		border-color: rgba(236, 72, 153, 0.25);
		box-shadow: 0 4px 20px rgba(124, 58, 237, 0.06);
	}

	.rq-type {
		display: inline-block;
		font-size: 0.65rem;
		font-weight: 600;
		text-transform: uppercase;
		letter-spacing: 0.08em;
		padding: 0.2rem 0.6rem;
		border-radius: 6px;
		margin-bottom: 0.5rem;
	}

	.rq-card.descriptive .rq-type {
		background: rgba(59, 130, 246, 0.1);
		color: #3b82f6;
	}

	.rq-card.comparative .rq-type {
		background: rgba(236, 72, 153, 0.1);
		color: #ec4899;
	}

	.rq-card.predictive .rq-type {
		background: rgba(124, 58, 237, 0.1);
		color: #7c3aed;
	}

	.rq-number {
		display: inline-block;
		font-size: 0.7rem;
		font-weight: 700;
		color: rgba(45, 27, 78, 0.35);
		margin-left: 0.5rem;
	}

	.rq-card p {
		font-size: 0.9rem;
		color: #4a3660;
		margin-bottom: 0;
		line-height: 1.6;
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
		.rq-grid {
			grid-template-columns: 1fr;
		}
	}
</style>
