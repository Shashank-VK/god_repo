# Skills

Every SKILL.md card, alphabetical by source.

### files/God research/B-category-catalogs/09-skills.md
- card: files/God research/B-category-catalogs/09-skills.md | part parts/05-firstpass-B-catalogs.md:3274 | lines 580 | verdict Partially
- WHAT: Agent Skills Catalog 09: comprehensive specification and taxonomy of 28 agent skills resources, standard specifications, official collections, indexes, methodology packs, domain skills, development and validation tooling, and distribution marketplaces verified as of 2026-10-09. Details the open Agent Skills standard (agentskills.io, directory layout with required SKILL.md YAML frontmatter + Markdo
- HOW: 1. Cross-Harness Skill Installation: Install skills universally using npx skills add <owner/repo> [--skill <name>] or discover them interactively with npx skills find <keyword>, automatically targeting appropriate global or project directories across 70+ detected agent runtimes (.claude/skills, .cod
- live: no live URLs
- conflicts: openai/skills repository is deprecated and superseded by OpenAI Plugins and the Build-plugins guide, though standard SKILL.md remains portable., MD-readable != works: GitHub Copilot lacks native skill directory loading and requires .github/copilot-instructions.md adapters; Claude plugin hooks do not reliably port to OpenAI Codex., License heterogeneity: Trail of Bits security skills are licensed under CC-BY-SA-4.0 (requiring share-alike on derivatives), Anthropic document skills carry proprietary license terms restricting redistribution, while Vercel and Matt Pocock skills are MIT-licensed., Ecosystem tool support matrix discrepancies: experimental allowed-tools frontmatter field has varying support across harnesses, with documented gaps in Zencoder and Kiro., Context budget trade-off: bulk-installing skills degrades model intent routing accuracy; quartermaster benchmark shows ~30 skills as the optimal accuracy threshold before selection degradation occurs.

### files/God research/atlas/catalogs/03a-skills.md
- card: files/God research/atlas/catalogs/03a-skills.md | part parts/08-atlas-33.md:17047 | lines 763 | verdict Verified
- WHAT: Atlas Catalog 03a — The Agent Skills Ecosystem (Part 6). Comprehensive survey of the open Agent Skills format (agentskills.io), 19 official company skill collections (Vercel, Sentry, Expo, Hugging Face, Stripe, Trail of Bits, Microsoft, Figma, Netlify, Angular, Supabase, Neon, ClickHouse, HashiCorp, Better Auth, LambdaTest, Capgo, OpenAI, Anthropic), skill installation infrastructure (skills.sh/np
- HOW: Install skills universally: `npx skills add <owner/repo> --skill <name>` (skills.sh CLI supports ~80 agents)
- live: https://agentskills.io; https://github.com/vercel-labs/skills; https://skills.sh; https://github.com/agentskills/agentskills; https://github.com/getsentry/skills; https://github.com/huggingface/skills; https://github.com/stripe/ai; https://github.com/trailofbits/skills; https://github.com/microsoft/skills; https://github.com/netlify/context-and-tools; https://github.com/supabase/agent-skills; http
- conflicts: Trail of Bits CC-BY-SA-4.0 license vs MIT/Apache-2.0 of most other collections, skills.sh telemetry enabled by default (documented in README), Agent Skill Exchange verification tiers are self-published; AIR research shows scan-once models have TOCTOU gaps, Snyk agent-scan requires paid token for verdicts; husk claims free offline alternative, Microsoft skills explicitly WIP; context bloat risk acknowledged in their own docs

### files/God research - gemini/03-skills-mcp.md
- card: files/God research - gemini/03-skills-mcp.md | part parts/09-gemini-secondpass-6.md:1644 | lines 545 | verdict Verified
- WHAT: Comprehensive architectural analysis and ecosystem catalog of Agent Skills (agentskills.io, SKILL.md specification), Model Context Protocol (MCP by Anthropic), and alternative extensibility paradigms (CLI/Terminal, REST/OpenAPI, LSP, Agent-to-Agent/A2A protocols). Covers the canonical SKILL.md directory hierarchy, YAML frontmatter schema, three-tier progressive disclosure lifecycle (Discovery, Act
- HOW: 1. Structure Agent Skills: Create a skill directory with SKILL.md containing YAML frontmatter (name: ^[a-z0-9-]+$, description: <=1024 chars, optional compatibility, allowed-tools) and progressive disclosure sections, with deterministic scripts in scripts/ and deep reference manuals in references/.
- live: no live URLs
- conflicts: Legacy HTTP+SSE vs Streamable HTTP: MCP specification 2024-11-05 legacy SSE required dual connections prone to proxy termination, superseded by 2025/2026 Streamable HTTP unified endpoint with session resumption tokens., TypeScript SDK package restructuring: Monolithic @modelcontextprotocol/sdk v1.x is legacy/deprecated and split into @modelcontextprotocol/server and @modelcontextprotocol/client in v2., Skill vs Tool overlap: Community confusion between procedural markdown skills (agentskills.io) and executable MCP tools resolved by standardizing skills as procedural playbooks and MCP as tool execution bus.

### files/God research/agy-pass/03-skills-mcp.md
- card: files/God research/agy-pass/03-skills-mcp.md | part parts/10-agy-thirdpass-7.md:1841 | lines 841 | verdict Verified
- WHAT: Comprehensive ecosystem reference catalog documenting 65 specifications, repositories, SDKs, tools, and alternatives across 20 distinct categories: 1. Agent Skills Standard & Core Specification (2: agentskills.io spec, progressive disclosure architecture); 2. Canonical & High-Impact Skills Repositories (4: anthropics/skills, VoltAgent awesome-agent-skills, obra/superpowers, mattpocock/skills); 3. 
- HOW: Packaging Skills: Structure skills conforming to agentskills.io standard with mandatory SKILL.md (YAML frontmatter with name and specific description) and optional scripts/, references/, and tests/ directories; validate via skills-validator.
- live: no live URLs
- conflicts: Skills vs MCP Paradigm Distinction: Agent Skills standardizes markdown-based procedural workflows and heuristic knowledge loaded progressively, whereas MCP standardizes JSON-RPC 2.0 executable tool and resource invocation over stdio/SSE., Stdio vs SSE Transport Trade-offs: Stdio requires local subprocess execution on the host machine, inheriting local security contexts, whereas SSE allows remote cloud hosting over HTTP but requires secure authentication and gateway management., MCP vs A2A Architectural Roles: MCP models client-to-server (Agent-to-Tool) relationships, whereas A2A models peer-to-peer (Agent-to-Agent) delegation and handshake protocols., Prompt Overhead vs Tool Richness: Registering dozens of MCP servers or monolithic skills degrades LLM reasoning and consumes token context, requiring two-stage semantic routers (SkillRouter) or progressive disclosure.

### files/solo-levelling/.harness/skills/alternatives-generator/SKILL.md
- card: files/solo-levelling/.harness/skills/alternatives-generator/SKILL.md | part parts/13-deve-solo.md:512 | lines 43 | verdict Verified
- WHAT: Architectural sparring skill (Workflow 3) derived from Google Design Doc culture (Malte Ubl / industrialempathy.com); generates 2 to 3 genuinely viable, non-strawman technical alternatives before committing to any design decision, dependency, or schema. Outputs structured technical summaries, pros, cons/risks, and rejection rationales. Complies with Phase 16 loop rails (max_steps: 2, deterministic
- HOW: Invoke prior to finalizing any architecture decision or filling out Design Notes.
- live: no live URLs
- conflicts: none

### files/solo-levelling/.harness/skills/failure-mode-analyzer/SKILL.md
- card: files/solo-levelling/.harness/skills/failure-mode-analyzer/SKILL.md | part parts/13-deve-solo.md:556 | lines 37 | verdict Verified
- WHAT: Distributed systems resilience skill (Workflow 4) rooted in Amazon and Netflix resilience engineering practices; identifies the top-3 failure modes for any external integration, dependency, API, queue, or database boundary. Outputs a 5-column matrix detailing mechanism, user-visible impact, handling strategy (Prevent vs Tolerate), and local test simulation recipe. Enforces loop rails (max_steps: 2
- HOW: Invoke before integrating external APIs, persistent queues, or distributed services.
- live: no live URLs
- conflicts: none

### files/solo-levelling/.harness/skills/fcar-reviewer/SKILL.md
- card: files/solo-levelling/.harness/skills/fcar-reviewer/SKILL.md | part parts/13-deve-solo.md:594 | lines 38 | verdict Verified
- WHAT: Adversarial quality review skill implementing the Fresh Context Adversarial Review (FCAR) protocol for Gate 4; evaluates an artifact against a 5-item locked rubric (sourced claims, 2+ non-goals, named sources, measurable metric, 1+ rejected alternative). Enforces strict context isolation (must run in fresh session with no prior memory via Claude Code new session or agy --no-context to prevent coll
- HOW: Mandatory execution at Gate 4 prior to artifact sign-off.
- live: no live URLs
- conflicts: none

### files/solo-levelling/.harness/skills/launch-checklist-runner/SKILL.md
- card: files/solo-levelling/.harness/skills/launch-checklist-runner/SKILL.md | part parts/13-deve-solo.md:633 | lines 51 | verdict Verified
- WHAT: Release gate skill (Workflow 5) enforcing Gate 6 pre-flight checks based on Google SRE Launch Checklist standards; evaluates repository state against an 8-item locked checklist (error rate alert, latency alert, tested staged rollback, dependency error handling, clean secret scan via scripts/secret-scan.sh, adversarial auth testing, 2x load test, postmortem template ready) and pre-committed rollbac
- HOW: Execute prior to any production deployment or customer-facing release.
- live: no live URLs
- conflicts: none

### files/solo-levelling/.harness/skills/postmortem-opener/SKILL.md
- card: files/solo-levelling/.harness/skills/postmortem-opener/SKILL.md | part parts/13-deve-solo.md:685 | lines 30 | verdict Verified
- WHAT: Incident analysis skill (Workflow 7) based on Google SRE and Amazon COE practices; generates a rigorous 3-section blameless postmortem draft within 48 hours of any production incident or data issue. Structures output into chronological Timeline with UTC/local timestamps, Five Whys Root Cause Chain targeting systemic flaws (never human error), and Corrective Actions Table with owners and due dates.
- HOW: Trigger within 48 hours following any customer-visible downtime or data corruption.
- live: no live URLs
- conflicts: none

### files/solo-levelling/.harness/skills/scope-gate/SKILL.md
- card: files/solo-levelling/.harness/skills/scope-gate/SKILL.md | part parts/13-deve-solo.md:716 | lines 35 | verdict Verified
- WHAT: Scope Gate Check skill (Workflow 2 in the 9 named workflows) enforcing Shape Up Scope Hammer and No-gos enforcement by semantically validating proposed tasks against pitch.md No-gos and Non-Goals to block mid-build scope creep.
- HOW: 1. Inspect the active pitch document (pitch.md), focusing specifically on ## No-gos and ## Non-Goals sections.
- live: no live URLs
- conflicts: none

### files/solo-levelling/.harness/skills/stakes-classifier/SKILL.md
- card: files/solo-levelling/.harness/skills/stakes-classifier/SKILL.md | part parts/13-deve-solo.md:752 | lines 42 | verdict Verified
- WHAT: Stakes Classifier skill (Workflow 8 in the 9 named workflows) classifying code paths or changes into HIGH, MEDIUM, or LOW stakes tiers to prescribe the mandatory review discipline before implementation begins.
- HOW: 1. Provide the proposed code change or feature description to the classifier.
- live: no live URLs
- conflicts: none

### files/solo-levelling/.harness/skills/unknown-first-sorter/SKILL.md
- card: files/solo-levelling/.harness/skills/unknown-first-sorter/SKILL.md | part parts/13-deve-solo.md:795 | lines 36 | verdict Verified
- WHAT: Unknown-First Sorter skill (Workflow 9 in the 9 named workflows) implementing Basecamp Shape Up Hill Chart methodology to sequence implementation scopes by uncertainty, enforcing Rule 7 by placing uphill work before downhill execution.
- HOW: 1. Supply candidate implementation scopes or features extracted from pitch.md.
- live: no live URLs
- conflicts: none

### files/solo-levelling/.harness/skills/working-backwards/SKILL.md
- card: files/solo-levelling/.harness/skills/working-backwards/SKILL.md | part parts/13-deve-solo.md:832 | lines 40 | verdict Verified
- WHAT: Working Backwards skill (Workflow 1 in the 9 named workflows) based on Amazon PR/FAQ product engineering principles, transforming initial bullet-point feature ideas into a one-page press release draft and an adversarial skeptical-customer critique.
- HOW: 1. Submit raw bullet-point idea to the working-backwards skill.
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/.harness/skills/01-repo-surveyor-map/SKILL.md
- card: files/solo-levelling/the harness/.harness/skills/01-repo-surveyor-map/SKILL.md | part parts/13-deve-solo.md:10543 | lines 178 | verdict Verified
- WHAT: Repo Surveyor & Architectural Mapping skill runbook enforcing Class-0 read-only discovery, bounded directory topology (depth <= 3), tech stack manifest detection, entrypoint identification, and REPO_MAP.md generation under a 2,000 token budget.
- HOW: Trigger on 'explore repo', 'map codebase', or 'understand architecture'
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/.harness/skills/02-git-worktree-isolation/SKILL.md
- card: files/solo-levelling/the harness/.harness/skills/02-git-worktree-isolation/SKILL.md | part parts/13-deve-solo.md:10853 | lines 112 | verdict Verified
- WHAT: Git Worktree Isolation skill runbook establishing isolated, zero-conflict filesystem worktrees linked to independent branches for speculative features, parallel agent workflows, and safe refactoring.
- HOW: Trigger on 'new feature', 'speculative change', 'isolate work', or 'git worktree'
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/.harness/skills/03-context-compaction-pruner/SKILL.md
- card: files/solo-levelling/the harness/.harness/skills/03-context-compaction-pruner/SKILL.md | part parts/13-deve-solo.md:11011 | lines 78 | verdict Verified
- WHAT: Context Compaction Pruner skill runbook establishing proactive memory compression, observation pruning, and conversational state distillation protocols to keep token utilization under 70% and prevent context rot.
- HOW: Trigger when conversation token count exceeds 28,000 tokens or prior to loading large files
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/.harness/skills/07-api-contract-first/SKILL.md
- card: files/solo-levelling/the harness/.harness/skills/07-api-contract-first/SKILL.md | part parts/13-deve-solo.md:11090 | lines 201 | verdict Verified
- WHAT: API Contract-First Design skill runbook mandating OpenAPI 3.1 and Protocol Buffers schema authoring, Spectral lint validation, and contract locking before backend or frontend code generation begins.
- HOW: Trigger on 'design api', 'draft openapi spec', 'create protobuf', or 'api contract first'
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/.harness/skills/08-database-schema-architect/SKILL.md
- card: files/solo-levelling/the harness/.harness/skills/08-database-schema-architect/SKILL.md | part parts/13-deve-solo.md:11292 | lines 156 | verdict Verified
- WHAT: Database Schema Architect skill runbook establishing normalized 3NF relational modeling, B-tree/GIN index optimization, and zero-downtime, non-blocking migration patterns (Alembic/Prisma).
- HOW: Trigger on 'design schema', 'create migration', or 'optimize database indexes'
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/.harness/skills/09-docker-sandbox-runner/SKILL.md
- card: files/solo-levelling/the harness/.harness/skills/09-docker-sandbox-runner/SKILL.md | part parts/13-deve-solo.md:11449 | lines 110 | verdict Verified
- WHAT: Docker & Sandbox Execution Runner skill runbook establishing procedures for dispatching untrusted commands and test suites through .harness/sandbox/gate.sh for credential masking and process isolation.
- HOW: Trigger on 'run command safely', 'sandbox execution', or 'isolated exec'
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/.harness/skills/11-litellm-router-admin/SKILL.md
- card: files/solo-levelling/the harness/.harness/skills/11-litellm-router-admin/SKILL.md | part parts/13-deve-solo.md:11684 | lines 175 | verdict Verified
- WHAT: LiteLLM Router Administration runbook governing model routing, failover configuration, token budget enforcement, and spend auditing across Claude, Gemini, OpenAI, and local models.
- HOW: Trigger on 'model routing', 'litellm', 'API gateway', or 'model fallback'
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/.harness/skills/21-tdd-red-green-refactor/SKILL.md
- card: files/solo-levelling/the harness/.harness/skills/21-tdd-red-green-refactor/SKILL.md | part parts/13-deve-solo.md:11860 | lines 58 | verdict Verified
- WHAT: TDD Red-Green-Refactor Loop skill runbook mandating test-first development where code changes require an initial failing test, minimal implementation to pass, and rigorous refactoring.
- HOW: Trigger on 'implement feature', 'fix bug', or 'add test'
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/.harness/skills/22-playwright-e2e-matrix/SKILL.md
- card: files/solo-levelling/the harness/.harness/skills/22-playwright-e2e-matrix/SKILL.md | part parts/13-deve-solo.md:11919 | lines 229 | verdict Verified
- WHAT: Playwright E2E Matrix skill runbook establishing deterministic, flake-free browser automation, resilient locator hierarchies, network mocking, and parallel test sharding.
- HOW: Trigger on 'e2e test', 'browser test', 'playwright', or 'UI automation'
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/.harness/skills/23-pytest-fixture-factory/SKILL.md
- card: files/solo-levelling/the harness/.harness/skills/23-pytest-fixture-factory/SKILL.md | part parts/13-deve-solo.md:12149 | lines 198 | verdict Verified
- WHAT: Pytest Fixture Factory skill runbook defining modular fixture architectures, precise fixture scoping, yield-based setup/teardown, transaction-isolated database testing, and parametrization.
- HOW: Trigger on 'pytest fixture', 'test setup', 'database fixture', or 'parametrize'
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/.harness/skills/26-systematic-rca/SKILL.md
- card: files/solo-levelling/the harness/.harness/skills/26-systematic-rca/SKILL.md | part parts/13-deve-solo.md:12348 | lines 101 | verdict Verified
- WHAT: Systematic Root Cause Analysis (RCA) skill runbook establishing a 5-phase scientific debugging methodology and 5-Whys causal chain analysis to resolve defects without speculative trial-and-error.
- HOW: Trigger on 'debug', 'error', 'failing test', or 'why is this broken'
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/.harness/skills/31-owasp-top10-vuln-scanner/SKILL.md
- card: files/solo-levelling/the harness/.harness/skills/31-owasp-top10-vuln-scanner/SKILL.md | part parts/13-deve-solo.md:12450 | lines 151 | verdict Verified
- WHAT: OWASP Top 10 Vulnerability Scanner skill runbook providing static application security testing (SAST) and code review procedures for SQLi, XSS, SSRF, IDOR, and broken auth.
- HOW: Trigger on 'owasp scan', 'security review', 'check sqli xss', or 'security audit'
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/.harness/skills/32-secrets-entropy-sanitizer/SKILL.md
- card: files/solo-levelling/the harness/.harness/skills/32-secrets-entropy-sanitizer/SKILL.md | part parts/13-deve-solo.md:12602 | lines 98 | verdict Verified
- WHAT: Secrets & High-Entropy Sanitizer skill runbook governing pre-commit credential scanning, Shannon entropy heuristics, and secret redaction to prevent high-entropy tokens from entering version control.
- HOW: Trigger on 'check for secrets', 'credential scan', or 'secret leak'
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/.harness/skills/35-cryptography-safe-patterns/SKILL.md
- card: files/solo-levelling/the harness/.harness/skills/35-cryptography-safe-patterns/SKILL.md | part parts/13-deve-solo.md:12756 | lines 204 | verdict Verified
- WHAT: Cryptography Safe Patterns skill runbook establishing mandatory modern cryptographic standards (AES-256-GCM, Argon2id, Ed25519) and prohibiting deprecated algorithms (MD5, SHA1, DES, ECB mode).
- HOW: Trigger on 'encrypt', 'hash password', 'sign data', or 'crypto'
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/.harness/skills/36-grill-me-socratic-planner/SKILL.md
- card: files/solo-levelling/the harness/.harness/skills/36-grill-me-socratic-planner/SKILL.md | part parts/13-deve-solo.md:12961 | lines 115 | verdict Verified
- WHAT: Grill-Me Socratic Planner skill runbook governing structured requirements interviews and edge-case probing before code implementation begins, eliminating hallucinated assumptions.
- HOW: Trigger on 'plan this', 'clarify requirements', or 'interview me'
- live: no live URLs
- conflicts: none

### files/deve/.harness/skills/alternatives-generator/SKILL.md
- card: files/deve/.harness/skills/alternatives-generator/SKILL.md | part parts/13-deve-solo.md:38664 | lines 43 | verdict Verified
- WHAT: Prompt skill forcing generation of 2-3 genuinely viable technical alternatives before any design decision, with mechanism/pros/cons/why-reject per alternative; self-certification blocked so the human must personally commit and log rejections.
- HOW: Invoke before committing to any design decision, new dependency, data schema, or architecture choice.
- live: no live URLs
- conflicts: Workflow alternatives-generator.yaml invokes skill 'alternatives-brainstorm', which does not match this frontmatter name 'alternatives-generator'.

### files/deve/.harness/skills/failure-mode-analyzer/SKILL.md
- card: files/deve/.harness/skills/failure-mode-analyzer/SKILL.md | part parts/13-deve-solo.md:38708 | lines 37 | verdict Verified
- WHAT: Prompt skill that, before integrating any external API/service/queue/DB boundary, produces a top-3 failure-mode matrix: exact mechanism, user-visible impact, prevent-vs-tolerate strategy, and a concrete local test simulation; the human decides prevention vs tolerance.
- HOW: Run before integrating any third-party API, external service, persistent queue, DB driver, or distributed boundary.
- live: no live URLs
- conflicts: Workflow failure-mode-analyzer.yaml invokes skill 'failure-mode-analysis', which does not match this frontmatter name 'failure-mode-analyzer'.

### files/deve/.harness/skills/fcar-reviewer/SKILL.md
- card: files/deve/.harness/skills/fcar-reviewer/SKILL.md | part parts/13-deve-solo.md:38746 | lines 38 | verdict Verified
- WHAT: Fresh Context Adversarial Review skill: a verbatim binary pass/fail reviewer prompt over a 5-item locked rubric (sourced claims, 2+ non-goals, named sources, measurable metric, 1+ rejected alternative). Must run in a fresh context; same-session review is reviewer collusion.
- HOW: Write the rubric BEFORE the artifact is complete.
- live: no live URLs
- conflicts: Skill name 'fcar-reviewer' vs workflow 'fcar-review.yaml'; verify.sh has an explicit case-mapping for this mismatch, confirming it as known., The prompt here, os/fcar-rubric.md and os/gates.md carry three near-identical rubric copies, a drift risk.

### files/deve/.harness/skills/launch-checklist-runner/SKILL.md
- card: files/deve/.harness/skills/launch-checklist-runner/SKILL.md | part parts/13-deve-solo.md:38785 | lines 51 | verdict Verified
- WHAT: Gate 6 skill verifying an 8-item pre-deploy checklist (monitoring, latency alert, staged rollback actually executed, dependency error handling, clean secret scan, adversarial auth test, 2x load test, postmortem template ready) and requiring a pre-committed rollback threshold before deploy; the human signs off on waivers.
- HOW: Run before ANY production deployment or customer-facing release.
- live: no live URLs
- conflicts: The skill lists 8 items plus two extra verifications (rollback threshold, rollback command); the launch-checklist template embeds the threshold as a preamble, so the tally differs slightly between skill and template.

### files/deve/.harness/skills/postmortem-opener/SKILL.md
- card: files/deve/.harness/skills/postmortem-opener/SKILL.md | part parts/13-deve-solo.md:38837 | lines 30 | verdict Verified
- WHAT: Incident skill generating a 3-section blameless postmortem (timeline, Five Whys root-cause chain to a systemic flaw, corrective-actions table with owners/due dates) using the postmortem template; the human must commit corrective actions to the task list.
- HOW: Trigger within 48 hours of any production incident, data corruption, or major outage.
- live: no live URLs
- conflicts: none

### files/deve/.harness/skills/scope-gate/SKILL.md
- card: files/deve/.harness/skills/scope-gate/SKILL.md | part parts/13-deve-solo.md:38868 | lines 35 | verdict Verified
- WHAT: Workflow 2 skill checking a proposed task against the pitch's No-gos/Non-Goals, calling scripts/scope-check.py (or semantic comparison), and issuing a hard BLOCK on overlap with two allowed resolutions: drop the task or explicitly amend the pitch.
- HOW: Run whenever a new feature/task is proposed during an active build cycle, before adding it to the implementation list.
- live: no live URLs
- conflicts: The skill's semantic comparison is stronger than the automated checker: scripts/scope-check.py is token-overlap only with a documented synonym false-negative, so the 'automated gate' can miss conflicts the prompt would catch.

### files/deve/.harness/skills/stakes-classifier/SKILL.md
- card: files/deve/.harness/skills/stakes-classifier/SKILL.md | part parts/13-deve-solo.md:38904 | lines 42 | verdict Verified
- WHAT: Workflow 8 skill classifying a code path/change as HIGH/MEDIUM/LOW stakes before implementation, returning a definite tier, one specific reason, the required review process, and one specific concern. HIGH covers money/auth/irreversible-data/crypto/silent-bug paths; MEDIUM covers external APIs/retry/input validation; LOW covers UI-only/full-coverage utilities/config/docs.
- HOW: Run before implementing any code path.
- live: no live URLs
- conflicts: none

### files/deve/.harness/skills/unknown-first-sorter/SKILL.md
- card: files/deve/.harness/skills/unknown-first-sorter/SKILL.md | part parts/13-deve-solo.md:38947 | lines 36 | verdict Verified
- WHAT: Workflow 9 skill sorting implementation scopes into UPHILL (uncertain/novel/unverified) and DOWNHILL (known/routine), sequencing all uphill scopes first and naming a derisking spike per uphill scope (Shape Up hill-chart method).
- HOW: Run at kickoff of any implementation cycle, before writing application code.
- live: no live URLs
- conflicts: none

### files/deve/.harness/skills/working-backwards/SKILL.md
- card: files/deve/.harness/skills/working-backwards/SKILL.md | part parts/13-deve-solo.md:38984 | lines 40 | verdict Verified
- WHAT: Workflow 1 skill turning a bullet-point idea into a one-page PR/FAQ press release using the prfaq template plus a harsh skeptical-customer challenge (numbered specific objections); 'a gentle review is a failed review'.
- HOW: Run at the start of any new project/idea/feature, before a pitch is written.
- live: no live URLs
- conflicts: none

