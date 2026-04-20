<script lang="ts">
	import { onMount } from 'svelte';

	interface Section {
		id: string;
		eyebrow: string;
		title: string;
		color: string;
		accent: string;
		icon: string;
		paragraphs: string[];
	}

	const sections: Section[] = [
		{
			id: 'summary',
			eyebrow: '01 — In Plain Terms',
			title: 'Non-Technical Summary',
			color: '#ec4899',
			accent: '#f472b6',
			icon: 'M4 6h16M4 12h10M4 18h16',
			paragraphs: [
				`Fraud detection will never be perfectly accurate. The key distinction with fraud detection models is being able to find a small number of fraudulent transactions that are hidden inside the massive amount of data. In our data set, there were only about 1 percent of transactions that were fraudulent. This makes the problem extremely difficult because most models will naturally predict transactions as safe due to this high amount of imbalance.`,
				`We tested multiple approaches, supervised models are models that learn from labeled examples, like logistic regression and support vector machines (SVMs) and unsupervised methods, such as clustering and pattern mining, which find patterns without labeled data. We also combined these models with ensemble techniques, which means using several models together to make better predictions.`,
				`From this research, the biggest takeaway was that no single model alone solves this problem. Models that were able to catch a good number of fraud would often flag too many normal transactions as fraud as well. On the other side of things, models that were more conservative missed fraud. Performance really spiked when we combined models together, specifically using stacking, which was able to catch more fraud while still not flagging too many non-fraudulent transactions.`
			]
		},
		{
			id: 'insights',
			eyebrow: '02 — What The Data Told Us',
			title: 'Key Insights & Discoveries',
			color: '#a855f7',
			accent: '#c084fc',
			icon: 'M9 21h6M12 3a7 7 0 00-4 12.745V17a1 1 0 001 1h6a1 1 0 001-1v-1.255A7 7 0 0012 3z',
			paragraphs: [
				`Early on, we really need to answer the question: Is fraud random? The answer to that is no. Across multiple models, we were able to discover that fraudulent activity follows consistent patterns across features like history, device behavior, and transaction velocity. This is a good indicator as to why SVM was able to achieve high recall, because there is a hidden structure that separates fraud from non-fraud.`,
				`But the structure is not perfect. Legitimate transactions share a lot of similar characteristics with fraud. This is why precision was consistently low across most of the models. This just goes to show that fraud detection is not just a classification problem; it is also a trade-off problem.`,
				`Another key insight that was discovered through our research was that supervised and unsupervised approaches have distinguishable differences. Supervised models were a lot better at identifying fraud directly when labeled data was available. On the other had unsupervised methods like K-means and Aprori were not the strongest predictors; they were really most useful for understanding how fraud is grouped and that feature combinations appear together.`,
				`As a result, we concluded that ensemble methods outperform individual models. When combining different models, we were able to capture different perspectives of the data that allowed us to capture both local and global patterns that ultimately led to a better performance overall.`
			]
		},
		{
			id: 'impact',
			eyebrow: '03 — Why It Matters',
			title: 'Real-World Impact',
			color: '#06b6d4',
			accent: '#22d3ee',
			icon: 'M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6',
			paragraphs: [
				`In the real world, fraud detection is essential for the success of a business. We suggest that relying on a single model is simply not realistic, and that instead a layered system must be put in place to both save resources and still be effective.`,
				`We found that a practical system will most likely use SVM as an initial filter because it's a model with high recall and flags potentially risky transactions. Then, additional models can be applied on top of this to reduce the number of false positives before they are sent to be reviewed by an individual or team. This both reduces the risk and keeps the number of unnecessary alerts manageable.`,
				`The importance of flexibility is also something to consider. Meaning that businesses might want to adjust how aggressive their fraud detection system is, depending on the situation. For example, during high-risk periods where a lot of applications are flowing in at the same time, it may make more sense to prioritize recall and catch as much fraud as possible because the cost of missing many cases would be so high. Then, during lower risk periods, businesses might want to improve precision and reduce the number of false alarms to keep the manual review manageable.`,
				`All in all, the research in this project shows that combining models and understanding patterns within the data is the key part of building both a practical and scalable fraud detection system.`
			]
		},
		{
			id: 'future',
			eyebrow: '04 — Where To Go Next',
			title: 'Limitations & Future Work',
			color: '#10b981',
			accent: '#34d399',
			icon: 'M13 10V3L4 14h7v7l9-11h-7z',
			paragraphs: [
				`The dataset used was synthetic, meaning they were based on older fraud patterns. The data set we designed to reflect real behavior, it may not fully capture how modern fraud operates today. Future work should evaluate models on more recent and real-world data to trly evalaute the models' effectiveness.`,
				`Second, the models that we have come up with struggle with precision, meaning there are a lot of false positives. This is so critical because it creates operational challenges, since each false positive needs to be reviewed; this can really impact the customer experience if implemented in a real-world environment. Future work should really focus on balancing this through threshold tuning, cost-sensitive learning, and more advanced models.`,
				`Another limitation was that the models were trained in a static environment. Where in the real world and with real systems, fraud patterns evolve over time. Future models and work should incorporate continuous learning methods to stream data directly into pipelines so models are able to adjust to new emerging patterns.`,
				`Finally, deep learning and an autoencoder might be another method worth exploring to capture more complex patterns within the data. This has the potential to improve both detection accuracy and be able to generalize to new types of fraud on continuously expanding data sets.`
			]
		}
	];

	let cards: HTMLElement[] = $state([]);

	function handleTilt(e: PointerEvent) {
		const card = e.currentTarget as HTMLElement;
		const rect = card.getBoundingClientRect();
		const x = (e.clientX - rect.left) / rect.width - 0.5;
		const y = (e.clientY - rect.top) / rect.height - 0.5;
		const rotY = x * 10;
		const rotX = -y * 10;
		card.style.setProperty('--rotX', `${rotX}deg`);
		card.style.setProperty('--rotY', `${rotY}deg`);
		card.style.setProperty('--mx', `${(x + 0.5) * 100}%`);
		card.style.setProperty('--my', `${(y + 0.5) * 100}%`);
	}

	function resetTilt(e: PointerEvent) {
		const card = e.currentTarget as HTMLElement;
		card.style.setProperty('--rotX', `0deg`);
		card.style.setProperty('--rotY', `0deg`);
	}

	onMount(async () => {
		const { gsap } = await import('gsap');
		const { ScrollTrigger } = await import('gsap/ScrollTrigger');
		gsap.registerPlugin(ScrollTrigger);

		gsap.from('.page-header h1', { opacity: 0, y: 40, duration: 0.8, delay: 0.1 });
		gsap.from('.page-header .doc-meta', { opacity: 0, y: 20, duration: 0.6, delay: 0.25 });
		gsap.from('.lede', { opacity: 0, y: 20, duration: 0.7, delay: 0.4 });

		cards.forEach((card, i) => {
			gsap.from(card, {
				opacity: 0,
				y: 80,
				rotateX: 15,
				duration: 0.9,
				ease: 'power3.out',
				scrollTrigger: {
					trigger: card,
					start: 'top 85%',
					toggleActions: 'play none none none'
				}
			});
		});
	});
</script>

<svelte:head>
	<title>Conclusion — CSCI 5502 Group 16</title>
</svelte:head>

<div class="conclusion-page">
	<section class="page-header">
		<h1>Conclusion &amp; <span class="gradient-text">Results</span></h1>
		<div class="doc-meta">
			<span class="meta-pill">CSCI 5502 — Data Mining</span>
			<span class="meta-pill">Group 16</span>
			<span class="meta-pill">Final Findings</span>
		</div>
		<p class="lede">
			A layered look at what we learned, what surprised us, what it means in the real world,
			and where this work should go next.
		</p>
	</section>

	<div class="floor">
		<div class="floor-grid"></div>
	</div>

	<section class="stack">
		{#each sections as section, i (section.id)}
			<article
				class="tilt-card"
				bind:this={cards[i]}
				onpointermove={handleTilt}
				onpointerleave={resetTilt}
				style="--accent: {section.color}; --accent-light: {section.accent};"
			>
				<div class="card-face">
					<div class="card-glow" aria-hidden="true"></div>
					<div class="card-shine" aria-hidden="true"></div>

					<header class="card-head">
						<div class="card-icon">
							<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="22" height="22">
								<path d={section.icon} />
							</svg>
						</div>
						<div class="card-number">{section.eyebrow}</div>
					</header>

					<h2 class="card-title">{section.title}</h2>
					<div class="divider"></div>

					<div class="card-body">
						{#each section.paragraphs as p}
							<p>{p}</p>
						{/each}
					</div>
				</div>

				<div class="card-shadow" aria-hidden="true"></div>
			</article>
		{/each}
	</section>

	<section class="closing">
		<div class="closing-inner">
			<div class="sparkle" aria-hidden="true"></div>
			<div class="quote-mark" aria-hidden="true">&ldquo;</div>
			<h3>All models are wrong, but some are <em>useful</em>.</h3>
			<p class="attribution">&mdash; George E. P. Box, statistician (1976)</p>
			<p class="thanks">Thank you for reading.</p>
		</div>
	</section>
</div>

<style>
	/* Styles generated/assisted by AI (Claude, Anthropic) */

	.conclusion-page {
		padding: 2rem 2rem 1rem;
		max-width: 1200px;
		margin: 0 auto;
		position: relative;
		overflow: hidden;
	}

	/* === Header === */
	.page-header {
		text-align: center;
		padding: 4rem 0 1rem;
		position: relative;
	}

	.eyebrow {
		display: inline-block;
		font-size: 0.75rem;
		letter-spacing: 0.28em;
		text-transform: uppercase;
		color: #7c3aed;
		font-weight: 700;
		margin-bottom: 1rem;
		padding: 0.35rem 0.9rem;
		border-radius: 100px;
		background: rgba(255, 255, 255, 0.7);
		border: 1px solid rgba(124, 58, 237, 0.2);
		box-shadow: 0 2px 10px rgba(124, 58, 237, 0.08);
	}

	h1 {
		font-size: clamp(2.2rem, 5.5vw, 3.8rem);
		font-weight: 800;
		color: #1a1a2e;
		letter-spacing: -0.03em;
		margin-bottom: 1.25rem;
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
		font-size: 0.8rem;
		font-weight: 500;
		color: #5b4578;
		background: rgba(255, 255, 255, 0.85);
		border: 1px solid rgba(236, 72, 153, 0.15);
		padding: 0.4rem 1rem;
		border-radius: 100px;
	}

	.lede {
		max-width: 620px;
		margin: 0 auto;
		font-size: 1.05rem;
		color: #4a3663;
		line-height: 1.65;
	}

	/* === Floating floor grid for depth cue === */
	.floor {
		position: absolute;
		left: 50%;
		top: 20%;
		transform: translateX(-50%);
		width: 110%;
		height: 60%;
		pointer-events: none;
		z-index: 0;
		overflow: hidden;
	}

	.floor-grid {
		position: absolute;
		inset: 0;
		background-image:
			linear-gradient(rgba(124, 58, 237, 0.06) 1px, transparent 1px),
			linear-gradient(90deg, rgba(236, 72, 153, 0.06) 1px, transparent 1px);
		background-size: 60px 60px;
		mask-image: radial-gradient(ellipse at center, black 0%, transparent 75%);
		-webkit-mask-image: radial-gradient(ellipse at center, black 0%, transparent 75%);
	}

	/* === Stack of 3D cards === */
	.stack {
		position: relative;
		z-index: 2;
		display: flex;
		flex-direction: column;
		gap: 3.5rem;
		padding: 2rem 0 2rem;
		perspective: 1400px;
		perspective-origin: 50% 40%;
	}

	.tilt-card {
		--rotX: 0deg;
		--rotY: 0deg;
		--mx: 50%;
		--my: 50%;

		position: relative;
		transform-style: preserve-3d;
		transform:
			perspective(1400px)
			rotateX(var(--rotX))
			rotateY(var(--rotY));
		transition: transform 0.35s cubic-bezier(0.23, 1, 0.32, 1);
		will-change: transform;
	}

	/* Alternate tilt offsets for visual rhythm */
	.tilt-card:nth-child(odd) {
		margin-right: 3rem;
	}
	.tilt-card:nth-child(even) {
		margin-left: 3rem;
	}

	.card-face {
		position: relative;
		border-radius: 28px;
		padding: 2.75rem 2.5rem;
		background:
			linear-gradient(145deg, rgba(255, 255, 255, 0.92) 0%, rgba(255, 255, 255, 0.78) 100%);
		backdrop-filter: blur(24px);
		border: 1px solid rgba(255, 255, 255, 0.85);
		box-shadow:
			0 40px 80px -20px rgba(26, 10, 46, 0.18),
			0 20px 40px -15px rgba(124, 58, 237, 0.15),
			0 4px 14px rgba(0, 0, 0, 0.05),
			inset 0 1px 0 rgba(255, 255, 255, 0.95),
			inset 0 -1px 0 rgba(255, 255, 255, 0.3);
		transform-style: preserve-3d;
		overflow: hidden;
	}

	/* Accent strip along top edge */
	.card-face::before {
		content: '';
		position: absolute;
		top: 0;
		left: 0;
		right: 0;
		height: 5px;
		background: linear-gradient(90deg, var(--accent), var(--accent-light), var(--accent));
		background-size: 200% 100%;
		animation: shimmer 6s linear infinite;
	}

	@keyframes shimmer {
		0% { background-position: 0% 0%; }
		100% { background-position: 200% 0%; }
	}

	.card-glow {
		position: absolute;
		top: -40%;
		left: var(--mx);
		width: 360px;
		height: 360px;
		transform: translate(-50%, -50%);
		background: radial-gradient(circle, color-mix(in srgb, var(--accent) 35%, transparent) 0%, transparent 70%);
		opacity: 0.55;
		filter: blur(40px);
		pointer-events: none;
		transition: left 0.3s ease;
	}

	.card-shine {
		position: absolute;
		inset: 0;
		pointer-events: none;
		background: radial-gradient(
			circle at var(--mx) var(--my),
			rgba(255, 255, 255, 0.35) 0%,
			transparent 35%
		);
		mix-blend-mode: overlay;
		transition: background 0.15s ease;
	}

	.card-shadow {
		position: absolute;
		left: 8%;
		right: 8%;
		bottom: -24px;
		height: 36px;
		background: radial-gradient(ellipse at center, rgba(26, 10, 46, 0.35) 0%, transparent 70%);
		filter: blur(14px);
		transform: translateZ(-60px);
		z-index: -1;
		pointer-events: none;
	}

	.card-head {
		display: flex;
		align-items: center;
		gap: 1rem;
		margin-bottom: 1.25rem;
		transform: translateZ(30px);
	}

	.card-icon {
		width: 48px;
		height: 48px;
		border-radius: 14px;
		background: linear-gradient(135deg, var(--accent), var(--accent-light));
		color: #ffffff;
		display: flex;
		align-items: center;
		justify-content: center;
		box-shadow:
			0 10px 25px color-mix(in srgb, var(--accent) 40%, transparent),
			inset 0 1px 0 rgba(255, 255, 255, 0.4);
		flex-shrink: 0;
	}

	.card-number {
		font-size: 0.78rem;
		font-weight: 700;
		letter-spacing: 0.22em;
		text-transform: uppercase;
		color: var(--accent);
		opacity: 0.85;
	}

	.card-title {
		font-size: clamp(1.4rem, 2.4vw, 1.85rem);
		font-weight: 800;
		color: #1a0a2e;
		letter-spacing: -0.02em;
		line-height: 1.2;
		transform: translateZ(40px);
	}

	.divider {
		height: 2px;
		margin: 1.25rem 0 1.5rem;
		background: linear-gradient(
			90deg,
			color-mix(in srgb, var(--accent) 40%, transparent) 0%,
			color-mix(in srgb, var(--accent) 10%, transparent) 60%,
			transparent 100%
		);
		border-radius: 2px;
		transform: translateZ(25px);
	}

	.card-body {
		transform: translateZ(20px);
	}

	.card-body p {
		font-size: 1rem;
		color: #3a2855;
		line-height: 1.8;
		margin-bottom: 1.15rem;
	}

	.card-body p:last-child {
		margin-bottom: 0;
	}

	/* === Closing flourish === */
	.closing {
		position: relative;
		z-index: 2;
		margin-top: 1rem;
		padding: 1rem 0 2rem;
		text-align: center;
	}

	.closing-inner {
		position: relative;
		max-width: 720px;
		margin: 0 auto;
		padding: 2.5rem 2rem;
		border-radius: 24px;
		background: linear-gradient(135deg, rgba(255, 255, 255, 0.9), rgba(255, 255, 255, 0.7));
		backdrop-filter: blur(20px);
		border: 1px solid rgba(255, 255, 255, 0.8);
		box-shadow:
			0 20px 60px rgba(124, 58, 237, 0.12),
			inset 0 1px 0 rgba(255, 255, 255, 0.9);
		overflow: hidden;
	}

	.sparkle {
		position: absolute;
		top: -50%;
		left: 50%;
		width: 400px;
		height: 400px;
		transform: translateX(-50%);
		background: conic-gradient(
			from 180deg at 50% 50%,
			rgba(236, 72, 153, 0.15),
			rgba(168, 85, 247, 0.15),
			rgba(6, 182, 212, 0.15),
			rgba(16, 185, 129, 0.15),
			rgba(236, 72, 153, 0.15)
		);
		filter: blur(60px);
		opacity: 0.6;
		animation: spin 18s linear infinite;
		pointer-events: none;
	}

	@keyframes spin {
		to { transform: translateX(-50%) rotate(360deg); }
	}

	.closing h3 {
		position: relative;
		font-size: clamp(1.15rem, 2.2vw, 1.5rem);
		font-weight: 700;
		color: #1a0a2e;
		letter-spacing: -0.015em;
		line-height: 1.45;
		margin-bottom: 0.75rem;
	}

	.closing h3 em {
		font-style: italic;
		background: linear-gradient(90deg, #ec4899, #7c3aed);
		background-clip: text;
		-webkit-background-clip: text;
		-webkit-text-fill-color: transparent;
	}

	.closing p {
		position: relative;
		color: #6b5585;
		font-size: 0.95rem;
		letter-spacing: 0.04em;
	}

	.quote-mark {
		position: relative;
		font-family: Georgia, serif;
		font-size: 5rem;
		line-height: 0.6;
		color: var(--accent, #a855f7);
		background: linear-gradient(135deg, #ec4899, #7c3aed);
		background-clip: text;
		-webkit-background-clip: text;
		-webkit-text-fill-color: transparent;
		margin-bottom: 0.25rem;
		opacity: 0.85;
	}

	.attribution {
		font-weight: 600;
		color: #5b4578 !important;
		margin-top: 0.75rem !important;
		font-size: 0.9rem !important;
	}

	.thanks {
		margin-top: 1.25rem !important;
		font-style: italic;
		opacity: 0.75;
	}

	/* === Responsive === */
	@media (max-width: 768px) {
		.conclusion-page {
			padding: 5rem 1rem 3rem;
		}

		.page-header {
			padding: 4rem 0 1.5rem;
		}

		.stack {
			gap: 2.5rem;
			perspective: 900px;
		}

		.tilt-card:nth-child(odd),
		.tilt-card:nth-child(even) {
			margin-left: 0;
			margin-right: 0;
		}

		.card-face {
			padding: 1.75rem 1.5rem;
			border-radius: 22px;
		}

		.card-body p {
			font-size: 0.95rem;
			line-height: 1.7;
		}

		.closing-inner {
			padding: 2rem 1.25rem;
		}
	}

	@media (max-width: 480px) {
		.card-face {
			padding: 1.5rem 1.25rem;
		}

		.card-icon {
			width: 40px;
			height: 40px;
			border-radius: 12px;
		}

		.card-number {
			font-size: 0.68rem;
		}
	}

	/* Respect reduced motion */
	@media (prefers-reduced-motion: reduce) {
		.tilt-card {
			transform: none !important;
			transition: none !important;
		}
		.card-face::before,
		.sparkle {
			animation: none;
		}
	}
</style>
