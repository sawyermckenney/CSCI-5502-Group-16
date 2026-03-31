<script lang="ts">
	import { onMount } from 'svelte';

	let imageFailed: Record<string, boolean> = $state({});
	let lightboxImage: { src: string; name: string } | null = $state(null);

	function handleImageError(name: string) {
		imageFailed[name] = true;
	}

	function openLightbox(src: string, name: string) {
		if (!imageFailed[name.toLowerCase().split(' ')[0]]) {
			lightboxImage = { src, name };
		}
	}

	function closeLightbox() {
		lightboxImage = null;
	}

	function handleKeydown(e: KeyboardEvent) {
		if (e.key === 'Escape' && lightboxImage) {
			closeLightbox();
		}
	}

	onMount(async () => {
		const { gsap } = await import('gsap');
		const { ScrollTrigger } = await import('gsap/ScrollTrigger');
		gsap.registerPlugin(ScrollTrigger);

		// Title reveal
		gsap.from('.page-header h1', { opacity: 0, y: 40, duration: 0.8, delay: 0.2 });
		gsap.from('.page-header .page-desc', { opacity: 0, y: 20, duration: 0.6, delay: 0.4 });

		// Cards stagger in
		gsap.from('.card', {
			opacity: 0,
			y: 100,
			rotateX: 15,
			stagger: 0.12,
			duration: 0.8,
			ease: 'power3.out',
			scrollTrigger: { trigger: '.grid', start: 'top 85%' }
		});
	});
</script>

<svelte:window onkeydown={handleKeydown} />

{#if lightboxImage}
<!-- svelte-ignore a11y_no_noninteractive_element_interactions -->
<div class="lightbox-overlay" onclick={closeLightbox} onkeydown={(e) => e.key === 'Enter' && closeLightbox()} role="dialog" aria-modal="true" aria-label="Profile picture" tabindex="-1">
	<button class="lightbox-close" onclick={closeLightbox} aria-label="Close">&times;</button>
	<!-- svelte-ignore a11y_click_events_have_key_events -->
	<!-- svelte-ignore a11y_no_noninteractive_element_interactions -->
	<img src={lightboxImage.src} alt={lightboxImage.name} class="lightbox-img" onclick={(e) => e.stopPropagation()} />
	<p class="lightbox-name">{lightboxImage.name}</p>
</div>
{/if}

<div class="page-bg">
<section class="page-header">
	<h1>Our <span class="gradient-text">Team</span></h1>
	<p class="page-desc">The people behind the data.</p>
</section>

<div class="grid">
	<div class="card">
		<div class="card-glow" aria-hidden="true"></div>
		<div class="card-content">
			<button class="avatar-wrap" onclick={() => openLightbox('/team/sam-meaux.jpg', 'Sam Meaux')} aria-label="View Sam Meaux's photo">
				<div class="avatar-ring"></div>
				{#if imageFailed['sam']}
					<div class="avatar">SM</div>
				{:else}
					<img src="/team/sam-meaux.jpg" alt="Sam Meaux" class="avatar-img" onerror={() => handleImageError('sam')} />
				{/if}
			</button>
			<h3>Sam Meaux</h3>
			<span class="role">Visualization Lead</span>
			<p class="bio">Sam Meaux heads the design of data visualizations for the project. He focuses on moving complex results into clear, interpretable visuals and effective communication of our findings.</p>
			<a href="https://www.linkedin.com/in/samuelmeaux/" target="_blank" rel="noopener noreferrer" class="linkedin-link">
				<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
					<path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
				</svg>
				<span>LinkedIn</span>
			</a>
		</div>
	</div>

	<div class="card">
		<div class="card-glow" aria-hidden="true"></div>
		<div class="card-content">
			<button class="avatar-wrap" onclick={() => openLightbox('/team/kayo-abdi.jpg', 'Kayo Abdi')} aria-label="View Kayo Abdi's photo">
				<div class="avatar-ring"></div>
				{#if imageFailed['kayo']}
					<div class="avatar">KA</div>
				{:else}
					<img src="/team/kayo-abdi.jpg" alt="Kayo Abdi" class="avatar-img" onerror={() => handleImageError('kayo')} />
				{/if}
			</button>
			<h3>Kayo Abdi</h3>
			<span class="role">Data Lead</span>
			<p class="bio">Kayo Abdi is in charge of data collection, preprocessing the data, ensuring quality. He maintains the datasets for analysis, while also deleivering a foundation for modeling and evaluation.</p>
			<a href="https://www.linkedin.com/in/abdirahman-kayo-abdi/" target="_blank" rel="noopener noreferrer" class="linkedin-link">
				<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
					<path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
				</svg>
				<span>LinkedIn</span>
			</a>
		</div>
	</div>

	<div class="card">
		<div class="card-glow" aria-hidden="true"></div>
		<div class="card-content">
			<button class="avatar-wrap" onclick={() => openLightbox('/team/david-savic.jpg', 'David Savić')} aria-label="View David Savić's photo">
				<div class="avatar-ring"></div>
				{#if imageFailed['david']}
					<div class="avatar">DS</div>
				{:else}
					<img src="/team/david-savic.jpg" alt="David Savić" class="avatar-img" onerror={() => handleImageError('david')} />
				{/if}
			</button>
			<h3>David Savić</h3>
			<span class="role">Modeling Lead</span>
			<p class="bio">David Savić spearheads on the development of machine learning models for fraud detection, focusing on supervised and unsupervised approaches. His work emphasizes evaluating model performance.</p>
			<a href="https://www.linkedin.com/in/david-savi%C4%87-375a46208/" target="_blank" rel="noopener noreferrer" class="linkedin-link">
				<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
					<path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
				</svg>
				<span>LinkedIn</span>
			</a>
		</div>
	</div>

	<div class="card">
		<div class="card-glow" aria-hidden="true"></div>
		<div class="card-content">
			<button class="avatar-wrap" onclick={() => openLightbox('/team/sawyer-mckenney.jpg', 'Sawyer McKenney')} aria-label="View Sawyer McKenney's photo">
				<div class="avatar-ring"></div>
				{#if imageFailed['sawyer']}
					<div class="avatar">SM</div>
				{:else}
					<img src="/team/sawyer-mckenney.jpg" alt="Sawyer McKenney" class="avatar-img" onerror={() => handleImageError('sawyer')} />
				{/if}
			</button>
			<h3>Sawyer McKenney</h3>
			<span class="role">Evaluation & Metrics Lead</span>
			<p class="bio">Sawyer McKenney designs the framework for evaluating the models and examining model performance using appropriate metrics. His role focuses on comparing trade-offs and ensuring accurate results. </p>
			<a href="https://www.linkedin.com/in/sawyer-mckenney/" target="_blank" rel="noopener noreferrer" class="linkedin-link">
				<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
					<path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
				</svg>
				<span>LinkedIn</span>
			</a>
		</div>
	</div>
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
		padding: 8rem 0 3rem;
	}

	h1 {
		font-size: clamp(2rem, 5vw, 3.5rem);
		font-weight: 800;
		color: #1a1a2e;
		letter-spacing: -0.03em;
		margin-bottom: 0.5rem;
	}

	.gradient-text {
		background: linear-gradient(90deg, #ec4899 20%, #ff4665 50%, #7c3aed 80%);
		background-clip: text;
		-webkit-background-clip: text;
		-webkit-text-fill-color: transparent;
	}

	.page-desc {
		color: #6b5585;
		font-size: 1.1rem;
	}

	.grid {
		display: grid;
		grid-template-columns: repeat(2, 1fr);
		gap: 2rem;
		padding-bottom: 5rem;
		max-width: 1100px;
		margin: 0 auto;
	}

	@media (max-width: 768px) {
		.grid {
			grid-template-columns: 1fr;
			max-width: 500px;
		}
	}

	.card {
		background: rgba(255, 255, 255, 0.95);
		border: 1px solid rgba(236, 72, 153, 0.12);
		border-radius: 24px;
		padding: 0;
		text-align: center;
		position: relative;
		overflow: hidden;
		box-shadow:
			0 4px 24px rgba(124, 58, 237, 0.06),
			0 1px 4px rgba(0, 0, 0, 0.04);
		transition: transform 0.5s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.4s, box-shadow 0.5s;
		display: flex;
		flex-direction: column;
	}

	/* Gradient accent bar at top */
	.card::before {
		content: '';
		display: block;
		height: 4px;
		background: linear-gradient(90deg, #ec4899, #a855f7, #7c3aed);
		border-radius: 24px 24px 0 0;
		flex-shrink: 0;
	}

	.card-glow {
		position: absolute;
		top: -50%;
		left: -50%;
		width: 200%;
		height: 200%;
		background: radial-gradient(circle at center, rgba(236, 72, 153, 0.06), transparent 40%);
		opacity: 0;
		transition: opacity 0.5s;
		pointer-events: none;
	}

	.card:hover {
		transform: translateY(-8px);
		border-color: rgba(236, 72, 153, 0.25);
		box-shadow:
			0 20px 60px rgba(124, 58, 237, 0.12),
			0 8px 24px rgba(236, 72, 153, 0.06);
	}

	.card:hover .card-glow {
		opacity: 1;
	}

	/* Card inner content */
	.card-content {
		padding: 2.25rem 2rem 2rem;
		display: flex;
		flex-direction: column;
		align-items: center;
		flex: 1;
	}

	/* === Avatar with spinning ring === */
	.avatar-wrap {
		position: relative;
		width: 120px;
		height: 120px;
		margin: 0 auto 1.25rem;
		background: none;
		border: none;
		padding: 0;
		cursor: pointer;
		transition: transform 0.3s ease;
	}

	.avatar-wrap:hover {
		transform: scale(1.05);
	}

	.avatar-wrap:focus-visible {
		outline: 2px solid #ec4899;
		outline-offset: 4px;
		border-radius: 50%;
	}

	.avatar-ring {
		position: absolute;
		inset: -4px;
		border-radius: 50%;
		border: 2px solid transparent;
		border-top-color: #ec4899;
		border-right-color: #a855f7;
		animation: ring-spin 3s infinite linear;
	}

	@keyframes ring-spin {
		0% { transform: rotateZ(0deg); }
		100% { transform: rotateZ(360deg); }
	}

	.avatar {
		width: 120px;
		height: 120px;
		border-radius: 50%;
		background: linear-gradient(135deg, #7c3aed, #ec4899);
		color: #ffffff;
		display: flex;
		align-items: center;
		justify-content: center;
		font-weight: 700;
		font-size: 1.5rem;
		box-shadow: 0 4px 20px rgba(124, 58, 237, 0.25);
	}

	.avatar-img {
		width: 120px;
		height: 120px;
		border-radius: 50%;
		object-fit: cover;
		object-position: center 20%;
		box-shadow: 0 4px 20px rgba(124, 58, 237, 0.25);
		border: 3px solid #fff;
	}

	h3 {
		font-size: 1.3rem;
		font-weight: 700;
		color: #2d1b4e;
		margin-bottom: 0.4rem;
	}

	.role {
		display: inline-block;
		font-size: 0.68rem;
		font-weight: 600;
		text-transform: uppercase;
		letter-spacing: 0.1em;
		color: #ec4899;
		background: rgba(236, 72, 153, 0.08);
		padding: 0.3rem 0.85rem;
		border-radius: 100px;
		margin-bottom: 1.25rem;
	}

	.bio {
		font-size: 0.88rem;
		color: #5b4578;
		line-height: 1.75;
		margin-bottom: 1.5rem;
		max-width: 380px;
		flex: 1;
	}

	.linkedin-link {
		display: inline-flex;
		align-items: center;
		gap: 0.5rem;
		padding: 0.55rem 1.25rem;
		background: linear-gradient(135deg, #0077b5, #0a66c2);
		color: #ffffff;
		text-decoration: none;
		font-size: 0.82rem;
		font-weight: 500;
		border-radius: 10px;
		transition: transform 0.3s, box-shadow 0.3s;
	}

	.linkedin-link:hover {
		transform: translateY(-2px);
		box-shadow: 0 6px 20px rgba(0, 119, 181, 0.35);
	}

	.linkedin-link svg {
		flex-shrink: 0;
	}

	/* === Lightbox === */
	.lightbox-overlay {
		position: fixed;
		inset: 0;
		background: rgba(0, 0, 0, 0.85);
		z-index: 1000;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		padding: 2rem;
		animation: fadeIn 0.3s ease;
	}

	@keyframes fadeIn {
		from { opacity: 0; }
		to { opacity: 1; }
	}

	.lightbox-close {
		position: absolute;
		top: 1.5rem;
		right: 1.5rem;
		background: none;
		border: none;
		color: white;
		font-size: 3rem;
		cursor: pointer;
		line-height: 1;
		transition: transform 0.2s;
	}

	.lightbox-close:hover {
		transform: scale(1.2);
	}

	.lightbox-img {
		max-width: 90vw;
		max-height: 75vh;
		object-fit: contain;
		border-radius: 12px;
		box-shadow: 0 8px 40px rgba(0, 0, 0, 0.5);
		animation: scaleIn 0.3s ease;
	}

	@keyframes scaleIn {
		from { transform: scale(0.9); opacity: 0; }
		to { transform: scale(1); opacity: 1; }
	}

	.lightbox-name {
		color: white;
		font-size: 1.5rem;
		font-weight: 600;
		margin-top: 1.5rem;
		text-shadow: 0 2px 8px rgba(0,0,0,0.5);
	}
</style>
