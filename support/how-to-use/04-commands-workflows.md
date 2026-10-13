# Commands and workflows

By execution order.

### files/opencode-research/research/08-pre-commit-hook.md
- card: files/opencode-research/research/08-pre-commit-hook.md | part parts/03-opencode-research-phases.md:1961 | lines 204 | verdict Verified
- WHAT: Phase 8 Task 3 architectural disambiguation and reference implementation for the Definition of Done (DoD) pre-commit hook: compares Option A (native Git .git/hooks/pre-commit shell script) against Option B (OpenCode plugin hook tool.execute.before in .opencode/plugins/dod-gate.ts); establishes a dual-layer enforcement model where the native Git pre-commit script acts as the authoritative hard, too
- HOW: Primary hard gate: Install executable bash script at .git/hooks/pre-commit (chmod +x); script reads feature_list.json via Node.js, checks for active features with status in_progress or blocked, and exits 1 with explanatory message if found (overrideable only via explicit git commit --no-verify)
- live: no live URLs
- conflicts: Architecture doc specifies pre-commit hook ambiguously between Git native hook and OpenCode plugin hook; analysis resolves this by proving OpenCode plugin hooks are flaky/inactive in headless/terminal/CI environments and mandating Git hook as the authoritative hard gate with OpenCode plugin hook as secondary advisory.

### files/opencode-research/harness-templates/README.md
- card: files/opencode-research/harness-templates/README.md | part parts/04-opencode-build-prompts.md:4540 | lines 30 | verdict Verified
- WHAT: Provenance and usage index for the four verbatim harness templates pulled from walkinglabs/learn-harness-engineering docs/en/resources/templates/ on 2026-08-09: AGENTS.md, init.sh, claude-progress.md, feature_list.json with subsystem mapping, file sizes, audit notes, and 6-step adoption checklist.
- HOW: Copy all four template files to project root
- live: no live URLs
- conflicts: none

### files/opencode-research/harness-templates/claude-progress.md
- card: files/opencode-research/harness-templates/claude-progress.md | part parts/04-opencode-build-prompts.md:4459 | lines 49 | verdict Verified
- WHAT: Agent-agnostic repository-local session progress log template (filename kept for course compatibility): Current Verified State block (root, startup/verification paths, highest-priority feature, blocker) plus per-session log entries (date, goal, completed, verification run, evidence, commits, artifacts, risks, next step).
- HOW: Fill Current Verified State with repo root, standard startup and verification paths, top unfinished feature, and blocker
- live: no live URLs
- conflicts: none

### files/opencode-research/harness-templates/feature_list.json
- card: files/opencode-research/harness-templates/feature_list.json | part parts/04-opencode-build-prompts.md:4393 | lines 65 | verdict Verified
- WHAT: Single-active-feature tracker template with enforcement rules (single_active_feature, passing_requires_evidence, do_not_skip_verification), status legend (not_started/in_progress/blocked/passing), and three example chat features each with priority, user_visible_behavior, verification[] steps, evidence[], and notes.
- HOW: Replace project name, last_updated, and example chat-001/002/003 features with real tasks
- live: no live URLs
- conflicts: none

### files/solo-levelling/lefthook.yml
- card: files/solo-levelling/lefthook.yml | part parts/13-deve-solo.md:8333 | lines 15 | verdict Verified
- WHAT: Git hook configuration utilizing Lefthook to enforce automated secret scanning, Python syntax compilation on staged files, and full verification gate checks before git push.
- HOW: 1. Install lefthook and run `lefthook install` to configure Git hooks.
- live: no live URLs
- conflicts: none

### files/solo-levelling/project-tracker.md
- card: files/solo-levelling/project-tracker.md | part parts/13-deve-solo.md:8970 | lines 19 | verdict Verified
- WHAT: Durable project tracking template for monitoring the execution status, lifecycle phases, appetite budgets, uphill/downhill scopes, and action items of solo engineering projects.
- HOW: 1. Populate Active Project name, Current Phase (Idea, Working Backwards, Pitch, Design, Build, Deploy), and Appetite.
- live: no live URLs
- conflicts: none

### files/solo-levelling/os/fcar-rubric.md
- card: files/solo-levelling/os/fcar-rubric.md | part parts/13-deve-solo.md:8636 | lines 46 | verdict Verified
- WHAT: The Fresh Context Adversarial Review (FCAR) rubric specification, containing mandatory invocation protocols, the non-optional CRITICAL RULE prohibiting conversational context sharing, the locked 5-item evaluation rubric, and the exact verbatim FCAR system prompt.
- HOW: Spawn a completely new LLM instance with zero session memory to review design artifacts
- live: no live URLs
- conflicts: none

### files/solo-levelling/os/gates.md
- card: files/solo-levelling/os/gates.md | part parts/13-deve-solo.md:8683 | lines 25 | verdict Verified
- WHAT: Specification of the 6 formal Decision Gates (Gate 1 Pitch, Gate 2 Design/FCAR, Gate 3 Pre-Implementation Scope, Gate 4 Irreversible Decision, Gate 5 PR/Test, Gate 6 Launch) and the explicit Gate Override Policy in the Solo AI Operating System.
- HOW: Validate each project milestone against its corresponding gate criteria before transitioning
- live: no live URLs
- conflicts: none

### files/solo-levelling/os/lifecycle.md
- card: files/solo-levelling/os/lifecycle.md | part parts/13-deve-solo.md:8709 | lines 54 | verdict Verified
- WHAT: Complete product development lifecycle sequence for the Solo AI Product Engineering System, defining the 6 linear stages (Idea -> Pitch -> Design -> Implementation -> Launch -> Postmortem) with strict inputs, outputs, gate criteria, and empirical company citations.
- HOW: Execute stage 1 (Idea/PRFAQ) using Amazon PR/FAQ principles to establish customer clarity
- live: no live URLs
- conflicts: none

### files/solo-levelling/os/quality-security.md
- card: files/solo-levelling/os/quality-security.md | part parts/13-deve-solo.md:8764 | lines 38 | verdict Verified
- WHAT: Specification of the quality, security, and reliability standards for the Solo AI Operating System, defining per-PR quality gates, launch security minimums, reliability bars, and pre-tool security guard regex patterns.
- HOW: Enforce zero lint errors, 100% test pass rate, and diff limits (<400 lines) on every PR
- live: no live URLs
- conflicts: none

### files/solo-levelling/os/artifacts/build-log-template.md
- card: files/solo-levelling/os/artifacts/build-log-template.md | part parts/13-deve-solo.md:8374 | lines 24 | verdict Verified
- WHAT: Standardized build log artifact template for recording living session progress, tracking uphill and downhill scope completions, and monitoring appetite consumption in the Solo AI Operating System.
- HOW: Copy template to project root as BUILD_LOG.md during implementation startup
- live: no live URLs
- conflicts: none

### files/solo-levelling/os/artifacts/design-note-template.md
- card: files/solo-levelling/os/artifacts/design-note-template.md | part parts/13-deve-solo.md:8399 | lines 41 | verdict Verified
- WHAT: Standardized Design Note artifact template structured into Context, Goals, Non-Goals (minimum 2 required), Detailed Design, Reversible/Irreversible Classification, Alternatives Considered, and FCAR Review Checkboxes.
- HOW: Author a Design Note covering problem context, concrete goals, and at least 2 explicit non-goals
- live: no live URLs
- conflicts: none

### files/solo-levelling/os/artifacts/launch-checklist-template.md
- card: files/solo-levelling/os/artifacts/launch-checklist-template.md | part parts/13-deve-solo.md:8441 | lines 24 | verdict Verified
- WHAT: The 8-item launch checklist artifact template enforcing non-negotiable pre-deployment verification across build verification, tests, logging, rollback strategy, secret scanning, dependency audit, authentication, and error budgets.
- HOW: Copy template as LAUNCH_CHECKLIST.md prior to initiating production deployment
- live: no live URLs
- conflicts: none

### files/solo-levelling/os/artifacts/pitch-template.md
- card: files/solo-levelling/os/artifacts/pitch-template.md | part parts/13-deve-solo.md:8466 | lines 29 | verdict Verified
- WHAT: Basecamp Shape Up inspired Pitch artifact template structured into Problem, Solution, Rabbit Holes, No-gos (minimum 3 required), Appetite budget, and Irreversible Commitment classification.
- HOW: Draft pitch defining raw user problem and concrete bounded solution
- live: no live URLs
- conflicts: none

### files/solo-levelling/os/artifacts/postmortem-template.md
- card: files/solo-levelling/os/artifacts/postmortem-template.md | part parts/13-deve-solo.md:8496 | lines 31 | verdict Verified
- WHAT: Standardized 3-section blameless postmortem artifact template comprising Incident Timeline, Root Cause Chain (Five Whys chained to systems, not humans), and Tracked Corrective Actions.
- HOW: Trigger postmortem upon any customer-impacting event or critical pipeline failure
- live: no live URLs
- conflicts: none

### files/solo-levelling/os/artifacts/prfaq-template.md
- card: files/solo-levelling/os/artifacts/prfaq-template.md | part parts/13-deve-solo.md:8528 | lines 30 | verdict Verified
- WHAT: Amazon Working Backwards inspired PR/FAQ artifact template consisting of a mock Press Release (Heading, Subheading, Summary, Problem, Solution, Leader Quote, Customer Quote, Call to Action) and an Internal FAQ addressing hard questions.
- HOW: Draft press release from the perspective of the launch date before writing any code
- live: no live URLs
- conflicts: none

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

### files/solo-levelling/.harness/sandbox/gate.sh
- card: files/solo-levelling/.harness/sandbox/gate.sh | part parts/13-deve-solo.md:468 | lines 43 | verdict Verified
- WHAT: Sandbox execution wrapper script for high-risk commands; prioritizes Docker isolation (read-only root, cap-drop ALL, no-new-privileges, network none, read-only workspace mount in alpine:latest), falls back to bubblewrap (bwrap with ro-bind /, dev/proc isolation, unshare-net), and defaults to host execution with a warning when neither is installed. Automatically filters all output through sed crede
- HOW: Execute via `task sandbox -- <command>` or invoke script directly with command arguments.
- live: no live URLs
- conflicts: Fallback path executes directly on host system without resource or network constraints if Docker and bwrap are missing.

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

### files/solo-levelling/the harness/.env.template
- card: files/solo-levelling/the harness/.env.template | part parts/13-deve-solo.md:9201 | lines 87 | verdict Verified
- WHAT: Environment configuration template defining required API keys (Anthropic, Gemini, OpenAI), LiteLLM proxy settings, Langfuse telemetry endpoints, database connection URIs, and security secrets for the Autonomous Dev Harness.
- HOW: Copy .env.template to .env before starting agent workflows: cp .env.template .env
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

### files/solo-levelling/the harness/.harness/sandbox/gate.sh
- card: files/solo-levelling/the harness/.harness/sandbox/gate.sh | part parts/13-deve-solo.md:10304 | lines 238 | verdict Verified
- WHAT: Linux namespace (Bubblewrap) and container (Docker/Podman) blast-radius isolation script enforcing read-only root filesystems, isolated process trees, credential masking, timeout enforcement, and air-gapped network modes.
- HOW: Invoke shell commands through sandbox gate: .harness/sandbox/gate.sh [OPTIONS] -- COMMAND [ARGS...]
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

### files/solo-levelling/the harness/scripts/run_validation.sh
- card: files/solo-levelling/the harness/scripts/run_validation.sh | part parts/13-deve-solo.md:32910 | lines 89 | verdict Unverified
- WHAT: Validation runner scaffolding timestamped scratch/validation/<ARCH>-<TS>/ runs with build-verify.yaml copy, git diagnostics, and friction-log reminders.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

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

### files/deve/.harness/permissions/check.py
- card: files/deve/.harness/permissions/check.py | part parts/13-deve-solo.md:38421 | lines 60 | verdict Verified
- WHAT: Runnable ABAC permission checker mirroring policies.cedar in Python. Denies sensitive paths (/etc, /root, .ssh, .aws, .gnupg, gcloud); requires approval + valid token for class-3 actions (git_push_main, drop_database, terraform_apply_production, publish_package); permits reads for anyone; permits workspace writes for Coder/DevOps/Planner; default-denies otherwise. Supports --selftest (6 assertions
- HOW: Invoke as the abac-check pre-tool hook for class-3 triggers, passing {principal,action,resource,has_approval,token_valid} on stdin.
- live: no live URLs
- conflicts: Divergence from policies.cedar: check.py substring-matches SENSITIVE_PATHS (e.g. 'gcloud') for ANY action, while policies.cedar forbids via path-like patterns with no plain 'gcloud' token., check.py loads presets.json into an unused PRESETS global, so presets are not actually enforced by the checker.

### files/deve/.harness/sandbox/gate.sh
- card: files/deve/.harness/sandbox/gate.sh | part parts/13-deve-solo.md:38604 | lines 59 | verdict Verified
- WHAT: Sandbox command runner (`task sandbox -- <command>`). Prefers Docker isolation (read-only root, cap-drop ALL, no-new-privileges, network none, memory/cpu limits, workspace mounted ro with an output rw bind), falls back to bubblewrap (ro-bind /, unshare-net), finally host execution (refused only when SANDBOX_STRICT=1). All output is piped through a credential-masking sed filter.
- HOW: Run `task sandbox -- <command>` for high-risk commands; args after -- are joined into the command.
- live: no live URLs
- conflicts: On the fallback branch the command runs unsandboxed on the host with no limits; SANDBOX_STRICT defaults to 0, so isolation is opt-in, not default., COMMAND is built from "$*" unquoted and passed via `sh -c`, so quoting/word-splitting semantics differ from a normal shell invocation.

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

### files/deve/lefthook.yml
- card: files/deve/lefthook.yml | part parts/13-deve-solo.md:39772 | lines 17 | verdict Verified
- WHAT: Git hook configuration via lefthook: pre-commit runs secret-scan and py_compile on staged *.py files; pre-push runs scripts/verify.sh and the pytest suite.
- HOW: Install lefthook and run `lefthook install` to register the hooks.
- live: no live URLs
- conflicts: Duplicate enforcement with Taskfile.yml and scripts/verify.sh; the same secret-scan/pytest runs in three places, which can drift., Requires an external lefthook binary that the repo does not vendor, so the hooks are inert until installed.

### files/deve/os/artifacts/build-log-template.md
- card: files/deve/os/artifacts/build-log-template.md | part parts/13-deve-solo.md:39823 | lines 24 | verdict Verified
- WHAT: Living build-log template with a Session Log block per session capturing scopes worked, uphill/downhill status, decisions (flagging irreversible ones), rabbit holes, change events, appetite consumed, and next-session plan; append-only, declared the source of truth for launch-time state.
- HOW: Copy into projects/<name>/build-log.md via `task new-project`.
- live: no live URLs
- conflicts: none

### files/deve/os/artifacts/design-note-template.md
- card: files/deve/os/artifacts/design-note-template.md | part parts/13-deve-solo.md:39848 | lines 41 | verdict Verified
- WHAT: Design Note template (Gate 4) requiring Context, Goals, minimum 2 Non-Goals, Design, minimum 1 rejected alternative, Rabbit Holes, Cross-cutting Concerns, and an FCAR Status block (not run / passed / passed with documented exception).
- HOW: Use for any change >1 day, external interface change, or irreversible decision.
- live: no live URLs
- conflicts: none

### files/deve/os/artifacts/launch-checklist-template.md
- card: files/deve/os/artifacts/launch-checklist-template.md | part parts/13-deve-solo.md:39890 | lines 24 | verdict Verified
- WHAT: Gate 6 launch checklist template: a pre-deploy rollback threshold statement (metric, %, 10-minute window, metric location, tested rollback command) followed by the 8-item verification table and a Gate 6 status line.
- HOW: Complete the rollback-threshold block BEFORE deploying.
- live: no live URLs
- conflicts: none

### files/deve/os/artifacts/pitch-template.md
- card: files/deve/os/artifacts/pitch-template.md | part parts/13-deve-solo.md:39915 | lines 28 | verdict Verified
- WHAT: Gate 3 pitch template: date, hard appetite limit, circuit-breaker date, Problem, Solution (fat-marker/breadboard sketch), Rabbit Holes, minimum 2 explicit No-gos, and a Reversibility Assessment listing irreversible commitments.
- HOW: Fill appetite and circuit-breaker date before any solution thinking (Gate 1/3).
- live: no live URLs
- conflicts: none

### files/deve/os/artifacts/postmortem-template.md
- card: files/deve/os/artifacts/postmortem-template.md | part parts/13-deve-solo.md:39944 | lines 31 | verdict Verified
- WHAT: Blameless postmortem template with metadata (incident/postmortem dates, severity, duration, blameless stance), Timeline, a Five-Whys root-cause chain explicitly chained to a systemic gap, and a Corrective Actions table (action/owner/due date/tracked) warning that untracked actions create false confidence.
- HOW: Use within 48 hours of incident resolution.
- live: no live URLs
- conflicts: none

### files/deve/os/artifacts/prfaq-template.md
- card: files/deve/os/artifacts/prfaq-template.md | part parts/13-deve-solo.md:39976 | lines 30 | verdict Verified
- WHAT: Working Backwards PR/FAQ template: a customer-perspective press release (problem, solution, concrete customer quote, getting started) plus an FAQ mandating at least 2 explicit non-goals, the most obvious alternative rejection, and an honest risk assessment.
- HOW: Use at idea stage before writing a pitch.
- live: no live URLs
- conflicts: none

### files/deve/os/gates.md
- card: files/deve/os/gates.md | part parts/13-deve-solo.md:40126 | lines 30 | verdict Verified
- WHAT: Decision-gate table (Gates 1-6) mapping trigger, artifact, blocking condition and override; the 5-item FCAR rubric summary; the hard-vs-soft gate override policy (hard = no override, soft = documented visible exception); and the tiny/default/high-stakes tiering rules.
- HOW: Route every project through Gates 1-6; treat hard gates as non-overridable.
- live: no live URLs
- conflicts: gates.md ties FCAR to Gate 4 as does CLAUDE.md; however the tier router exempts tiny projects from Gate 4/6 with no code enforcement.

### files/deve/scripts/scope-check.py
- card: files/deve/scripts/scope-check.py | part parts/13-deve-solo.md:40336 | lines 106 | verdict Verified
- WHAT: Automated scope gate: parses a pitch's No-gos/Non-Goals section (bullets, numbered, or star), lowercases and stopword-filters both task and No-gos, flags a conflict when >=2 content words overlap, has a --tier tiny option that warns+passes on a missing section, and returns exit 1 on conflict or (default tier) a missing section.
- HOW: Run `python3 scripts/scope-check.py --task "<task>" --pitch "<path-to-pitch.md>"`.
- live: no live URLs
- conflicts: Documented false-negative: a synonym task sharing <2 tokens with a No-go passes (test_synonym_false_negative_documented)., Exit code 1 is overloaded (real conflict vs missing section); the scope-gate workflow assumes exit_code==0 == approved and cannot distinguish the two.

### files/deve/scripts/secret-scan.sh
- card: files/deve/scripts/secret-scan.sh | part parts/13-deve-solo.md:40443 | lines 43 | verdict Verified
- WHAT: Secret scanner: greps recursively for 7 patterns (api_key/secret/password/token assignments, plus ASIA/sk-/ghp_ prefixes), excluding .git, node_modules, *.env.template, secret-scan.sh itself and GOD_PROMPT.md; prints matches and exits 1 if any are found, 0 if clean.
- HOW: Run `bash scripts/secret-scan.sh [target]` (default target .).
- live: no live URLs
- conflicts: Excludes *.env.template, secret-scan.sh and GOD_PROMPT.md by name and only matches quoted secrets; unquoted assignments are missed - pre_tool_guard covers some unquoted forms, so the two scanners are complementary but inconsistent.

### files/deve/scripts/verify.sh
- card: files/deve/scripts/verify.sh | part parts/13-deve-solo.md:40883 | lines 75 | verdict Verified
- WHAT: Master verification gate: runs secret-scan, AST syntax checks for the guard and scope-check, existence checks for every OS doc/template/harness config/skill/CLAUDE.md, the pytest suite, a flake8/ruff/py_compile lint fallback, the permissions --selftest, and a check that no __pycache__/.pyc are git-tracked; then cross-checks each skill dir against a workflows/*.yaml (with explicit cases for fcar-re
- HOW: Run `bash scripts/verify.sh` (Taskfile's `task verify` also runs lint/test/secret-scan).
- live: no live URLs
- conflicts: The skill/workflow cross-check only WARNs on a missing/mismatched workflow yaml and still exits 0 if no hard check failed, so a broken skill->workflow binding does not fail the gate., The 'no __pycache__/.pyc tracked' check uses `git ls-files`; if run outside a git repo, verify.sh fails on that check even though other checks pass.

### files/builders-playbook/product_engineering/report/06-automation-stack-workflows.md
- card: files/builders-playbook/product_engineering/report/06-automation-stack-workflows.md | part parts/14-bp-report.md:760 | lines 106 | verdict Verified
- WHAT: System architecture specification detailing the 12-layer automation stack (from VCS/CI to AIOps) and 9 end-to-end workflow reconstructions, distinguishing empirically verified production implementations (GitHub Copilot agent, Sentry Seer, GitHub environments, Anthropic multi-agent research) from proposed reference designs.
- HOW: Follow the decision ladder to select between deterministic scripts, structured workflows, autonomous agents, and multi-agent systems.
- live: no live URLs
- conflicts: Autonomous developer efficiency claims vs GitHub and OpenAI telemetry showing agent traffic driving a 10x surge in CI/CD pipeline load., High SAST scanner adoption vs benchmarked 43-61% detection blind spots and 41-50% false positive rates.

### files/builders-playbook/product_engineering/report/16-implementation-roadmap.md
- card: files/builders-playbook/product_engineering/report/16-implementation-roadmap.md | part parts/14-bp-report.md:2208 | lines 160 | verdict Partially
- WHAT: Proposed 4-phase implementation roadmap sequencing engineering capabilities to ensure verification capacity precedes generation scale: Phase 0 Foundations (releasable mainline, one-command builds, managed runtime, golden signals, rehearsed rollback; exit via Gates 8 and 9 lightweight); Phase 1 First Loop (running one complete discovery-to-measure bet end-to-end, supervised coding agents, UX states
- HOW: Execute Phase 0 before writing product features: establish git branch protection, automated CI, golden signal telemetry, and rehearsed rollback.
- live: no live URLs
- conflicts: Calendar-driven project management vs quality-gate-driven phased transitions, Vendor pressure to scale AI coding immediately vs empirical requirement to harden review and verification gates first

### files/builders-playbook/product_engineering/report/17-checklists-templates.md
- card: files/builders-playbook/product_engineering/report/17-checklists-templates.md | part parts/14-bp-report.md:2369 | lines 271 | verdict Verified
- WHAT: Engineering checklists and templates repository: Problem-discovery checklist (12 checkpoints with evidence requirements and kill rules), Decision-criteria gate (7 criteria scored Pass/Conditional/Fail with fail-stops-all rule), Validation stage gates (per-experiment verdicts Validated/Invalidated/Inconclusive and per-idea gates Problem through Scale), 9 Quality-gate tables (Discovery to Post-launc
- HOW: Run the Problem-discovery checklist and Decision-criteria gate before investing engineering resources in solution building.
- live: no live URLs
- conflicts: Self-reported developer or agent completion vs independent re-checkable artifact requirement, Perceived high quality of demos vs audited reality inventories revealing simulated backend logic

### files/builders-playbook/product_engineering/research/domain-a/08-cicd-deployment.md
- card: files/builders-playbook/product_engineering/research/domain-a/08-cicd-deployment.md | part parts/15-bp-core-research.md:1247 | lines 69 | verdict Verified
- WHAT: AI-Assisted CI/CD and Deployment practices (Domain A, Area 8): agents authoring and hardening CI/CD pipelines (GitHub Actions skills, OIDC pinning, workflow optimization); CI as the non-negotiable enforcement layer for agentic development (PR quality gates: build, full test suite, lint, SAST, CVE scans; main merge gates: versioned snapshots, staging CD, releasability flags); identical harness enfo
- HOW: Use specialized CI agent skills to generate and harden GitHub Actions workflows, ensuring actions are pinned to commit SHAs and OIDC is configured properly.
- live: no live URLs
- conflicts: Autonomous agent delivery claims ('Scrum team as code') vs empirical enterprise reality of 70-95% unassisted pilot failure without strict CI gates

### files/builders-playbook/product_engineering/research/domain-b/08-evals.md
- card: files/builders-playbook/product_engineering/research/domain-b/08-evals.md | part parts/15-bp-core-research.md:2234 | lines 82 | verdict Verified
- WHAT: AI Product Evaluation Systems and Practices (Domain B, Area 8): rationale and methodology for evaluating non-deterministic AI products; the four-layer evaluation stack (golden datasets versioned like code with 20-30% holdouts; deterministic assertions ~60% of mix; calibrated LLM-as-judge ~30% with multi-judge and position-swap bias controls; human evaluation ~10% for reference calibration and 1-5%
- HOW: Curate a versioned golden dataset of representative inputs, edge cases, and past failure incidents, maintaining a 20-30% holdout split that is never used during prompt engineering.
- live: no live URLs
- conflicts: Subjective playground inspection vs statistically grounded CI evaluation suites, Uncalibrated LLM-as-judge scores vs human-calibrated multi-layer eval rubrics

### files/builders-playbook/product_engineering/research/quality/03-quality-gates.md
- card: files/builders-playbook/product_engineering/research/quality/03-quality-gates.md | part parts/15-bp-core-research.md:5646 | lines 200 | verdict Verified
- WHAT: Practical Quality-Gate System (§23): governing principles including the Evidence Principle ('a passing build, green tests, pretty screenshot, or agent "done" must NEVER alone count as proof of readiness' due to assertion weakening and status hallucination); three strict verdicts (GO, NO-GO, NOT ASSESSED, with precedence NO-GO > NOT ASSESSED > GO); three-tier risk calibration (Tier 1 High, Tier 2 S
- HOW: Evaluate readiness against concrete artifacts that a stranger could independently inspect (test reports with assertion counts, signed security audits, performance traces), never subjective status declarations.
- live: no live URLs
- conflicts: Agent status assertions and green CI builds vs substantive evidence of correctness and rigorous test assertion density, Rapid continuous deployment pressure vs disciplined phase-gate verification

### files/builders-playbook/product_engineering/research/automation/02-workflows.md
- card: files/builders-playbook/product_engineering/research/automation/02-workflows.md | part parts/15-bp-core-research.md:6233 | lines 267 | verdict Verified
- WHAT: Nine end-to-end workflow reconstructions (W1 idea-to-concept through W9 parallel-agent research) sharing a ten-part anatomy of triggers, inputs, decisions, tool calls, state changes, validation, outputs, failure handling, permissions, and approvals; four workflows are marked PROPOSED reference designs and five are VERIFIED reconstructions of documented GitHub, Sentry, and Anthropic practice.
- HOW: Treat every automation as proposing and the pull request with CI plus human review as disposing; never let agents merge on their own word.
- live: no live URLs
- conflicts: Anthropic multi-agent gains vs Cognition warnings against parallel writers, resolved as different problem classes with writes kept single-threaded.

### files/builders-playbook/product_engineering/research/rules/04-templates/00-index.md
- card: files/builders-playbook/product_engineering/research/rules/04-templates/00-index.md | part parts/17-bp-evidence-playbook.md:7627 | lines 43 | verdict Unverified
- WHAT: Master map of the 18 fill-ready lifecycle templates in order, defining when the minimal small-bet chain suffices versus the full large-bet sequence, with shared conventions (prompt italics, checkboxes, N/A-with-reason, named rules) and co-location-with-code guidance.
- HOW: Start at problem validation and follow the chain appropriate to the bet size
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/rules/04-templates/01-problem-validation.md
- card: files/builders-playbook/product_engineering/research/rules/04-templates/01-problem-validation.md | part parts/17-bp-evidence-playbook.md:7671 | lines 55 | verdict Unverified
- WHAT: Problem-validation template proving a problem is real before resourcing a bet: customer-worded statement, evidence log demanding at least three independent sources, four-risk retirement verdicts, disconfirming voices, and an explicit proceed, park, or kill decision with acceptance criteria.
- HOW: Fill the evidence log from independent sources before writing any solution text
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/rules/04-templates/02-idea-evaluation.md
- card: files/builders-playbook/product_engineering/research/rules/04-templates/02-idea-evaluation.md | part parts/17-bp-evidence-playbook.md:7727 | lines 57 | verdict Unverified
- WHAT: Idea-evaluation template scoring two to four candidate solutions plus a do-nothing baseline against weighted outcome, risk, and appetite criteria, producing a winner with pre-written kill criteria and a recorded rejection rationale for the rest.
- HOW: Define weighted criteria before scoring any candidate
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/rules/04-templates/03-prd.md
- card: files/builders-playbook/product_engineering/research/rules/04-templates/03-prd.md | part parts/17-bp-evidence-playbook.md:7785 | lines 69 | verdict Unverified
- WHAT: Press-release-first PRD template (full form for significant bets, sections 1-3 only as PR/FAQ for small ones) with headline, FAQ including dreaded questions, outcome metric with kill criteria and guardrails, appetite with scope and no-gos, fat-marker UX flows covering all states, and an open-questions table.
- HOW: Write the press release and FAQ before any design artifact
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/rules/04-templates/04-technical-design-document.md
- card: files/builders-playbook/product_engineering/research/rules/04-templates/04-technical-design-document.md | part parts/17-bp-evidence-playbook.md:7855 | lines 71 | verdict Unverified
- WHAT: Technical design template covering architecture, interfaces, data, and novelty justification, with a mandatory per-integration failure-mode table, blast-radius and rollback planning, trust-boundary security, golden-signal operability, alternatives, and a rollout and migration plan with flags.
- HOW: Fill one failure row per integration: timeout, retry, breaker, bulkhead, fallback
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/rules/04-templates/05-architecture-decision-record.md
- card: files/builders-playbook/product_engineering/research/rules/04-templates/05-architecture-decision-record.md | part parts/17-bp-evidence-playbook.md:7927 | lines 45 | verdict Unverified
- WHAT: Twenty-minute architecture decision record: title, status, date, deciders, context with constraints, the decision itself, good and bad consequences with reversal cost and innovation-token spend, alternatives, and filing/linking acceptance so rationale and undo cost survive with the code.
- HOW: Write the ADR at decision time, not retrospectively
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/rules/04-templates/06-design-system-definition.md
- card: files/builders-playbook/product_engineering/research/rules/04-templates/06-design-system-definition.md | part parts/17-bp-evidence-playbook.md:7973 | lines 66 | verdict Unverified
- WHAT: Shared-UI-foundations template used only when two or more surfaces share UI: scope with non-goals, three to five principles with opposites, token and component tables noting borrowed-vs-built provenance with all states and accessibility, patterns, an accessibility baseline with checking, and lightweight governance.
- HOW: Prove multi-surface sharing need before defining anything
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/rules/04-templates/07-prototype-acceptance.md
- card: files/builders-playbook/product_engineering/research/rules/04-templates/07-prototype-acceptance.md | part parts/17-bp-evidence-playbook.md:8040 | lines 50 | verdict Unverified
- WHAT: Prototype-acceptance template separating real from simulated capabilities: what was asked, a mandatory reality-inventory table per capability, learnings with feasibility surprises, a default-throwaway versus evolve verdict, and a proceed, iterate, or kill decision.
- HOW: Inventory every demonstrated capability as real or simulated — no blanks
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/rules/04-templates/08-development-task-definition.md
- card: files/builders-playbook/product_engineering/research/rules/04-templates/08-development-task-definition.md | part parts/17-bp-evidence-playbook.md:8091 | lines 53 | verdict Unverified
- WHAT: Single-unit build task definition for human or agent: one-sentence task sized to one or two days, context links, in-scope and out-of-scope with do-not-touch areas, checkable acceptance criteria with tests and docs, mandatory verification steps including transcripts for agents, and risks with unknowns.
- HOW: Keep the unit to a day or two; split anything larger
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/rules/04-templates/09-agent-instructions.md
- card: files/builders-playbook/product_engineering/research/rules/04-templates/09-agent-instructions.md | part parts/17-bp-evidence-playbook.md:8145 | lines 64 | verdict Unverified
- WHAT: Standing repository agent instructions (e.g., AGENTS.md): authority tiers of allowed, needs-approval, and forbidden actions, task-execution rules for small boring diffs, a non-negotiable verification checklist, a tool and permission manifest, failure and escalation behavior, and workflow-versus-agent choice guidance.
- HOW: Declare the three authority tiers before granting any tool access
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/rules/04-templates/10-test-plan.md
- card: files/builders-playbook/product_engineering/research/rules/04-templates/10-test-plan.md | part parts/17-bp-evidence-playbook.md:8210 | lines 59 | verdict Unverified
- WHAT: Proportional verification plan: scope, automated critical-path gates through production-shaped paths, a test matrix spanning happy, error, failure-mode, migration, content, accessibility, and performance cases, environment parity with production synthetics, a 48-hour flaky-test quarantine policy, and entry/exit criteria.
- HOW: Gate release on critical paths exercised through production-shaped paths
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/rules/04-templates/11-code-review.md
- card: files/builders-playbook/product_engineering/research/rules/04-templates/11-code-review.md | part parts/17-bp-evidence-playbook.md:8270 | lines 57 | verdict Unverified
- WHAT: Dual code-review checklist pairing author preparation (small diff, demonstrated verification, explainable AI-generated code, no secrets or dead code, stated why with a low/standard/high risk tier) with reviewer scrutiny (correctness, design fit, security, operability, test adequacy) and four outcomes including escalate.
- HOW: Authors declare the risk tier and complete prep before requesting review
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/rules/04-templates/12-ux-visual-qa.md
- card: files/builders-playbook/product_engineering/research/rules/04-templates/12-ux-visual-qa.md | part parts/17-bp-evidence-playbook.md:8328 | lines 63 | verdict Unverified
- WHAT: Pre-release UX and visual pass: scope with devices and browsers, a mandatory per-flow states table (loading, empty, error, offline, permission, rate-limit, destructive, success), responsive checks on real devices, token and visual verification, accessibility spot-checks, and content review with no placeholders and user-worded errors.
- HOW: Walk every flow through each state in the table; mark genuinely inapplicable states with reason
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/rules/04-templates/13-security-verification.md
- card: files/builders-playbook/product_engineering/research/rules/04-templates/13-security-verification.md | part parts/17-bp-evidence-playbook.md:8392 | lines 72 | verdict Unverified
- WHAT: OWASP-ASVS-structured security gate targeting Level 1 minimum (Level 2 for sensitive data): scope with target level, threat-model table including agent tools, per-requirement gap register with verdict, evidence, owner, and date, automated scan results, AI-code sign-off, and disclosure-readiness checks.
- HOW: Threat-model trust boundaries at design time, not as a pre-launch scramble
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/rules/04-templates/14-release-readiness.md
- card: files/builders-playbook/product_engineering/research/rules/04-templates/14-release-readiness.md | part parts/17-bp-evidence-playbook.md:8465 | lines 62 | verdict Unverified
- WHAT: Per-release go/no-go gate: release identity down to build ID, commit, and pipeline, verification evidence (CI, critical paths, review, security, UX QA), rollout steps with flags and migrations, exact rehearsed rollback with kill switch, operability (dashboards, alerts, on-call, AI cost), comms, and a signed GO/NO-GO with named dated exceptions.
- HOW: Assemble verification, rollout, reversibility, and operability evidence in one record
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/rules/04-templates/15-incident-response.md
- card: files/builders-playbook/product_engineering/research/rules/04-templates/15-incident-response.md | part parts/17-bp-evidence-playbook.md:8528 | lines 75 | verdict Unverified
- WHAT: Two-part incident template: run the event (declare severity, name commander and channel, loop assess-mitigate-communicate-record until resolved and closed) then produce a blameless systems-focused postmortem within five days with factual timeline, impact, contributing factors, what went well, and owned dated actions.
- HOW: Declare severity and command early; communicate on a cadence even without news
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/rules/04-templates/16-post-launch-evaluation.md
- card: files/builders-playbook/product_engineering/research/rules/04-templates/16-post-launch-evaluation.md | part parts/17-bp-evidence-playbook.md:8604 | lines 53 | verdict Unverified
- WHAT: Bet-judgment template comparing pre-committed metric, baseline, and target against actuals plus guardrails and qualitative signal, explaining the gap in data versus belief, and forcing a keep, bounded-fix, or kill decision with a removal plan — no wait-and-see allowed.
- HOW: Copy the committed metric, baseline, and target verbatim before entering actuals
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/rules/04-templates/17-product-authenticity-polish.md
- card: files/builders-playbook/product_engineering/research/rules/04-templates/17-product-authenticity-polish.md | part parts/17-bp-evidence-playbook.md:8658 | lines 77 | verdict Unverified
- WHAT: Gawande-style killer-items polish checklist across ten dimensions — visual identity, functional completeness with no dead controls, responsive behavior, accessibility, content quality, realistic disclosed demos, full UX states, security basics, privacy with consent and minimization, and trust through honest pricing, claims, support, and terms.
- HOW: Walk all ten dimensions; mark items pass, fixed, or reasoned N/A
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/rules/04-templates/18-launch-readiness.md
- card: files/builders-playbook/product_engineering/research/rules/04-templates/18-launch-readiness.md | part parts/17-bp-evidence-playbook.md:8736 | lines 66 | verdict Unverified
- WHAT: Final public-launch gate in two parts: technical correctness and operability (build and deploy provenance, reliability and scale with load and breaking-point knowledge, backups with recovery objectives, on-call coverage, security and privacy posture, observability with cost and analytics) plus whole-product new-user experience (stranger first-run, polish pass, content, pricing, support, status) wi
- HOW: Complete the technical half and the stranger first-run half independently
- live: no live URLs
- conflicts: none

### files/builders-playbook/02-project-execution-plan.md
- card: files/builders-playbook/02-project-execution-plan.md | part parts/17-bp-evidence-playbook.md:185 | lines 138 | verdict Unverified
- WHAT: Personal project operating system for solo builders: six phases (intake, quick validation, light spec, build, ship, iterate) with exit gates, the nine-report-gates-to-five-solo-gates mapping with verdict discipline, the 30-minute weekly ritual and 45-minute pre-build sit-down, the five-bullet daily build-log habit, the 15-minute blameless retrospective format, the hackathon-vs-project mode compres
- HOW: Run new work through the six phases with Bet/Merge/Release/Ship/Watch gates and dated build-log evidence
- live: no live URLs
- conflicts: none

### files/builders-playbook/03-checklists.md
- card: files/builders-playbook/03-checklists.md | part parts/17-bp-evidence-playbook.md:324 | lines 71 | verdict Unverified
- WHAT: Solo-sized print-friendly checklists with per-item sourcing: pre-hackathon prep (rubric, track, evaluator, boring stack, repo/CI/secrets, deploy path, mocks, video plan, sit-down, sleep), the three during-hackathon gates (Deployment, Testing, Implementation with Proposed hour boundaries), the demo-day checklist (backup video, script, reality inventory, no dead controls or placeholder copy, effort-
- HOW: Run pre-hackathon prep before the clock starts, including deploy-path and backup-video checks
- live: no live URLs
- conflicts: none

### files/builders-playbook/templates/battle-plan-48h.md
- card: files/builders-playbook/templates/battle-plan-48h.md | part parts/17-bp-evidence-playbook.md:689 | lines 68 | verdict Unverified
- WHAT: Fill-in-ready one-page 48-hour battle-plan template adapting the base-report PRD and evaluation-date templates: event and cutoff header, demo-moment outcome metric, judging-criteria mapping table with kill rule, hero-feature block with 3-minute filter, sacred cut list, prize-track call, five-phase battle rhythm with Proposed hours, insurance-moves checklist, roles-for-one timeboxes, and sign-off g
- HOW: Fill it in the 10-minute pre-hack sit-down before any coding starts
- live: no live URLs
- conflicts: none

### files/builders-playbook/templates/build-log.md
- card: files/builders-playbook/templates/build-log.md | part parts/17-bp-evidence-playbook.md:873 | lines 19 | verdict Unverified
- WHAT: Daily build-log template adapting the incident-response and stop-discipline templates into a five-bullet habit: status, changed (links not prose), decisions as solo ADRs, blockers with next steps, and gate verdicts with unknowns-never-pass discipline, framed as the evidence artifact for every gate.
- HOW: Copy one block per day into the project file, newest at the bottom
- live: no live URLs
- conflicts: none

### files/builders-playbook/templates/demo-script.md
- card: files/builders-playbook/templates/demo-script.md | part parts/17-bp-evidence-playbook.md:819 | lines 53 | verdict Unverified
- WHAT: Three-minute demo-script template adapting prototype-acceptance and demo-authenticity checklists: 10-second hook, 90-second live hero demo with user-narrated steps, 30-second reality inventory table with spoken disclosure, 30-second how-it-works engineering proof, 20-second impact close with sponsor-track landing, plus before-recording backup-video insurance and after-recording complement-and-subm
- HOW: Script the 3-minute video in the five beats before recording
- live: no live URLs
- conflicts: none

### files/builders-playbook/templates/idea-evaluator.md
- card: files/builders-playbook/templates/idea-evaluator.md | part parts/17-bp-evidence-playbook.md:758 | lines 60 | verdict Unverified
- WHAT: Idea-evaluator template adapting the base-report idea-evaluation template by replacing scored dimensions with one operational filter: one-sentence idea and problem statement, judge-first lean-in filter with the 3-minute demo decision tree, problem-solution-impact story test, five-item Verified score-killer screen, sponsor-track fit check, two-hour validation bet design, and a build/scope-down/kill
- HOW: Run one sheet per idea after 30-60 minutes of wide generation
- live: no live URLs
- conflicts: none

### files/builders-playbook/templates/project-retrospective.md
- card: files/builders-playbook/templates/project-retrospective.md | part parts/17-bp-evidence-playbook.md:893 | lines 33 | verdict Unverified
- WHAT: Project retrospective template merging incident-postmortem and post-launch-evaluation templates into a 15-minute (5-minute hackathon) bullets-only format: metric-copied verdict line, Repeat section for practices to keep, Kill section where each item produces one concrete OS change, Lessons section feeding the idea parking lot, and the 5-minute abandonment retro distinguishing appetite problems fro
- HOW: Run within 48 hours of the keep/fix/kill verdict with the metric copied from the bet doc
- live: no live URLs
- conflicts: none

