# Engagement Agent Product Spec v1.0.0

## Document Status

- Product: `Engagement Agent`
- Version: `v1.0.0`
- Status: `Draft`
- Owner: `Product / AI Experience`

## Overview

The `Engagement Agent` is a lightweight AI-powered feature for the Cortex Cinema mobile app. Its purpose is to increase user interest in a movie by showing short, compelling content on the movie detail page.

For each movie, the feature generates three content blocks:

- `Fun Fact`
- `Hook`
- `Why Watch This Now`

This experience should help movies feel more exciting, more relevant, and easier to choose without requiring the user to enter a chat flow.

## Problem Statement

Users often browse multiple movies without converting into a meaningful action such as watching a trailer, adding a title to a watchlist, or starting playback. Standard metadata such as poster, synopsis, genre, and ratings is useful, but it is not always enough to create emotional interest or urgency.

The app needs a lightweight engagement layer that helps users feel:

- curious about a movie
- emotionally pulled toward it
- personally matched to it

## Product Goal

Increase movie detail page engagement and improve watch intent by showing concise, AI-generated movie engagement content.

## Objectives

### Primary Objectives

- Increase `detail page -> watch trailer`
- Increase `detail page -> add to watchlist`
- Increase `detail page -> start watching`

### Secondary Objectives

- Increase dwell time on movie detail pages
- Improve movie discovery satisfaction
- Gather feedback signals for future personalization

## Non-Goals

Version `v1.0.0` does not include:

- full chat assistant
- voice assistant
- multi-agent orchestration
- MCP server
- deep long-term memory
- advanced recommendation ranking
- spoiler discussion mode
- external editorial or trivia integrations beyond current data sources

## Target Users

### Primary Users

- users browsing movies and deciding what to watch
- users who need a stronger reason to click, save, or watch

### Secondary Users

- returning users with enough history for light personalization
- new users who still benefit from generic engagement copy

## User Stories

- As a user browsing a movie, I want to see an interesting fact so the movie feels more memorable.
- As a user deciding whether to watch, I want a short hook so I can quickly understand why the movie might be exciting.
- As a returning user, I want the app to explain why a movie fits my taste so recommendations feel more personal.
- As a new user, I still want useful and engaging content even if the app knows little about me.

## Core Experience

On the movie detail page, the app displays three short engagement cards:

- `Did you know?`
- `Why it’s worth watching`
- `Why it matches your taste`

Each card should be concise, scannable, and spoiler-safe.

## Feature Scope

### In Scope

- Generate three engagement snippets per movie detail page
- Use TMDB metadata as the primary movie source
- Support optional fun fact enrichment from approved web or social signal sources
- Use basic user activity for personalization where available
- Return structured, ready-to-render content
- Support fallback output if personalization or generation is unavailable
- Capture simple feedback such as `helpful` and `not helpful`

### Out of Scope

- open-ended assistant conversation
- recommendation engine redesign
- social or group recommendations
- post-watch discussion flows
- second-screen or live viewing assistant experiences

## Functional Requirements

For each movie detail request, the system must provide:

- one `Fun Fact`
- one `Hook`
- one `Why Watch This Now`

### Content Requirements

- concise
- engaging
- spoiler-safe by default
- appropriate for mobile UI
- personalized when enough user context exists
- generic fallback when user context is weak or unavailable

### Behavior Requirements

- content appears on movie detail page load
- response format is consistent
- fallback content is available if generation fails
- content avoids fabricated specific claims not supported by available data

## Content Definitions

### Fun Fact

An interesting, fact-style insight about the movie, cast, director, genre, scale, or cultural and acclaim context.

For `v1.0.0`, this may be closer to an `interesting insight` than deep verified trivia.

When available, the system may enrich `Fun Fact` generation with approved external content such as publisher pages, interviews, public movie coverage, or high-signal social discussions. External content should be treated as enrichment input, not as automatically trusted fact.

### Hook

A short, curiosity-driven line that makes the movie feel exciting or emotionally appealing.

### Why Watch This Now

A short reason the user should consider watching now, ideally tied to taste, mood, or recent viewing behavior.

## Personalization Rules

The system should personalize only when enough user context exists.

### Personalization Tiers

- `High`: clear recent preferences and strong behavior signals
- `Medium`: some preference signals available
- `Low`: weak signal, minimal personalization
- `None`: no useful user signal

### Rules

- mention only one or two user taste signals
- avoid overly specific behavioral references
- avoid creepy or surveillance-like phrasing
- if confidence is low, use generic copy instead

Example:

`You’ve been leaning toward cerebral sci-fi lately, and this fits that mood.`

## Data Sources

### Movie Data

- TMDB movie details
- TMDB credits
- TMDB genre and popularity context
- optional similar movie context if needed

### Fun Fact Enrichment Data

- approved web pages with movie coverage, interviews, or production context
- approved public social media posts or discussion threads with strong relevance signals
- internal extracted summaries from scraped pages or social sources

### Source Rules

- TMDB remains the default structured source for every title
- external web and social sources are optional enrichment for `Fun Fact` only in `v1.0.0`
- source allowlists should be used for web scraping targets
- social content should be used for trend, buzz, or interesting angles, not as sole proof of factual claims
- unsupported or conflicting external claims must be dropped rather than generated

### Approved Source Examples

- studio or distributor press pages
- official movie websites
- official cast, director, or studio YouTube interviews
- reputable entertainment publishers such as Variety, Deadline, The Hollywood Reporter, or Empire
- film festival pages and official Q&A summaries
- approved public social platforms such as Reddit discussion threads, X posts, YouTube comments, or TikTok clips used only as trend or audience-interest signals

### Disallowed or High-Risk Source Examples

- anonymous low-quality blog networks
- scraped pages with no visible source or author context
- repost aggregators that copy entertainment news without attribution
- private, deleted, or access-restricted social content
- rumor-only posts without independent support
- forum or social claims treated as factual production history without confirmation

### User Data

- recently viewed titles
- likes or positive interactions
- watchlist saves
- genre preferences
- actor or director affinity inferred from behavior
- completion or watch activity where available

## Experience Rules

### UI Rules

- each content block should be one or two lines
- content should be easy to scan
- the experience should feel like enhancement, not interruption
- no chat UI in `v1.0.0`

### Safety Rules

- no spoilers in the default experience
- no unsupported production trivia
- no sensitive profiling language
- no harmful or offensive language
- no direct reuse of unverified social claims as facts
- no copyrighted long-form copied text from scraped sources

## Success Metrics

### Primary Metrics

- movie detail to trailer click-through rate
- movie detail to watchlist conversion
- movie detail to start-watching conversion

### Secondary Metrics

- dwell time on movie detail page
- engagement card feedback rate
- positive feedback ratio
- repeat browsing sessions

### Quality Metrics

- fallback rate
- generation latency
- personalization usage rate
- flagged or low-quality response rate
- source-backed fact usage rate

## Acceptance Criteria

Version `v1.0.0` is successful when:

- users see three engagement cards on movie detail pages
- cards render consistently for supported titles
- content is concise and spoiler-safe
- personalized `Why Watch This Now` appears when sufficient user data exists
- generic fallback appears when it does not
- the system captures basic feedback and usage analytics
- latency is acceptable for a mobile detail page experience
- the product team can measure impact on watch-intent actions

## Risks

- TMDB may not contain rich enough data for truly unique fun facts
- scraped web content may be noisy, duplicated, or unreliable
- social media content may be inaccurate, hype-driven, or manipulative
- LLM output may become repetitive across titles
- hallucinated facts may reduce trust
- cold-start users may receive weaker copy
- generation latency may hurt detail page experience
- scraping and source maintenance may increase operational complexity

## Risk Mitigation

- frame `Fun Fact` as insight-style content, not guaranteed deep trivia
- use strict prompting and output validation
- prefer broad, safe claims over risky specifics
- use approved source allowlists and source quality scoring
- treat social content as inspiration or trend signal unless independently supported
- cache generated content where practical
- use generic fallbacks for low-confidence cases
- measure quality through feedback and conversion

## Rollout Plan

### Phase 1

Generic engagement content using movie metadata only.

### Phase 2

Add lightweight personalization for `Why Watch This Now`.

### Phase 3

Improve fact richness and copy diversity based on results.

### Phase 4

Add approved web scraping and social enrichment for higher-quality `Fun Fact` generation with source filtering, extraction, and trust controls.

## Release Recommendation

Ship `v1.0.0` as a focused movie detail page enhancement, not as a full assistant. The goal is to validate whether AI-generated engagement copy increases watch intent before investing in more complex agent architecture.
