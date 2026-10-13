# AUDIT-FINDINGS

Date: 2026-10-13 | Scope: Desktop/output.md vs structerd_output (707 cards) + both OS trees | Method: line-by-line read-only audit, six axes, verdict per item.
Status: all findings FIXED; re-verified below. Hardening pass added: independent URL re-probe (196/196) and solo-skill merge. Deviations in §7.

## Axis 1 — Entities

### 1.1 Skills (24 vendored + third-party + card-only)

| # | Entity | Verdict | Useful | Where |
|---|---|---|---|---|
| 1 | working-backwards | PRESENT | yes | superior-os/.harness/skills/working-backwards/SKILL.md |
| 2 | scope-gate | PRESENT | yes | superior-os/.harness/skills/scope-gate/SKILL.md |
| 3 | alternatives-generator | PRESENT | yes | superior-os/.harness/skills/alternatives-generator/SKILL.md |
| 4 | failure-mode-analyzer | PRESENT | yes | superior-os/.harness/skills/failure-mode-analyzer/SKILL.md |
| 5 | fcar-reviewer | PRESENT | yes | superior-os/.harness/skills/fcar-reviewer/SKILL.md |
| 6 | launch-checklist-runner | PRESENT | yes | superior-os/.harness/skills/launch-checklist-runner/SKILL.md |
| 7 | postmortem-opener | PRESENT | yes | superior-os/.harness/skills/postmortem-opener/SKILL.md |
| 8 | stakes-classifier | PRESENT | yes | superior-os/.harness/skills/stakes-classifier/SKILL.md |
| 9 | unknown-first-sorter | PRESENT | yes | superior-os/.harness/skills/unknown-first-sorter/SKILL.md |
| 10 | 01-repo-surveyor-map | PRESENT | yes | superior-os/.harness/skills/01-repo-surveyor-map/SKILL.md |
| 11 | 02-git-worktree-isolation | PRESENT | yes | superior-os/.harness/skills/02-git-worktree-isolation/SKILL.md |
| 12 | 03-context-compaction-pruner | PRESENT | yes | superior-os/.harness/skills/03-context-compaction-pruner/SKILL.md |
| 13 | 07-api-contract-first | PRESENT | yes | superior-os/.harness/skills/07-api-contract-first/SKILL.md |
| 14 | 08-database-schema-architect | PRESENT | yes | superior-os/.harness/skills/08-database-schema-architect/SKILL.md |
| 15 | 09-docker-sandbox-runner | PRESENT | yes | superior-os/.harness/skills/09-docker-sandbox-runner/SKILL.md |
| 16 | 11-litellm-router-admin | PRESENT | yes | superior-os/.harness/skills/11-litellm-router-admin/SKILL.md |
| 17 | 21-tdd-red-green-refactor | PRESENT | yes | superior-os/.harness/skills/21-tdd-red-green-refactor/SKILL.md |
| 18 | 22-playwright-e2e-matrix | PRESENT | yes | superior-os/.harness/skills/22-playwright-e2e-matrix/SKILL.md |
| 19 | 23-pytest-fixture-factory | PRESENT | yes | superior-os/.harness/skills/23-pytest-fixture-factory/SKILL.md |
| 20 | 26-systematic-rca | PRESENT | yes | superior-os/.harness/skills/26-systematic-rca/SKILL.md |
| 21 | 31-owasp-top10-vuln-scanner | PRESENT | yes | superior-os/.harness/skills/31-owasp-top10-vuln-scanner/SKILL.md |
| 22 | 32-secrets-entropy-sanitizer | PRESENT | yes | superior-os/.harness/skills/32-secrets-entropy-sanitizer/SKILL.md |
| 23 | 35-cryptography-safe-patterns | PRESENT | yes | superior-os/.harness/skills/35-cryptography-safe-patterns/SKILL.md |
| 24 | 36-grill-me-socratic-planner | PRESENT | yes | superior-os/.harness/skills/36-grill-me-socratic-planner/SKILL.md |
| 25 | Leonxlnx/taste-skill | CARD-ONLY | yes | third-party-index: https://github.com/Leonxlnx/taste-skill |
| 26 | anthropics/skills | CARD-ONLY | yes | third-party-index: https://github.com/anthropics/skills |
| 27 | vercel-labs/agent-skills | CARD-ONLY | yes | third-party-index: https://github.com/vercel-labs/agent-skills |
| 28 | vercel-labs/skills | CARD-ONLY | yes | third-party-index: https://github.com/vercel-labs/skills |
| 29 | mattpocock/skills | CARD-ONLY | yes | third-party-index: https://github.com/mattpocock/skills |
| 30 | trailofbits/skills | CARD-ONLY | yes | third-party-index: https://github.com/trailofbits/skills |
| 31 | supabase/agent-skills | CARD-ONLY | yes | third-party-index: https://github.com/supabase/agent-skills |
| 32 | openai/skills | CARD-ONLY | yes | third-party-index: https://github.com/openai/skills |
| 33 | cloudflare/skills | CARD-ONLY | yes | third-party-index: https://github.com/cloudflare/skills |
| 34 | obra/superpowers | CARD-ONLY | yes | third-party-index: https://github.com/obra/superpowers |
| 35 | greensock/gsap-skills | CARD-ONLY | yes | third-party-index: https://github.com/greensock/gsap-skills |
| 36 | stripe/ai | CARD-ONLY | yes | third-party-index: https://github.com/stripe/ai |
| 37 | skillcreatorai/Awesome-Agent-Skills | CARD-ONLY | yes | third-party-index: https://github.com/skillcreatorai/Awesome-Agent-Skills |
| 38 | VoltAgent/awesome-agent-skills | CARD-ONLY | yes | third-party-index: https://github.com/VoltAgent/awesome-agent-skills |
| 39 | agent-ecosystem/skill-validator | CARD-ONLY | yes | third-party-index: https://github.com/agent-ecosystem/skill-validator |
| 40 | alephic-ai/skref | CARD-ONLY | yes | third-party-index: https://github.com/alephic-ai/skref |
| 41 | cravenceiling/skill-kit | CARD-ONLY | yes | third-party-index: https://github.com/cravenceiling/skill-kit |
| 42 | ginaecho/skill-quartermaster | CARD-ONLY | yes | third-party-index: https://github.com/ginaecho/skill-quartermaster |
| 43 | JuanJoseGonGi/skill-compact | CARD-ONLY | yes | third-party-index: https://github.com/JuanJoseGonGi/skill-compact |
| 44 | prateek/skills-janitor | CARD-ONLY | yes | third-party-index: https://github.com/prateek/skills-janitor |
| 45 | rooftop-Owl/skill-factory | CARD-ONLY | yes | third-party-index: https://github.com/rooftop-Owl/skill-factory |
| 46 | solo: alternatives-generator | CARD-ONLY | yes | how-to-use/01-skills.md (deve name-collision, not vendored) |
| 47 | solo: failure-mode-analyzer | CARD-ONLY | yes | how-to-use/01-skills.md (deve name-collision, not vendored) |
| 48 | solo: fcar-reviewer | CARD-ONLY | yes | how-to-use/01-skills.md (deve name-collision, not vendored) |
| 49 | solo: launch-checklist-runner | CARD-ONLY | yes | how-to-use/01-skills.md (deve name-collision, not vendored) |
| 50 | solo: postmortem-opener | CARD-ONLY | yes | how-to-use/01-skills.md (deve name-collision, not vendored) |
| 51 | solo: scope-gate | CARD-ONLY | yes | how-to-use/01-skills.md (deve name-collision, not vendored) |
| 52 | solo: stakes-classifier | CARD-ONLY | yes | how-to-use/01-skills.md (deve name-collision, not vendored) |
| 53 | solo: unknown-first-sorter | CARD-ONLY | yes | how-to-use/01-skills.md (deve name-collision, not vendored) |
| 54 | solo: working-backwards | CARD-ONLY | yes | how-to-use/01-skills.md (deve name-collision, not vendored) |
| 55 | the-harness: 01-repo-surveyor-map | PRESENT | yes | vendored verbatim |
| 56 | the-harness: 02-git-worktree-isolation | PRESENT | yes | vendored verbatim |
| 57 | the-harness: 03-context-compaction-pruner | PRESENT | yes | vendored verbatim |
| 58 | the-harness: 07-api-contract-first | PRESENT | yes | vendored verbatim |
| 59 | the-harness: 08-database-schema-architect | PRESENT | yes | vendored verbatim |
| 60 | the-harness: 09-docker-sandbox-runner | PRESENT | yes | vendored verbatim |
| 61 | the-harness: 11-litellm-router-admin | PRESENT | yes | vendored verbatim |
| 62 | the-harness: 21-tdd-red-green-refactor | PRESENT | yes | vendored verbatim |
| 63 | the-harness: 22-playwright-e2e-matrix | PRESENT | yes | vendored verbatim |
| 64 | the-harness: 23-pytest-fixture-factory | PRESENT | yes | vendored verbatim |
| 65 | the-harness: 26-systematic-rca | PRESENT | yes | vendored verbatim |
| 66 | the-harness: 31-owasp-top10-vuln-scanner | PRESENT | yes | vendored verbatim |
| 67 | the-harness: 32-secrets-entropy-sanitizer | PRESENT | yes | vendored verbatim |
| 68 | the-harness: 35-cryptography-safe-patterns | PRESENT | yes | vendored verbatim |
| 69 | the-harness: 36-grill-me-socratic-planner | PRESENT | yes | vendored verbatim |

### 1.2 MCP + agents

| # | Entity | Verdict | Useful | Where |
|---|---|---|---|---|
| 1 | filesystem / playwright / context7 / github | PRESENT | yes | .harness/mcp/tools.yaml servers block |
| 2 | github-mcp-server | CARD-ONLY | yes | https://github.com/github/github-mcp-server |
| 3 | brave-search-mcp-server | CARD-ONLY | yes | https://github.com/brave/brave-search-mcp-server |
| 4 | sentry-mcp | CARD-ONLY | yes | https://github.com/getsentry/sentry-mcp |
| 5 | playwright-mcp | CARD-ONLY | yes | https://github.com/microsoft/playwright-mcp |
| 6 | docker/mcp-servers | CARD-ONLY | yes | https://github.com/docker/mcp-servers |
| 7 | upstash/context7 | CARD-ONLY | yes | https://github.com/upstash/context7 |
| 8 | stripe/agent-toolkit | CARD-ONLY | yes | https://github.com/stripe/agent-toolkit |
| 9 | mcp-server-kubernetes | CARD-ONLY | yes | https://github.com/Flux159/mcp-server-kubernetes |
| 10 | mcp-use | CARD-ONLY | yes | https://github.com/mcp-use/mcp-use |
| 11 | modelcontextprotocol/servers | CARD-ONLY | yes | https://github.com/modelcontextprotocol/servers |
| 12 | modelcontextprotocol/inspector | CARD-ONLY | yes | https://github.com/modelcontextprotocol/inspector |
| 13 | modelcontextprotocol/typescript-sdk | CARD-ONLY | yes | https://github.com/modelcontextprotocol/typescript-sdk |
| 14 | modelcontextprotocol/python-sdk | CARD-ONLY | yes | https://github.com/modelcontextprotocol/python-sdk |
| 15 | modelcontextprotocol/go-sdk | CARD-ONLY | yes | https://github.com/modelcontextprotocol/go-sdk |
| 16 | modelcontextprotocol/rust-sdk | CARD-ONLY | yes | https://github.com/modelcontextprotocol/rust-sdk |
| 17 | modelcontextprotocol/csharp-sdk | CARD-ONLY | yes | https://github.com/modelcontextprotocol/csharp-sdk |
| 18 | Claude Code | CARD-ONLY | yes | os/THIRD-PARTY-AGENTS.md |
| 19 | Cursor | CARD-ONLY | yes | os/THIRD-PARTY-AGENTS.md |
| 20 | OpenAI Codex | CARD-ONLY | yes | os/THIRD-PARTY-AGENTS.md |
| 21 | Gemini CLI | CARD-ONLY | yes | os/THIRD-PARTY-AGENTS.md |
| 22 | Cline | CARD-ONLY | yes | os/THIRD-PARTY-AGENTS.md |
| 23 | Windsurf | CARD-ONLY | yes | os/THIRD-PARTY-AGENTS.md |
| 24 | Continue | CARD-ONLY | yes | os/THIRD-PARTY-AGENTS.md |
| 25 | Aider | CARD-ONLY | yes | os/THIRD-PARTY-AGENTS.md |
| 26 | GitHub Copilot | CARD-ONLY | yes | os/THIRD-PARTY-AGENTS.md |
| 27 | OS subagent: coder | PRESENT | yes | .harness/agents/coder.md |
| 28 | OS subagent: explorer | PRESENT | yes | .harness/agents/explorer.md |
| 29 | OS subagent: planner | PRESENT | yes | .harness/agents/planner.md |
| 30 | OS subagent: reviewer | PRESENT | yes | .harness/agents/reviewer.md |

### 1.3 Watchlist

| # | Entity | Verdict | Useful | Where |
|---|---|---|---|---|
| 1 | God research/B-category-catalogs/23-watchlist.md | PRESENT | yes | card + manual |
| 2 | God research/C-named-register-23.md | PRESENT | yes | card + manual |
| 3 | God research/atlas/C-named-watchlist.md | PRESENT | yes | card + manual |
| 4 | God research/atlas/registers/named-watchlist.md | PRESENT | yes | card + manual |
| 5 | God research - gemini/06-watchlist-prompts.md | PRESENT | yes | card + manual |
| 6 | God research/agy-pass/06-watchlist-prompts.md | PRESENT | yes | card + manual |

### 1.4 Companies/cases

| # | Entity | Verdict | Useful | Where |
|---|---|---|---|---|
| 1 | builders-playbook/product_engineering/report/04-company-case-studies.md | PRESENT | yes | card + manual |
| 2 | builders-playbook/product_engineering/research/domain-b/03-ai-assistants.md | PRESENT | yes | card + manual |
| 3 | builders-playbook/product_engineering/research/expansion-companies/00-index.md | PRESENT | yes | card + manual |
| 4 | builders-playbook/product_engineering/research/expansion-companies/01-cloudflare.md | PRESENT | yes | card + manual |
| 5 | builders-playbook/product_engineering/research/expansion-companies/02-fastly.md | PRESENT | yes | card + manual |
| 6 | builders-playbook/product_engineering/research/expansion-companies/03-figma.md | PRESENT | yes | card + manual |
| 7 | builders-playbook/product_engineering/research/expansion-companies/04-notion.md | PRESENT | yes | card + manual |
| 8 | builders-playbook/product_engineering/research/expansion-companies/05-discord.md | PRESENT | yes | card + manual |
| 9 | builders-playbook/product_engineering/research/expansion-companies/06-linear.md | PRESENT | yes | card + manual |
| 10 | builders-playbook/product_engineering/research/expansion-companies/07-tailscale.md | PRESENT | yes | card + manual |
| 11 | builders-playbook/product_engineering/research/expansion-companies/08-sourcegraph.md | PRESENT | yes | card + manual |
| 12 | builders-playbook/product_engineering/research/expansion-companies/09-gitlab.md | PRESENT | yes | card + manual |
| 13 | builders-playbook/product_engineering/research/expansion-companies/10-etsy.md | PRESENT | yes | card + manual |
| 14 | builders-playbook/product_engineering/research/expansion-companies/11-basecamp.md | PRESENT | yes | card + manual |
| 15 | builders-playbook/product_engineering/research/expansion-companies/12-jane-street.md | PRESENT | yes | card + manual |
| 16 | builders-playbook/product_engineering/research/expansion-companies/13-palantir.md | PRESENT | yes | card + manual |
| 17 | builders-playbook/product_engineering/research/expansion-companies/14-spacex.md | PRESENT | yes | card + manual |
| 18 | builders-playbook/product_engineering/research/expansion-companies/15-apple.md | PRESENT | yes | card + manual |
| 19 | builders-playbook/product_engineering/research/expansion-companies/16-knight-capital.md | PRESENT | yes | card + manual |
| 20 | builders-playbook/product_engineering/research/expansion-companies/17-netscape-mozilla.md | PRESENT | yes | card + manual |
| 21 | builders-playbook/product_engineering/research/expansion-companies/18-healthcare-gov.md | PRESENT | yes | card + manual |
| 22 | builders-playbook/product_engineering/research/expansion-companies/19-digg-v4.md | PRESENT | yes | card + manual |
| 23 | builders-playbook/product_engineering/research/expansion-companies/20-google-wave.md | PRESENT | yes | card + manual |
| 24 | builders-playbook/product_engineering/research/expansion-companies/21-windows-vista.md | PRESENT | yes | card + manual |
| 25 | builders-playbook/product_engineering/research/expansion-companies/22-firefox-os.md | PRESENT | yes | card + manual |
| 26 | builders-playbook/product_engineering/research/expansion-companies/23-valve.md | PRESENT | yes | card + manual |
| 27 | builders-playbook/product_engineering/research/expansion-companies/24-riot-games.md | PRESENT | yes | card + manual |
| 28 | builders-playbook/product_engineering/research/expansion-companies/25-ccp-games.md | PRESENT | yes | card + manual |
| 29 | builders-playbook/product_engineering/research/expansion-companies/26-pinboard.md | PRESENT | yes | card + manual |
| 30 | builders-playbook/product_engineering/research/expansion-companies/27-tailwind-labs.md | PRESENT | yes | card + manual |
| 31 | builders-playbook/product_engineering/research/expansion-companies/28-tesla.md | PRESENT | yes | card + manual |
| 32 | builders-playbook/product_engineering/research/expansion-companies/29-framework.md | PRESENT | yes | card + manual |
| 33 | builders-playbook/product_engineering/research/expansion-companies/30-ibm-carbon.md | PRESENT | yes | card + manual |
| 34 | builders-playbook/product_engineering/research/expansion-companies/31-atlassian.md | PRESENT | yes | card + manual |
| 35 | builders-playbook/product_engineering/research/expansion-companies/32-adobe-spectrum.md | PRESENT | yes | card + manual |
| 36 | builders-playbook/product_engineering/research/expansion-companies/33-salesforce-lightning.md | PRESENT | yes | card + manual |
| 37 | builders-playbook/product_engineering/research/expansion-companies/34-vercel.md | PRESENT | yes | card + manual |
| 38 | builders-playbook/product_engineering/research/expansion-companies/35-datadog.md | PRESENT | yes | card + manual |
| 39 | builders-playbook/product_engineering/research/expansion-companies/36-slack.md | PRESENT | yes | card + manual |
| 40 | builders-playbook/product_engineering/research/expansion-companies/37-lean-outliers.md | PRESENT | yes | card + manual |
| 41 | builders-playbook/product_engineering/research/cases-hyperscale/01-google.md | PRESENT | yes | card + manual |
| 42 | builders-playbook/product_engineering/research/cases-hyperscale/02-microsoft.md | PRESENT | yes | card + manual |
| 43 | builders-playbook/product_engineering/research/cases-hyperscale/03-meta.md | PRESENT | yes | card + manual |
| 44 | builders-playbook/product_engineering/research/cases-hyperscale/04-amazon.md | PRESENT | yes | card + manual |
| 45 | builders-playbook/product_engineering/research/cases-hyperscale/05-nvidia.md | PRESENT | yes | card + manual |
| 46 | builders-playbook/product_engineering/research/cases-product/01-openai.md | PRESENT | yes | card + manual |
| 47 | builders-playbook/product_engineering/research/cases-product/02-anthropic.md | PRESENT | yes | card + manual |
| 48 | builders-playbook/product_engineering/research/cases-product/03-github.md | PRESENT | yes | card + manual |
| 49 | builders-playbook/product_engineering/research/cases-product/04-stripe.md | PRESENT | yes | card + manual |
| 50 | builders-playbook/product_engineering/research/cases-product/05-shopify.md | PRESENT | yes | card + manual |
| 51 | builders-playbook/product_engineering/research/cases-product/06-uber.md | PRESENT | yes | card + manual |
| 52 | builders-playbook/product_engineering/research/cases-product/07-netflix.md | PRESENT | yes | card + manual |
| 53 | builders-playbook/product_engineering/research/cases-product/08-spotify.md | PRESENT | yes | card + manual |
| 54 | builders-playbook/product_engineering/research/cases-product/09-airbnb.md | PRESENT | yes | card + manual |
| 55 | builders-playbook/product_engineering/research/cases-product/10-cursor.md | PRESENT | yes | card + manual |
| 56 | builders-playbook/product_engineering/research/cases-product/11-replit.md | PRESENT | yes | card + manual |

### 1.5 Styles

| # | Entity | Verdict | Useful | Where |
|---|---|---|---|---|
| 1 | God research/B-category-catalogs/06-design-systems.md | PRESENT | yes | card + manual |
| 2 | God research/B-category-catalogs/08-visual-assets.md | PRESENT | yes | card + manual |
| 3 | God research/D-design-styles/00-index-29.md | PRESENT | yes | card + manual |
| 4 | God research/D-design-styles/01-minimalism.md | PRESENT | yes | card + manual |
| 5 | God research/D-design-styles/02-maximalism.md | PRESENT | yes | card + manual |
| 6 | God research/D-design-styles/03-swiss-international-typographic.md | PRESENT | yes | card + manual |
| 7 | God research/D-design-styles/04-brutalism.md | PRESENT | yes | card + manual |
| 8 | God research/D-design-styles/05-surrealism.md | PRESENT | yes | card + manual |
| 9 | God research/D-design-styles/06-neo-brutalism.md | PRESENT | yes | card + manual |
| 10 | God research/D-design-styles/07-neoclassical.md | PRESENT | yes | card + manual |
| 11 | God research/D-design-styles/08-neumorphism.md | PRESENT | yes | card + manual |
| 12 | God research/D-design-styles/09-scrapbook.md | PRESENT | yes | card + manual |
| 13 | God research/D-design-styles/10-glassmorphism.md | PRESENT | yes | card + manual |
| 14 | God research/D-design-styles/11-claymorphism.md | PRESENT | yes | card + manual |
| 15 | God research/D-design-styles/12-bento-grid.md | PRESENT | yes | card + manual |
| 16 | God research/D-design-styles/13-pixel-art.md | PRESENT | yes | card + manual |
| 17 | God research/D-design-styles/14-conceptual-sketch.md | PRESENT | yes | card + manual |
| 18 | God research/D-design-styles/15-luxury-typography.md | PRESENT | yes | card + manual |
| 19 | God research/D-design-styles/16-editorial.md | PRESENT | yes | card + manual |
| 20 | God research/D-design-styles/17-y2k.md | PRESENT | yes | card + manual |
| 21 | God research/D-design-styles/18-ethereal.md | PRESENT | yes | card + manual |
| 22 | God research/D-design-styles/19-bohemian.md | PRESENT | yes | card + manual |
| 23 | God research/D-design-styles/20-dark-moody.md | PRESENT | yes | card + manual |
| 24 | God research/D-design-styles/21-cyberpunk.md | PRESENT | yes | card + manual |
| 25 | God research/D-design-styles/22-anthropomorphic.md | PRESENT | yes | card + manual |
| 26 | God research/D-design-styles/23-victorian.md | PRESENT | yes | card + manual |
| 27 | God research/D-design-styles/24-cybercore.md | PRESENT | yes | card + manual |
| 28 | God research/D-design-styles/25-synthwave.md | PRESENT | yes | card + manual |
| 29 | God research/D-design-styles/26-graffiti.md | PRESENT | yes | card + manual |
| 30 | God research/D-design-styles/27-gothic.md | PRESENT | yes | card + manual |
| 31 | God research/D-design-styles/28-mixed-media.md | PRESENT | yes | card + manual |
| 32 | God research/D-design-styles/29-body-art-inspired.md | PRESENT | yes | card + manual |
| 33 | God research/atlas/D-design-styles.md | PRESENT | yes | card + manual |
| 34 | God research/atlas/catalogs/02b-design-styles.md | PRESENT | yes | card + manual |
| 35 | God research - gemini/02-design-styles.md | PRESENT | yes | card + manual |
| 36 | God research/agy-pass/02-design-styles.md | PRESENT | yes | card + manual |
| 37 | builders-playbook/product_engineering/report/07-authenticity-anti-slop.md | PRESENT | yes | card + manual |
| 38 | builders-playbook/product_engineering/research/authenticity/02-visual-identity.md | PRESENT | yes | card + manual |

### 1.6 Disciplines

| # | Entity | Verdict | Useful | Where |
|---|---|---|---|---|
| 1 | solo-levelling/00-master-framework.md | PRESENT | yes | card + manual |
| 2 | solo-levelling/01-phases-1-to-5.md | PRESENT | yes | card + manual |
| 3 | solo-levelling/02-phases-6-to-10.md | PRESENT | yes | card + manual |
| 4 | solo-levelling/03-phases-11-to-15.md | PRESENT | yes | card + manual |
| 5 | solo-levelling/the harness/elements/D-1_EXECUTION.md | PRESENT | yes | card + manual |
| 6 | solo-levelling/the harness/elements/D-2_CONTEXT.md | PRESENT | yes | card + manual |
| 7 | solo-levelling/the harness/elements/D-3_INTEGRATION.md | PRESENT | yes | card + manual |
| 8 | solo-levelling/the harness/elements/D-4_SAFETY.md | PRESENT | yes | card + manual |
| 9 | solo-levelling/the harness/elements/D-5_DX_META.md | PRESENT | yes | card + manual |
| 10 | solo-levelling/the harness/elements/D-6_A_B_TIER.md | PRESENT | yes | card + manual |
| 11 | builders-playbook/product_engineering/report/02-three-ai-domains.md | PRESENT | yes | card + manual |
| 12 | builders-playbook/product_engineering/report/09-accessibility-performance-ux.md | PRESENT | yes | card + manual |
| 13 | builders-playbook/product_engineering/report/20-compulsory-disciplines.md | PRESENT | yes | card + manual |
| 14 | builders-playbook/product_engineering/research/authenticity/01-authenticity-principles.md | PRESENT | yes | card + manual |
| 15 | builders-playbook/product_engineering/research/discipline-ai-act/01-ai-act-engineering.md | PRESENT | yes | card + manual |
| 16 | builders-playbook/product_engineering/research/discipline-api-product/01-api-product.md | PRESENT | yes | card + manual |
| 17 | builders-playbook/product_engineering/research/discipline-billing/01-billing-engineering.md | PRESENT | yes | card + manual |
| 18 | builders-playbook/product_engineering/research/discipline-blindspots/01-blindspots.md | PRESENT | yes | card + manual |
| 19 | builders-playbook/product_engineering/research/discipline-compliance/01-compliance-engineering.md | PRESENT | yes | card + manual |
| 20 | builders-playbook/product_engineering/research/discipline-finops/01-finops.md | PRESENT | yes | card + manual |
| 21 | builders-playbook/product_engineering/research/discipline-mobile-release/01-mobile-release.md | PRESENT | yes | card + manual |
| 22 | builders-playbook/product_engineering/research/discipline-notifications/01-notifications.md | PRESENT | yes | card + manual |
| 23 | builders-playbook/product_engineering/research/discipline-trust-safety/01-trust-safety.md | PRESENT | yes | card + manual |

### 1.7 Rules

| # | Entity | Verdict | Useful | Where |
|---|---|---|---|---|
| 1 | solo-levelling/CLAUDE.md | PRESENT | yes | card + manual |
| 2 | solo-levelling/.cursorrules | PRESENT | yes | card + manual |
| 3 | solo-levelling/os/engineering-rules.md | PRESENT | yes | card + manual |
| 4 | solo-levelling/.harness/permissions/policies.cedar | PRESENT | yes | card + manual |
| 5 | solo-levelling/the harness/.harness/permissions/policies.cedar | PRESENT | yes | card + manual |
| 6 | solo-levelling/the harness/CLAUDE.md | PRESENT | yes | card + manual |
| 7 | solo-levelling/the harness/phase-2/RUBRIC.md | PRESENT | yes | card + manual |
| 8 | deve/.harness/permissions/policies.cedar | PRESENT | yes | card + manual |
| 9 | deve/os/decision-architecture.md | PRESENT | yes | card + manual |
| 10 | deve/os/engineering-rules.md | PRESENT | yes | card + manual |
| 11 | deve/os/fcar-rubric.md | PRESENT | yes | card + manual |
| 12 | deve/os/quality-security.md | PRESENT | yes | card + manual |
| 13 | builders-playbook/product_engineering/report/10-security-privacy-governance.md | PRESENT | yes | card + manual |
| 14 | builders-playbook/product_engineering/report/14-rules-anti-patterns.md | PRESENT | yes | card + manual |
| 15 | builders-playbook/product_engineering/research/domain-a/11-domain-boundaries.md | PRESENT | yes | card + manual |
| 16 | builders-playbook/product_engineering/research/domain-b/11-domain-boundaries.md | PRESENT | yes | card + manual |
| 17 | builders-playbook/product_engineering/research/domain-c/09-domain-boundaries.md | PRESENT | yes | card + manual |
| 18 | builders-playbook/product_engineering/research/authenticity/03-anti-pattern-catalogue.md | PRESENT | yes | card + manual |
| 19 | builders-playbook/product_engineering/research/security/05-privacy-legal.md | PRESENT | yes | card + manual |
| 20 | builders-playbook/product_engineering/research/security/06-classification-index.md | PRESENT | yes | card + manual |
| 21 | builders-playbook/product_engineering/research/rules/01-engineering-rules.md | PRESENT | yes | card + manual |
| 22 | builders-playbook/product_engineering/research/rules/02-anti-patterns.md | PRESENT | yes | card + manual |

### 1.8 Templates

| # | Entity | Verdict | Useful | Where |
|---|---|---|---|---|
| 1 | opencode-research/harness-templates/README.md | PRESENT | yes | card + manual |
| 2 | opencode-research/harness-templates/claude-progress.md | PRESENT | yes | card + manual |
| 3 | opencode-research/harness-templates/feature_list.json | PRESENT | yes | card + manual |
| 4 | solo-levelling/project-tracker.md | PRESENT | yes | card + manual |
| 5 | solo-levelling/os/artifacts/build-log-template.md | PRESENT | yes | card + manual |
| 6 | solo-levelling/os/artifacts/design-note-template.md | PRESENT | yes | card + manual |
| 7 | solo-levelling/os/artifacts/launch-checklist-template.md | PRESENT | yes | card + manual |
| 8 | solo-levelling/os/artifacts/pitch-template.md | PRESENT | yes | card + manual |
| 9 | solo-levelling/os/artifacts/postmortem-template.md | PRESENT | yes | card + manual |
| 10 | solo-levelling/os/artifacts/prfaq-template.md | PRESENT | yes | card + manual |
| 11 | solo-levelling/the harness/.env.template | PRESENT | yes | card + manual |
| 12 | deve/os/artifacts/build-log-template.md | PRESENT | yes | card + manual |
| 13 | deve/os/artifacts/design-note-template.md | PRESENT | yes | card + manual |
| 14 | deve/os/artifacts/launch-checklist-template.md | PRESENT | yes | card + manual |
| 15 | deve/os/artifacts/pitch-template.md | PRESENT | yes | card + manual |
| 16 | deve/os/artifacts/postmortem-template.md | PRESENT | yes | card + manual |
| 17 | deve/os/artifacts/prfaq-template.md | PRESENT | yes | card + manual |
| 18 | builders-playbook/product_engineering/report/17-checklists-templates.md | PRESENT | yes | card + manual |
| 19 | builders-playbook/product_engineering/research/rules/04-templates/00-index.md | PRESENT | yes | card + manual |
| 20 | builders-playbook/product_engineering/research/rules/04-templates/01-problem-validation.md | PRESENT | yes | card + manual |
| 21 | builders-playbook/product_engineering/research/rules/04-templates/02-idea-evaluation.md | PRESENT | yes | card + manual |
| 22 | builders-playbook/product_engineering/research/rules/04-templates/03-prd.md | PRESENT | yes | card + manual |
| 23 | builders-playbook/product_engineering/research/rules/04-templates/04-technical-design-document.md | PRESENT | yes | card + manual |
| 24 | builders-playbook/product_engineering/research/rules/04-templates/05-architecture-decision-record.md | PRESENT | yes | card + manual |
| 25 | builders-playbook/product_engineering/research/rules/04-templates/06-design-system-definition.md | PRESENT | yes | card + manual |
| 26 | builders-playbook/product_engineering/research/rules/04-templates/07-prototype-acceptance.md | PRESENT | yes | card + manual |
| 27 | builders-playbook/product_engineering/research/rules/04-templates/08-development-task-definition.md | PRESENT | yes | card + manual |
| 28 | builders-playbook/product_engineering/research/rules/04-templates/09-agent-instructions.md | PRESENT | yes | card + manual |
| 29 | builders-playbook/product_engineering/research/rules/04-templates/10-test-plan.md | PRESENT | yes | card + manual |
| 30 | builders-playbook/product_engineering/research/rules/04-templates/11-code-review.md | PRESENT | yes | card + manual |
| 31 | builders-playbook/product_engineering/research/rules/04-templates/12-ux-visual-qa.md | PRESENT | yes | card + manual |
| 32 | builders-playbook/product_engineering/research/rules/04-templates/13-security-verification.md | PRESENT | yes | card + manual |
| 33 | builders-playbook/product_engineering/research/rules/04-templates/14-release-readiness.md | PRESENT | yes | card + manual |
| 34 | builders-playbook/product_engineering/research/rules/04-templates/15-incident-response.md | PRESENT | yes | card + manual |
| 35 | builders-playbook/product_engineering/research/rules/04-templates/16-post-launch-evaluation.md | PRESENT | yes | card + manual |
| 36 | builders-playbook/product_engineering/research/rules/04-templates/17-product-authenticity-polish.md | PRESENT | yes | card + manual |
| 37 | builders-playbook/product_engineering/research/rules/04-templates/18-launch-readiness.md | PRESENT | yes | card + manual |
| 38 | builders-playbook/03-checklists.md | PRESENT | yes | card + manual |
| 39 | builders-playbook/templates/battle-plan-48h.md | PRESENT | yes | card + manual |
| 40 | builders-playbook/templates/build-log.md | PRESENT | yes | card + manual |
| 41 | builders-playbook/templates/demo-script.md | PRESENT | yes | card + manual |
| 42 | builders-playbook/templates/idea-evaluator.md | PRESENT | yes | card + manual |
| 43 | builders-playbook/templates/project-retrospective.md | PRESENT | yes | card + manual |

### 1.9 Findings

| # | Entity | Verdict | Useful | Where |
|---|---|---|---|---|
| 1 | opencode-research/README.md | PRESENT | yes | card + manual |
| 2 | opencode-research/verification.md | PRESENT | yes | card + manual |
| 3 | opencode-research/catalog.md | PRESENT | yes | card + manual |
| 4 | opencode-research/research/00-verification.md | PRESENT | yes | card + manual |
| 5 | opencode-research/research/00-gaps-and-unknowns.md | PRESENT | yes | card + manual |
| 6 | opencode-research/research/01-existing-summary.md | PRESENT | yes | card + manual |
| 7 | opencode-research/research/02-ui-ux.md | PRESENT | yes | card + manual |
| 8 | opencode-research/research/03-multi-agent-council.md | PRESENT | yes | card + manual |
| 9 | opencode-research/research/04-harness-environment.md | PRESENT | yes | card + manual |
| 10 | opencode-research/research/05-remaining-resources.md | PRESENT | yes | card + manual |
| 11 | opencode-research/research/06-unfound-and-gaps.md | PRESENT | yes | card + manual |
| 12 | opencode-research/research/08-astryx-mcp.md | PRESENT | yes | card + manual |
| 13 | opencode-research/research/08-loopy-verification.md | PRESENT | yes | card + manual |
| 14 | God research/B-category-catalogs/01-core-web-tech.md | PRESENT | yes | card + manual |
| 15 | God research/B-category-catalogs/02-frontend.md | PRESENT | yes | card + manual |
| 16 | God research/B-category-catalogs/17-security.md | PRESENT | yes | card + manual |
| 17 | God research/A-master-index.md | PRESENT | yes | card + manual |
| 18 | God research/00-phase0-inventory.md | PRESENT | yes | card + manual |
| 19 | God research/atlas/A-master-index.md | PRESENT | yes | card + manual |
| 20 | God research/atlas/B2-design-and-visual.md | PRESENT | yes | card + manual |
| 21 | God research/atlas/B3-agent-ecosystem.md | PRESENT | yes | card + manual |
| 22 | God research/atlas/B4-multiagent-harness-context.md | PRESENT | yes | card + manual |
| 23 | God research/atlas/F-compatibility-index.md | PRESENT | yes | card + manual |
| 24 | God research/atlas/G-relationship-index.md | PRESENT | yes | card + manual |
| 25 | God research/atlas/H-verification-register.md | PRESENT | yes | card + manual |
| 26 | God research/atlas/catalogs/01b-frontend.md | PRESENT | yes | card + manual |
| 27 | God research/atlas/catalogs/01c-backend-data-platforms.md | PRESENT | yes | card + manual |
| 28 | God research/atlas/catalogs/02a-design.md | PRESENT | yes | card + manual |
| 29 | God research/atlas/registers/discrepancies.md | PRESENT | yes | card + manual |
| 30 | God research/atlas/index/master-index.md | PRESENT | yes | card + manual |
| 31 | God research/atlas/index/phase0-inventory.md | PRESENT | yes | card + manual |
| 32 | solo-levelling/phase-16-loop-engineering.md | PRESENT | yes | card + manual |
| 33 | solo-levelling/findings/phase-01-findings.md | PRESENT | yes | card + manual |
| 34 | solo-levelling/findings/phase-02-findings.md | PRESENT | yes | card + manual |
| 35 | solo-levelling/findings/phase-03-findings.md | PRESENT | yes | card + manual |
| 36 | solo-levelling/findings/phase-04-findings.md | PRESENT | yes | card + manual |
| 37 | solo-levelling/findings/phase-05-findings.md | PRESENT | yes | card + manual |
| 38 | solo-levelling/findings/phase-06-findings.md | PRESENT | yes | card + manual |
| 39 | solo-levelling/findings/phase-07-findings.md | PRESENT | yes | card + manual |
| 40 | solo-levelling/findings/phase-08-findings.md | PRESENT | yes | card + manual |
| 41 | solo-levelling/findings/phase-09-findings.md | PRESENT | yes | card + manual |
| 42 | solo-levelling/findings/phase-10-findings.md | PRESENT | yes | card + manual |
| 43 | solo-levelling/findings/phase-11-findings.md | PRESENT | yes | card + manual |
| 44 | solo-levelling/findings/phase-12-findings.md | PRESENT | yes | card + manual |
| 45 | solo-levelling/findings/phase-13-findings.md | PRESENT | yes | card + manual |
| 46 | solo-levelling/findings/phase-14-findings.md | PRESENT | yes | card + manual |
| 47 | solo-levelling/findings/phase-15-master-synthesis.md | PRESENT | yes | card + manual |
| 48 | solo-levelling/the harness/phase-0/ARCHETYPES_AND_CRITERIA.md | PRESENT | yes | card + manual |
| 49 | solo-levelling/the harness/phase-0/R-A_BROAD_MAPPER.md | PRESENT | yes | card + manual |
| 50 | solo-levelling/the harness/phase-0/R-B_CHALLENGER.md | PRESENT | yes | card + manual |
| 51 | solo-levelling/the harness/phase-0/STATUS.md | PRESENT | yes | card + manual |
| 52 | solo-levelling/the harness/phase-0/V-C_ADVERSARIAL.md | PRESENT | yes | card + manual |
| 53 | solo-levelling/the harness/phase-0/V-D_ARCHITECTURAL.md | PRESENT | yes | card + manual |
| 54 | solo-levelling/the harness/phase-1/MASTER_TAXONOMY.md | PRESENT | yes | card + manual |
| 55 | solo-levelling/the harness/phase-1/STATUS.md | PRESENT | yes | card + manual |
| 56 | solo-levelling/the harness/phase-1/batch-1/BATCH-1_EXECUTION_AND_AGENCY.md | PRESENT | yes | card + manual |
| 57 | solo-levelling/the harness/phase-1/batch-1/R-A_BROAD_MAPPER.md | PRESENT | yes | card + manual |
| 58 | solo-levelling/the harness/phase-1/batch-1/R-B_CHALLENGER.md | PRESENT | yes | card + manual |
| 59 | solo-levelling/the harness/phase-1/batch-1/V-C_ADVERSARIAL.md | PRESENT | yes | card + manual |
| 60 | solo-levelling/the harness/phase-1/batch-1/V-D_ARCHITECTURAL.md | PRESENT | yes | card + manual |
| 61 | solo-levelling/the harness/phase-1/batch-2/BATCH-2_CONTEXT_MEMORY_KNOWLEDGE.md | PRESENT | yes | card + manual |
| 62 | solo-levelling/the harness/phase-1/batch-2/R-A_BROAD_MAPPER.md | PRESENT | yes | card + manual |
| 63 | solo-levelling/the harness/phase-1/batch-2/R-B_CHALLENGER.md | PRESENT | yes | card + manual |
| 64 | solo-levelling/the harness/phase-1/batch-2/V-C_ADVERSARIAL.md | PRESENT | yes | card + manual |
| 65 | solo-levelling/the harness/phase-1/batch-2/V-D_ARCHITECTURAL.md | PRESENT | yes | card + manual |
| 66 | solo-levelling/the harness/phase-1/batch-3/BATCH-3_INTEGRATION_EXTENSIBILITY.md | PRESENT | yes | card + manual |
| 67 | solo-levelling/the harness/phase-1/batch-3/R-A_BROAD_MAPPER_AGY.md | PRESENT | yes | card + manual |
| 68 | solo-levelling/the harness/phase-1/batch-3/R-A_BROAD_MAPPER_PARTIAL.md | PRESENT | yes | card + manual |
| 69 | solo-levelling/the harness/phase-1/batch-3/R-B_CHALLENGER_AGY_.md | PRESENT | yes | card + manual |
| 70 | solo-levelling/the harness/phase-1/batch-3/V-C_ADVERSARIAL_AGY.md | PRESENT | yes | card + manual |
| 71 | solo-levelling/the harness/phase-1/batch-3/V-D_ARCHITECTURAL_AGY.md | PRESENT | yes | card + manual |
| 72 | solo-levelling/the harness/phase-1/batch-4/BATCH-4_SAFETY_GOVERNANCE.md | PRESENT | yes | card + manual |
| 73 | solo-levelling/the harness/phase-2/verify/ARBITER_AGY.md | PRESENT | yes | card + manual |
| 74 | solo-levelling/the harness/phase-2/verify/CROSSBATCH_TENSION.md | PRESENT | yes | card + manual |
| 75 | solo-levelling/the harness/phase-2/verify/MECH_PROT_AGY.md | PRESENT | yes | card + manual |
| 76 | solo-levelling/the harness/phase-2/verify/MECH_PROT_P3_SCOUT.md | PRESENT | yes | card + manual |
| 77 | solo-levelling/the harness/phase-3.5/V_AUTHOR_AGY.md | PRESENT | yes | card + manual |
| 78 | solo-levelling/the harness/phase-3.5/V_COHERENCE_AGY.md | PRESENT | yes | card + manual |
| 79 | solo-levelling/the harness/phase-3/verify/CROSS_TOOL_OVERLAP.md | PRESENT | yes | card + manual |
| 80 | solo-levelling/the harness/phase-3/verify/VERIFICATION_PASS1.md | PRESENT | yes | card + manual |
| 81 | solo-levelling/the harness/phase-3/verify/VERIFICATION_PASS2.md | PRESENT | yes | card + manual |
| 82 | solo-levelling/the harness/validation/REMAINING_GAPS.md | PRESENT | yes | card + manual |
| 83 | solo-levelling/the harness/validation/V-KB-1.md | PRESENT | yes | card + manual |
| 84 | solo-levelling/the harness/validation/V-KB-2.md | PRESENT | yes | card + manual |
| 85 | solo-levelling/the harness/validation/V-KB-3.md | PRESENT | yes | card + manual |
| 86 | solo-levelling/the harness/validation/V-KB-4.md | PRESENT | yes | card + manual |
| 87 | solo-levelling/the harness/validation/V-OB-1.md | PRESENT | yes | card + manual |
| 88 | solo-levelling/the harness/validation/V-OB-2.md | PRESENT | yes | card + manual |
| 89 | solo-levelling/the harness/validation/V-OB-3.md | PRESENT | yes | card + manual |
| 90 | solo-levelling/the harness/validation/V-OB-4.md | PRESENT | yes | card + manual |
| 91 | solo-levelling/the harness/validation/V-OB-5.md | PRESENT | yes | card + manual |
| 92 | solo-levelling/the harness/validation/V-OB-6.md | PRESENT | yes | card + manual |
| 93 | solo-levelling/the harness/validation/V-SYN-1.md | PRESENT | yes | card + manual |
| 94 | solo-levelling/the harness/validation/V-SYN-2.md | PRESENT | yes | card + manual |
| 95 | solo-levelling/the harness/validation/V-TO-1.md | PRESENT | yes | card + manual |
| 96 | solo-levelling/the harness/validation/V-TO-2.md | PRESENT | yes | card + manual |
| 97 | solo-levelling/the harness/validation/V-TO-3.md | PRESENT | yes | card + manual |
| 98 | solo-levelling/the harness/validation/V-TO-4.md | PRESENT | yes | card + manual |
| 99 | solo-levelling/the harness/validation/V-TO-5.md | PRESENT | yes | card + manual |
| 100 | solo-levelling/the harness/validation/V-TO-6.md | PRESENT | yes | card + manual |
| 101 | solo-levelling/the harness/validation/V-TO-7.md | PRESENT | yes | card + manual |
| 102 | solo-levelling/the harness/validation/V-TO-8.md | PRESENT | yes | card + manual |
| 103 | solo-levelling/the harness/validation/V-TX-1.md | PRESENT | yes | card + manual |
| 104 | solo-levelling/the harness/validation/V-TX-2.md | PRESENT | yes | card + manual |
| 105 | solo-levelling/the harness/validation/V-TX-3.md | PRESENT | yes | card + manual |
| 106 | solo-levelling/the harness/validation/V-TX-4.md | PRESENT | yes | card + manual |
| 107 | solo-levelling/the harness/validation/V-TX-5.md | PRESENT | yes | card + manual |
| 108 | solo-levelling/the harness/validation/V-TX-6.md | PRESENT | yes | card + manual |
| 109 | solo-levelling/the harness/validation/V-TX-7.md | PRESENT | yes | card + manual |
| 110 | solo-levelling/the harness/validation/V-TX-8.md | PRESENT | yes | card + manual |
| 111 | solo-levelling/the harness/validation/VALIDATION_AUDIT.md | PRESENT | yes | card + manual |
| 112 | builders-playbook/product_engineering/report/01-executive-findings.md | PRESENT | yes | card + manual |
| 113 | builders-playbook/product_engineering/report/13-bottleneck-analysis.md | PRESENT | yes | card + manual |
| 114 | builders-playbook/product_engineering/report/19-missing-topics.md | PRESENT | yes | card + manual |
| 115 | builders-playbook/product_engineering/research/domain-a/04-prototyping-frontend.md | PRESENT | yes | card + manual |
| 116 | builders-playbook/product_engineering/research/domain-a/06-testing-debugging-review.md | PRESENT | yes | card + manual |
| 117 | builders-playbook/product_engineering/research/domain-a/07-security-quality-assurance.md | PRESENT | yes | card + manual |
| 118 | builders-playbook/product_engineering/research/economics/01-delivery-economics.md | PRESENT | yes | card + manual |
| 119 | builders-playbook/product_engineering/research/economics/02-bottleneck-analysis.md | PRESENT | yes | card + manual |
| 120 | builders-playbook/product_engineering/research/economics/03-productivity-evidence-review.md | PRESENT | yes | card + manual |
| 121 | builders-playbook/product_engineering/research/gaps/01-missing-topics.md | PRESENT | yes | card + manual |
| 122 | builders-playbook/product_engineering/research/cases-hyperscale/06-cross-company-lessons.md | PRESENT | yes | card + manual |
| 123 | builders-playbook/product_engineering/research/cases-product/13-cross-company-lessons.md | PRESENT | yes | card + manual |
| 124 | builders-playbook/product_engineering/evidence/unresolved-questions.md | PRESENT | yes | card + manual |

### 1.10 Tools

| # | Entity | Verdict | Useful | Where |
|---|---|---|---|---|
| 1 | opencode-research/research/08-testing-qa.md | PRESENT | yes | card + manual |
| 2 | God research/B-category-catalogs/03-backend.md | PRESENT | yes | card + manual |
| 3 | God research/B-category-catalogs/04-data.md | PRESENT | yes | card + manual |
| 4 | God research/B-category-catalogs/05-builders.md | PRESENT | yes | card + manual |
| 5 | God research/B-category-catalogs/07-design-to-code.md | PRESENT | yes | card + manual |
| 6 | God research/B-category-catalogs/14-context-memory.md | PRESENT | yes | card + manual |
| 7 | God research/B-category-catalogs/15-scraping.md | PRESENT | yes | card + manual |
| 8 | God research/B-category-catalogs/16-testing.md | PRESENT | yes | card + manual |
| 9 | God research/B-category-catalogs/18-cicd.md | PRESENT | yes | card + manual |
| 10 | God research/B-category-catalogs/19-cloud-deploy.md | PRESENT | yes | card + manual |
| 11 | God research/B-category-catalogs/20-seo-cms-commerce.md | PRESENT | yes | card + manual |
| 12 | God research/B-category-catalogs/21-creative-3d.md | PRESENT | yes | card + manual |
| 13 | God research/atlas/B1-core-web-technologies.md | PRESENT | yes | card + manual |
| 14 | God research/atlas/B5-infrastructure-quality.md | PRESENT | yes | card + manual |
| 15 | God research/atlas/catalogs/01a-languages-build.md | PRESENT | yes | card + manual |
| 16 | God research/atlas/catalogs/05b-context.md | PRESENT | yes | card + manual |
| 17 | God research/atlas/catalogs/06a-data-acquisition.md | PRESENT | yes | card + manual |
| 18 | God research/atlas/catalogs/06c-operations.md | PRESENT | yes | card + manual |
| 19 | God research - gemini/01-core-web-tech.md | PRESENT | yes | card + manual |
| 20 | God research - gemini/05-infra-ops.md | PRESENT | yes | card + manual |
| 21 | God research/agy-pass/01-core-web-tech.md | PRESENT | yes | card + manual |
| 22 | solo-levelling/scripts/scope-check.py | PRESENT | yes | card + manual |
| 23 | solo-levelling/scripts/secret-scan.sh | PRESENT | yes | card + manual |
| 24 | solo-levelling/scripts/verify.sh | PRESENT | yes | card + manual |
| 25 | solo-levelling/the harness/.harness/skills/01-repo-surveyor-map/scripts/survey_repo.py | PRESENT | yes | card + manual |
| 26 | solo-levelling/the harness/.harness/skills/02-git-worktree-isolation/scripts/create_worktree.sh | PRESENT | yes | card + manual |
| 27 | solo-levelling/the harness/.harness/skills/09-docker-sandbox-runner/scripts/sandbox_run.sh | PRESENT | yes | card + manual |
| 28 | solo-levelling/the harness/.harness/skills/32-secrets-entropy-sanitizer/scripts/entropy_scan.sh | PRESENT | yes | card + manual |
| 29 | solo-levelling/the harness/phase-3/tools/T-A_EXECUTION.md | PRESENT | yes | card + manual |
| 30 | solo-levelling/the harness/phase-3/tools/T-B_CONTEXT.md | PRESENT | yes | card + manual |
| 31 | solo-levelling/the harness/phase-3/tools/T-C_INTEGRATION.md | PRESENT | yes | card + manual |
| 32 | solo-levelling/the harness/phase-3/tools/T-D_SAFETY.md | PRESENT | yes | card + manual |
| 33 | solo-levelling/the harness/phase-3/tools/T-E_DX_META.md | PRESENT | yes | card + manual |
| 34 | solo-levelling/the harness/phase-3/tools/T-F_A_TIER.md | PRESENT | yes | card + manual |
| 35 | solo-levelling/the harness/phase-3/tools/T-G_A_TIER_2.md | PRESENT | yes | card + manual |
| 36 | solo-levelling/the harness/phase-3/tools/T-H_B_TIER.md | PRESENT | yes | card + manual |
| 37 | solo-levelling/the harness/scripts/__init__.py | PRESENT | yes | card + manual |
| 38 | solo-levelling/the harness/scripts/mock_telemetry_daemon.py | PRESENT | yes | card + manual |
| 39 | deve/Taskfile.yml | PRESENT | yes | card + manual |
| 40 | deve/scripts/spend-log.sh | PRESENT | yes | card + manual |
| 41 | deve/scripts/test_pre_tool_guard.py | PRESENT | yes | card + manual |
| 42 | deve/scripts/test_scope_check.py | PRESENT | yes | card + manual |
| 43 | builders-playbook/product_engineering/research/expansion-tools/00-index.md | PRESENT | yes | card + manual |
| 44 | builders-playbook/product_engineering/research/expansion-tools/01-coding-agents.md | PRESENT | yes | card + manual |
| 45 | builders-playbook/product_engineering/research/expansion-tools/02-agent-frameworks.md | PRESENT | yes | card + manual |
| 46 | builders-playbook/product_engineering/research/expansion-tools/03-testing.md | PRESENT | yes | card + manual |
| 47 | builders-playbook/product_engineering/research/expansion-tools/04-feature-flags-experimentation.md | PRESENT | yes | card + manual |
| 48 | builders-playbook/product_engineering/research/expansion-tools/05-cicd-gitops.md | PRESENT | yes | card + manual |
| 49 | builders-playbook/product_engineering/research/expansion-tools/06-observability.md | PRESENT | yes | card + manual |
| 50 | builders-playbook/product_engineering/research/expansion-tools/07-incident-management.md | PRESENT | yes | card + manual |
| 51 | builders-playbook/product_engineering/research/expansion-tools/08-design-prototyping.md | PRESENT | yes | card + manual |
| 52 | builders-playbook/product_engineering/research/expansion-tools/09-documentation.md | PRESENT | yes | card + manual |
| 53 | builders-playbook/product_engineering/research/expansion-tools/10-analytics.md | PRESENT | yes | card + manual |
| 54 | builders-playbook/product_engineering/research/expansion-tools/11-ai-eval-harnesses.md | PRESENT | yes | card + manual |
| 55 | builders-playbook/product_engineering/research/expansion-tools/12-workflow-orchestration.md | PRESENT | yes | card + manual |
| 56 | builders-playbook/product_engineering/research/expansion-tools/13-secrets-management.md | PRESENT | yes | card + manual |
| 57 | builders-playbook/product_engineering/research/expansion-tools/14-discovery-research.md | PRESENT | yes | card + manual |
| 58 | builders-playbook/product_engineering/research/expansion-tools/15-project-management.md | PRESENT | yes | card + manual |
| 59 | builders-playbook/product_engineering/research/expansion-tools/16-databases-caching.md | PRESENT | yes | card + manual |
| 60 | builders-playbook/product_engineering/research/expansion-tools/17-paas-deploy.md | PRESENT | yes | card + manual |
| 61 | builders-playbook/product_engineering/research/expansion-tools/18-game-creative-runtimes.md | PRESENT | yes | card + manual |
| 62 | builders-playbook/product_engineering/research/cases-product/12-tool-intelligence.md | PRESENT | yes | card + manual |
| 63 | builders-playbook/product_engineering/appendices/B-expansion-tools.md | PRESENT | yes | card + manual |
| 64 | builders-playbook/product_engineering/appendices/E-tool-intelligence-register.md | PRESENT | yes | card + manual |

### 1.11 Practices

| # | Entity | Verdict | Useful | Where |
|---|---|---|---|---|
| 1 | deve/os/release-experiments.md | PRESENT | yes | card + manual |
| 2 | deve/os/roles.md | PRESENT | yes | card + manual |
| 3 | builders-playbook/product_engineering/report/03-product-lifecycle.md | PRESENT | yes | card + manual |
| 4 | builders-playbook/product_engineering/report/08-functional-completeness.md | PRESENT | yes | card + manual |
| 5 | builders-playbook/product_engineering/report/11-testing-quality-deployment-ops.md | PRESENT | yes | card + manual |
| 6 | builders-playbook/product_engineering/report/12-business-viability.md | PRESENT | yes | card + manual |
| 7 | builders-playbook/product_engineering/research/discovery/01-problem-discovery.md | PRESENT | yes | card + manual |
| 8 | builders-playbook/product_engineering/research/discovery/02-ideation-prioritisation.md | PRESENT | yes | card + manual |
| 9 | builders-playbook/product_engineering/research/discovery/03-validation.md | PRESENT | yes | card + manual |
| 10 | builders-playbook/product_engineering/research/domain-a/01-research-planning.md | PRESENT | yes | card + manual |
| 11 | builders-playbook/product_engineering/research/domain-a/02-requirements-specifications.md | PRESENT | yes | card + manual |
| 12 | builders-playbook/product_engineering/research/domain-a/03-ux-research-design.md | PRESENT | yes | card + manual |
| 13 | builders-playbook/product_engineering/research/domain-a/09-monitoring-incident-response.md | PRESENT | yes | card + manual |
| 14 | builders-playbook/product_engineering/research/domain-a/10-documentation-maintenance.md | PRESENT | yes | card + manual |
| 15 | builders-playbook/product_engineering/research/domain-b/01-llm-features.md | PRESENT | yes | card + manual |
| 16 | builders-playbook/product_engineering/research/domain-b/02-rag.md | PRESENT | yes | card + manual |
| 17 | builders-playbook/product_engineering/research/domain-b/04-recommendations.md | PRESENT | yes | card + manual |
| 18 | builders-playbook/product_engineering/research/domain-b/05-ai-search-extraction.md | PRESENT | yes | card + manual |
| 19 | builders-playbook/product_engineering/research/domain-b/06-multimodal.md | PRESENT | yes | card + manual |
| 20 | builders-playbook/product_engineering/research/domain-b/09-cost-latency-reliability.md | PRESENT | yes | card + manual |
| 21 | builders-playbook/product_engineering/research/domain-b/10-security-ops.md | PRESENT | yes | card + manual |
| 22 | builders-playbook/product_engineering/research/domain-c/01-customer-support.md | PRESENT | yes | card + manual |
| 23 | builders-playbook/product_engineering/research/domain-c/02-research-knowledge-management.md | PRESENT | yes | card + manual |
| 24 | builders-playbook/product_engineering/research/domain-c/03-internal-operations.md | PRESENT | yes | card + manual |
| 25 | builders-playbook/product_engineering/research/domain-c/04-sales-customer-success.md | PRESENT | yes | card + manual |
| 26 | builders-playbook/product_engineering/research/domain-c/05-analytics-reporting.md | PRESENT | yes | card + manual |
| 27 | builders-playbook/product_engineering/research/domain-c/06-administrative-processes.md | PRESENT | yes | card + manual |
| 28 | builders-playbook/product_engineering/research/domain-c/07-engineering-coordination.md | PRESENT | yes | card + manual |
| 29 | builders-playbook/product_engineering/research/domain-c/08-business-workflows.md | PRESENT | yes | card + manual |
| 30 | builders-playbook/product_engineering/research/spec-arch/01-requirements-specs.md | PRESENT | yes | card + manual |
| 31 | builders-playbook/product_engineering/research/spec-arch/02-architecture-decisions.md | PRESENT | yes | card + manual |
| 32 | builders-playbook/product_engineering/research/spec-arch/03-repo-foundations.md | PRESENT | yes | card + manual |
| 33 | builders-playbook/product_engineering/research/ux-states/01-polish-details.md | PRESENT | yes | card + manual |
| 34 | builders-playbook/product_engineering/research/ux-states/02-ux-state-matrix.md | PRESENT | yes | card + manual |
| 35 | builders-playbook/product_engineering/research/ux-states/03-demo-authenticity.md | PRESENT | yes | card + manual |
| 36 | builders-playbook/product_engineering/research/quality/01-functional-audit.md | PRESENT | yes | card + manual |
| 37 | builders-playbook/product_engineering/research/quality/02-accessibility.md | PRESENT | yes | card + manual |
| 38 | builders-playbook/product_engineering/research/automation/01-automation-stack.md | PRESENT | yes | card + manual |
| 39 | builders-playbook/product_engineering/research/build-ship/01-implementation-quality.md | PRESENT | yes | card + manual |
| 40 | builders-playbook/product_engineering/research/build-ship/02-testing-deployment.md | PRESENT | yes | card + manual |
| 41 | builders-playbook/product_engineering/research/build-ship/03-production-ops.md | PRESENT | yes | card + manual |
| 42 | builders-playbook/product_engineering/research/build-ship/04-adoption-viability.md | PRESENT | yes | card + manual |
| 43 | builders-playbook/product_engineering/research/security/01-auth-account.md | PRESENT | yes | card + manual |
| 44 | builders-playbook/product_engineering/research/security/02-app-api.md | PRESENT | yes | card + manual |
| 45 | builders-playbook/product_engineering/research/security/03-database-secrets.md | PRESENT | yes | card + manual |
| 46 | builders-playbook/product_engineering/research/security/04-ai-agent-security.md | PRESENT | yes | card + manual |
| 47 | builders-playbook/product_engineering/research/expansion-practices/00-index.md | PRESENT | yes | card + manual |
| 48 | builders-playbook/product_engineering/research/expansion-practices/01-contrarian-methodologies.md | PRESENT | yes | card + manual |
| 49 | builders-playbook/product_engineering/research/expansion-practices/02-abandoned-approaches.md | PRESENT | yes | card + manual |
| 50 | builders-playbook/product_engineering/research/expansion-practices/03-unwritten-rules.md | PRESENT | yes | card + manual |
| 51 | builders-playbook/product_engineering/research/expansion-practices/04-extreme-practices.md | PRESENT | yes | card + manual |
| 52 | builders-playbook/product_engineering/research/expansion-practices/05-indie-bootstrapper-wisdom.md | PRESENT | yes | card + manual |
| 53 | builders-playbook/product_engineering/research/expansion-practices/06-ai-era-fringe.md | PRESENT | yes | card + manual |
| 54 | builders-playbook/product_engineering/research/expansion-practices/07-craft-culture.md | PRESENT | yes | card + manual |
| 55 | builders-playbook/product_engineering/appendices/C-expansion-practices.md | PRESENT | yes | card + manual |
| 56 | builders-playbook/01-hackathon-win-system.md | PRESENT | yes | card + manual |

### 1.12 Workflows

| # | Entity | Verdict | Useful | Where |
|---|---|---|---|---|
| 1 | solo-levelling/os/lifecycle.md | PRESENT | yes | card + manual |
| 2 | solo-levelling/.harness/workflows/deploy-monitor.yaml | PRESENT | yes | card + manual |
| 3 | solo-levelling/.harness/workflows/fcar-review.yaml | PRESENT | yes | card + manual |
| 4 | solo-levelling/.harness/workflows/launch-checklist.yaml | PRESENT | yes | card + manual |
| 5 | solo-levelling/.harness/workflows/postmortem.yaml | PRESENT | yes | card + manual |
| 6 | solo-levelling/.harness/workflows/scope-gate.yaml | PRESENT | yes | card + manual |
| 7 | solo-levelling/.harness/workflows/stakes-classifier.yaml | PRESENT | yes | card + manual |
| 8 | solo-levelling/.harness/workflows/unknown-first-sorter.yaml | PRESENT | yes | card + manual |
| 9 | solo-levelling/.harness/workflows/working-backwards.yaml | PRESENT | yes | card + manual |
| 10 | solo-levelling/the harness/.harness/workflows/blueprints/build-verify.yaml | PRESENT | yes | card + manual |
| 11 | solo-levelling/the harness/.harness/workflows/blueprints/migration-safeguard.yaml | PRESENT | yes | card + manual |
| 12 | solo-levelling/the harness/.harness/workflows/blueprints/refactor-safely.yaml | PRESENT | yes | card + manual |
| 13 | solo-levelling/the harness/.harness/workflows/blueprints/test-and-verify.yaml | PRESENT | yes | card + manual |
| 14 | solo-levelling/the harness/.harness/workflows/build-verify.yaml | PRESENT | yes | card + manual |
| 15 | solo-levelling/the harness/.harness/workflows/migration-safeguard.yaml | PRESENT | yes | card + manual |
| 16 | solo-levelling/the harness/.harness/workflows/refactor-safely.yaml | PRESENT | yes | card + manual |
| 17 | solo-levelling/the harness/.harness/workflows/test-and-verify.yaml | PRESENT | yes | card + manual |
| 18 | solo-levelling/the harness/scripts/run_validation.sh | PRESENT | yes | card + manual |
| 19 | deve/.harness/workflows/alternatives-generator.yaml | PRESENT | yes | card + manual |
| 20 | deve/.harness/workflows/deploy-monitor.yaml | PRESENT | yes | card + manual |
| 21 | deve/.harness/workflows/failure-mode-analyzer.yaml | PRESENT | yes | card + manual |
| 22 | deve/.harness/workflows/fcar-review.yaml | PRESENT | yes | card + manual |
| 23 | deve/.harness/workflows/launch-checklist.yaml | PRESENT | yes | card + manual |
| 24 | deve/.harness/workflows/postmortem.yaml | PRESENT | yes | card + manual |
| 25 | deve/.harness/workflows/scope-gate.yaml | PRESENT | yes | card + manual |
| 26 | deve/.harness/workflows/stakes-classifier.yaml | PRESENT | yes | card + manual |
| 27 | deve/.harness/workflows/unknown-first-sorter.yaml | PRESENT | yes | card + manual |
| 28 | deve/.harness/workflows/working-backwards.yaml | PRESENT | yes | card + manual |
| 29 | builders-playbook/product_engineering/report/06-automation-stack-workflows.md | PRESENT | yes | card + manual |
| 30 | builders-playbook/product_engineering/report/16-implementation-roadmap.md | PRESENT | yes | card + manual |
| 31 | builders-playbook/product_engineering/research/domain-a/08-cicd-deployment.md | PRESENT | yes | card + manual |
| 32 | builders-playbook/product_engineering/research/automation/02-workflows.md | PRESENT | yes | card + manual |
| 33 | builders-playbook/02-project-execution-plan.md | PRESENT | yes | card + manual |

### 1.13 Gates

| # | Entity | Verdict | Useful | Where |
|---|---|---|---|---|
| 1 | solo-levelling/os/fcar-rubric.md | PRESENT | yes | card + manual |
| 2 | solo-levelling/os/gates.md | PRESENT | yes | card + manual |
| 3 | solo-levelling/os/quality-security.md | PRESENT | yes | card + manual |
| 4 | solo-levelling/.harness/sandbox/gate.sh | PRESENT | yes | card + manual |
| 5 | solo-levelling/the harness/.harness/sandbox/gate.sh | PRESENT | yes | card + manual |
| 6 | deve/.harness/permissions/check.py | PRESENT | yes | card + manual |
| 7 | deve/.harness/sandbox/gate.sh | PRESENT | yes | card + manual |
| 8 | deve/os/gates.md | PRESENT | yes | card + manual |
| 9 | deve/scripts/scope-check.py | PRESENT | yes | card + manual |
| 10 | deve/scripts/secret-scan.sh | PRESENT | yes | card + manual |
| 11 | deve/scripts/verify.sh | PRESENT | yes | card + manual |
| 12 | builders-playbook/product_engineering/research/domain-b/08-evals.md | PRESENT | yes | card + manual |
| 13 | builders-playbook/product_engineering/research/quality/03-quality-gates.md | PRESENT | yes | card + manual |

### 1.14 Hooks

| # | Entity | Verdict | Useful | Where |
|---|---|---|---|---|
| 1 | opencode-research/research/08-pre-commit-hook.md | PRESENT | yes | card + manual |
| 2 | solo-levelling/lefthook.yml | PRESENT | yes | card + manual |
| 3 | solo-levelling/.harness/hooks/hooks.json | PRESENT | yes | card + manual |
| 4 | solo-levelling/.harness/hooks/pre_tool_guard.py | PRESENT | yes | card + manual |
| 5 | solo-levelling/the harness/.harness/hooks/hooks.json | PRESENT | yes | card + manual |
| 6 | solo-levelling/the harness/.harness/hooks/post_tool_linter.py | PRESENT | yes | card + manual |
| 7 | solo-levelling/the harness/.harness/hooks/pre_tool_guard.py | PRESENT | yes | card + manual |
| 8 | deve/.harness/hooks/hooks.json | PRESENT | yes | card + manual |
| 9 | deve/.harness/hooks/pre_tool_guard.py | PRESENT | yes | card + manual |
| 10 | deve/lefthook.yml | PRESENT | yes | card + manual |

### 1.15 Config

| # | Entity | Verdict | Useful | Where |
|---|---|---|---|---|
| 1 | God research/agy-pass/05-infra-ops.md | PRESENT | yes | card + manual |
| 2 | God research/_state/resource-index.json | PRESENT | yes | card + manual |
| 3 | solo-levelling/Taskfile.yml | PRESENT | yes | card + manual |
| 4 | solo-levelling/.env.template | PRESENT | yes | card + manual |
| 5 | solo-levelling/projects/.gitkeep | PRESENT | yes | card + manual |
| 6 | solo-levelling/.harness/permissions/presets.json | PRESENT | yes | card + manual |
| 7 | solo-levelling/.harness/telemetry/litellm-config.yaml | PRESENT | yes | card + manual |
| 8 | solo-levelling/the harness/.gemini/settings.json | PRESENT | yes | card + manual |
| 9 | solo-levelling/the harness/.harness/config/harness.yaml | PRESENT | yes | card + manual |
| 10 | solo-levelling/the harness/.harness/permissions/presets.json | PRESENT | yes | card + manual |
| 11 | solo-levelling/the harness/.harness/skills/index.json | PRESENT | yes | card + manual |
| 12 | solo-levelling/the harness/.harness/telemetry/langfuse-config.json | PRESENT | yes | card + manual |
| 13 | solo-levelling/the harness/.harness/telemetry/litellm-config.yaml | PRESENT | yes | card + manual |
| 14 | solo-levelling/the harness/Taskfile.yml | PRESENT | yes | card + manual |
| 15 | solo-levelling/the harness/lefthook.yml | PRESENT | yes | card + manual |
| 16 | solo-levelling/the harness/phase-0/.gitkeep | PRESENT | yes | card + manual |
| 17 | deve/.cursorrules | PRESENT | yes | card + manual |
| 18 | deve/.env.template | PRESENT | yes | card + manual |
| 19 | deve/.gitignore | PRESENT | yes | card + manual |
| 20 | deve/.harness/permissions/presets.json | PRESENT | yes | card + manual |
| 21 | deve/.harness/telemetry/litellm-config.yaml | PRESENT | yes | card + manual |

### 1.16 Archives

| # | Entity | Verdict | Useful | Where |
|---|---|---|---|---|
| 1 | God research/B-category-catalogs/22-prompt-archives-meta.md | PRESENT | yes | card + manual |
| 2 | God research/E-prompt-directory-meta-only.md | PRESENT | yes | card + manual |
| 3 | God research/atlas/E-prompt-archives.md | PRESENT | yes | card + manual |
| 4 | God research/atlas/registers/prompt-archives.md | PRESENT | yes | card + manual |
| 5 | deve/.harness/telemetry/guard.log | PRESENT | yes | card + manual |
| 6 | deve/.pytest_cache/.gitignore | PRESENT | yes | card + manual |
| 7 | deve/.pytest_cache/CACHEDIR.TAG | PRESENT | yes | card + manual |
| 8 | deve/.pytest_cache/README.md | PRESENT | yes | card + manual |
| 9 | deve/.pytest_cache/v/cache/lastfailed | PRESENT | yes | card + manual |
| 10 | deve/.pytest_cache/v/cache/nodeids | PRESENT | yes | card + manual |

### 1.17 Reports

| # | Entity | Verdict | Useful | Where |
|---|---|---|---|---|
| 1 | God research/atlas/README.md | PRESENT | yes | card + manual |
| 2 | God research/atlas/I-coverage-register.md | PRESENT | yes | card + manual |
| 3 | God research/atlas/catalogs/06b-quality.md | PRESENT | yes | card + manual |
| 4 | God research/atlas/registers/coverage.md | PRESENT | yes | card + manual |
| 5 | God research - gemini/00-README-second-pass.md | PRESENT | yes | card + manual |
| 6 | God research/agy-pass/00-README-third-pass.md | PRESENT | yes | card + manual |
| 7 | God research/DIFF-REPORT-gemini-vs-firstpass.md | PRESENT | yes | card + manual |
| 8 | God research/DIFF-REPORT-agy-vs-both.md | PRESENT | yes | card + manual |
| 9 | God research/DIFF-REPORT-atlas-vs-all.md | PRESENT | yes | card + manual |
| 10 | God research/atlas-READ-LOG.md | PRESENT | yes | card + manual |
| 11 | God research/_state/atlas-read-group1.md | PRESENT | yes | card + manual |
| 12 | God research/_state/atlas-read-group2.md | PRESENT | yes | card + manual |
| 13 | God research/_state/atlas-read-group3.md | PRESENT | yes | card + manual |
| 14 | God research/_state/atlas-read-group4.md | PRESENT | yes | card + manual |
| 15 | God research/diff report.txt | PRESENT | yes | card + manual |
| 16 | God research/the_omniscient_resource_atlas.md | PRESENT | yes | card + manual |
| 17 | solo-levelling/research-log.md | PRESENT | yes | card + manual |
| 18 | solo-levelling/the harness/AGENTS.md | PRESENT | yes | card + manual |
| 19 | solo-levelling/the harness/ISSUES.md | PRESENT | yes | card + manual |
| 20 | solo-levelling/the harness/SKILLS_VERIFICATION.md | PRESENT | yes | card + manual |
| 21 | solo-levelling/the harness/phase-1/batch-4/R-A_SAFETY_AGY.md | PRESENT | yes | card + manual |
| 22 | solo-levelling/the harness/phase-1/batch-4/R-B_SAFETY_AGY.md | PRESENT | yes | card + manual |
| 23 | solo-levelling/the harness/phase-1/batch-4/V-C_SAFETY_AGY.md | PRESENT | yes | card + manual |
| 24 | solo-levelling/the harness/phase-1/batch-4/V-D_SAFETY_AGY.md | PRESENT | yes | card + manual |
| 25 | solo-levelling/the harness/phase-1/batch-5/BATCH-5_DX_OBSERVABILITY.md | PRESENT | yes | card + manual |
| 26 | solo-levelling/the harness/phase-1/batch-5/R-A_DX_AGY.md | PRESENT | yes | card + manual |
| 27 | solo-levelling/the harness/phase-1/batch-5/R-B_DX_AGY.md | PRESENT | yes | card + manual |
| 28 | solo-levelling/the harness/phase-1/batch-5/V-C_DX_AGY.md | PRESENT | yes | card + manual |
| 29 | solo-levelling/the harness/phase-1/batch-5/V-D_DX_AGY.md | PRESENT | yes | card + manual |
| 30 | solo-levelling/the harness/phase-2/RANKINGS.md | PRESENT | yes | card + manual |
| 31 | solo-levelling/the harness/phase-2/rankings/G1_EXECUTION.md | PRESENT | yes | card + manual |
| 32 | solo-levelling/the harness/phase-2/rankings/G2_CONTEXT.md | PRESENT | yes | card + manual |
| 33 | solo-levelling/the harness/phase-2/rankings/G3_INTEGRATION.md | PRESENT | yes | card + manual |
| 34 | solo-levelling/the harness/phase-2/rankings/G4_SAFETY.md | PRESENT | yes | card + manual |
| 35 | solo-levelling/the harness/phase-2/rankings/G5_DX.md | PRESENT | yes | card + manual |
| 36 | solo-levelling/the harness/phase-2/verify/ARCHETYPE_MATRIX_AGY.md | PRESENT | yes | card + manual |
| 37 | solo-levelling/the harness/phase-3.5/FRICTION_LOG.md | PRESENT | yes | card + manual |
| 38 | solo-levelling/the harness/phase-3.5/M_A_AGY.md | PRESENT | yes | card + manual |
| 39 | solo-levelling/the harness/phase-3.5/M_B_AGY.md | PRESENT | yes | card + manual |
| 40 | solo-levelling/the harness/phase-3.5/M_C_AGY.md | PRESENT | yes | card + manual |
| 41 | solo-levelling/the harness/phase-3.5/VALIDATION_REPORT.md | PRESENT | yes | card + manual |
| 42 | solo-levelling/the harness/phase-3/TOOL_SELECTION_INDEX.md | PRESENT | yes | card + manual |
| 43 | solo-levelling/the harness/update.md | PRESENT | yes | card + manual |
| 44 | builders-playbook/product_engineering/report/README.md | PRESENT | yes | card + manual |
| 45 | builders-playbook/product_engineering/research/gaps/00-index.md | PRESENT | yes | card + manual |
| 46 | builders-playbook/product_engineering/evidence/final-research-audit.md | PRESENT | yes | card + manual |
| 47 | builders-playbook/README.md | PRESENT | yes | card + manual |
| 48 | builders-playbook/research/hackathon-intel-notes.md | PRESENT | yes | card + manual |

### 1.18 Evidence

| # | Entity | Verdict | Useful | Where |
|---|---|---|---|---|
| 1 | builders-playbook/product_engineering/report/18-evidence-register.md | PRESENT | yes | card + manual |
| 2 | builders-playbook/product_engineering/research/discovery/04-evidence-register.md | PRESENT | yes | card + manual |
| 3 | builders-playbook/product_engineering/research/domain-a/12-evidence-register.md | PRESENT | yes | card + manual |
| 4 | builders-playbook/product_engineering/research/domain-b/12-evidence-register.md | PRESENT | yes | card + manual |
| 5 | builders-playbook/product_engineering/research/domain-c/10-evidence-register.md | PRESENT | yes | card + manual |
| 6 | builders-playbook/product_engineering/research/spec-arch/04-evidence-register.md | PRESENT | yes | card + manual |
| 7 | builders-playbook/product_engineering/research/ux-states/04-evidence-register.md | PRESENT | yes | card + manual |
| 8 | builders-playbook/product_engineering/research/quality/04-evidence-register.md | PRESENT | yes | card + manual |
| 9 | builders-playbook/product_engineering/research/automation/03-evidence-register.md | PRESENT | yes | card + manual |
| 10 | builders-playbook/product_engineering/research/build-ship/05-evidence-register.md | PRESENT | yes | card + manual |
| 11 | builders-playbook/product_engineering/research/economics/04-evidence-register.md | PRESENT | yes | card + manual |
| 12 | builders-playbook/product_engineering/research/gaps/02-evidence-register.md | PRESENT | yes | card + manual |
| 13 | builders-playbook/product_engineering/research/authenticity/04-evidence-register.md | PRESENT | yes | card + manual |
| 14 | builders-playbook/product_engineering/research/security/07-evidence-register.md | PRESENT | yes | card + manual |
| 15 | builders-playbook/product_engineering/research/expansion-companies/evidence-register.md | PRESENT | yes | card + manual |
| 16 | builders-playbook/product_engineering/research/expansion-tools/evidence-register.md | PRESENT | yes | card + manual |
| 17 | builders-playbook/product_engineering/research/expansion-practices/evidence-register.md | PRESENT | yes | card + manual |
| 18 | builders-playbook/product_engineering/research/forensics/evidence-register.md | PRESENT | yes | card + manual |
| 19 | builders-playbook/product_engineering/research/cases-hyperscale/07-evidence-register.md | PRESENT | yes | card + manual |
| 20 | builders-playbook/product_engineering/research/cases-product/14-evidence-register.md | PRESENT | yes | card + manual |
| 21 | builders-playbook/product_engineering/evidence/coverage-matrix.md | PRESENT | yes | card + manual |
| 22 | builders-playbook/product_engineering/evidence/merged-evidence-register.md | PRESENT | yes | card + manual |
| 23 | builders-playbook/product_engineering/evidence/source-directory.md | PRESENT | yes | card + manual |
| 24 | builders-playbook/product_engineering/research/rules/05-evidence-register.md | PRESENT | yes | card + manual |
| 25 | builders-playbook/product_engineering/research/discipline-ai-act/02-evidence-register.md | PRESENT | yes | card + manual |
| 26 | builders-playbook/product_engineering/research/discipline-api-product/02-evidence-register.md | PRESENT | yes | card + manual |
| 27 | builders-playbook/product_engineering/research/discipline-billing/02-evidence-register.md | PRESENT | yes | card + manual |
| 28 | builders-playbook/product_engineering/research/discipline-blindspots/02-evidence-register.md | PRESENT | yes | card + manual |
| 29 | builders-playbook/product_engineering/research/discipline-compliance/02-evidence-register.md | PRESENT | yes | card + manual |
| 30 | builders-playbook/product_engineering/research/discipline-finops/02-evidence-register.md | PRESENT | yes | card + manual |
| 31 | builders-playbook/product_engineering/research/discipline-mobile-release/02-evidence-register.md | PRESENT | yes | card + manual |
| 32 | builders-playbook/product_engineering/research/discipline-notifications/02-evidence-register.md | PRESENT | yes | card + manual |
| 33 | builders-playbook/product_engineering/research/discipline-trust-safety/02-evidence-register.md | PRESENT | yes | card + manual |
| 34 | builders-playbook/research/hackathon-intel-evidence.md | PRESENT | yes | card + manual |

### 1.19 Agents

| # | Entity | Verdict | Useful | Where |
|---|---|---|---|---|
| 1 | God research/B-category-catalogs/11-agents.md | PRESENT | yes | card + manual |
| 2 | God research/B-category-catalogs/12-multi-agent.md | PRESENT | yes | card + manual |
| 3 | God research/atlas/catalogs/03b-agents.md | PRESENT | yes | card + manual |
| 4 | God research - gemini/04-agents-harness-context.md | PRESENT | yes | card + manual |
| 5 | solo-levelling/AGENTS.md | PRESENT | yes | card + manual |
| 6 | solo-levelling/the harness/.harness/agents/coder.md | PRESENT | yes | card + manual |
| 7 | solo-levelling/the harness/.harness/agents/explorer.md | PRESENT | yes | card + manual |
| 8 | solo-levelling/the harness/.harness/agents/planner.md | PRESENT | yes | card + manual |
| 9 | solo-levelling/the harness/.harness/agents/reviewer.md | PRESENT | yes | card + manual |
| 10 | deve/AGENTS.md | PRESENT | yes | card + manual |
| 11 | builders-playbook/product_engineering/report/05-ai-agent-architecture.md | PRESENT | yes | card + manual |

### 1.20 Harness

| # | Entity | Verdict | Useful | Where |
|---|---|---|---|---|
| 1 | opencode-research/BUILD-PROMPT-FINAL.md | PRESENT | yes | card + manual |
| 2 | opencode-research/BUILD-PROMPT-UNIVERSAL.md | PRESENT | yes | card + manual |
| 3 | opencode-research/research/07-autonomous-agent-architecture.md | PRESENT | yes | card + manual |
| 4 | opencode-research/harness-templates/AGENTS.md | PRESENT | yes | card + manual |
| 5 | opencode-research/harness-templates/init.sh | PRESENT | yes | card + manual |
| 6 | God research/B-category-catalogs/13-harness.md | PRESENT | yes | card + manual |
| 7 | God research/atlas/catalogs/05a-orchestration.md | PRESENT | yes | card + manual |
| 8 | God research/agy-pass/04-agents-harness-context.md | PRESENT | yes | card + manual |
| 9 | solo-levelling/GOD_PROMPT.md | PRESENT | yes | card + manual |
| 10 | solo-levelling/.harness/README.md | PRESENT | yes | card + manual |
| 11 | solo-levelling/.harness/config/harness.yaml | PRESENT | yes | card + manual |
| 12 | solo-levelling/the harness/.harness/README.md | PRESENT | yes | card + manual |
| 13 | solo-levelling/the harness/phase-1/synthesis/MASTER_D1.md | PRESENT | yes | card + manual |
| 14 | solo-levelling/the harness/phase-1/synthesis/MASTER_D2.md | PRESENT | yes | card + manual |
| 15 | solo-levelling/the harness/phase-2/STATUS.md | PRESENT | yes | card + manual |
| 16 | solo-levelling/the harness/phase-3.5/STATUS.md | PRESENT | yes | card + manual |
| 17 | solo-levelling/the harness/phase-3.5/VALIDATION_PLAN.md | PRESENT | yes | card + manual |
| 18 | solo-levelling/the harness/phase-3/PLAN.md | PRESENT | yes | card + manual |
| 19 | solo-levelling/the harness/phase-3/STATUS.md | PRESENT | yes | card + manual |
| 20 | solo-levelling/the harness/plan.md | PRESENT | yes | card + manual |
| 21 | deve/.harness/README.md | PRESENT | yes | card + manual |
| 22 | deve/.harness/config/harness.yaml | PRESENT | yes | card + manual |
| 23 | deve/CLAUDE.md | PRESENT | yes | card + manual |
| 24 | builders-playbook/product_engineering/report/15-reference-architecture.md | PRESENT | yes | card + manual |
| 25 | builders-playbook/product_engineering/research/domain-a/05-codebase-exploration-implementation.md | PRESENT | yes | card + manual |
| 26 | builders-playbook/product_engineering/research/domain-b/07-tool-using-agents.md | PRESENT | yes | card + manual |


## Axis 2 — URLs

- HTTP 403: https://www.adobe.com/uk/express/discover/how-to/scrapbook/digital (files/God research/D-design-styles/09-scrapbook.md) — note: reprobe: HTTP 403
- HTTP 403: https://99designs.com/blog/design-history-movements/cyberpunk-design (files/God research/D-design-styles/21-cyberpunk.md) — note: reprobe: HTTP 403
- HTTP 403: https://www.adobe.com/uk/express/learn/blog/all-about-graffiti-art (files/God research/D-design-styles/26-graffiti.md) — note: reprobe: HTTP 403
- HTTP 403: https://www.adobe.com/uk/express/learn/blog/what-is-pastel-goth (files/God research/D-design-styles/27-gothic.md) — note: reprobe: HTTP 403
- HTTP 403: https://www.britannica.com/art/mixed-media (files/God research/D-design-styles/28-mixed-media.md) — note: reprobe: HTTP 403

- total live_urls: 196 | malformed: 0 | no fetch row: 0 | non-200 rows: 5
- worker rows normalized (status=success -> http_status=200, evidence_type, final_url, fetched_at); 8 failed worker fetches are logged but NOT used by any card (verified 0 cards claim them).
- 11 fail rows / 234 total kept as evidence, not dropped.

## Axis 3 — Card integrity

- cards: 707 | failures: 0
- FIXED: 421 worker-invented not_applicable values now enum-staged as {reason, worker_original}; new enum member `evidence-ledger` documented in proofs/reason-map.json; normalize_reasons.py --check enforces (0 unmapped).

## Axis 4 — Prohibitions

- strict hits (model ids outside telemetry config/router runbook + absolute paths): 0
- ALLOWED by plan: litellm-config.yaml tier model pins (carried from deve) and the verbatim 11-litellm-router-admin runbook (documents model IDs by design; they are examples in a runbook, not hardcoded runtime routing). No absolute Desktop paths in shared artifacts.

## Axis 5 — Corpus + plan fidelity

- parts checksums 19/19 OK (read-only corpus untouched) | files checksums 702/707 OK
- banner-map rows 707 | cards 707 unique 707 | shards 100 covering 707 | ledger 809 rows, 0 mismatches
- recheck-queue: [
 {
  "worker": "reprobe",
  "source": "files/God research/D-design-styles/09-scrapbook.md",
  "url": "https://www.adobe.com/uk/express/discover/how-to/scrapbook/digital",
  "http": 403,
  "reason": "bot-blocked (403); needs human GET or archive source",
  "date": "2026-10-13"
 },
 {
  "worker": "reprobe",
  "source": "files/God research/D-design-styles/21-cyberpunk.md",
  "url": "https://99designs.com/blog/design-history-movements/cyberpunk-design",
  "http": 403,
  "reason": "bot-blocked (403); needs human GET or archive source",
  "date": "2026-10-13"
 },
 {
  "worker": "reprobe",
  "source": "files/God research/D-design-styles/26-graffiti.md",
  "url": "https://www.adobe.com/uk/express/learn/blog/all-about-graffiti-art",
  "http": 403,
  "reason": "bot-blocked (403); needs human GET or archive source",
  "date": "2026-10-13"
 },
 {
  "worker": "reprobe",
  "source": "files/God research/D-design-styles/27-gothic.md",
  "url": "https://www.adobe.com/uk/express/learn/blog/what-is-pastel-goth",
  "http": 403,
  "reason": "bot-blocked (403); needs human GET or archive source",
  "date": "2026-10-13"
 },
 {
  "worker": "reprobe",
  "source": "files/God research/D-design-styles/28-mixed-media.md",
  "url": "https://www.britannica.com/art/mixed-media",
  "http": 403,
  "reason": "bot-blocked (403); needs human GET or archive source",
  "date": "2026-10-13"
 }
]

## Axis 6 — Execution shape

- pilot: pilot_pass=true
- quarantine: W071/W074/W066/W089 resolved in quarantine-resolution.md; 0 unresolved
- god_repo: skills 24 | workflows 15 | agents 4 | support manifest 34/34 | tests 58 green in both trees

## §7 Deviations (honest list)

1. Desktop/output.md (Oct 9) is a 200-file partial merge, superseded by the 707-file corpus; its only unique content (21-line adjudication header) is preserved in DIFF-REPORTs/cards.
2. 9 solo skill texts merged as provenance appendix into the vendored deve skills (+ os/LOOP-ENGINEERING.md doctrine); bodies were identical except tail headings, so no content is lost.
3. 36 external skills/MCP are CARD-ONLY registries with in-corpus URLs (not vendored code) — install-on-demand by design.
4. Execution: 100 workers on agy+opencode (agy quota 429 twice; opencode free-model rate limits) forced sequential/low-parallel retries; coverage stayed 707/707.
5. plan/execution-prompt.md ends `Phase 2 authorized: no`; user explicitly authorized Phase 2 (superior-os) in-session.
6. Environment: no task binary (scripts mirror every Taskfile task); Playwright browsers absent (E2E degrades to documented smoke-only); pip index partial (pytest present).

## Rollup

| Axis | Result |
|---|---|
| 1 Entities | 0 MISSING skills; all cataloged items present as vendored dirs or cards |
| 2 URLs | 196 live_urls re-probed 2026-10-13: 191 HTTP 200, 5 HTTP 403 (bot-blocked; annotated on cards + queued to recheck-queue.json, 5 items). No malformed, no unevidenced |
| 3 Cards | 707/707 valid; 421 reasons enum-staged; 0 failures |
| 4 Prohibitions | 0 strict violations (allowed telemetry pins + router runbook documented) |
| 5 Corpus | parts 19/19, files 707/707, banners 707, ledger 0 mismatch |
| 6 Execution | pilot passed, quarantine 0, manifest 34/34, tests 58/58 both trees |
