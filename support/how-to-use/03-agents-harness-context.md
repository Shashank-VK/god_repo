# Agents, harness, context

By lifecycle stage.

### files/opencode-research/BUILD-PROMPT-FINAL.md
- card: files/opencode-research/BUILD-PROMPT-FINAL.md | part parts/04-opencode-build-prompts.md:1 | lines 2261 | verdict Verified
- WHAT: The OpenCode Autonomous Agent Toolkit Final Consolidated Build Phases: authoritative master build specification and prompt sequence (Phases 1 through 5, gate checks, architecture invariants, and 160+ tool catalog) for constructing an enterprise-grade autonomous coding agent harness in RULES. Integrates walkinglabs durable session state templates (AGENTS.md, feature_list.json, claude-progress.md, i
- HOW: 1. Pre-build gate: verify RULES/ workspace is empty (contains only audits/), harness-templates exist, and Node.js/npx are available.
- live: no live URLs
- conflicts: loop init destructive overwrite: running npx @cobusgreyling/loop init overwrites existing AGENTS.md; build prompt prescribes immediate restoration from opencode-research/harness-templates/AGENTS.md followed by re-appending the Autonomy Boundary., loopy global directory containment breach: npx skills add installs loopy into ~/.agents/skills/loopy outside project boundaries; resolved by moving skill into RULES/.agents/skills/loopy and creating a Windows directory junction or symlink., Superpowers interactive loop incompatibility: obra/superpowers interactive Q&A workflow conflicts with autonomous Layer 2 loop execution; designated strictly as Layer 1 manual tool., Astryx MCP non-existence: Astryx lacks an MCP server; attempts to configure MCP fail; harness must invoke @astryxdesign/cli via bash tool execution., Persistent memory mutual exclusivity: tickernelz/opencode-mem (local vector DB with web UI) and thedotmack/claude-mem (semantic session compression) cannot be co-installed without context duplication; harness enforces strict either/or selection., Manual evidence propagation gap in loopy: Forward-Future/loopy does not automatically push run receipts to feature_list.json evidence[]; agent must manually copy run receipts prior to completion., Playwright MCP configuration collision: playwright init-agents auto-injects playwright-test MCP block into opencode.json; harness instructions ensure both playwright and playwright-test blocks are merged without truncation.

### files/opencode-research/BUILD-PROMPT-UNIVERSAL.md
- card: files/opencode-research/BUILD-PROMPT-UNIVERSAL.md | part parts/04-opencode-build-prompts.md:2263 | lines 2072 | verdict Verified
- WHAT: Universal phase-gated autonomous AI coding agent harness build prompt (Pre-build gate check, Phases 1 through 5, post-build verification, first real task execution, and locked architecture reference) designed to construct an autonomous-but-bounded development environment inside a target workspace (RULES/) across any host agent tool (OpenCode, Claude Code, Codex, or untested CLIs) via an initial To
- HOW: Execute Phase 1 Part 1A (Tool Discovery Protocol) first in every session to detect tool identity, skills path (.agents/skills/), command path, MCP config format, and intercept hooks before modifying files.
- live: no live URLs
- conflicts: Loop init clobbers custom AGENTS.md, requiring mandatory manual restoration and re-appending of the Autonomy Boundary., Astryx was previously hallucinated as an MCP server; verified as CLI bash tool only (@astryxdesign/cli)., Loop-engineering package name was previously misidentified; verified as @cobusgreyling/loop., Loopy installation default places files outside project containment, requiring junction/symlink resolution into .agents/skills/loopy., Native tool-call interception hooks vary across agent environments (OpenCode plugin vs Claude Code settings.json vs unsupported in Codex), making the git pre-commit hook the only truly universal hard gate., Playwright agent loop flag is agent-specific (--loop=opencode, --loop=claude) and unsupported in tools like Codex., Loopy does not automatically transfer execution run receipts to feature_list.json evidence[], requiring explicit manual propagation by the agent before commit.

### files/opencode-research/research/07-autonomous-agent-architecture.md
- card: files/opencode-research/research/07-autonomous-agent-architecture.md | part parts/03-opencode-research-phases.md:1272 | lines 342 | verdict Verified
- WHAT: Autonomous agent orchestration architecture specification for OpenCode (Phase 6, locked post-Q1 through Q5 decisions with Phase 8 corrections): establishes a 3-layer orchestration stack (scaffolding/governance via cobusgreyling/loop-engineering, bounded loop design via Forward-Future/loopy skill, and session state via walkinglabs as the sole source of truth), defines the two-tier Autonomy Boundary
- HOW: Scaffold governance and audit tools using cobusgreyling/loop-engineering (loop init, loop doctor, loop-audit, loop-gate, loop-context)
- live: no live URLs
- conflicts: State duplication conflict: huangruiteng/loopx maintains separate state stores (.loopx/, .codex/goals/, .local/) with no bridge to walkinglabs; excluded to maintain walkinglabs as sole state truth., State duplication conflict: cobusgreyling/goal-engineering uses GOAL.md which duplicates feature_list.json and claude-progress.md; excluded., Naming conflict: /goal command name collides with Grok Build CLI and OpenAI Codex native mechanics; replaced by /idea., Tooling protocol mismatch: Astryx has no MCP server; attempting to configure in opencode.json MCP will fail; must be invoked via bash CLI., Receipt propagation gap: loopy run receipts do not automatically write into feature_list.json evidence[]; agent manual copy required.

### files/opencode-research/research/08-pre-commit-hook.md
- card: files/opencode-research/research/08-pre-commit-hook.md | part parts/03-opencode-research-phases.md:1961 | lines 204 | verdict Verified
- WHAT: Phase 8 Task 3 architectural disambiguation and reference implementation for the Definition of Done (DoD) pre-commit hook: compares Option A (native Git .git/hooks/pre-commit shell script) against Option B (OpenCode plugin hook tool.execute.before in .opencode/plugins/dod-gate.ts); establishes a dual-layer enforcement model where the native Git pre-commit script acts as the authoritative hard, too
- HOW: Primary hard gate: Install executable bash script at .git/hooks/pre-commit (chmod +x); script reads feature_list.json via Node.js, checks for active features with status in_progress or blocked, and exits 1 with explanatory message if found (overrideable only via explicit git commit --no-verify)
- live: no live URLs
- conflicts: Architecture doc specifies pre-commit hook ambiguously between Git native hook and OpenCode plugin hook; analysis resolves this by proving OpenCode plugin hooks are flaky/inactive in headless/terminal/CI environments and mandating Git hook as the authoritative hard gate with OpenCode plugin hook as secondary advisory.

### files/opencode-research/harness-templates/AGENTS.md
- card: files/opencode-research/harness-templates/AGENTS.md | part parts/04-opencode-build-prompts.md:4336 | lines 56 | verdict Verified
- WHAT: AGENTS.md long-running coding-agent contract: 6-step startup workflow (pwd, read claude-progress.md, read feature_list.json, git log -5, run init.sh, run verification), one-feature-at-a-time working rules, required artifacts, evidence-gated Definition of Done, and 5-step end-of-session checklist leaving repo restartable.
- HOW: Copy AGENTS.md to project root as-is or adjusted to local conventions
- live: no live URLs
- conflicts: none

### files/opencode-research/harness-templates/init.sh
- card: files/opencode-research/harness-templates/init.sh | part parts/04-opencode-build-prompts.md:4509 | lines 30 | verdict Verified
- WHAT: Standard bash startup/verification script (set -euo pipefail): cds to repo root, runs configurable INSTALL_CMD and VERIFY_CMD arrays, prints START_CMD, and execs the app only when RUN_START_COMMAND=1; top three variables are the per-project customization point.
- HOW: Set INSTALL_CMD, VERIFY_CMD, START_CMD arrays at the top to project commands
- live: no live URLs
- conflicts: none

### files/God research/B-category-catalogs/11-agents.md
- card: files/God research/B-category-catalogs/11-agents.md | part parts/05-firstpass-B-catalogs.md:4640 | lines 518 | verdict Partially
- WHAT: Coding Agents Catalog 11: comprehensive taxonomy and specification of 25 coding agents, extension systems, and cross-cutting harness primitives verified as of 2026-10-09. Details 10 core coding agents (OpenCode terminal/desktop/IDE OSS agent, Claude Code Anthropic reference CLI/IDE agent, Cursor AI-native IDE agent, OpenAI Codex Rust CLI/cloud/SDK agent, Gemini CLI open-source agent with Antigravi
- HOW: 1. Cross-Harness Instruction Authoring: Create a root AGENTS.md file to establish vendor-neutral instructions automatically discovered and respected across OpenCode, Cursor, Windsurf, Cline, Codex, and Claude Code.
- live: no live URLs
- conflicts: Roo Code official extension was shut down on 2026-05-15; community fork ZooCode or Cline recommended for active development., Continue.dev was acquired by Cursor/Anysphere in June 2026, and its GitHub repository was made read-only., Gemini CLI unpaid/Google-One consumer tier migrated to Antigravity CLI on 2026-06-18., Subagent permission inheritance varies significantly across harnesses: Claude Code inherits parent permission modes unless constrained, whereas OpenCode enforces separate per-subagent permission definitions., Aider relies on git-native workflows and repository map AST indexing with tree-sitter rather than native first-party MCP host integrations.

### files/God research/B-category-catalogs/12-multi-agent.md
- card: files/God research/B-category-catalogs/12-multi-agent.md | part parts/05-firstpass-B-catalogs.md:5159 | lines 480 | verdict Partially
- WHAT: Comprehensive 2026 multi-agent catalog and architectural guide covering 22 resources categorized into subagent runtime primitives, enterprise frameworks, peer protocols, and multi-agent coordination patterns. Primitives and runtimes include Claude Agent Teams and subagents (.claude/agents/*.md with permissionMode and background sessions), OpenCode subagents (v2 modes primary/subagent/all with inde
- HOW: 1. Distinguish runtime class before deployment: Verify whether multi-agent delegation executes in a real runtime (independent OS processes, fresh context windows, isolated tool sandboxes, and per-session permission checks) or single-model roleplay (simulated in a single chat transcript); enforce rea
- live: no live URLs
- conflicts: Real runtime vs Single-model roleplay: Single-model roleplay simulates multiple roles (e.g. MetaGPT SOP prompts, Act as 3 reviewers) inside a single context window without execution isolation, tool sandboxing, or independent memory; real runtimes enforce process/session boundaries, distinct permission models, separate context limits, and auditable tool execution traces., A2A Protocol vs Model Context Protocol (MCP): MCP operates inside the agent as an agent-to-tool bus for local resources and tool invocation, whereas A2A standardizes communication between agents across organizational and network boundaries with AgentCard discovery (/.well-known/agent.json) and task lifecycle states; while MCP can be adapted for agent delegation (e.g. Codex-as-MCP-server), A2A provides formal multi-agent task contracts., Orchestrator Fan-Out Storms and Coordination Overhead: Anthropic research demonstrates that unconstrained subagent spawning leads to 50-subagent storms, redundant searches, and degraded synthesis; strict subagent budgeting, scoped briefs, and structured citation requirements are necessary to realize breadth-first speedups without token runaway., Adversarial Sabotage Amplification: Multi-agent orchestration architectures can amplify adversarial sabotage (empirical studies demonstrate sabotage rates escalating from 0% in single agents to 94% across 3 agents when naive orchestrators uncritically relay disable-monitoring or shutdown instructions); strict tool allowlists, human-in-the-loop approvals, and prompt isolation are mandatory., AutoGen Maintenance vs Microsoft Agent Framework (MAF): AutoGen 0.4 is in maintenance-only status; enterprise and greenfield multi-agent deployments under the Microsoft ecosystem have converged on Microsoft Agent Framework (MAF 1.0) and Semantic Kernel., Framework Level of Abstraction (CrewAI vs LangGraph): CrewAI provides high-level role-oriented abstractions (Crews, Flows, Tasks) with Pydantic typing, whereas LangGraph provides low-level deterministic cyclic state graphs (StateGraph) with explicit nodes, edges, and checkpointers; choosing between them requires balancing developer ergonomics against granular state-machine control.

### files/God research/B-category-catalogs/13-harness.md
- card: files/God research/B-category-catalogs/13-harness.md | part parts/05-firstpass-B-catalogs.md:5640 | lines 479 | verdict Verified
- WHAT: Comprehensive catalog and architectural inventory of 23 agent harness systems, execution controls, isolation primitives, and verification patterns audited as of 2026-10-09. Spans 10 foundational control areas: (1) Spec-Driven Development engines (GitHub Spec Kit specify-cli, OpenSpec OPSX deltas, Conductor for Gemini CLI/Claude, and AIDE/Canon/Product-Forge workflows); (2) Feature tracking and tas
- HOW: 1. Spec-Driven Scaffolding: Initialize project specs using Spec Kit (specify init <project> --integration <agent>) or OpenSpec (openspec init); execute feature flows with slash commands (/specify, /plan, /tasks, /implement, /converge or /opsx:explore, /propose, /apply, /verify, /archive).
- live: no live URLs
- conflicts: Prompt vs deterministic enforcement gap: Spec files and system prompts provide steering but cannot enforce policy; hard boundaries require OS-level sandboxes, PreToolUse hooks, and pre-commit verification., Worktree shared-state leakage: Git worktrees share the underlying .git object database and local CoW caches (node_modules, target); untrusted code execution requires containerized isolation beyond local worktrees., Turn-level checkpointing scope limitations: Native agent checkpoints (/rewind, /undo) capture foreground file edits but fail to track concurrent subagent edits, external process mutations, or background daemons, requiring git-level branch tracking for complete rollback fidelity., Git AI attribution boundaries: Tool result outputs and bulk file movements (git mv) can create attribution tracking gaps unless filtered and captured via dedicated agent-v1 presets., Self-improving memory risks: Unreviewed automatic persistence of instructions from execution transcripts into long-term agent memory or routines introduces susceptibility to indirect prompt injection.

### files/God research/atlas/catalogs/03b-agents.md
- card: files/God research/atlas/catalogs/03b-agents.md | part 08-atlas-33.md | lines 885 | verdict Partially
- WHAT: Comprehensive catalog of 15 ready-made coding agents (Claude Code, Cursor, OpenAI Codex CLI, Antigravity CLI, GitHub Copilot CLI, Windsurf/Devin Desktop, Cline, Roo Code, Aider, Amp, Factory Droid, Kimi Code, Pi, OpenCode cross-ref, Gemini CLI historical) plus 1 host-surface record (VS Code Marketplace), 1 legacy alias note (Kimi CLI), 5 emerging agents (Qwen Code, Crush, Kilo Code, Goose, Continu
- HOW: Reference agent capabilities when selecting or comparing coding agents
- live: https://code.claude.com/docs/en/plugins; https://cursor.com/docs/context/rules; https://developers.openai.com/codex/skills; https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli; https://docs.windsurf.com/windsurf/cascade/memories; https://docs.cline.bot/; https://roocodeinc.github.io/Roo-Code/features/custom-modes/; https://ampcode.com/manual; https://github.com/Moonsho
- conflicts: Amp editor-integration status: Feb 2026 CLI-only pivot reports vs current manual showing web/macOS/iOS/CLI (Unresolved), Pi Rust rewrite (noeljackson/pi) relationship to earendil-works/pi (Unresolved), Crush license: MIT vs FSL-1.1-MIT across sources (Unresolved), ~/.cursor/commands user-level path: community-reported but no official doc captured (Unresolved), Kimi Code swarm scale claim (300 sub-agents) from single secondary source (Unverified)

### files/God research/atlas/catalogs/05a-orchestration.md
- card: files/God research/atlas/catalogs/05a-orchestration.md | part parts/08-atlas-33.md:21544 | lines 1400 | verdict Partially
- WHAT: Omniscient Resource Atlas Catalog 05a: comprehensive research catalog covering Multi-Agent Systems & Orchestration (Part 9) and Harness Engineering & Autonomous Software Development (Part 10) across 57 cataloged resources. Subsections include: General multi-agent frameworks (LangGraph directed graph runtime with durable execution and HITL; Microsoft AutoGen in maintenance mode since Oct 2025; AG2 
- HOW: 1. Multi-agent framework selection: For complex stateful graphs with cyclic loops, checkpoints, and human approvals, use LangGraph; for lightweight handoff/routing swarms, use OpenAI Agents SDK; for enterprise multi-runtime Azure environments, migrate from AutoGen to Microsoft Agent Framework; for A
- live: no live URLs
- conflicts: Microsoft AutoGen moved to maintenance mode on 2025-10-02; PyPI package autogen is owned by the AG2 community fork, while Microsoft official successor is Microsoft Agent Framework (MAF)., ACP protocol name collision: IBM ACP (archived/merged into A2A Aug 2025) vs Commerce ACP (OpenAI/Stripe REST API Feb 2026) vs Zed Agent Client Protocol vs AGNTCY Agent Connect Protocol (archived Apr 2026)., SWE-agent officially superseded by mini-SWE-agent (~100-line bash ReAct loop) which achieved 65% on SWE-bench Verified with Claude 3.7 Sonnet., SWE-bench Verified is widely acknowledged as contaminated by training data overlap, requiring evaluation migration to SWE-bench Pro, SWE-bench Live, and SWE-rebench V2., MetaGPT repository migrated from geekan/MetaGPT to FoundationAgents/MetaGPT, with core team focusing on commercial MGX platform and open-source repo experiencing reduced commit frequency., Langfuse cost tracking only prices generation and embedding spans by design; tool execution and agent orchestration spans are unpriced, creating visibility gaps.

### files/God research - gemini/04-agents-harness-context.md
- card: files/God research - gemini/04-agents-harness-context.md | part parts/09-gemini-secondpass-6.md:2190 | lines 910 | verdict Verified
- WHAT: Comprehensive reference catalog and system architecture analysis of 68 resources across four core layers of AI-assisted software engineering: (1) Coding Agents & Extension Architectures (OpenCode, Claude Code, Cursor, Codex CLI, Gemini CLI/Antigravity, Copilot, Windsurf, Cline, Roo Code, Aider, MCP, SKILL.md, AGENTS.md, Claude Agent SDK, Cursor Rules, OpenCode permission schema, Cline/Roo custom m
- HOW: 1. Enforce Real Runtime Isolation: Spawn multi-agent subagents in isolated processes or execution sessions with independent context windows and scoped tool permissions so noisy child traces (build failures, grep logs) do not pollute the parent context window.
- live: no live URLs
- conflicts: Real Runtimes vs Roleplay: Industry consensus establishes that single-model roleplay (e.g., MetaGPT prompt simulation) lacks process/memory isolation and suffers persona bleeding, whereas real runtimes (Claude Subagents, OpenCode, LangGraph) enforce physical context firewalls., Microsoft AutoGen governance: Original AutoGen entered maintenance mode with PyPI autogen managed by AG2 community fork, while Microsoft official runtime shifted to Microsoft Agent Framework (MAF)., Dense Vector limitations for code: Pure dense vector search fails on exact compiler error codes and AST symbol hierarchies, necessitating hybrid Tree-sitter/BM25/vector pipelines.

### files/God research/agy-pass/04-agents-harness-context.md
- card: files/God research/agy-pass/04-agents-harness-context.md | part parts/10-agy-thirdpass-7.md:2683 | lines 638 | verdict Verified
- WHAT: Third-pass engineering research compendium on autonomous coding agents, multi-agent runtimes, harness engineering, and context/memory architectures. Details 9 modern coding agents (OpenCode, Claude Code, Cursor, Codex/Canvas, Gemini CLI/Antigravity, Copilot, Windsurf, Cline, Roo Code); contrasts true distributed multi-agent runtimes (process isolation, separate context windows, event-driven async 
- HOW: 1. Agent Selection & Routing: Route tasks dynamically using Tiered Model Routing (cheap models like Gemini Flash/Haiku for file search and symbol extraction; frontier models like Claude Sonnet/OpenAI o1/o3-mini for architectural synthesis and root-cause debugging).
- live: no live URLs
- conflicts: Single-Model Roleplay vs Distributed Multi-Agent: Roleplay accumulates quadratic context tokens O(N^2) and propagates hallucinations across turns, whereas true multi-agent runtimes enforce isolated process boundaries, least-privilege tool binding, and linear token scaling., Dense Vector Search vs Exact Code Retrieval: Dense embeddings fail on exact variable names and hexadecimal error codes, necessitating hybrid search combining dense vectors with sparse BM25 via Reciprocal Rank Fusion (RRF).

### files/God research/agy-pass/05-infra-ops.md
- card: files/God research/agy-pass/05-infra-ops.md | part parts/10-agy-thirdpass-7.md:3322 | lines 614 | verdict Verified
- WHAT: Authoritative engineering reference manual for infrastructure and operations across 7 operational pillars, detailing 131 verified resources. Features an architectural deep dive contrasting enforceable isolation (CPU hardware virtualization, seccomp-bpf, Wasm linear memory, gVisor Sentry interception, Firecracker microVMs) against non-enforceable prompt-only controls (system prompts, Llama Guard, N
- HOW: 1. Enforceable Isolation Enforcement: For untrusted code execution or autonomous agent shells, mandate Tier 4 (gVisor runsc) or Tier 5 (AWS Firecracker / Kata Containers) sandboxing; never rely on Tier 0 system prompts or guardrail classifiers for security boundaries.
- live: no live URLs
- conflicts: Prompt-Only Controls vs Enforceable Sandboxing: System prompts and classifier guardrails operate on stochastic linguistic probabilities and fail under direct/indirect prompt injection, whereas hardware virtualization (KVM/Firecracker) and syscall filtering (seccomp/gVisor) provide mathematically and kernel-enforced isolation invariants., Standard Container Security vs MicroVMs: Standard Docker containers share the host Linux kernel, leaving hosts vulnerable to kernel zero-days (e.g. Dirty COW, io_uring escapes), whereas MicroVMs (Firecracker) provide dedicated guest kernels and isolated memory page tables.

### files/God research/_state/resource-index.json
- card: files/God research/_state/resource-index.json | part parts/12-diffs-adjudication.md:974 | lines 1 | verdict Verified
- WHAT: JSON resource index mapping 45 foundational tools, frameworks, and repositories across Sections A-E and research phases (Phase 2, 3, 4A, 4C, 5, 8). Tracks canonical repository names, categories, target URLs, and historical prior statuses (e.g. facebook/astryx CLI-only no-MCP, ruvnet/ruflo ex-Claude-Flow, emilkowalski/skills voice-to-text fix, teng-lin/notebooklm-py unofficial RPC, vercel-labs/deep
- HOW: Load and parse resource-index.json as structured JSON to resolve canonical repository URLs and historical verification decisions.
- live: no live URLs
- conflicts: facebook/astryx verified as CLI-only with no MCP server support., gsd-build/get-shit-done archived June 2026 due to security issues; replaced by live community fork open-gsd/gsd-core., ruvnet/ruflo confirmed as canonical identity succeeding Claude Flow., okjpg/llm-council confirmed not found / unverified, suspected voice-to-text error for karpathy/llm-council.

### files/solo-levelling/AGENTS.md
- card: files/solo-levelling/AGENTS.md | part parts/13-deve-solo.md:2448 | lines 51 | verdict Verified
- WHAT: Agent governance registry and operating contract for the Solo AI Product Engineering System, codifying agent roles, autonomous loop constraints (max_steps=15, state debounce, ECT termination), 6-gate execution lifecycle, and historical fleet provenance.
- HOW: 1. Place at repository root as AGENTS.md to configure agent runtime rules.
- live: no live URLs
- conflicts: none

### files/solo-levelling/GOD_PROMPT.md
- card: files/solo-levelling/GOD_PROMPT.md | part parts/13-deve-solo.md:2564 | lines 1935 | verdict Verified
- WHAT: Master bootstrapping prompt and self-contained specification that scaffolds the entire Solo AI Product Engineering Operating System and AI Development Harness, including directory trees, governance files, skills, templates, Taskfile, lefthook, and verification scripts.
- HOW: 1. Paste into a fresh workspace to automatically generate all governance files, directories, templates, scripts, and skills.
- live: no live URLs
- conflicts: none

### files/solo-levelling/Taskfile.yml
- card: files/solo-levelling/Taskfile.yml | part parts/13-deve-solo.md:4500 | lines 77 | verdict Verified
- WHAT: Task runner configuration (Task v3) defining automated quality gates, project initialization, testing, linting, secret scanning, and launch verification tasks for the Solo AI Product Engineering Harness.
- HOW: 1. Install Task via official taskfile.dev instructions.
- live: https://taskfile.dev
- conflicts: none

### files/solo-levelling/lefthook.yml
- card: files/solo-levelling/lefthook.yml | part parts/13-deve-solo.md:8333 | lines 15 | verdict Verified
- WHAT: Git hook configuration utilizing Lefthook to enforce automated secret scanning, Python syntax compilation on staged files, and full verification gate checks before git push.
- HOW: 1. Install lefthook and run `lefthook install` to configure Git hooks.
- live: no live URLs
- conflicts: none

### files/solo-levelling/.env.template
- card: files/solo-levelling/.env.template | part parts/13-deve-solo.md:14 | lines 13 | verdict Verified
- WHAT: Environment variable template defining required configuration keys for AI model APIs (Anthropic, Google AI) and production monitoring DSN, while safeguarding against credential leakage.
- HOW: 1. Copy .env.template to .env in repository root: `cp .env.template .env`.
- live: no live URLs
- conflicts: none

### files/solo-levelling/os/lifecycle.md
- card: files/solo-levelling/os/lifecycle.md | part parts/13-deve-solo.md:8709 | lines 54 | verdict Verified
- WHAT: Complete product development lifecycle sequence for the Solo AI Product Engineering System, defining the 6 linear stages (Idea -> Pitch -> Design -> Implementation -> Launch -> Postmortem) with strict inputs, outputs, gate criteria, and empirical company citations.
- HOW: Execute stage 1 (Idea/PRFAQ) using Amazon PR/FAQ principles to establish customer clarity
- live: no live URLs
- conflicts: none

### files/solo-levelling/projects/.gitkeep
- card: files/solo-levelling/projects/.gitkeep | part parts/13-deve-solo.md:8990 | lines 1 | verdict Verified
- WHAT: Gitkeep marker maintaining the projects/ directory structure for subproject workspaces within the Solo AI Product Engineering System repository.
- HOW: Initialize new product workspaces inside projects/<project-name> using os/ templates and scripts
- live: no live URLs
- conflicts: none

### files/solo-levelling/.harness/README.md
- card: files/solo-levelling/.harness/README.md | part parts/13-deve-solo.md:28 | lines 27 | verdict Verified
- WHAT: Architecture index and operational manifest for the Solo AI Product Engineering System v1.0 (.harness/); maps key harness directories (config, hooks, permissions, sandbox, telemetry, mcp, skills, workflows) and defines non-negotiable safety and governance principles including security-first pre-tool guard (SC-07), loop rails max_steps=15 with IAL debounce (Phase 16), deadlock-free ABAC requiring h
- HOW: Use as the master onboarding directory and manifest for the .harness/ tree.
- live: no live URLs
- conflicts: README table lists telemetry/litellm-config.yaml, but only 9 skills and 8 workflow definitions are present across the assigned trees.

### files/solo-levelling/.harness/config/harness.yaml
- card: files/solo-levelling/.harness/config/harness.yaml | part parts/13-deve-solo.md:56 | lines 52 | verdict Verified
- WHAT: Master harness configuration binding loop engineering rails (global max_steps=15, debounce_identical_calls=true, require_deterministic_termination=true, self_certification_blocked=true), OS lifecycle gates 1-6 with mandatory Gate 4 FCAR, 9 enabled workflows, telemetry routing to litellm-config.yaml with hard budget enforcement, and security pointers (pre_tool_guard.py, secret-scan.sh, policies.ced
- HOW: Load at agent session initialization to apply global loop limits and safety rails.
- live: no live URLs
- conflicts: Configuration specifies telemetry budget_enforcement as 'hard', whereas underlying scripts may only log warnings without an active LiteLLM proxy.

### files/solo-levelling/.harness/hooks/hooks.json
- card: files/solo-levelling/.harness/hooks/hooks.json | part parts/13-deve-solo.md:109 | lines 46 | verdict Verified
- WHAT: Lifecycle interceptor manifest declaring three pre-tool hooks ('security-guard' executing pre_tool_guard.py with throw_fatal_error on block/error; 'checkpoint-before-destructive' triggering human approval [Y/n] on write_file, git commit/push, deploy, kubectl apply; 'ial-debounce' raising fatal error on consecutive identical tool+args) and one post-tool hook ('secret-scan-after-write' running scrip
- HOW: Intercept agent tool calls prior to execution and run enabled pre_tool_hooks.
- live: no live URLs
- conflicts: Trigger patterns mix tool names (write_file) with bash prefix commands (bash:git commit, bash:deploy), requiring dispatch normalization in the harness runner.

### files/solo-levelling/.harness/hooks/pre_tool_guard.py
- card: files/solo-levelling/.harness/hooks/pre_tool_guard.py | part parts/13-deve-solo.md:156 | lines 89 | verdict Verified
- WHAT: Pre-tool Python security guard enforcing zero-false-positive regex blocking on command invocations (bash, shell, run_command, execute); blocks recursive/force rm on system paths (/etc, /usr, /var, /home, /root, /sys, /proc, ~/), quoted rm force flags, -- flag injection, piped script execution (curl/wget piped to bash/python), git force-push to main/master, AWS STS temporary keys (ASIA...), and unq
- HOW: Pipe JSON payload {'tool': '<name>', 'args': {...}} into stdin of pre_tool_guard.py prior to tool dispatch.
- live: no live URLs
- conflicts: Fails open (exit 0) on JSON parse or unexpected runtime exceptions, which prioritizes workflow continuity over strict fail-closed security.

### files/solo-levelling/.harness/permissions/presets.json
- card: files/solo-levelling/.harness/permissions/presets.json | part parts/13-deve-solo.md:429 | lines 38 | verdict Verified
- WHAT: Role-based tool access presets defining default permissions across 4 project archetypes (C1-ProductEngineering, C2-DataMLOps, C3-PersonalAutomation, C4-AgenticResearch); specifies allowed tools, human-in-the-loop (HITL) escalation triggers (git commit, deploy, schema writes, dataset overwrites, cron/systemd installs, bulk model calls), filesystem read/write boundaries, and network egress policies 
- HOW: Apply preset configurations at session start based on the target project archetype.
- live: no live URLs
- conflicts: Uses compound command names (e.g., 'bash:read', 'bash:test') that require parsing by the harness execution layer to align with Cedar action primitives.

### files/solo-levelling/.harness/telemetry/litellm-config.yaml
- card: files/solo-levelling/.harness/telemetry/litellm-config.yaml | part parts/13-deve-solo.md:873 | lines 35 | verdict Verified
- WHAT: LiteLLM router and telemetry configuration file defining tiered model routing (primary: claude-sonnet-4-5, fallback: gemini-2.0-flash, budget: gemini-2.0-flash-lite), per-task spend caps, workflow-specific model pinning, and daily budget limits.
- HOW: 1. Load config into LiteLLM proxy or local SDK router.
- live: no live URLs
- conflicts: none

### files/solo-levelling/.harness/workflows/deploy-monitor.yaml
- card: files/solo-levelling/.harness/workflows/deploy-monitor.yaml | part parts/13-deve-solo.md:909 | lines 53 | verdict Verified
- WHAT: Deployment Monitor workflow state machine specification implementing automated canary monitoring and immediate rollback execution inspired by Netflix canary philosophy.
- HOW: 1. Start deployment pipeline at state `deploy_start`.
- live: no live URLs
- conflicts: none

### files/solo-levelling/.harness/workflows/fcar-review.yaml
- card: files/solo-levelling/.harness/workflows/fcar-review.yaml | part parts/13-deve-solo.md:963 | lines 48 | verdict Verified
- WHAT: Fresh Context Adversarial Review (FCAR) workflow state machine enforcing Gate 4 compliance by purging agent memory prior to evaluating design artifacts against an adversarial rubric.
- HOW: 1. Trigger workflow on `receive_artifact`.
- live: no live URLs
- conflicts: none

### files/solo-levelling/.harness/workflows/launch-checklist.yaml
- card: files/solo-levelling/.harness/workflows/launch-checklist.yaml | part parts/13-deve-solo.md:1012 | lines 53 | verdict Verified
- WHAT: Launch Checklist workflow state machine executing Google SRE-aligned pre-flight verification, secret scanning, and Gate 6 clearance before production deployment.
- HOW: 1. Initiate workflow at `initiate_precheck`.
- live: no live URLs
- conflicts: none

### files/solo-levelling/.harness/workflows/postmortem.yaml
- card: files/solo-levelling/.harness/workflows/postmortem.yaml | part parts/13-deve-solo.md:1066 | lines 39 | verdict Verified
- WHAT: Postmortem workflow state machine (Workflow 7) implementing Google SRE and Amazon Correction of Errors (COE) methodology to systematically analyze incidents, root causes, and corrective actions.
- HOW: 1. Feed incident payload into state `receive_incident`.
- live: no live URLs
- conflicts: none

### files/solo-levelling/.harness/workflows/scope-gate.yaml
- card: files/solo-levelling/.harness/workflows/scope-gate.yaml | part parts/13-deve-solo.md:1106 | lines 45 | verdict Verified
- WHAT: Scope Gate workflow state machine specification (Workflow 2) automating Basecamp Shape Up Scope Hammer enforcement by running scope checks against pitch.md No-gos.
- HOW: 1. Ingest task description at state `receive_task`.
- live: no live URLs
- conflicts: none

### files/solo-levelling/.harness/workflows/stakes-classifier.yaml
- card: files/solo-levelling/.harness/workflows/stakes-classifier.yaml | part parts/13-deve-solo.md:1152 | lines 40 | verdict Verified
- WHAT: Stakes Classifier workflow state machine specification (Workflow 8) routing code modifications into tier-specific review pipelines based on automated risk analysis.
- HOW: 1. Pass proposed code change at state `receive_change`.
- live: no live URLs
- conflicts: none

### files/solo-levelling/.harness/workflows/unknown-first-sorter.yaml
- card: files/solo-levelling/.harness/workflows/unknown-first-sorter.yaml | part parts/13-deve-solo.md:1193 | lines 37 | verdict Verified
- WHAT: Unknown-First Sorter workflow state machine specification (Workflow 9) operationalizing Basecamp Shape Up Hill Chart sequencing by ordering scopes uphill-first and updating build-log.md.
- HOW: 1. Input candidate scopes at state `receive_scopes`.
- live: no live URLs
- conflicts: none

### files/solo-levelling/.harness/workflows/working-backwards.yaml
- card: files/solo-levelling/.harness/workflows/working-backwards.yaml | part parts/13-deve-solo.md:1231 | lines 38 | verdict Verified
- WHAT: Working Backwards workflow state machine specification (Workflow 1) orchestrating Amazon PR/FAQ draft generation, customer challenge critiques, and Gate 2 validation.
- HOW: 1. Feed raw idea to state `receive_idea`.
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/.gemini/settings.json
- card: files/solo-levelling/the harness/.gemini/settings.json | part parts/13-deve-solo.md:9289 | lines 16 | verdict Verified
- WHAT: Gemini IDE and agent configuration linking in-process hooks (.harness/hooks/hooks.json), MCP server definitions (.harness/mcp/mcp_servers.json), sandbox execution gate (.harness/sandbox/gate.sh), Cedar policies, and telemetry configs.
- HOW: Keep in project root under .gemini/settings.json for Gemini workspace initialization
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/.harness/README.md
- card: files/solo-levelling/the harness/.harness/README.md | part parts/13-deve-solo.md:9306 | lines 34 | verdict Verified
- WHAT: Versioned Harness-as-Code architecture manifest and operating rules for the Solo AI Product Engineering System v1.0 (.harness/), documenting directory layouts, element mappings (CAP-01 through PROT-03), operating rules, validation evidence, and semver tracking.
- HOW: Consult as the primary architectural entry point for .harness/ subsystem layout
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/.harness/agents/coder.md
- card: files/solo-levelling/the harness/.harness/agents/coder.md | part parts/13-deve-solo.md:9341 | lines 68 | verdict Verified
- WHAT: Sandboxed implementation and test-driven engineering subagent specification operating under Class-1 and Class-2 permissions, restricted to workspace boundaries (src/, tests/, docs/, scratch/), enforcing TDD Red-Green-Refactor invariants and pre/post tool hooks.
- HOW: Invoke coder subagent for atomic, test-backed code modifications and refactoring tasks
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/.harness/agents/explorer.md
- card: files/solo-levelling/the harness/.harness/agents/explorer.md | part parts/13-deve-solo.md:9410 | lines 68 | verdict Verified
- WHAT: Fast, zero-side-effect codebase research and AST navigation subagent specification operating under Class-0 strict read-only permissions with lightweight model routing (coding-fast) and read-only tool allowlists.
- HOW: Invoke explorer subagent for codebase discovery, grep/AST symbol search, and documentation synthesis
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/.harness/agents/planner.md
- card: files/solo-levelling/the harness/.harness/agents/planner.md | part parts/13-deve-solo.md:9479 | lines 71 | verdict Verified
- WHAT: High-reasoning strategic decomposition and state-machine orchestration subagent specification operating under Class-0 read-only orchestration permissions with interactive user questioning and subagent management capabilities.
- HOW: Invoke planner subagent at the beginning of complex workflows to decompose goals into deterministic state-machine tasks
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/.harness/agents/reviewer.md
- card: files/solo-levelling/the harness/.harness/agents/reviewer.md | part parts/13-deve-solo.md:9551 | lines 81 | verdict Verified
- WHAT: Multi-perspective staff code review and security audit subagent specification evaluating diffs for correctness, security vulnerabilities (OWASP), regression risks, and architectural integrity using a high-reasoning model tier.
- HOW: Invoke reviewer subagent after coder completes implementation to perform fresh-context audit
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/.harness/config/harness.yaml
- card: files/solo-levelling/the harness/.harness/config/harness.yaml | part parts/13-deve-solo.md:9633 | lines 181 | verdict Verified
- WHAT: Declarative Master Harness-as-Code manifest defining project agents (planner, explorer, coder, reviewer), MCP servers, Cedar ABAC permission engine, telemetry budget caps ($5/session, $50/day), sandbox parameters, and enabled workflows.
- HOW: Validate configuration integrity via task harness-check
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/.harness/hooks/hooks.json
- card: files/solo-levelling/the harness/.harness/hooks/hooks.json | part parts/13-deve-solo.md:9815 | lines 47 | verdict Verified
- WHAT: Deterministic in-process lifecycle interceptor manifest configuring PreToolUse and PostToolUse hooks for command safety validation (pre_tool_guard.py), secret leak detection, and post-write linting (post_tool_linter.py).
- HOW: Reference in agent IDE settings as the active hooks configuration file
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/.harness/hooks/post_tool_linter.py
- card: files/solo-levelling/the harness/.harness/hooks/post_tool_linter.py | part parts/13-deve-solo.md:9863 | lines 76 | verdict Verified
- WHAT: Deterministic post-tool auto-formatter and AST syntax validator script running Ruff and Prettier on modified files immediately after file write/edit tools, returning syntax errors directly to agent context.
- HOW: Invoked automatically via PostToolUse hook on write_to_file and replace_file_content calls
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/.harness/hooks/pre_tool_guard.py
- card: files/solo-levelling/the harness/.harness/hooks/pre_tool_guard.py | part parts/13-deve-solo.md:9940 | lines 94 | verdict Verified
- WHAT: Deterministic pre-tool security guard script rejecting destructive shell commands (rm -rf, mkfs, dd, fork bombs, force push) and scanning file contents for high-entropy secrets and API keys (AWS, GitHub, Slack tokens).
- HOW: Invoked automatically via PreToolUse hook on run_command and file write tools
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/.harness/permissions/presets.json
- card: files/solo-levelling/the harness/.harness/permissions/presets.json | part parts/13-deve-solo.md:10186 | lines 117 | verdict Verified
- WHAT: Role and archetype permission presets configuring tool allowlists, denylists, and Human-in-the-Loop (HITL) escalation triggers for canonical archetypes C1 through C6.
- HOW: Load archetype preset matching current task context (e.g., C1_ProductEngineering for web dev)
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/.harness/skills/index.json
- card: files/solo-levelling/the harness/.harness/skills/index.json | part parts/13-deve-solo.md:13077 | lines 568 | verdict Verified
- WHAT: Progressive disclosure registry indexing all 40 harness skills with names, domains, triggers, tiers (Essential, Recommended, Optional), and paths, enabling agents to discover skills on demand.
- HOW: Query index.json by trigger phrase to discover relevant skills for a task
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/.harness/telemetry/langfuse-config.json
- card: files/solo-levelling/the harness/.harness/telemetry/langfuse-config.json | part parts/13-deve-solo.md:13646 | lines 16 | verdict Verified
- WHAT: Langfuse LLM observability and tracing configuration defining telemetry endpoints, credential references, flush intervals, and session archetype tagging.
- HOW: Configure environment variables LANGFUSE_PUBLIC_KEY and LANGFUSE_SECRET_KEY in .env
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/.harness/telemetry/litellm-config.yaml
- card: files/solo-levelling/the harness/.harness/telemetry/litellm-config.yaml | part parts/13-deve-solo.md:13663 | lines 47 | verdict Verified
- WHAT: LiteLLM Proxy routing configuration defining virtual model tiers (coding-primary, coding-fast, coding-local), latency-based routing, automatic failover chains, and hard spend caps ($5/session, $50/day).
- HOW: Deploy LiteLLM proxy referencing this config file to route agent LLM calls
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/.harness/workflows/blueprints/build-verify.yaml
- card: files/solo-levelling/the harness/.harness/workflows/blueprints/build-verify.yaml | part parts/13-deve-solo.md:13711 | lines 61 | verdict Verified
- WHAT: Deterministic YAML workflow definition for 'build-verify' (blueprint template) orchestrating multi-stage pipeline execution, tool verification gates, and rollback compensation.
- HOW: Execute workflow via harness runner or Taskfile for build-verify operations
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/.harness/workflows/blueprints/migration-safeguard.yaml
- card: files/solo-levelling/the harness/.harness/workflows/blueprints/migration-safeguard.yaml | part parts/13-deve-solo.md:13773 | lines 40 | verdict Verified
- WHAT: Deterministic YAML workflow definition for 'migration-safeguard' (blueprint template) orchestrating multi-stage pipeline execution, tool verification gates, and rollback compensation.
- HOW: Execute workflow via harness runner or Taskfile for migration-safeguard operations
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/.harness/workflows/blueprints/refactor-safely.yaml
- card: files/solo-levelling/the harness/.harness/workflows/blueprints/refactor-safely.yaml | part parts/13-deve-solo.md:13814 | lines 70 | verdict Verified
- WHAT: Deterministic YAML workflow definition for 'refactor-safely' (blueprint template) orchestrating multi-stage pipeline execution, tool verification gates, and rollback compensation.
- HOW: Execute workflow via harness runner or Taskfile for refactor-safely operations
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/.harness/workflows/blueprints/test-and-verify.yaml
- card: files/solo-levelling/the harness/.harness/workflows/blueprints/test-and-verify.yaml | part parts/13-deve-solo.md:13885 | lines 35 | verdict Verified
- WHAT: Deterministic YAML workflow definition for 'test-and-verify' (blueprint template) orchestrating multi-stage pipeline execution, tool verification gates, and rollback compensation.
- HOW: Execute workflow via harness runner or Taskfile for test-and-verify operations
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/.harness/workflows/build-verify.yaml
- card: files/solo-levelling/the harness/.harness/workflows/build-verify.yaml | part parts/13-deve-solo.md:13921 | lines 61 | verdict Verified
- WHAT: Deterministic YAML workflow definition for 'build-verify' (executable workflow) orchestrating multi-stage pipeline execution, tool verification gates, and rollback compensation.
- HOW: Execute workflow via harness runner or Taskfile for build-verify operations
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/.harness/workflows/migration-safeguard.yaml
- card: files/solo-levelling/the harness/.harness/workflows/migration-safeguard.yaml | part parts/13-deve-solo.md:13983 | lines 40 | verdict Verified
- WHAT: Deterministic YAML workflow definition for 'migration-safeguard' (executable workflow) orchestrating multi-stage pipeline execution, tool verification gates, and rollback compensation.
- HOW: Execute workflow via harness runner or Taskfile for migration-safeguard operations
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/.harness/workflows/refactor-safely.yaml
- card: files/solo-levelling/the harness/.harness/workflows/refactor-safely.yaml | part parts/13-deve-solo.md:14024 | lines 70 | verdict Verified
- WHAT: Deterministic YAML workflow definition for 'refactor-safely' (executable workflow) orchestrating multi-stage pipeline execution, tool verification gates, and rollback compensation.
- HOW: Execute workflow via harness runner or Taskfile for refactor-safely operations
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/.harness/workflows/test-and-verify.yaml
- card: files/solo-levelling/the harness/.harness/workflows/test-and-verify.yaml | part parts/13-deve-solo.md:14095 | lines 35 | verdict Verified
- WHAT: Deterministic YAML workflow definition for 'test-and-verify' (executable workflow) orchestrating multi-stage pipeline execution, tool verification gates, and rollback compensation.
- HOW: Execute workflow via harness runner or Taskfile for test-and-verify operations
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/Taskfile.yml
- card: files/solo-levelling/the harness/Taskfile.yml | part parts/13-deve-solo.md:14498 | lines 79 | verdict Verified
- WHAT: Taskfile automation runner manifest defining project tasks for testing (task test), linting (task lint), verification (task verify), sandboxing (task sandbox), and harness integrity checking (task harness-check).
- HOW: Run automated tests: task test
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/lefthook.yml
- card: files/solo-levelling/the harness/lefthook.yml | part parts/13-deve-solo.md:15624 | lines 40 | verdict Verified
- WHAT: Lefthook Git security and quality gate configuration executing parallel pre-commit hooks (Gitleaks, Ruff, pre-tool-guard, pytest unit tests) and post-commit changelog updates.
- HOW: Install and activate via lefthook install to enforce pre-commit gating
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-0/.gitkeep
- card: files/solo-levelling/the harness/phase-0/.gitkeep | part parts/13-deve-solo.md:15665 | lines 0 | verdict Verified
- WHAT: Gitkeep marker maintaining the directory structure of the phase-0 repository workspace in git version control.
- HOW: Retain in version control to ensure directory persistence.
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-1/synthesis/MASTER_D1.md
- card: files/solo-levelling/the harness/phase-1/synthesis/MASTER_D1.md | part parts/13-deve-solo.md:23944 | lines 493 | verdict Unverified
- WHAT: Canonical convergence: ~101 raw batch 1-5 candidates into 56 elements (38 CAP) with L1-L5 layer architecture and 6 collision resolutions; gate P1-43 PASS.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-1/synthesis/MASTER_D2.md
- card: files/solo-levelling/the harness/phase-1/synthesis/MASTER_D2.md | part parts/13-deve-solo.md:24438 | lines 288 | verdict Unverified
- WHAT: Level-hygiene audit of 101 candidates against 6-tier ontology yielding 36 true CAPs and binning 65 non-CAPs (PROT/MEC/FW/ART/Tools) across 7 boundary checks.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-2/STATUS.md
- card: files/solo-levelling/the harness/phase-2/STATUS.md | part parts/13-deve-solo.md:24898 | lines 7 | verdict Unverified
- WHAT: Seven-line stale NOT STARTED status stub dated 2026-08-31 superseded by the converged 2026-09-01 rankings.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-3.5/STATUS.md
- card: files/solo-levelling/the harness/phase-3.5/STATUS.md | part parts/13-deve-solo.md:27644 | lines 7 | verdict Unverified
- WHAT: Seven-line stale NOT STARTED stub superseded by 2026-09-01 FRICTION_LOG/VALIDATION_REPORT showing V1-V4 plus sprint complete.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-3.5/VALIDATION_PLAN.md
- card: files/solo-levelling/the harness/phase-3.5/VALIDATION_PLAN.md | part parts/13-deve-solo.md:27652 | lines 32 | verdict Unverified
- WHAT: Empirical validation framework: materialize .harness/, dogfood real tasks, capture SC friction with sev schema, feed back to P1/P2/P3.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-3/PLAN.md
- card: files/solo-levelling/the harness/phase-3/PLAN.md | part parts/13-deve-solo.md:28196 | lines 50 | verdict Unverified
- WHAT: Deployment plan dispatching a 26-agent tool-selection fleet (T-A..T-H plus verify/build/cross) with 7-point verification gate and anti-bloat test.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-3/STATUS.md
- card: files/solo-levelling/the harness/phase-3/STATUS.md | part parts/13-deve-solo.md:28247 | lines 7 | verdict Unverified
- WHAT: Seven-line stale NOT STARTED stub superseded by the converged 2026-09-01 TOOL_SELECTION_INDEX.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/plan.md
- card: files/solo-levelling/the harness/plan.md | part parts/13-deve-solo.md:31996 | lines 393 | verdict Unverified
- WHAT: 137-micro-task gated spiral operating system: 4-agent R-A/R-B/V-C/V-D flow, quality bar, stop rules, and phase gates P0-13 through P4-15.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/scripts/run_validation.sh
- card: files/solo-levelling/the harness/scripts/run_validation.sh | part parts/13-deve-solo.md:32910 | lines 89 | verdict Unverified
- WHAT: Validation runner scaffolding timestamped scratch/validation/<ARCH>-<TS>/ runs with build-verify.yaml copy, git diagnostics, and friction-log reminders.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/deve/.cursorrules
- card: files/deve/.cursorrules | part parts/13-deve-solo.md:38032 | lines 12 | verdict Verified
- WHAT: Cursor IDE behavioral rules for the Solo AI Product Engineering System: an autonomous execution protocol forbidding straight-to-code work and mandating project scaffolding (pitch/prfaq/design-note), appetite-before-solution, non-goals + alternatives, uphill-first ordering, TDD, and evidence-carrying termination (tests + linter exit 0).
- HOW: Place at a project root so Cursor loads it as system-level behavioral guardrails.
- live: no live URLs
- conflicts: Enforcement gap: .cursorrules is advisory text while hooks.json/pre_tool_guard.py are the real enforcement layer; a Cursor agent can bypass it.

### files/deve/.env.template
- card: files/deve/.env.template | part parts/13-deve-solo.md:38045 | lines 13 | verdict Verified
- WHAT: Environment variable template listing required AI model API keys (Anthropic, Google AI) plus a mandatory monitoring DSN, with instructions to copy to .env and never commit it.
- HOW: Copy .env.template to .env and fill real values.
- live: no live URLs
- conflicts: The monitoring DSN is marked required before production deploy, but no code in the repo consumes it - it is a process reminder, not enforced config.

### files/deve/.gitignore
- card: files/deve/.gitignore | part parts/13-deve-solo.md:38059 | lines 4 | verdict Verified
- WHAT: Minimal repository ignore file excluding .env, compiled Python artifacts (*.pyc) and __pycache__/ directories.
- HOW: Keep .env in the ignore list to support the zero-secret-leakage rule.
- live: no live URLs
- conflicts: The top-level .gitignore does not list .pytest_cache/ or output/, so the pytest cache relies on its own internal .gitignore.

### files/deve/.harness/README.md
- card: files/deve/.harness/README.md | part parts/13-deve-solo.md:38064 | lines 27 | verdict Verified
- WHAT: Index/manifest of the AI Development Harness: maps every harness path (config, hooks, permissions, sandbox, telemetry, mcp, skills, workflows) and states the safety/governance principles (security-first, loop rails max_steps=15, IAL debounce, ABAC class-3 approval, isolated FCAR).
- HOW: Use as the entry point/table-of-contents when onboarding the harness.
- live: no live URLs
- conflicts: README describes 'skills/' as 9 OS Workflow skills and 'workflows/' as the 9 state machines, but the tree also contains workflows/fcar-review.yaml (a 10th workflow) not counted in the 9.

### files/deve/.harness/config/harness.yaml
- card: files/deve/.harness/config/harness.yaml | part parts/13-deve-solo.md:38092 | lines 50 | verdict Verified
- WHAT: Master harness configuration: harness version/name; loop-engineering rails (max_steps_global 15, debounce identical calls, deterministic termination, self-certification blocked); OS gate list 1-6 with FCAR required for Gate 4; the enabled workflow list; skill count/FCAR reviewer rule; telemetry config pointer and advisory budget note; security component pointers.
- HOW: Load first as the harness boot config.
- live: no live URLs
- conflicts: workflows.enabled lists 9 workflows but fcar-review.yaml exists outside that list., telemetry.budget_enforcement is 'advisory' yet litellm-config declares hard_stop_at_pct 100, so caps only bite behind an external proxy.

### files/deve/.harness/hooks/hooks.json
- card: files/deve/.harness/hooks/hooks.json | part parts/13-deve-solo.md:38143 | lines 55 | verdict Verified
- WHAT: Hook manifest declaring four pre-tool interceptors (security-guard, abac-check, checkpoint-before-destructive requiring [Y/n], IAL debounce on identical repeat) and one post-tool hook (secret-scan-after-write), plus a global loop_rails max_steps=15 that throws fatal error on exceed.
- HOW: Wire each enabled pre_tool_hook script into the agent's tool-call path before execution.
- live: no live URLs
- conflicts: abac-check matches underscore trigger names (git_push_main, drop_database, ...) while checkpoint triggers use bash: prefixes (bash:git push) - inconsistent naming for the same action space.

### files/deve/.harness/hooks/pre_tool_guard.py
- card: files/deve/.harness/hooks/pre_tool_guard.py | part parts/13-deve-solo.md:38199 | lines 121 | verdict Verified
- WHAT: Security guard run before every tool execution. Reads JSON {tool,args} from stdin and denies (exit 1) on ~18 regex patterns: destructive rm on system paths / quoted / -- separator, curl/wget piped to bash/python, curl -fsSL, chmod +x, base64 decode, env|printenv, AKIA/sk-/ghp_/ASIA secrets, force-push to main/master, and unquoted password/token/api_key assignments. Fails OPEN (exit 0) on JSON pars
- HOW: Call before every bash/shell/run_command/execute tool call, passing the invocation JSON on stdin.
- live: no live URLs
- conflicts: Over-broad match: the pattern \b(env|printenv)\b blocks any command containing 'env' (e.g. `env FOO=1 python app.py`), a common benign idiom., Fail-open design: a crash or malformed JSON silently allows execution; guard.log shows ten such fail-open events already., Cookie-cutter secret regex only matches 20+ char unquoted values, a subset of what quality-security.md implies is covered.

### files/deve/.harness/permissions/presets.json
- card: files/deve/.harness/permissions/presets.json | part parts/13-deve-solo.md:38565 | lines 38 | verdict Verified
- WHAT: Per-archetype role permission presets for the four project classes (C1 ProductEngineering, C2 DataMLOps, C3 PersonalAutomation, C4 AgenticResearch): allowed tools, HITL escalation triggers, filesystem read/write scopes, and network egress policy.
- HOW: At session start, select the archetype and apply its allowed_tools and filesystem/network scopes.
- live: no live URLs
- conflicts: Vocabulary gap: presets use archetypes C1-C4 and tool names like 'bash:test', but policies.cedar/check.py use Cedar roles and actions like write_to_file; no explicit mapping table exists., Unverified binding: nothing loads presets.json at runtime (check.py reads it into an unused global).

### files/deve/.harness/telemetry/litellm-config.yaml
- card: files/deve/.harness/telemetry/litellm-config.yaml | part parts/13-deve-solo.md:39037 | lines 36 | verdict Partially
- WHAT: LiteLLM routing config with three named routing tiers - primary, fallback, budget - each carrying a max_tokens and per-task USD budget cap, a routing_strategy (default primary, fallback on primary failure, budget for low-stakes, primary for FCAR/high-stakes review), and global daily spend limits with alert at 80% and hard stop at 100%.
- HOW: Run a LiteLLM proxy pointed at this config to enforce routing and caps.
- live: no live URLs
- conflicts: harness.yaml marks budget_enforcement 'advisory' while this file declares hard_stop_at_pct 100 - enforcement depends on an external proxy not present in the repo., spend-log.sh's manual >= $8.00 warning aligns numerically with alert_at_pct 80, but spend-log.sh is not wired to the router's actual spend.

### files/deve/.harness/workflows/alternatives-generator.yaml
- card: files/deve/.harness/workflows/alternatives-generator.yaml | part parts/13-deve-solo.md:39074 | lines 36 | verdict Verified
- WHAT: Deterministic YAML state machine for Workflow 3: receive_problem -> generate_alternatives -> evaluate_alternatives (branch count>=3) -> alternatives_ready (human checkpoint Accept/Regenerate) -> alternatives_accepted; max_steps 5, fatal on exceed.
- HOW: Load as the state machine governing alternative-generation sessions.
- live: no live URLs
- conflicts: This workflow names skill 'alternatives-brainstorm', but the installed skill is 'alternatives-generator' - the reference is unresolved.

### files/deve/.harness/workflows/deploy-monitor.yaml
- card: files/deve/.harness/workflows/deploy-monitor.yaml | part parts/13-deve-solo.md:39111 | lines 53 | verdict Verified
- WHAT: Workflow 6 automated deployment state machine (no skill dir): deploy_start -> verify_rollback_threshold (fatal if missing) -> execute_deploy -> monitor_window (10 min via monitor_metric) -> check_metric branch -> trigger_rollback (immediate) or deploy_stable; rollback completion triggers Workflow 7 Postmortem.
- HOW: Run immediately post-deploy; it refuses to proceed unless a rollback threshold is committed in the launch checklist.
- live: no live URLs
- conflicts: verify.sh explicitly notes this is 'automated-only (no skill dir) by design', confirming a deliberate asymmetry with the other workflows.

### files/deve/.harness/workflows/failure-mode-analyzer.yaml
- card: files/deve/.harness/workflows/failure-mode-analyzer.yaml | part parts/13-deve-solo.md:39165 | lines 34 | verdict Verified
- WHAT: Workflow 4 state machine: receive_design -> analyze_failures (skill failure-mode-analysis) -> review_risks (human checkpoint Mitigate/Accept) -> mitigations_applied or risks_accepted; max_steps 4, fatal on exceed.
- HOW: Run before an external integration; feed the design description.
- live: no live URLs
- conflicts: Skill reference 'failure-mode-analysis' does not match the installed skill frontmatter name 'failure-mode-analyzer'.

### files/deve/.harness/workflows/fcar-review.yaml
- card: files/deve/.harness/workflows/fcar-review.yaml | part parts/13-deve-solo.md:39200 | lines 48 | verdict Verified
- WHAT: Gate 4 FCAR state machine: receive_artifact -> clear_context (explicit context clear) -> run_fcar -> evaluate branch -> gate_passed, or gate_failed -> human checkpoint (Revise/Waive) -> waive_with_exception (human writes permanent exception) -> gate_passed; max_steps 6.
- HOW: Run whenever a design note is required; explicitly clear ALL authoring context first.
- live: no live URLs
- conflicts: fcar-review.yaml is not listed in harness.yaml workflows.enabled, so the Gate-4-only workflow lives outside the enabled workflow registry.

### files/deve/.harness/workflows/launch-checklist.yaml
- card: files/deve/.harness/workflows/launch-checklist.yaml | part parts/13-deve-solo.md:39249 | lines 53 | verdict Verified
- WHAT: Gate 6 state machine: initiate_precheck -> run_secret_scan (bash scripts/secret-scan.sh) -> run_checklist (skill launch-checklist-runner) -> evaluate_items branch -> gate_6_passed or checklist_blocked (human checkpoint Fix/Waive/Abort) -> record_waiver -> gate_6_passed; deploy_aborted terminal; max_steps 6.
- HOW: Run before any production deploy.
- live: no live URLs
- conflicts: none

### files/deve/.harness/workflows/postmortem.yaml
- card: files/deve/.harness/workflows/postmortem.yaml | part parts/13-deve-solo.md:39303 | lines 39 | verdict Verified
- WHAT: Workflow 7 state machine: receive_incident -> compile_timeline (skill postmortem-opener) -> human_review (Accept/Revise) -> verify_tasks_tracked (every corrective action has owner/due date/tracker entry) -> postmortem_closed (creates postmortem artifact); max_steps 5.
- HOW: Run on any incident above defined severity (e.g. after a deploy-monitor rollback).
- live: no live URLs
- conflicts: none

### files/deve/.harness/workflows/scope-gate.yaml
- card: files/deve/.harness/workflows/scope-gate.yaml | part parts/13-deve-solo.md:39343 | lines 45 | verdict Verified
- WHAT: Workflow 2 state machine: receive_task -> run_scope_check (bash scripts/scope-check.py with task+pitch args) -> evaluate_conflict branch on exit_code==0 -> task_approved, or conflict_detected -> human checkpoint Drop/Amend -> task_dropped or amend_pitch -> task_approved; max_steps 5.
- HOW: Run before adding any task to the active scope.
- live: no live URLs
- conflicts: Depends on scripts/scope-check.py exit code, but that checker returns 1 both for a real conflict and for a missing No-gos section, so the workflow cannot distinguish 'conflict' from 'misconfigured pitch' without reading stdout.

### files/deve/.harness/workflows/stakes-classifier.yaml
- card: files/deve/.harness/workflows/stakes-classifier.yaml | part parts/13-deve-solo.md:39389 | lines 40 | verdict Verified
- WHAT: Workflow 8 state machine: receive_change -> classify_stakes (skill stakes-classifier) -> route_tier branch on tier -> low_tier_approval (AI-first, cursory review), medium_tier_review (line-by-line), high_tier_reimplementation (independent human re-implementation before merge); max_steps 4.
- HOW: Run before implementing any code change.
- live: no live URLs
- conflicts: none

### files/deve/.harness/workflows/unknown-first-sorter.yaml
- card: files/deve/.harness/workflows/unknown-first-sorter.yaml | part parts/13-deve-solo.md:39430 | lines 37 | verdict Verified
- WHAT: Workflow 9 state machine: receive_scopes -> classify_scopes (skill unknown-first-sorter) -> human_confirm_sequence (Approve/Reorder) -> update_build_log (append sequenced scopes to build-log.md) -> sequencing_complete; max_steps 4.
- HOW: Run at kickoff of an implementation cycle.
- live: no live URLs
- conflicts: none

### files/deve/.harness/workflows/working-backwards.yaml
- card: files/deve/.harness/workflows/working-backwards.yaml | part parts/13-deve-solo.md:39468 | lines 38 | verdict Verified
- WHAT: Workflow 1 state machine: receive_idea -> draft_prfaq (skill working-backwards) -> human_review (Revise/Proceed/Kill) -> complete (Gate 2 PASSED, creates prfaq artifact) or killed (log reason, archive pitch stub); max_steps 5.
- HOW: Run at the start of a new idea/project.
- live: no live URLs
- conflicts: none

### files/deve/AGENTS.md
- card: files/deve/AGENTS.md | part parts/13-deve-solo.md:39575 | lines 48 | verdict Verified
- WHAT: Agent registry and operating contract: a taxonomy of four role categories (C1 ProductEngineering, C2 DataMLOps, C3 PersonalAutomation, C4 AgenticResearch) with autonomy models, toolsets and verification gates; the four loop rails (max_steps 15, IAL debounce, deterministic/evidence-carrying termination, fresh-context adversarial review); the autonomous project execution protocol; and source links f
- HOW: Read before deploying or invoking any agent; it defines which role/gate applies.
- live: no live URLs
- conflicts: AGENTS.md cites external design sources (Anthropic multi-agent, OpenAI Agents SDK, AWS Bedrock AgentCore, Google SRE) whose live URLs are not fetched/pinned in this corpus read, so claim provenance is unverified here.

### files/deve/CLAUDE.md
- card: files/deve/CLAUDE.md | part parts/13-deve-solo.md:39624 | lines 66 | verdict Verified
- WHAT: Claude harness bridge: eight mandatory behaviors (preserve code integrity, strict typing, zero secret leakage, verification-before-done, anti-bloat, checkpoint-before-destructive, loop rails, deterministic termination), the autonomous project execution protocol mapped to the OS gates, a lifecycle quick reference with tier router, a key-files table, and quick commands.
- HOW: Read at the start of any task in the repository.
- live: no live URLs
- conflicts: Two parallel gate taxonomies exist: CLAUDE.md's lifecycle quick reference and os/gates.md's gate table; they must be kept in sync manually.

### files/deve/lefthook.yml
- card: files/deve/lefthook.yml | part parts/13-deve-solo.md:39772 | lines 17 | verdict Verified
- WHAT: Git hook configuration via lefthook: pre-commit runs secret-scan and py_compile on staged *.py files; pre-push runs scripts/verify.sh and the pytest suite.
- HOW: Install lefthook and run `lefthook install` to register the hooks.
- live: no live URLs
- conflicts: Duplicate enforcement with Taskfile.yml and scripts/verify.sh; the same secret-scan/pytest runs in three places, which can drift., Requires an external lefthook binary that the repo does not vendor, so the hooks are inert until installed.

### files/builders-playbook/product_engineering/report/05-ai-agent-architecture.md
- card: files/builders-playbook/product_engineering/report/05-ai-agent-architecture.md | part parts/14-bp-report.md:629 | lines 130 | verdict Verified
- WHAT: Architectural blueprint and security control catalog for AI agent harnesses, emphasizing that product value resides in the harness rather than the underlying foundation model: covering workflow topologies, context engineering, tool design, memory tiers, eval methodology, cost/latency optimization, and OWASP-aligned security controls.
- HOW: Separate brain (LLM intent interpretation) from body (deterministic code execution and validation).
- live: no live URLs
- conflicts: Multi-agent performance claims (+90.2% on research evals) vs 15x token cost overhead and failure on code synthesis tasks., Vendor-reported benchmark accuracy (e.g. Fin Apex 73.1%) vs independent real-world evaluations (42-50%).

### files/builders-playbook/product_engineering/report/06-automation-stack-workflows.md
- card: files/builders-playbook/product_engineering/report/06-automation-stack-workflows.md | part parts/14-bp-report.md:760 | lines 106 | verdict Verified
- WHAT: System architecture specification detailing the 12-layer automation stack (from VCS/CI to AIOps) and 9 end-to-end workflow reconstructions, distinguishing empirically verified production implementations (GitHub Copilot agent, Sentry Seer, GitHub environments, Anthropic multi-agent research) from proposed reference designs.
- HOW: Follow the decision ladder to select between deterministic scripts, structured workflows, autonomous agents, and multi-agent systems.
- live: no live URLs
- conflicts: Autonomous developer efficiency claims vs GitHub and OpenAI telemetry showing agent traffic driving a 10x surge in CI/CD pipeline load., High SAST scanner adoption vs benchmarked 43-61% detection blind spots and 41-50% false positive rates.

### files/builders-playbook/product_engineering/report/15-reference-architecture.md
- card: files/builders-playbook/product_engineering/report/15-reference-architecture.md | part parts/14-bp-report.md:1994 | lines 213 | verdict Verified
- WHAT: Reference architecture for software engineering systems: minimum-viable architecture (day one: modular monolith on managed services, bounded contexts with mechanically enforced boundaries, PostgreSQL, object storage, managed CI/CD, golden signals, and security scan gates) and advanced mature architecture (grown on pain: modular monolith core, selectively extracted services via ADRs, async messagin
- HOW: Default to a modular monolith deployed on managed PaaS with PostgreSQL; enforce module boundaries using import-linter rules and CI contracts.
- live: no live URLs
- conflicts: Industry hype around early microservice adoption vs empirical findings showing 10-20x operational cost inflation and reduced feature velocity, Autonomous agent coding promises vs requirement for single-threaded writes and human-in-the-loop verification

### files/builders-playbook/product_engineering/report/16-implementation-roadmap.md
- card: files/builders-playbook/product_engineering/report/16-implementation-roadmap.md | part parts/14-bp-report.md:2208 | lines 160 | verdict Partially
- WHAT: Proposed 4-phase implementation roadmap sequencing engineering capabilities to ensure verification capacity precedes generation scale: Phase 0 Foundations (releasable mainline, one-command builds, managed runtime, golden signals, rehearsed rollback; exit via Gates 8 and 9 lightweight); Phase 1 First Loop (running one complete discovery-to-measure bet end-to-end, supervised coding agents, UX states
- HOW: Execute Phase 0 before writing product features: establish git branch protection, automated CI, golden signal telemetry, and rehearsed rollback.
- live: no live URLs
- conflicts: Calendar-driven project management vs quality-gate-driven phased transitions, Vendor pressure to scale AI coding immediately vs empirical requirement to harden review and verification gates first

### files/builders-playbook/product_engineering/research/domain-a/05-codebase-exploration-implementation.md
- card: files/builders-playbook/product_engineering/research/domain-a/05-codebase-exploration-implementation.md | part parts/15-bp-core-research.md:1001 | lines 94 | verdict Verified
- WHAT: Coding Agents, Context Injection, and Implementation Practices (Domain A, Area 5): cross-agent context file precedence hierarchy (AGENTS.md universal root layered with tool-specific files CLAUDE.md, .cursorrules, copilot-instructions.md); best practices for instruction authoring (lean <200 lines, imperative commands, negative prohibitions, growing from observed mistakes); negative findings on inst
- HOW: Place AGENTS.md at the repo root with concise project architecture, validation commands, and boundary rules; layer tool-specific files (CLAUDE.md) on top without duplicating content.
- live: no live URLs
- conflicts: Developer perception of +20-24% speedup vs measured METR RCT showing 19% slowdown on familiar complex codebases, Agent self-reported completion ('all tests pass') vs independent audit showing 34.7% oversold success and test deletion gaming

### files/builders-playbook/product_engineering/research/domain-a/08-cicd-deployment.md
- card: files/builders-playbook/product_engineering/research/domain-a/08-cicd-deployment.md | part parts/15-bp-core-research.md:1247 | lines 69 | verdict Verified
- WHAT: AI-Assisted CI/CD and Deployment practices (Domain A, Area 8): agents authoring and hardening CI/CD pipelines (GitHub Actions skills, OIDC pinning, workflow optimization); CI as the non-negotiable enforcement layer for agentic development (PR quality gates: build, full test suite, lint, SAST, CVE scans; main merge gates: versioned snapshots, staging CD, releasability flags); identical harness enfo
- HOW: Use specialized CI agent skills to generate and harden GitHub Actions workflows, ensuring actions are pinned to commit SHAs and OIDC is configured properly.
- live: no live URLs
- conflicts: Autonomous agent delivery claims ('Scrum team as code') vs empirical enterprise reality of 70-95% unassisted pilot failure without strict CI gates

### files/builders-playbook/product_engineering/research/domain-b/07-tool-using-agents.md
- card: files/builders-playbook/product_engineering/research/domain-b/07-tool-using-agents.md | part parts/15-bp-core-research.md:2135 | lines 98 | verdict Verified
- WHAT: Tool-Using and Autonomous Systems as Products (Domain B, Area 7): compounding failure mathematics across multi-step execution (Sierra tau-bench showing GPT-4o drops from 61% single-trial success to ~25% across an 8-trial session; Salesforce MCP-Universe showing 43.7% multi-tool success); five predictable tool-call failure modes (execution failure, malformed arguments, hallucinated tool names, time
- HOW: Isolate API authentication, rate-limiting, retries, and secrets injection in a deterministic client wrapper; never pass raw credentials to or through the model.
- live: no live URLs
- conflicts: High single-call model benchmark scores vs compounding multi-step tool-use failure rates (0.85^10 = ~20%), Prompt-level safety requests vs deterministic external harness guardrails

### files/builders-playbook/product_engineering/research/automation/02-workflows.md
- card: files/builders-playbook/product_engineering/research/automation/02-workflows.md | part parts/15-bp-core-research.md:6233 | lines 267 | verdict Verified
- WHAT: Nine end-to-end workflow reconstructions (W1 idea-to-concept through W9 parallel-agent research) sharing a ten-part anatomy of triggers, inputs, decisions, tool calls, state changes, validation, outputs, failure handling, permissions, and approvals; four workflows are marked PROPOSED reference designs and five are VERIFIED reconstructions of documented GitHub, Sentry, and Anthropic practice.
- HOW: Treat every automation as proposing and the pull request with CI plus human review as disposing; never let agents merge on their own word.
- live: no live URLs
- conflicts: Anthropic multi-agent gains vs Cognition warnings against parallel writers, resolved as different problem classes with writes kept single-threaded.

### files/builders-playbook/02-project-execution-plan.md
- card: files/builders-playbook/02-project-execution-plan.md | part parts/17-bp-evidence-playbook.md:185 | lines 138 | verdict Unverified
- WHAT: Personal project operating system for solo builders: six phases (intake, quick validation, light spec, build, ship, iterate) with exit gates, the nine-report-gates-to-five-solo-gates mapping with verdict discipline, the 30-minute weekly ritual and 45-minute pre-build sit-down, the five-bullet daily build-log habit, the 15-minute blameless retrospective format, the hackathon-vs-project mode compres
- HOW: Run new work through the six phases with Bet/Merge/Release/Ship/Watch gates and dated build-log evidence
- live: no live URLs
- conflicts: none

