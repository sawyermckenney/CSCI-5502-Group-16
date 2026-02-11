<script lang="ts">
	import { page } from '$app/state';
	import favicon from '$lib/assets/favicon.svg';
	import { onMount } from 'svelte';

	let { children } = $props();
	const hideVideoBg = $derived(
		['/team', '/proposal'].some((path) => page.url.pathname.startsWith(path))
	);

	let showDisclaimer = $state(false);
	let dismissedDisclaimer = $state(false);

	function dismissDisclaimer() {
		dismissedDisclaimer = true;
		try { sessionStorage.setItem('disclaimerDismissed', '1'); } catch {}
	}

	onMount(async () => {
		try {
			if (!sessionStorage.getItem('disclaimerDismissed')) {
				setTimeout(() => { showDisclaimer = true; }, 800);
			} else {
				dismissedDisclaimer = true;
			}
		} catch {
			setTimeout(() => { showDisclaimer = true; }, 800);
		}

		// Force video play on mobile — if blocked, hide video to show gradient fallback
		const vid = document.querySelector('.video-bg video') as HTMLVideoElement;
		if (vid) {
			vid.play().catch(() => {
				vid.style.display = 'none';
			});
		}

		const { gsap } = await import('gsap');
		const { ScrollTrigger } = await import('gsap/ScrollTrigger');
		gsap.registerPlugin(ScrollTrigger);

		// Navbar blur on scroll
		ScrollTrigger.create({
			start: 'top -80',
			onUpdate: (self) => {
				const nav = document.querySelector('nav');
				if (nav) {
					if (self.direction === 1 && self.scroll() > 80) {
						nav.classList.add('scrolled');
					} else if (self.scroll() <= 80) {
						nav.classList.remove('scrolled');
					}
				}
			}
		});
	});
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
	<link rel="preconnect" href="https://fonts.googleapis.com" />
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous" />
	<link
		href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap"
		rel="stylesheet"
	/>
	<title>CSCI 5502 - Group 16</title>
</svelte:head>

<div class="app" class:light-bg={hideVideoBg}>
	<!-- Fullscreen video background -->
	{#if !hideVideoBg}
		<div class="video-bg" aria-hidden="true">
			<div class="video-fallback"></div>
			<video autoplay loop muted playsinline>
				<source src="/heroVideo.mp4" type="video/mp4" />
			</video>
			<div class="video-overlay"></div>
		</div>
	{/if}

	<nav>
		<div class="nav-inner">
			<a href="/" class="nav-logo-pill" class:active={page.url.pathname === '/'}>
				<span class="logo-diamond"></span>
				<span class="logo-text">GROUP 16</span>
			</a>
			<div class="nav-links">
				<a href="/" class="nav-link" class:active={page.url.pathname === '/'}>Introduction</a>
				<a href="/proposal" class="nav-link" class:active={page.url.pathname.startsWith('/proposal')}>Proposal</a>
				<a href="/team" class="nav-link" class:active={page.url.pathname.startsWith('/team')}>Team</a>
			</div>
		</div>
	</nav>

	<main>
		{@render children()}
	</main>

	<footer>
		<div class="footer-glow" aria-hidden="true"></div>
		<p>CSCI 5502 Data Mining &mdash; Group 16 &mdash; University of Colorado Boulder</p>
	</footer>

	{#if showDisclaimer && !dismissedDisclaimer}
		<!-- svelte-ignore a11y_no_static_element_interactions -->
		<div class="disclaimer-banner" class:visible={showDisclaimer}>
			<div class="disclaimer-inner">
				<svg class="disclaimer-icon" viewBox="0 0 20 20" fill="currentColor" width="16" height="16">
					<path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd" />
				</svg>
				<p class="disclaimer-text">
					<strong>Academic Disclaimer:</strong> This website was built with the assistance of AI tools (Claude, Anthropic). No member of Group 16 claims sole authorship of the site design or code.
				</p>
				<button class="disclaimer-dismiss" onclick={dismissDisclaimer} aria-label="Dismiss disclaimer">
					<svg viewBox="0 0 20 20" fill="currentColor" width="14" height="14">
						<path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
					</svg>
				</button>
			</div>
		</div>
	{/if}
</div>

<style>
	/* Styles generated/assisted by AI (Claude, Anthropic) */

	:global(*, *::before, *::after) {
		box-sizing: border-box;
		margin: 0;
		padding: 0;
	}

	:global(body) {
		font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
		color: #e8e0f0;
		background: #0a0a0f;
		line-height: 1.6;
		overflow-x: hidden;
		-webkit-font-smoothing: antialiased;
	}

	:global(::selection) {
		background: rgba(236, 72, 153, 0.3);
		color: #ffffff;
	}

	.app {
		display: flex;
		flex-direction: column;
		min-height: 100vh;
		position: relative;
	}

	.app.light-bg {
		background: linear-gradient(160deg, #ffffff 0%, #fdf2f8 20%, #fce7f3 40%, #f5d0fe 60%, #e9d5ff 75%, #c4b5fd 90%, #a78bfa 100%);
	}

	/* === Fullscreen Video Background === */
	.video-bg {
		position: fixed;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
		z-index: 0;
		overflow: hidden;
		background: #0a0a0f;
	}

	.video-fallback {
		position: absolute;
		inset: 0;
		background:
			radial-gradient(ellipse at 20% 50%, rgba(124, 58, 237, 0.15) 0%, transparent 50%),
			radial-gradient(ellipse at 80% 20%, rgba(236, 72, 153, 0.12) 0%, transparent 50%),
			radial-gradient(ellipse at 60% 80%, rgba(168, 85, 247, 0.1) 0%, transparent 50%),
			linear-gradient(160deg, #0a0a0f 0%, #0d0d1a 30%, #110d1f 60%, #0a0a0f 100%);
		animation: fallbackShift 12s ease-in-out infinite alternate;
	}

	@keyframes fallbackShift {
		0% { background-position: 0% 0%, 100% 0%, 50% 100%, 0% 0%; }
		100% { background-position: 30% 20%, 70% 40%, 40% 60%, 0% 0%; }
	}

	.video-bg video {
		position: relative;
		z-index: 1;
		width: 100%;
		height: 100%;
		object-fit: cover;
	}

	.video-overlay {
		position: absolute;
		inset: 0;
		z-index: 2;
		background: radial-gradient(ellipse at center, rgba(10, 10, 15, 0.35) 0%, rgba(10, 10, 15, 0.8) 100%);
	}

	/* === Navigation === */
	nav {
		position: fixed;
		top: 1.25rem;
		left: 50%;
		transform: translateX(-50%);
		z-index: 100;
		width: calc(100% - 3rem);
		max-width: 720px;
		background: rgba(255, 255, 255, 0.1);
		backdrop-filter: blur(24px) saturate(1.8);
		-webkit-backdrop-filter: blur(24px) saturate(1.8);
		border: 1px solid rgba(255, 255, 255, 0.2);
		border-radius: 50px;
		padding: 0.4rem;
		box-shadow:
			0 8px 32px rgba(0, 0, 0, 0.08),
			0 2px 8px rgba(0, 0, 0, 0.04),
			inset 0 1px 0 rgba(255, 255, 255, 0.25),
			inset 0 -1px 0 rgba(255, 255, 255, 0.05);
		transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
	}

	nav :global(.scrolled) {
		background: rgba(255, 255, 255, 0.14);
		border-color: rgba(255, 255, 255, 0.15);
	}

	.nav-inner {
		margin: 0 auto;
		display: flex;
		align-items: center;
		gap: 0.35rem;
		height: 44px;
	}

	/* Logo pill on the left */
	.nav-logo-pill {
		display: flex;
		align-items: center;
		gap: 0.5rem;
		padding: 0 1.1rem;
		height: 100%;
		border-radius: 40px;
		background: rgba(255, 255, 255, 0.12);
		color: rgba(255, 255, 255, 0.55);
		text-decoration: none;
		font-size: 0.75rem;
		font-weight: 700;
		letter-spacing: 0.12em;
		transition: color 0.3s, background 0.3s;
		white-space: nowrap;
		flex-shrink: 0;
	}

	.nav-logo-pill:hover {
		background: rgba(255, 255, 255, 0.18);
		color: rgba(255, 255, 255, 0.85);
	}

	.nav-logo-pill.active {
		background: rgba(255, 255, 255, 0.18);
		color: #ffffff;
	}

	.logo-diamond {
		display: inline-block;
		width: 8px;
		height: 8px;
		background: linear-gradient(135deg, #ec4899, #a855f7);
		transform: rotate(45deg);
		border-radius: 1.5px;
		flex-shrink: 0;
		transition: transform 0.6s;
	}

	.nav-logo-pill:hover .logo-diamond {
		transform: rotate(225deg);
	}

	.logo-text {
		font-weight: 700;
	}

	/* Nav links spread across the rest */
	.nav-links {
		display: flex;
		align-items: center;
		flex: 1;
		justify-content: center;
		gap: 0.25rem;
	}

	.nav-link {
		color: rgba(255, 255, 255, 0.5);
		text-decoration: none;
		font-size: 0.8rem;
		font-weight: 500;
		letter-spacing: 0.02em;
		padding: 0.5rem 1rem;
		border-radius: 40px;
		transition: color 0.3s, background 0.3s;
		position: relative;
		white-space: nowrap;
	}

	.nav-link::after {
		content: '';
		position: absolute;
		bottom: 4px;
		left: 50%;
		transform: translateX(-50%) scale(0);
		width: 4px;
		height: 4px;
		border-radius: 50%;
		background: #ffffff;
		transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
	}

	.nav-link:hover {
		color: rgba(255, 255, 255, 0.9);
	}

	.nav-link.active {
		color: #ffffff;
	}

	.nav-link.active::after {
		transform: translateX(-50%) scale(1);
	}

	/* Light background nav — glass adapts to light pages */
	.light-bg nav {
		background: rgba(255, 255, 255, 0.35);
		border: 1px solid rgba(255, 255, 255, 0.5);
		box-shadow:
			0 8px 32px rgba(124, 58, 237, 0.06),
			0 2px 8px rgba(0, 0, 0, 0.03),
			inset 0 1px 0 rgba(255, 255, 255, 0.6),
			inset 0 -1px 0 rgba(255, 255, 255, 0.1);
	}

	.light-bg .nav-logo-pill {
		background: rgba(255, 255, 255, 0.35);
		color: rgba(45, 27, 78, 0.55);
	}

	.light-bg .nav-logo-pill:hover {
		background: rgba(255, 255, 255, 0.5);
		color: rgba(45, 27, 78, 0.8);
	}

	.light-bg .nav-logo-pill.active {
		background: rgba(255, 255, 255, 0.5);
		color: #2d1b4e;
	}

	.light-bg .nav-link {
		color: rgba(45, 27, 78, 0.45);
	}

	.light-bg .nav-link:hover {
		color: rgba(45, 27, 78, 0.8);
	}

	.light-bg .nav-link.active {
		color: #2d1b4e;
	}

	.light-bg .nav-link.active::after {
		background: #2d1b4e;
	}

	/* === Main === */
	main {
		flex: 1;
		max-width: 1200px;
		margin: 0 auto;
		padding: 0 2rem;
		padding-top: 72px;
		width: 100%;
		position: relative;
		z-index: 1;
	}

	.light-bg main {
		max-width: none;
		padding: 0;
	}

	/* === Footer === */
	footer {
		position: relative;
		z-index: 1;
		text-align: center;
		padding: 3rem 2rem;
		border-top: 1px solid rgba(255, 255, 255, 0.06);
	}

	.footer-glow {
		position: absolute;
		bottom: 0;
		left: 50%;
		transform: translateX(-50%);
		width: 400px;
		height: 100px;
		background: radial-gradient(ellipse, rgba(168, 85, 247, 0.1) 0%, transparent 70%);
		pointer-events: none;
	}

	footer p {
		color: rgba(255, 255, 255, 0.3);
		font-size: 0.85rem;
		font-weight: 400;
	}

	.light-bg footer {
		border-top: 1px solid rgba(124, 58, 237, 0.15);
	}

	.light-bg footer p {
		color: #6b5585;
	}

	/* === Disclaimer Banner === */
	.disclaimer-banner {
		position: fixed;
		bottom: 1.25rem;
		left: 50%;
		transform: translateX(-50%) translateY(120%);
		z-index: 200;
		width: calc(100% - 2rem);
		max-width: 640px;
		background: rgba(255, 255, 255, 0.12);
		backdrop-filter: blur(24px) saturate(1.8);
		-webkit-backdrop-filter: blur(24px) saturate(1.8);
		border: 1px solid rgba(255, 255, 255, 0.18);
		border-radius: 16px;
		box-shadow:
			0 8px 32px rgba(0, 0, 0, 0.15),
			inset 0 1px 0 rgba(255, 255, 255, 0.2);
		transition: transform 0.5s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.5s ease;
		opacity: 0;
	}

	.disclaimer-banner.visible {
		transform: translateX(-50%) translateY(0);
		opacity: 1;
	}

	.disclaimer-inner {
		display: flex;
		align-items: flex-start;
		gap: 0.65rem;
		padding: 0.85rem 1rem;
	}

	.disclaimer-icon {
		flex-shrink: 0;
		color: rgba(255, 255, 255, 0.5);
		margin-top: 2px;
	}

	.disclaimer-text {
		font-size: 0.78rem;
		line-height: 1.5;
		color: rgba(255, 255, 255, 0.65);
		flex: 1;
	}

	.disclaimer-text strong {
		color: rgba(255, 255, 255, 0.85);
		font-weight: 600;
	}

	.disclaimer-dismiss {
		background: rgba(255, 255, 255, 0.08);
		border: none;
		border-radius: 8px;
		padding: 0.4rem;
		cursor: pointer;
		color: rgba(255, 255, 255, 0.4);
		transition: background 0.2s, color 0.2s;
		flex-shrink: 0;
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.disclaimer-dismiss:hover {
		background: rgba(255, 255, 255, 0.15);
		color: rgba(255, 255, 255, 0.8);
	}

	/* Light-bg disclaimer overrides */
	.light-bg .disclaimer-banner {
		background: rgba(255, 255, 255, 0.45);
		border: 1px solid rgba(255, 255, 255, 0.5);
		box-shadow:
			0 8px 32px rgba(124, 58, 237, 0.08),
			inset 0 1px 0 rgba(255, 255, 255, 0.5);
	}

	.light-bg .disclaimer-icon {
		color: rgba(45, 27, 78, 0.45);
	}

	.light-bg .disclaimer-text {
		color: rgba(45, 27, 78, 0.6);
	}

	.light-bg .disclaimer-text strong {
		color: #2d1b4e;
	}

	.light-bg .disclaimer-dismiss {
		background: rgba(45, 27, 78, 0.06);
		color: rgba(45, 27, 78, 0.35);
	}

	.light-bg .disclaimer-dismiss:hover {
		background: rgba(45, 27, 78, 0.1);
		color: rgba(45, 27, 78, 0.7);
	}
</style>
