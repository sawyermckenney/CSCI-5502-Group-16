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

		<!-- Introduction -->
		<section class="intro reveal">
			<div class="intro-grid">
				<div class="intro-content">
					<div class="intro-label">
						<span class="intro-icon">◆</span>
						<span>Project Overview</span>
					</div>
					<h2><span class="text-pop">Research Question</span></h2>
					<p class="intro-lead">
						How do supervised fraud detection models compare to unsupervised anomaly-based methods in identifying rare fraudulent transactions, and how does performance change under different fraud rates (imbalance levels) and different alert thresholds (false positive cost)?
					</p>
					<p>
						The goal of this project is to evaluate and compare supervised and unsupervised approaches for detecting fraudulent financial transactions under extreme class imbalance, while keeping the focus on data mining tasks: discovering patterns, identifying unusual behavior, and understanding trade-offs in detection systems.
					</p>
				</div>
				<div class="intro-visual">
					<div class="visual-card">
						<div class="visual-header">The Challenge</div>
						<div class="visual-bars">
							<div class="bar-row">
								<span class="bar-label">Legitimate</span>
								<div class="bar bar-legitimate"></div>
								<span class="bar-pct">99.83%</span>
							</div>
							<div class="bar-row">
								<span class="bar-label">Fraud</span>
								<div class="bar bar-fraud"></div>
								<span class="bar-pct">0.17%</span>
							</div>
						</div>
						<p class="visual-caption">"A classifier that says 'legit' for every record hits 99.8% accuracy but protects no one. Traditional loss functions minimise overall error, so the model happily ignores the minority class."</p>
						<a href="https://mlpills.substack.com/p/issue-99-imbalanced-data-in-fraud" target="_blank" rel="noopener noreferrer" class="visual-cite">— ML Pills, "Imbalanced Data in Fraud Detection"</a>
					</div>
				</div>
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

	/* === Introduction === */
	.intro {
		margin-bottom: 5rem;
	}

	.intro-grid {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 3rem;
		align-items: center;
	}

	@media (max-width: 900px) {
		.intro-grid {
			grid-template-columns: 1fr;
		}
	}

	.intro-content {
		padding-right: 1rem;
	}

	.intro-label {
		display: inline-flex;
		align-items: center;
		gap: 0.5rem;
		font-size: 0.75rem;
		font-weight: 600;
		text-transform: uppercase;
		letter-spacing: 0.1em;
		color: #ec4899;
		margin-bottom: 1rem;
	}

	.intro-icon {
		font-size: 0.6rem;
	}

	.intro h2 {
		font-size: 2rem;
		font-weight: 700;
		color: #ffffff;
		margin-bottom: 1.25rem;
		line-height: 1.2;
	}

	.text-pop {
		background: linear-gradient(90deg, #ec4899, #f97316);
		background-clip: text;
		-webkit-background-clip: text;
		-webkit-text-fill-color: transparent;
	}

	.intro-lead {
		font-size: 1.15rem;
		color: rgba(255, 255, 255, 0.75);
		margin-bottom: 1rem;
		font-weight: 500;
	}

	.intro-content p {
		color: rgba(255, 255, 255, 0.5);
		line-height: 1.8;
		margin-bottom: 1.5rem;
	}

	/* Visual card */
	.intro-visual {
		display: flex;
		justify-content: center;
	}

	.visual-card {
		background: rgba(255, 255, 255, 0.03);
		border: 1px solid rgba(255, 255, 255, 0.08);
		border-radius: 16px;
		padding: 1.75rem;
		width: 100%;
		max-width: 360px;
	}

	.visual-header {
		font-size: 0.7rem;
		font-weight: 600;
		text-transform: uppercase;
		letter-spacing: 0.1em;
		color: rgba(255, 255, 255, 0.4);
		margin-bottom: 1.25rem;
	}

	.visual-bars {
		display: flex;
		flex-direction: column;
		gap: 0.75rem;
		margin-bottom: 1rem;
	}

	.bar-row {
		display: grid;
		grid-template-columns: 70px 1fr 50px;
		align-items: center;
		gap: 0.75rem;
	}

	.bar-label {
		font-size: 0.8rem;
		color: rgba(255, 255, 255, 0.5);
	}

	.bar {
		height: 24px;
		border-radius: 4px;
		position: relative;
		overflow: hidden;
	}

	.bar-legitimate {
		background: linear-gradient(90deg, rgba(34, 197, 94, 0.3), rgba(34, 197, 94, 0.6));
		width: 100%;
	}

	.bar-fraud {
		background: linear-gradient(90deg, rgba(239, 68, 68, 0.5), rgba(236, 72, 153, 0.8));
		width: 3px;
		min-width: 3px;
	}

	.bar-pct {
		font-size: 0.75rem;
		font-weight: 600;
		color: rgba(255, 255, 255, 0.6);
		text-align: right;
	}

	.visual-caption {
		font-size: 0.8rem;
		color: rgba(255, 255, 255, 0.35);
		line-height: 1.5;
		font-style: italic;
		margin: 0;
		padding-top: 0.75rem;
		border-top: 1px solid rgba(255, 255, 255, 0.06);
	}

	.visual-cite {
		display: block;
		font-size: 0.7rem;
		color: rgba(236, 72, 153, 0.6);
		text-decoration: none;
		margin-top: 0.5rem;
		transition: color 0.3s;
	}

	.visual-cite:hover {
		color: #ec4899;
	}
</style>
