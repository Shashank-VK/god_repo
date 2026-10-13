# Anti-patterns

By severity/source order.

### files/opencode-research/README.md
- card: files/opencode-research/README.md | part parts/01-opencode-research-root.md:1 | lines 162 | verdict Verified
- WHAT: Comprehensive index, phase tracker (Phases 0 through 7), directory map, live repository verification corrections, and locked-in architectural decisions for the OpenCode ecosystem research harness.
- HOW: Consult Phase Status (0-7) to navigate specific research notes from anti-hallucination passes to autonomous agent architecture
- live: no live URLs
- conflicts: none

### files/opencode-research/verification.md
- card: files/opencode-research/verification.md | part parts/01-opencode-research-root.md:164 | lines 75 | verdict Verified
- WHAT: Final verification checklist reconciling all 26 catalog elements from catalog.md, 15 selected research tools, and 4 walkinglabs harness templates, documenting inclusion/exclusion rationale for the OpenCode build prompt.
- HOW: Verify tool inclusion against the 26-element catalog accounting table (Section 1)
- live: no live URLs
- conflicts: none

### files/opencode-research/catalog.md
- card: files/opencode-research/catalog.md | part parts/02-opencode-catalog-26.md:1 | lines 2994 | verdict Verified
- WHAT: Authoritative 26-element OpenCode ecosystem research catalog and master index auditing 163 usable resources and 43 excluded Claude-Code-only tools across Skills, Permission Modes, Checkpoints/Rewind, Context Management, Hooks, MCP Servers, Sandboxing, Subagents, Plugins/Marketplaces, Output Styles, Background Tasks, Security Review, Headless CI, Cost/Usage Tracking, Agent-Team Frameworks, Workflow
- HOW: Consult the 26-element master table (lines 8-36) to audit available tooling counts (163 usable vs 43 excluded) across OpenCode SDLC phases.
- live: no live URLs
- conflicts: Native sandboxing gap: OpenCode permissions are UX confirmation boundaries, not security isolation; true containment requires external Docker/VM containers., Python SDK gap: OpenCode lacks an official Python SDK (open issue #4031); developers must use official JS/TS or Go SDKs or author plugins directly in JS/TS., StatusLine customization gap: OpenCode lacks Claude Code native JSON statusLine shell pipe hook (issues #30295, #8619 open), requiring TUI sidebar/footer plugins (sub-agent-statusline, token-tracker)., Decentralized marketplace: OpenCode lacks a centralized official plugin marketplace, relying on community registries (awesome-opencode, opencode-market, opencode-marketplace, OCX)., Excluded Claude Code tooling: 43 tools (including garrytan/gstack, native /rewind, Shift+Tab toggles) are Claude-exclusive and incompatible without dedicated translation adapters.

### files/opencode-research/research/00-verification.md
- card: files/opencode-research/research/00-verification.md | part parts/03-opencode-research-phases.md:1 | lines 83 | verdict Verified
- WHAT: Phase 0 Verification Report establishing empirical ground truth across five audit sections: Section A (re-checks facebook/astryx, karpathy/llm-council, okjpg/llm-council unverifiable, ngmeyer/council-review archived into ngmeyer/skills, Graphify-Labs/graphify 104k+ stars; notes Astryx MCP claim was wrong and uses bash CLI only); Section B (corrects ruvnet/ruflo formerly Claude Flow, emilkowalski/s
- HOW: Consult Section A and B corrections before adding dependencies (use ruvnet/ruflo instead of rufl0, emilkowalski/skills instead of enilkowaski, teng-lin/notebooklm-py with breakage caveats)
- live: no live URLs
- conflicts: facebook/astryx MCP claim corrected in Phase 8: packages/mcp returned 404, integration is bash CLI calls only: npx @astryxdesign/cli <command> --dense, walkinglabs five layers framework does not reside at docs/en/resources/templates/index.md (which is a template guide); canonical layers in repo are Instructions, State, Verification, Scope Boundaries, Lifecycle Handoff rather than the paraphrased diagnostic layers

### files/opencode-research/research/00-gaps-and-unknowns.md
- card: files/opencode-research/research/00-gaps-and-unknowns.md | part parts/03-opencode-research-phases.md:85 | lines 67 | verdict Verified
- WHAT: Phase 0 Gaps and Unknowns report cataloging unverifiable items, retired or security-flagged tooling, fragile unofficial APIs, URL content discrepancies, name mismatches, and identified ecosystem gaps: records okjpg/llm-council as completely unverifiable and flagged for exclusion in Phase 5; documents ngmeyer/council-review archived and migrated to ngmeyer/skills; warns against gsd-build/get-shit-d
- HOW: Consult Completely Unverifiable section to exclude ghost repos (okjpg/llm-council) from research passes and build prompts
- live: no live URLs
- conflicts: none

### files/opencode-research/research/01-existing-summary.md
- card: files/opencode-research/research/01-existing-summary.md | part parts/03-opencode-research-phases.md:153 | lines 224 | verdict Verified
- WHAT: Phase 1 Existing Research Summary distilling the 26-element OpenCode ecosystem research catalog (163 usable resources across skills, permissions, checkpoints, context management, hooks, MCPs, sandboxes, subagents, plugins, themes, tasks, security review, CI, cost tracking, multi-agent frameworks, workflows, SDKs, methodologies, doc MCPs, statuslines, worktrees, awesome-lists, security scanners, gu
- HOW: Use each element paragraph as a self-contained summary to understand OpenCode ecosystem tooling coverage without reloading the full multi-file discovery catalog.
- live: no live URLs
- conflicts: none

### files/opencode-research/research/02-ui-ux.md
- card: files/opencode-research/research/02-ui-ux.md | part parts/03-opencode-research-phases.md:378 | lines 250 | verdict Verified
- WHAT: Phase 2 research findings on UI/UX, design systems, frontend and backend resources, and agent-usable 3D web templates: establishes facebook/astryx (React 19+/StyleX design system with CLI bash integration) as Top Pick #1, keysjoao/laws-of-ux-skills (SKILL.md package for UX guidance/audit/pre-ship) as Top Pick #2, VoltAgent/awesome-design-md (DESIGN.md plain-text design tokens/intent) as Top Pick #
- HOW: For Astryx frontend components: Scaffold with 'npx @astryxdesign/cli init --features agents' to generate AGENTS.md component inventory, then execute CLI queries via bash 'npx @astryxdesign/cli component <Name> --dense' to retrieve token-efficient props without hallucination
- live: no live URLs
- conflicts: Astryx integration method conflict: Section A notes native MCP server in opencode.json, but Section E / Phase 8 correction notes MCP package was not found in repo and requires CLI bash calls: npx @astryxdesign/cli component <Name> --dense

### files/opencode-research/research/03-multi-agent-council.md
- card: files/opencode-research/research/03-multi-agent-council.md | part parts/03-opencode-research-phases.md:629 | lines 192 | verdict Verified
- WHAT: Phase 3 multi-agent deliberation and hallucination-reduction research: comparative analysis of llm-council forks (karpathy/llm-council, unconfirmed okjpg/llm-council, ngmeyer/council-review, ngmeyer/skills, native deliberation plugin, and Open Conclave), architectural assessment of n8n MCP integration, empirical survey of Mixture-of-Agents (MoA) and 2025 Self-MoA aggregation dynamics, and producti
- HOW: Trigger the Two-Judge Verification Pass selectively on high-stakes tasks: architectural decisions, algorithm selection, security-critical code, or suspicious primary agent responses; bypass for routine edits to avoid compounding latency.
- live: no live URLs
- conflicts: Repository status conflict: ngmeyer/council-review was previously misclassified as archived; verified live and active alongside parallel ngmeyer/skills monorepo., Catalog discrepancy: okjpg/llm-council cited in early catalogs does not exist as an independent GitHub repository and must be omitted., MoA performance assumption: 2024 MoA optimism qualified by 2025 Self-MoA findings showing repeated sampling from a top model plus synthesis matches or beats diverse smaller models, while saturated benchmarks mask persistent failures on frontier tests., n8n orchestration mismatch: Presumed bi-directional MCP integration actually requires n8n to act as orchestrator over OpenCode rather than OpenCode driving n8n.

### files/opencode-research/research/04-harness-environment.md
- card: files/opencode-research/research/04-harness-environment.md | part parts/03-opencode-research-phases.md:822 | lines 173 | verdict Verified
- WHAT: Phase 4 research findings on harness engineering, environment integration, and session governance: debunking native OpenCode terminal to Antigravity DOM inspection claims while providing the MCP browser bridge configuration (puppeteer/playwright/@modelcontextprotocol/server-puppeteer); confirming full native OpenCode slash command support in Antigravity's PTY terminal (.opencode/commands/ and ~/.c
- HOW: For browser/DOM inspection from OpenCode terminal: Configure an MCP server in opencode.json under mcp.browser using npx -y @modelcontextprotocol/server-puppeteer, puppeteer, or playwright to enable navigate, click, screenshot, and evaluate_javascript tools
- live: no live URLs
- conflicts: Antigravity DOM inspection integration: False assumption of native zero-config IDE integration vs reality of separate terminal process requiring explicit MCP server bridge (@modelcontextprotocol/server-puppeteer), Claude Code proxying: Proposal to proxy Claude Code via claude-code-router rejected as unnecessary complexity and latency overhead given OpenCode native routing capabilities

### files/opencode-research/research/05-remaining-resources.md
- card: files/opencode-research/research/05-remaining-resources.md | part parts/03-opencode-research-phases.md:996 | lines 214 | verdict Verified
- WHAT: Phase 5 Remaining Named Resources research document detailing comprehensive, standardized 5-point evaluations (What it does, OpenCode support type, When to use, When NOT to use, Final verdict) for 20 verified ecosystem resources: Graphify-Labs/graphify (native AST codebase knowledge graph; top pick), ruvnet/ruflo (MCP swarm meta-harness with HNSW/SONA memory; power-user tool), emilkowalski/skills 
- HOW: For codebase comprehension: Install and invoke Graphify-Labs/graphify via native /graphify command to build dependency knowledge graphs without vector database overhead
- live: no live URLs
- conflicts: Security deprecation: gsd-build/get-shit-done was archived in June 2026 due to deep shell permissions; the active community-audited fork is open-gsd/gsd-core., Architectural layer boundary: vercel/eve is a framework for building standalone AI agents, not an extension or skill designed to run inside OpenCode., Stability caveat: teng-lin/notebooklm-py depends on undocumented Google internal RPCs that are vulnerable to silent breaking changes., KanakMalpani/LoopBench is an MLPerf-style benchmark evaluation suite rather than an active development loop harness.

### files/opencode-research/research/06-unfound-and-gaps.md
- card: files/opencode-research/research/06-unfound-and-gaps.md | part parts/03-opencode-research-phases.md:1211 | lines 60 | verdict Verified
- WHAT: Phase 6 ecosystem reconciliation report documenting unfound or distorted resources, resolved research contradictions, critical security status alerts, path misalignments, seven structural gaps in the 2026 OpenCode ecosystem with their practical workarounds, and the final seven-part research map: resolves non-existent okjpg/llm-council (redirects to ngmeyer/skills or deliberation plugin); confirms 
- HOW: Consult Unverifiable / Distorted Resources table before referencing or adding third-party repos: reject okjpg/llm-council, confirm KanakMalpani/Loop-Engineering, and avoid archived gsd-build
- live: no live URLs
- conflicts: okjpg/llm-council does not exist on public GitHub under that username; ecosystem alternative is ngmeyer/skills or native deliberation plugin., KanakMalpani/Loop-Engineering was previously incorrectly reported missing due to confusion with KanakMalpani/LoopBench; both repositories exist independently., ngmeyer/council-review was previously incorrectly marked archived; it is active and maintained alongside the ngmeyer/skills monorepo., gsd-build/get-shit-done was archived June 2026 for security; active fork is open-gsd/gsd-core., walkinglabs 5-layers URL points to live docs but does not contain the 5-layer framework at that path; framework resides elsewhere in the repo under alternate layer names.

### files/opencode-research/research/08-astryx-mcp.md
- card: files/opencode-research/research/08-astryx-mcp.md | part parts/03-opencode-research-phases.md:1615 | lines 169 | verdict Verified
- WHAT: Phase 8 Task 4 research verification of Astryx MCP configuration: confirms facebook/astryx is a live Meta/StyleX design system but contains no MCP server package or mcp CLI subcommand (404 on packages/mcp-server and packages/mcp, astryx.design/docs/mcp unresolving, zero MCP references in @astryxdesign/cli README); disproves circulating opencode.json MCP configuration snippet (which fails with ERR_
- HOW: Query components during UI builds via bash tool calls: npx @astryxdesign/cli search button --dense or npx @astryxdesign/cli component Button --dense
- live: no live URLs
- conflicts: Architecture doc (07-autonomous-agent-architecture.md) claims Astryx MCP tools are auto-called via MCP, but facebook/astryx contains no MCP server package or mcp subcommand; integration must use CLI bash tool calls with --dense instead of opencode.json MCP configuration.

### files/opencode-research/research/08-loopy-verification.md
- card: files/opencode-research/research/08-loopy-verification.md | part parts/03-opencode-research-phases.md:1785 | lines 175 | verdict Verified
- WHAT: Phase 8 Task 2 deep verification of Forward-Future/loopy: confirms loopy is an agent companion SKILL.md for the public Loop Library catalog (signals.forwardfuture.com/loop-library/) rather than a standalone loop execution engine; clarifies install path (npx skills add Forward-Future/loopy --skill loopy -g), absence of opencode.json config, minimal persistent state store limited to repo-root LOOPS.
- HOW: Install the loopy skill via the Agent Skills interactive installer: npx skills add Forward-Future/loopy --skill loopy -g (or platform-specific flags for codex, cursor, claude-code)
- live: no live URLs
- conflicts: Architecture doc (07-autonomous-agent-architecture.md) describes loopy as the bounded loop execution layer, but loopy is a guided SKILL.md for the Loop Library rather than an execution engine; bounded behavior is driven by loop design and agent adherence rather than engine-level controls., Integration gap: Loopy Run produces in-session run receipts that do not auto-propagate to walkinglabs feature_list.json evidence[], requiring explicit instruction in AGENTS.md.

### files/opencode-research/research/08-testing-qa.md
- card: files/opencode-research/research/08-testing-qa.md | part parts/03-opencode-research-phases.md:2166 | lines 198 | verdict Verified
- WHAT: Phase 8 Task 1 testing and QA automation evaluation for OpenCode: validates michaljach/opencode-browser (plugin wrapper around browsermcp.io for interactive Chrome/Edge browser automation via @browsermcp/mcp@0.1.3, requiring extension and interactive display, suited for in-session smoke testing) versus official Playwright AI agents (v1.56+ Planner, Generator, Healer via npx playwright init-agents 
- HOW: Primary test gate: Configure VERIFY_CMD=npx playwright test in init.sh to produce deterministic, assertion-backed pass/fail signals and test output evidence for feature_list.json
- live: no live URLs
- conflicts: Conflict between interactive browser automation and assertion testing: using browsermcp alone fails DoD requirements because it cannot run in headless CI and lacks assertion guarantees; resolved by pairing browsermcp for interactive smoke testing with Playwright CLI in init.sh as the authoritative DoD gate., Token efficiency tradeoff: playwright-mcp README warns against continuous MCP tool usage for routine test execution due to heavy schema and accessibility tree token overhead, recommending CLI-based test execution instead.

### files/God research/B-category-catalogs/01-core-web-tech.md
- card: files/God research/B-category-catalogs/01-core-web-tech.md | part parts/05-firstpass-B-catalogs.md:1 | lines 497 | verdict Verified
- WHAT: Comprehensive 2026 core web platform catalog and baseline reference covering 24 fundamental web technologies across 6 key layers: Markup & Standards (WHATWG HTML living standard, W3C CSS modular snapshots, WHATWG DOM); CSS Tooling & Preprocessors (Dart Sass, PostCSS 8); Language Specifications & Toolchains (ECMAScript TC39 drafts/signals, TypeScript 5.x/7.0 roadmap, JS engine triage notes V8/Spide
- HOW: Use WHATWG HTML and DOM living standards as definitive authoritative behavior for semantic elements, parsing, and DOM manipulation; track MDN BCD and Can I Use tables for cross-browser baseline capabilities.
- live: no live URLs
- conflicts: TypeScript transpile vs type-checking gap: Bundlers (esbuild, SWC) strip TypeScript types without verification; CI pipelines must explicitly run tsc --noEmit., Sass syntax transition: Legacy @import is deprecated in Dart Sass in favor of @use/@forward modules., HTML specification authority: W3C versioned HTML snapshots are superseded by the living standard maintained by WHATWG., Client storage encryption: IndexedDB provides origin isolation but is not encrypted at rest by default; sensitive PII requires explicit client-side cryptographic wrapping.

### files/God research/B-category-catalogs/02-frontend.md
- card: files/God research/B-category-catalogs/02-frontend.md | part parts/05-firstpass-B-catalogs.md:499 | lines 579 | verdict Verified
- WHAT: Comprehensive 2026 frontend catalog and architectural reference auditing 28 essential resources across 5 key functional areas: UI runtimes & compilation models (React 19 with React Compiler GA and RSC, Vue 3.5+ with Vapor Mode preview, Svelte 5 Runes, SolidJS 2.0 fine-grained reactivity, Angular v20/v21 Signals, Preact 3KB runtime, Qwik 2.x resumability, Lit 3 Web Components); Meta-frameworks & SS
- HOW: 1. UI Runtime Selection: Standardize on React 19 for expansive ecosystem scale and React Compiler auto-memoization; adopt Vue 3.5+ (with opt-in Vapor Mode) for SFC rapid delivery; leverage Svelte 5 (Runes) or SolidJS 2.0 for maximum runtime performance and fine-grained reactive updates without VDOM 
- live: no live URLs
- conflicts: Framework consolidation: Remix merged into React Router v7 (remix-run/react-router), deprecating standalone Remix package versions while Remix v3 explores an experimental bundler-free architecture., State separation boundary: Traditional global state stores (Redux, Zustand) frequently conflict with server caches when developers duplicate API responses; standard 2026 practice strictly delegates asynchronous server state to TanStack Query and restricts client stores to ephemeral UI state., RSC security boundary: React Server Components and Server Actions introduce secret exposure risks if server data flight payloads are not explicitly sanitized prior to streaming to the client browser., Reactivity model divergence: Svelte 5 introduces explicit Runes (, , ) deprecating legacy reactive declarations ($:), while Vue 3 introduces experimental opt-in Vapor Mode bypassing the virtual DOM entirely.

### files/God research/B-category-catalogs/03-backend.md
- card: files/God research/B-category-catalogs/03-backend.md | part parts/05-firstpass-B-catalogs.md:1079 | lines 540 | verdict Partially
- WHAT: Comprehensive 2026 backend reference catalog covering 26 core technologies across six architectural tiers: Server Runtimes (Node.js 20/22 LTS with Undici, streams, and worker threads; cross-referenced with Bun and Deno); Web Application & API Frameworks (Express.js 5.x with native promise routing, Fastify v5 high-throughput AJV schema engine, NestJS 10/11 enterprise DI and modular architecture, Ho
- HOW: 1. Backend framework selection: For TypeScript monoliths and team-scale architectures, standardize on NestJS with Fastify adapter (@nestjs/platform-fastify) or pure Fastify v5 for high-throughput microservices; use Hono v4 for multi-runtime edge deployments (Cloudflare Workers, Bun, Deno, Node); dep
- live: no live URLs
- conflicts: Redis licensing transition: Redis transitioned to RSALv2/SSPLv1 and AGPLv3 dual-licensing in 2024; open-source and commercial distributions must evaluate whether to remain on Redis or migrate to the Linux Foundation Valkey fork., Serverless Framework v4 licensing: Serverless Framework changed licensing terms in v4 introducing commercial paywalls for organizations above certain revenue thresholds, requiring teams to evaluate staying on v3 or migrating to SST/AWS SAM/CDK., Python async pitfall in FastAPI: Mixing blocking synchronous database drivers (e.g. psycopg2) inside async def routes starves the Starlette/Uvicorn threadpool; asynchronous drivers (asyncpg, SQLAlchemy async) or standard def routes are strictly required., OpenAPI 3.0 vs 3.1 tooling divergence: OpenAPI 3.1 aligns with full JSON Schema 2020-12 (including nullable via type arrays), which causes incompatibilities with legacy OpenAPI 3.0 code generators and Swagger UI versions., tRPC full-stack monorepo coupling: tRPC eliminates build-time codegen by importing server router types directly into client TS code, making it optimal for monolithic TypeScript repos but unsuitable for multi-language polyglot environments where gRPC or OpenAPI are required., Node.js request-scoped dependency injection overhead: NestJS REQUEST-scoped providers create new instances per incoming HTTP request, degrading throughput and causing memory pressure in high-RPS environments compared to singleton providers.

### files/God research/B-category-catalogs/04-data.md
- card: files/God research/B-category-catalogs/04-data.md | part parts/05-firstpass-B-catalogs.md:1620 | lines 503 | verdict Partially
- WHAT: Comprehensive reference catalog of 24 modern data tier technologies covering relational databases (PostgreSQL 17/18/19 beta, MySQL 8.x/HeatWave, SQLite, libSQL/Turso, CockroachDB), NoSQL/document/KV/wide-column stores (MongoDB 8.x, Redis 7.x, Valkey, Apache Cassandra, ScyllaDB), graph databases (Neo4j), search engines (Elasticsearch 8.x, Meilisearch, Typesense), vector databases (Pinecone, Weaviat
- HOW: 1. Relational database baseline: Deploy PostgreSQL (v15+ mandatory due to v14 EOL; 17/18 recommended) for standard transactional workloads; pair with pgvector and pgx-bm25 for unified vector and BM25 search without ancillary search clusters; adopt connection poolers (PgBouncer, Supavisor) for server
- live: no live URLs
- conflicts: Licensing transition and forks: Redis transitioned from BSD-3-Clause to source-available RSALv2/SSPLv1 (plus AGPLv3 dual license), prompting the Linux Foundation Valkey fork; commercial redistributions must distinguish between Redis and Valkey., PostgreSQL lifecycle: PostgreSQL 14 reaches official EOL on 2026-11-12; production systems must target PostgreSQL 15, 16, 17, or 18., MongoDB and Elasticsearch licensing: MongoDB SSPL and Elastic License/SSPL are not OSI-approved licenses; managed cloud reselling requires commercial agreements or open-source forks (FerretDB for Mongo wire protocol, OpenSearch for Elasticsearch)., TypeScript ORM paradigms: Prisma uses a domain-specific schema language (schema.prisma) and precompiled query engines, whereas Drizzle and Kysely use pure TypeScript schema definitions and thin SQL query generation, creating distinct trade-offs between schema tooling vs bundle size and serverless cold start times., SQLite concurrency model: SQLite supports only a single concurrent writer; high-write throughput workloads require distributed replication mechanisms (libSQL/Turso, LiteFS) or migration to client-server RDBMS (PostgreSQL, MySQL).

### files/God research/B-category-catalogs/05-builders.md
- card: files/God research/B-category-catalogs/05-builders.md | part parts/05-firstpass-B-catalogs.md:2124 | lines 619 | verdict Partially
- WHAT: Comprehensive Builders catalog 05 documenting 30 foundational technologies across styling, package management, build systems, compilers, linters, monorepo orchestrators, cross-cutting SaaS infrastructure, scaffolding CLIs, and software architecture methodologies. Covers: (1) Styling, tokens, and UI primitives: Tailwind CSS v4.x (CSS-first @theme, Lightning CSS engine, OKLCH color spaces, Vite 8 su
- HOW: 1. Styling and component architecture: Configure modern UI foundations using Tailwind CSS v4 via @tailwindcss/vite with CSS-first @theme blocks and OKLCH color palettes; initialize accessible component registries with npx shadcn@latest init/add wrapping Radix UI primitives; define cross-platform des
- live: no live URLs
- conflicts: Tailwind CSS v4 architectural transition: Tailwind v4 shifts from JavaScript configuration (tailwind.config.js) to CSS-first configuration (@theme with Lightning CSS and OKLCH color palettes), requiring migration codemods and breaking legacy tailwind.config.js plugins., Vite 8 bundler unification: Vite 8 unifies development and production bundling on Rust-based Rolldown (replacing Rollup), requiring compatibility verification for custom Rollup plugins., ESLint 9 flat config deprecation: ESLint v9 makes flat config (eslint.config.js) default and drops legacy .eslintrc formats, requiring FlatCompat bridges or full rewrites for existing plugin configurations., Transpiler vs type checker divergence: Fast transpilers (esbuild, SWC) strip TypeScript syntax without performing semantic type checking, necessitating explicit tsc --noEmit steps in CI quality gates., Package manager install-script security: Modern package managers (pnpm 10/11 with onlyBuiltDependencies and npm 11 allowScripts) restrict or require explicit approval for postinstall lifecycle scripts, breaking legacy dependencies relying on unvetted postinstall steps., Component registry ownership: shadcn/ui provides source code copied directly into repositories rather than versioned npm dependencies, shifting upstream maintenance, bug fixes, and regression testing entirely to application owners., Stripe webhook signature verification: Stripe webhook signature checking requires the raw, unparsed HTTP request buffer; frameworks that automatically parse JSON request bodies before webhook handler execution cause signature verification failures.

### files/God research/B-category-catalogs/07-design-to-code.md
- card: files/God research/B-category-catalogs/07-design-to-code.md | part parts/05-firstpass-B-catalogs.md:2922 | lines 173 | verdict Partially
- WHAT: Design-to-Code catalog 07: Comprehensive empirical research specification and taxonomy cataloging 20 tools across Figma-to-code pipelines, design token extractors, headless Figma inspectors, screenshot-to-code multimodal engines, and visual QA regression gates (verified as of 2026-10-09). Cataloged entries include: (A) Figma-to-Code deterministic and agent pipelines: Figma REST API (platform cloud
- HOW: 1. Headless token and design extraction: Use khanglvm/figma-lens CLI or MCP (figma-lens scout/extract/detail) or felixAnhalt/figma-to-code-mcp to fetch heavily compacted, CSS-aligned layouts without exhausting LLM context windows or requiring full Figma desktop GUI.
- live: no live URLs
- conflicts: Raw Figma REST API file dumps exceed LLM context windows (tens of thousands of tokens per frame); requires compacting layers like felixAnhalt/figma-to-code-mcp (99.5% cut) or khanglvm/figma-lens., Figma variable write-back via REST API (POST /v1/files/:key/variables) is restricted to Enterprise plans; Pro and Org plans must use local plugin bridges (e.g. gregorymm/design-tokens generated plugin, spfr/figma-design-pipeline); Starter plans are unsupported., Local .fig binary files cannot be accessed via official Figma REST or MCP servers; local binary parsing requires engines like followtheart/d2c, while CDP/desktop bridges (catisfy2/figma-ds-cli, rudraptpsingh/figbridge) require an active desktop session., Local WebSocket and CDP bridge port dependencies: spfr/figma-design-pipeline uses ports 4010-4014; rudraptpsingh/figbridge uses port 7331; boring-km/figma-draft-to-code uses port 9001., Licensing conflicts: tortastudios/figtree-cli uses BSL-1.1 (non-OSI source-available with commercial time-delay restrictions); PixelPappa/tokken uses AGPL-3.0 network copyleft; Lost Pixel uses MPL-2.0 copyleft; BackstopJS and screenshot-to-code use MIT; Playwright uses Apache-2.0; Anima, Locofy, Builder.io, Chromatic, Percy, and Applitools are proprietary commercial platforms., abi/screenshot-to-code self-hosting requires multiple third-party API keys (OpenAI, Anthropic, Gemini, or Replicate for images) and Playwright Chromium for local self-render checks; hosted version at screenshottocode.com is commercial/paid.

### files/God research/B-category-catalogs/14-context-memory.md
- card: files/God research/B-category-catalogs/14-context-memory.md | part parts/05-firstpass-B-catalogs.md:6120 | lines 524 | verdict Partially
- WHAT: Comprehensive architectural reference catalog auditing 24 context-memory and retrieval resources across 5 distinct operational mechanisms (local-index, service, vector ANN, graph/AST, and direct-retrieval). Covers dense embedding models (OpenAI text-embedding-3-small/large, Gemini embedding-001, local Sentence-Transformers all-MiniLM-L6-v2/MPNet), sparse/multi-vector representations and rerankers 
- HOW: 1. Embedding and reranking pipeline: Standardize on OpenAI text-embedding-3-small (1536d) or Gemini embedding-001 (3072d) for cloud RAG, or Sentence-Transformers (all-MiniLM-L6-v2 384d) for air-gapped deployments; for codebases, deploy hybrid sparse-dense retrieval (FastEmbed/SPLADE + dense) and app
- live: no live URLs
- conflicts: Vector DB over-engineering vs Direct Retrieval: Teams frequently deploy complex vector database infrastructure (RAG) when deterministic direct retrieval (versioned specs, llms.txt, ADRs) or repomix whole-repo packing achieves superior recall, lower latency, and zero embedding drift for small-to-medium codebases., pgvector scale ceiling: PostgreSQL pgvector offers exceptional developer ergonomics and ACID transactions for deployments under 10M vectors, but experiences index build latency and recall degradation under high-QPS workloads above 10M vectors, necessitating migration to dedicated engines like Qdrant or Pinecone., Dense vector semantic fuzziness vs AST exactness: Dense embeddings (OpenAI text-embedding-3, Gemini) excel at natural language intent but struggle with exact code identifiers, variable names, and syntax structures; pairing with sparse inverted indices (SPLADE/FastEmbed) or deterministic AST tools (ast-grep, tree-sitter, LSP) is essential for software engineering agents., Cross-session memory durability vs prompt injection: Committing project memory conventions to version-controlled files (CLAUDE.md, GEMINI.md, AGENTS.md) ensures organizational memory survives agent restarts, but creates an attack surface where untrusted pull requests can inject malicious system instructions., Context window compaction information loss: Automated conversation compaction (Claude PreCompact/PostCompact, Cline compaction modes) prunes conversational transcripts to prevent token overflow, risking the loss of subtle negative constraints and edge-case instructions unless explicitly persisted to external handoff notes or disk checkpoints.

### files/God research/B-category-catalogs/15-scraping.md
- card: files/God research/B-category-catalogs/15-scraping.md | part parts/05-firstpass-B-catalogs.md:6645 | lines 422 | verdict Partially
- WHAT: Comprehensive 2026 web scraping, crawling, and data extraction ecosystem catalog documenting 20 foundational technologies across 8 functional dimensions: (1) Crawling frameworks: Scrapy (mature Python static-first crawling framework with spiders, scheduler, dupefilter, pipelines, auto-throttle, and Twisted/asyncio engine) and Crawlee (Apify Node.js/Python framework unifying Cheerio, Playwright, an
- HOW: 1. Enforce the 2026 hybrid stack consensus rule: Always attempt lightweight direct HTTP requests (httpx, requests) paired with fast HTML parsing (Cheerio in Node.js, BeautifulSoup4 or lxml in Python) before escalating to browser automation; inspect browser Network tabs for hidden internal JSON/REST 
- live: no live URLs
- conflicts: Browser execution cost vs HTTP throughput disparity: Headless browsers (Playwright, Puppeteer) consume 10x-50x more CPU/memory and require 2-10 seconds per page compared to sub-100ms direct HTTP requests (httpx/requests), creating a steep operational cost cliff unless strictly gated behind dynamic rendering necessity., LLM extraction flexibility vs deterministic fidelity: Generative extractors (Firecrawl /extract, ScrapeGraphAI) parse arbitrary unstructured layouts without CSS selectors but introduce token latency, hallucination risks, and non-deterministic field formats, necessitating schema validation and fallback paths., Anti-bot TLS fingerprinting vs standard HTTP client headers: Modern WAFs (Cloudflare, Akamai) drop requests before evaluating HTTP headers based on JA3/JA4 TLS and HTTP/2 fingerprints, requiring specialized clients like curl_cffi over standard requests/httpx., DOM CSS selector fragility vs Structured Data persistence: CSS and XPath selectors break frequently upon frontend redesigns or automated obfuscation, whereas schema.org JSON-LD script tags provide stable, semantic entity representations across layout updates., Self-hosted crawler infrastructure overhead vs Managed cloud API unit economics: Operating distributed Playwright clusters, residential proxy pools, and captcha solvers incurs substantial DevOps overhead, whereas managed services (Firecrawl, Apify) become cost-prohibitive at scale beyond ~100k pages/month., XML/PDF parsing security vulnerability vs Parsing fidelity: Deep document and XML parsers (lxml, PyMuPDF) can be exploited via XML External Entity (XXE) expansion or malicious PDF embedded actions unless explicitly run in sandboxed, network-restricted worker processes.

### files/God research/B-category-catalogs/16-testing.md
- card: files/God research/B-category-catalogs/16-testing.md | part parts/05-firstpass-B-catalogs.md:7068 | lines 461 | verdict Partially
- WHAT: Authoritative 2026 testing ecosystem reference catalog covering 22 core resources across 14 testing dimensions: JS/TS unit and integration runners (Vitest, Jest), Python testing standard (pytest), JVM enterprise testing (JUnit 5), browser E2E automation (Playwright Test, Cypress, Selenium WebDriver + WebdriverIO), component and visual regression testing (Storybook Test + Chromatic, Percy / Applito
- HOW: 1. Unit and integration testing: Standardize modern JS/TS projects on Vitest (native ESM, Vite pipeline integration, HMR watch); maintain legacy Jest test suites without rewriting unless migrating bundlers; standardize Python services on pytest with pytest-asyncio and pytest-cov; use JUnit 5 (Jupite
- live: no live URLs
- conflicts: Simulation runner versus real browser rendering disparity: jsdom/happy-dom runners used in Vitest/Jest execute quickly in Node.js but do not compute layout, CSS cascade rules, or visual bounding boxes, requiring real browser E2E verification via Playwright., AI test assertion and oracle hallucination risk: Generative AI test creation tools (Codium/Qodo, Copilot) frequently generate valid syntax with fabricated or tautological assertion logic, necessitating strict human verification before test adoption., Absolute coverage metrics versus diff-coverage gaming: Absolute repository coverage thresholds encourage superficial assertions and low-value unit tests; modern CI consensus gates require diff-coverage on PR changes., Mutation test and load test CI pipeline overhead: Full mutation analysis (Stryker/Mutmut) and high-VU load tests (k6/Locust) consume prohibitive CI compute minutes if run on every commit; best practices isolate them to nightly scheduled runs., Docker-in-Docker CI execution security: Testcontainers requires Docker daemon access in CI runners, necessitating container socket mounting or Testcontainers Cloud agents to prevent security misconfigurations.

### files/God research/B-category-catalogs/17-security.md
- card: files/God research/B-category-catalogs/17-security.md | part parts/05-firstpass-B-catalogs.md:7530 | lines 426 | verdict Verified
- WHAT: Authoritative 2026 security engineering and infra-ops catalog evaluating 20 critical technologies and defense practices across 5 domains: SAST/DAST (01 Semgrep fast YAML AST/regex PR gates, 02 CodeQL deep cross-file taint analysis DB, 03 SonarQube/SonarCloud quality gates/hotspots, 04 OWASP ZAP active/passive web/API scanner, 05 Burp Suite enterprise pentest and manual proxy); Dependencies & Suppl
- HOW: 1. SAST PR and Nightly Gates: Configure Semgrep in every pull request gate (semgrep scan --error --config p/owasp-top-ten) for median ~10s AST scans; schedule CodeQL (codeql-action) for nightly or merge-to-main builds to perform deep cross-file dataflow and source-to-sink taint analysis.
- live: no live URLs
- conflicts: Enforceability vs prompt-only boundary confusion: Developers frequently mistake natural-language system instructions (CLAUDE.md, AGENTS.md) or unbrokered LLM filters (Rebuff) for enforceable security boundaries; catalog formalizes that only kernel/hypervisor/broker mechanisms (gVisor, Firecracker, Docker cap-drop, nsjail, E2B, platform permission checks) provide deny-by-default containment., Container isolation vs VM boundary: Standard Docker containers share the host kernel; mounting the Docker daemon socket or granting root/privileged capabilities completely nullifies container isolation, requiring microVMs (Firecracker, E2B) or user-space kernels (gVisor) for untrusted multi-tenant workloads., SAST speed vs depth trade-off: Fast AST pattern matching (Semgrep) operates within seconds for PR gating but misses complex inter-procedural taint flow in open-source tiers; database-backed deep analyzers (CodeQL) trace source-to-sink dataflow accurately but require multi-minute compilation runs suitable for nightly builds., DAST active scanning recall limits: Active vulnerability scanners (OWASP ZAP) achieve low strict recall (~8.3% on modern web benchmarks) on multi-step workflows, authenticated paths, and business logic flaws without scripted automation and human penetration testing., Secrets detection verification gap: Traditional entropy/regex scanners (Gitleaks, detect-secrets) produce significant noise and false positives requiring manual triage; active verification scanners (TruffleHog) validate credentials directly against provider APIs, demanding immediate rotation for confirmed hits.

### files/God research/B-category-catalogs/18-cicd.md
- card: files/God research/B-category-catalogs/18-cicd.md | part parts/05-firstpass-B-catalogs.md:7957 | lines 421 | verdict Partially
- WHAT: Comprehensive CI/CD reference catalog 18 auditing 20 core technologies across git worktree parallel workspaces, pre-commit hook frameworks, CI/CD orchestration engines, container build layers, development environments, declarative/imperative IaC pipelines, PR release automation, accelerated runner infrastructure, and headless CI coding agents. Covers: (1) VCS & Workspaces: Git + Git Worktrees (uti
- HOW: 1. Multi-lane local and agent branching: Use "git worktree add ../feature-branch feature-branch" to create linked checkouts for concurrent agent tasks; maintain isolated per-worktree environment files and prune worktrees upon task completion with "git worktree prune".
- live: no live URLs
- conflicts: Client-side vs server-side verification: Local pre-commit hooks (pre-commit, Husky) provide fast developer feedback but can be bypassed with --no-verify; server-side CI required checks are mandatory for definitive quality gating., CI YAML configuration sprawl vs programmable pipelines: Complex, nested YAML workflows across GitHub Actions and GitLab CI create vendor lock-in and local testing friction, contrasting with containerized code-driven pipelines (Dagger, Earthly) that guarantee local-CI parity., IaC licensing and ecosystem bifurcation: HashiCorp Terraform licensing transition to BSL-1.1 prompted the Linux Foundation OpenTofu (MPL-2.0) fork, requiring teams to select between proprietary upstream features and open-source ecosystem neutrality., Imperative vs declarative IaC: Declarative HCL tooling (Terraform, OpenTofu) provides predictable state drift detection and plan review, whereas general-purpose language IaC (Pulumi) offers software-engineering abstractions but increases runtime complexity., Automated semver release strategies: Fully automated conventional-commit releases (semantic-release) enforce strict commit message formats, whereas Changesets decouples change notes into explicit PR markdown files suited for multi-package monorepos., Hosted SaaS runners vs hybrid self-hosted compute: Public cloud runner fleets (GitHub Actions, CircleCI) reduce operational overhead but incur high costs and lack local network access, contrasting with hybrid architectures (Buildkite, GHA ARC) that execute jobs on private infrastructure., Autonomous AI agents vs deterministic gate enforcement: Headless coding agents (GitLab Duo Workflow, GitHub Copilot Workspace) accelerate backlog resolution but produce prompt-driven code requiring strict sandbox isolation, mandatory CI gate verification, and human peer approval.

### files/God research/B-category-catalogs/19-cloud-deploy.md
- card: files/God research/B-category-catalogs/19-cloud-deploy.md | part parts/05-firstpass-B-catalogs.md:8379 | lines 421 | verdict Partially
- WHAT: Authoritative 2026 Cloud Deploy ecosystem catalog surveying 20 foundational resources across hosting, serverless compute, edge networks, content delivery, runtime secrets, preview/rollback release workflows, observability/telemetry, scheduling/cron, and headless deploy agents. Covers 13 managed services (Vercel, Netlify, Cloudflare Pages/Workers, Render, Fly.io, Railway, AWS Lambda + S3/CloudFront
- HOW: 1. Hosting and runtime selection: Select Vercel for Next.js production where App Router, Server Actions, PPR, and Fluid Compute active-CPU billing outweigh bandwidth premiums; choose Netlify for Jamstack diversity (Astro, Hugo, Eleventy) with built-in forms and edge functions; deploy to Cloudflare P
- live: no live URLs
- conflicts: Serverless hosting convenience versus bandwidth and compute cost premium: Managed platforms (Vercel, Netlify) provide zero-configuration developer experience but introduce steep bandwidth pricing (0-50/TB overage) and require paid database add-ons compared to raw cloud primitives (AWS S3 + CloudFront costing ~/mo for comparable static assets)., Separation of concerns between CI and CD: Common anti-pattern embeds imperative deployment scripts directly inside GitHub Actions or CircleCI pipelines, whereas resilient cloud architecture mandates decoupling CI build/test steps from declarative GitOps sync controllers (Argo CD, Flux)., Railway developer experience versus production stability: Railway offers top-tier Dockerfile onboarding and preview environments but logged 5 major operational outages across a 6-month window in 2026 reports, necessitating careful SLA validation before production adoption., Edge database scale and concurrency constraints: Cloudflare D1 provides low-latency edge SQLite replication but enforces a rigid 10GB hard ceiling and single-writer serial execution, making it unsuitable for high-write SaaS architectures suited for PostgreSQL., Headless deploy agent autonomy risk: Autonomous deploy agents (Dagger, Replit, Vercel) can automate preview generation and infrastructure diffs but create severe availability and security risks if permitted to auto-promote releases to production without mandatory human review and OIDC least-privilege scoping.

### files/God research/B-category-catalogs/20-seo-cms-commerce.md
- card: files/God research/B-category-catalogs/20-seo-cms-commerce.md | part parts/05-firstpass-B-catalogs.md:8801 | lines 463 | verdict Partially
- WHAT: Catalog 20 SEO / CMS / Commerce reference architecture auditing 22 resources and standards across four domains: (1) SEO Foundations (Next.js Metadata API, sitemap.xml / robots.txt RFC 9309 specs, Schema.org JSON-LD structured data vocabularies, Google Search Console index monitoring, Lighthouse / Core Web Vitals lab and CrUX field metrics); (2) Analytics, Compliance & Experimentation (Google Analy
- HOW: 1. Implement programmatic SEO and structured data: Use Next.js App Router metadataBase to construct absolute Open Graph and Twitter image URLs; generate dynamic sitemaps and robots rules via sitemap.ts and robots.ts; inject Schema.org JSON-LD scripts directly into server components for Product and A
- live: no live URLs
- conflicts: Content management versus commerce authority (The Anti-Duplication Rule): Duplicating product prices, currency conversions, and inventory quantities into headless CMS fields causes dangerous price desynchronization and overselling; CMSs must store entity references (handles/IDs) while the commerce API remains the single authoritative source of truth resolved at render time., Content caching longevity versus commerce pricing freshness: Marketing and editorial content benefits from long-term CDN caching with on-demand webhook invalidation (revalidateTag), whereas transactional commerce data requires ultra-short caching (<60s) or real-time server fetches to reflect live inventory and currency fluctuations., Monolithic simplicity versus headless composability: Monolithic architectures (WordPress, WooCommerce, standard Shopify) offer rapid time-to-market and low infrastructure overhead (~$60–$150/year) for low-velocity content, whereas headless composable stacks (Sanity + Shopify + Next.js, Strapi + Medusa) yield superior developer experience and sub-1.5s Core Web Vitals at the cost of higher operational overhead (~$250–$3500/month) and multi-vendor coordination., Client-side experimentation flicker versus server-side edge routing: Client-side A/B testing tools (traditional Optimizely or Google Optimize scripts) induce layout shift (CLS penalties) and flicker, while server/edge middleware routing (GrowthBook, Optimizely Full Stack) eliminates flicker but requires CDN middleware logic and careful bot-exclusion to prevent Google cloaking penalties., Privacy analytics compliance versus conversion attribution: Standard Google Analytics 4 provides deep ad-network attribution but introduces severe GDPR/ePrivacy compliance overhead requiring Consent Mode v2 and CMP prior-blocking, while cookieless privacy-first engines (Plausible, Matomo) minimize consent friction but lack granular retargeting capabilities., SaaS commerce convenience versus open-source self-hosted operational liability: Managed commerce platforms (Shopify) abstract PCI compliance, global scaling, and hosting at the price of recurring transaction fees (1.5–2% + monthly tiers), whereas open-source headless alternatives (Medusa, Saleor) eliminate platform fees but transfer full database, cache, security patching, and PCI SAQ scope to engineering teams.

### files/God research/B-category-catalogs/21-creative-3d.md
- card: files/God research/B-category-catalogs/21-creative-3d.md | part parts/05-firstpass-B-catalogs.md:9265 | lines 175 | verdict Partially
- WHAT: Catalog 21 Creative 3D reference auditing 20 tools and frameworks across 4 domains (Foundations SVG/Canvas/WebGL, Shaders/postFX, Particles, and SVG-to-3D Products/Maps): (A) Foundations (Three.js WebGL/WebGPU renderer, React Three Fiber declarative React reconciler, Drei helper suite, SVG ExtrudeGeometry and opentype.js vector-to-3D pipeline); (B) Shaders & Postprocessing (pmndrs react-postproces
- HOW: 1. Scaffold React 3D scenes with R3F and Drei: Install "three", "@react-three/fiber", and "@react-three/drei"; lock peer dependencies (e.g. three >=0.156 with R3F v8, React 18/19); wrap scenes in declarative <Canvas> with OrbitControls and Environment staging.
- live: no live URLs
- conflicts: WebGPU availability vs WebGL fallback: WebGPU compute paths (Three-VFX, threeparticles) offer native GPU performance but require three >=0.160 and async Canvas gl initialization, mandating WebGL CPU fallbacks for unsupported browsers (~21% global)., Font licensing in extruded 3D vector geometry: Extruding fonts via opentype.js into 3D meshes (3dsvg, ExtrudeGeometry) inherits the source font license (e.g. SIL OFL-1.1 Reserved Font Names, Apache 2.0), preventing uncredited commercial resale as raw geometry., Postprocessing GPU overhead on mobile: Single-triangle EffectPass chains (react-postprocessing) require WebGL2 MSAA and heavy fragment passes that degrade performance on mobile; shaders like bloom and motion blur must be conditionally gated., Map tile provider licensing and attribution: Using Leaflet, deck.gl, or MapLibre GL JS requires separate licensing and attribution compliance for basemaps and vector tiles (OSM ODbL, CARTO, Mapbox ToS) independent of the open-source library code license., Unverified licenses in catalog records: Shader Park (06), heinergiehl R3F FBO ping-pong starter (08), vectorforge (17), and React-Leaflet (18) are noted as requiring explicit LICENSE file verification before commercial deployment., Archived package lineage: Legacy @tsparticles/react wrapper was archived, requiring developers to adopt the modern tsparticles React package structure.

### files/God research/A-master-index.md
- card: files/God research/A-master-index.md | part parts/07-watchlist-prompts-CE.md:421 | lines 97 | verdict Verified
- WHAT: Master reconciliation index and cross-pass audit synthesizer unifying First Pass (FP: 23 category catalogs, 29 design styles, Phase 0 inventory), Gemini Second Pass (G: G-01 through G-06), and third pass (agy-pass / gemini-3.8-flash-high fallback). Adjudicates watchlist candidates into 13 resolved, 9 provisional, 1 partial (awesome-claude-skills), reconciles prompt archives (asgeirtj meta vs Louis
- HOW: Use Section 1 mapping table to translate first-pass category catalog files (B-01 through B-23, D-00 through D-29) to second-pass Gemini pointers (G-01 through G-06) and evaluate category relationships.
- live: no live URLs
- conflicts: Astryx integration scope nuance: first pass verified CLI-only with no MCP in packages/cli tree, whereas Gemini second pass identified hosted MCP route in apps/docsite/src/app/mcp/route.ts, reconciled as dual-surface (CLI-local + hosted web MCP)., DeepSec repository status: first pass identified vercel/deepsec as HTTP 404, whereas subsequent passes identified vercel-labs/deepsec as HTTP 200 with npx deepsec init., awesome-claude-skills naming collision: multiple distinct high-star community repositories share the identical name (travisvn, ComposioHQ, BehiSecc, karanb192), precluding a single canonical entity without organization namespace.

### files/God research/00-phase0-inventory.md
- card: files/God research/00-phase0-inventory.md | part parts/07-watchlist-prompts-CE.md:519 | lines 214 | verdict Verified
- WHAT: Phase 0 foundational source inventory and reconciliation audit documenting the complete 23-file OpenCode ecosystem research corpus (5 root documents, 13 deep-dive research notes, and 5 walkinglabs harness templates). Synthesizes canonical repository status, star metrics, and integration boundaries across 47+ named tooling candidates, summarizes the 26-element ecosystem catalog (163 usable vs 43 ex
- HOW: Consult the 23-file Source File Map to navigate research modules across UI/UX, council ensembles, loop engineering, QA testing, and harness templates.
- live: no live URLs
- conflicts: Astryx MCP versus CLI: earlier phase notes assumed packages/mcp-server existed, but Phase 8 direct verification confirmed Astryx is strictly CLI-based, requiring bash execution rather than MCP server registration., loopy receipt persistence: loopy run receipts remain in-session and are not automatically synced to feature_list.json evidence[], requiring explicit Layer 2 instructions in AGENTS.md to avoid DoD verification failures., GSD repository provenance: original gsd-build/get-shit-done was archived in June 2026 due to security concerns, requiring complete migration to the community-maintained fork open-gsd/gsd-core., ngmeyer repo status: initial reports claimed council-review was archived and replaced by skills monorepo, whereas direct verification proved both repositories remain live and maintained in parallel., KanakMalpani repo status: initial reports misidentified Loop-Engineering as replaced by LoopBench, whereas Loop-Engineering (framework) and LoopBench (benchmark) are separate active repositories.

### files/God research/atlas/A-master-index.md
- card: files/God research/atlas/A-master-index.md | part parts/08-atlas-33.md:72 | lines 1378 | verdict Verified
- WHAT: Deliverable A master index registering 1,152 canonical resource directory rows across 32 discrete technical categories (Agent skills 29, Build/CI/CD/operations 48, Coding agents & extensions 28, Context & memory 57, Backend/data/services 85, Frontend frameworks & components 192, Languages & browser tech 169, Data acquisition & public APIs 89, 29 distinct Design styles 105 total, Design systems & a
- HOW: Search Deliverable A by category or resource name to quickly identify canonical URLs, maintainers, package types, and verified capabilities.
- live: no live URLs
- conflicts: Cal.com production repository privatized and relicensed closed-source on 2026-04-14, publishing feature-stripped MIT cal.diy fork, Auth.js (next-auth) maintenance transition: README states project is part of Better Auth, recommending Better Auth for new projects, Lucia auth library officially discontinued by its author; classified as Historical with better-auth as successor, Rye deprecated by Astral in favor of Astral uv, with official migration guides and security updates halted, Origin UI transferred to cosscom/coss and relicensed AGPL-3.0 with only apps/ui and apps/origin remaining MIT, Prisma 7 architectural shift: Rust-free TypeScript engine replacing previous native binary engine, Turso scale-to-zero model deprecated in January 2026 in favor of always-on architecture, PlanetScale free tier elimination in March 2024 shifting platform to strictly paid usage models

### files/God research/atlas/B1-core-web-technologies.md
- card: files/God research/atlas/B1-core-web-technologies.md | part parts/08-atlas-33.md:1451 | lines 929 | verdict Partially
- WHAT: Deliverable B1 condensed category catalog comprising 648 verified records across 6 major technical sectors: 1. Core web development technologies & browser platform standards (58 records: ECMAScript 2026/Temporal API, TypeScript 7 Go port, Wasm 3.0, WASI 0.3.0, WebGPU/WebGL2, WebRTC, WebSocket RFC 6455, WebTransport Baseline 2026, WHATWG DOM/Fetch/Streams, WCAG 2.2 AA a11y, i18n); 2. Build, compile
- HOW: Standardize client and frontend toolchains: adopt Vite 8 powered by Rolldown and Oxc; use Base UI and React Aria Components for accessible unstyled primitives; integrate TanStack Query for server state and TanStack Table for headless datagrids; use Motion for UI animations and GSAP for scroll-driven
- live: no live URLs
- conflicts: TypeScript 7.0 compiler port to Go (tsgo) drops programmatic compiler APIs (ts.createProgram), requiring typescript-eslint and AST transformers to pin to TS 6.x until 7.1, Node.js native type stripping (amaro) evaluated tsgo and rejected it due to lack of blank-spacing mode and binary distribution overhead, keeping SWC, Auth.js (next-auth) joined Better Auth; maintainers recommend Better Auth for new projects except stateless database-less setups, Cal.com production repo privatized on 2026-04-14; community fork cal.diy is stripped of enterprise/team modules, Prisma 7 abandoned Rust binary engine in favor of a pure TypeScript engine lineage, Stytch acquired by Twilio in November 2025 for $104.1M cash while continuing brand APIs, Payload CMS acquired by Figma in June 2025 with open-source MIT core preserved but cloud sign-ups paused, Lemon Squeezy acquired by Stripe in July 2024 and being transitioned into Stripe Managed Payments

### files/God research/atlas/B2-design-and-visual.md
- card: files/God research/atlas/B2-design-and-visual.md | part parts/08-atlas-33.md:2381 | lines 148 | verdict Verified
- WHAT: Deliverable B2 category catalog condensing 97 verified essentials across UI/UX design systems and interface guidelines (22 records), UI/UX theory, principles, and audit resources (7 records), design inspiration and resource directories (15 records), design-to-code resources (19 records), visual/creative assets and pipelines (20 records), and interactive experiences/creative technologies (14 record
- HOW: Consult Section 6 for enterprise and accessible UI/UX design systems (IBM Carbon, Adobe Spectrum, Shopify Polaris Web Components, Microsoft Fluent 2, GitHub Primer, Radix UI, Base UI, Ark UI, Tailwind/DaisyUI, Shoelace, Style Dictionary, MUI X).
- live: no live URLs
- conflicts: Shopify Polaris React library (@shopify/polaris) deprecated in favor of Polaris Web Components (<s-*>) released 2025-10-01., NextUI renamed to HeroUI (2025) and re-architected on React Aria components + Tailwind v4., Base UI forked from MUI Base into standalone headless primitives and adopted as shadcn default headless primitive layer in July 2026., GSAP acquired by Webflow (Oct 2024) with Club plugins made free for commercial use in May 2025.

### files/God research/atlas/B3-agent-ecosystem.md
- card: files/God research/atlas/B3-agent-ecosystem.md | part parts/08-atlas-33.md:2530 | lines 250 | verdict Verified
- WHAT: Deliverable B3 category catalog condensing 133 verified essentials across Agent Skills and GitHub skill collections (28 records), MCP servers, specifications, SDKs, registries, and gateways (84 records), and Coding Agents and extension hosts (21 records). Covers official skills, MCP 2025-11-25 / OAuth 2.1 specs, reference and vendor MCP servers, and extension architectures for 17+ coding agents.
- HOW: Consult Section 9 for official vendor Agent Skills (Vercel, Sentry, Expo, Hugging Face, Stripe, Trail of Bits, Microsoft, Figma, Netlify, Angular, Supabase, Neon, ClickHouse, HashiCorp, Better Auth, LambdaTest, Capgo) and skill tooling (skills.sh CLI, ai-linter, skills_lint.dart, Agent Skill Exchang
- live: no live URLs
- conflicts: Gemini CLI succeeded by Antigravity CLI (agy) announced at Google I/O 2026; Gemini CLI categorized as Historical., Windsurf/Cascade rebranded/transitioned to Devin Desktop following Cognition acquisition., OpenAI openai/skills repo explicitly deprecated in favor of openai/plugins and Codex Agent Skills., FastMCP 1.0 adopted into official Anthropic MCP Python SDK; standalone FastMCP v3 continues independently., ACP name collision: IBM Agent Communication Protocol (merged into A2A Aug 2025) vs Zed/JetBrains Agent Client Protocol vs Commerce ACP (OpenAI/Stripe).

### files/God research/atlas/B4-multiagent-harness-context.md
- card: files/God research/atlas/B4-multiagent-harness-context.md | part parts/08-atlas-33.md:2781 | lines 151 | verdict Verified
- WHAT: Deliverable B4 category catalog condensing 113 verified essentials across Multi-Agent Systems and Agent Orchestration (24 records), Harness Engineering and Autonomous Software Development (31 records), and Context Databases, Memory, and Repository Intelligence (58 records).
- HOW: Consult Section 12 for multi-agent orchestration frameworks (LangGraph, AG2, Microsoft Agent Framework MAF, CrewAI, OpenAI Agents SDK, Google ADK v2.0, MetaGPT, AWS Strands, PydanticAI, Smolagents, BeeAI, Mastra) and agent protocols (A2A v1.0, AG-UI, AGNTCY, AP2, ANP).
- live: no live URLs
- conflicts: Microsoft AutoGen placed into maintenance mode; AG2 fork created by original authors; Microsoft launched Microsoft Agent Framework (MAF) as enterprise successor., OpenAI Swarm experimental framework superseded by production OpenAI Agents SDK (March 2025)., SWE-agent README confirmed supersession notice favoring mini-SWE-agent and SWE-ReX runtime., Amazon Q Developer superseded/replaced by AWS Kiro agentic IDE (Nov 2025 GA)., IBM ACP merged into Google/Linux Foundation A2A (Aug 2025); IBM repository archived., Tessl spec-as-source platform never reached GA and pivoted to agent skills in mid-2026.

### files/God research/atlas/B5-infrastructure-quality.md
- card: files/God research/atlas/B5-infrastructure-quality.md | part parts/08-atlas-33.md:2933 | lines 473 | verdict Partially
- WHAT: Deliverable B5 category catalog condensing 316 verified essentials across Web Crawling, Scraping, and Research Tools (Section 15, 90 records across web data acquisition, public API directories, research/ingestion tools), Testing, QA, and Verification (Section 16, 75 records across unit/integration, browser automation, visual regression, accessibility, device clouds, mobile, API/contract testing, l
- HOW: Consult Section 15 for web crawling, document parsing, and ingestion: deploy Crawl4AI or Scrapy for scalable web extraction; use Jina Reader (r.jina.ai) or Tavily/Exa for clean LLM-ready markdown; parse rich documents via Docling (PDF layouts/tables) or MarkItDown; monitor target changes via changed
- live: no live URLs
- conflicts: Trivy-action supply-chain hijack (2026-03-19): Threat actor TeamPCP hijacked tags 75/76 of aquasecurity/trivy-action and released malicious v0.69.4 exfiltrating CI secrets to scan.aquasecurtiy.org (CVE-2026-33634 / GHSA-69fq-xp46-6x23); requires SHA-pinning., Gitpod platform transition: OpenAI acquired Gitpod in June 2026, rebranding the product to Ona; Gitpod Classic scheduled for sunset on 2026-10-15 requiring migration to devcontainers/Ona., MCP security tooling rebrand: Invariant Labs mcp-scan acquired by Snyk and rebranded to Snyk Agent Scan (uvx snyk-agent-scan)., pa11y-ci licensing correction: License classification corrected from secondary reports in source catalog., Optic API contract tooling: Optic API changelog and diff repository archived in January 2026., UptimeRobot licensing policy: Free tier restricted to non-commercial monitoring since October 2024., Statsig brand consolidation: Amplitude took over Statsig brand and customer base in May 2026, while OpenAI retained engineering staff.

### files/God research/atlas/F-compatibility-index.md
- card: files/God research/atlas/F-compatibility-index.md | part parts/08-atlas-33.md:4967 | lines 99 | verdict Verified
- WHAT: Deliverable F compatibility and integration index classifying cross-agent compatibility, open standards (Agent Skills SKILL.md, MCP, AGENTS.md, OpenAPI-to-MCP, DESIGN.md), host extension surfaces across 12+ coding agents, integration tiers for 38 selected resources, explicit non-integrations, and unverified compatibility claims.
- HOW: Use Section F1 (Open Standards) to evaluate cross-host portability across Agent Skills (SKILL.md), Model Context Protocol (MCP), AGENTS.md, OpenAPI-to-MCP adapters, and DESIGN.md.
- live: no live URLs
- conflicts: garrytan/gstack with OpenCode shows mixed evidence: Phase-5 reported compatibility while Element-1 sweep excluded it as Claude-Code-only (unresolved)., facebook/astryx integration conflict: early documentation claimed native MCP support, but Phase-8 direct verification confirmed CLI bash calls only with no MCP package in repo.

### files/God research/atlas/G-relationship-index.md
- card: files/God research/atlas/G-relationship-index.md | part parts/08-atlas-33.md:5067 | lines 70 | verdict Verified
- WHAT: Deliverable G resource relationship index documenting 29 renames and successor chains, companion and dependency graphs across standards/toolchains, and 8 critical name collisions to prevent project conflation.
- HOW: Consult Section G1 to resolve legacy project names to canonical active successors (e.g. Claude Flow -> ruvnet/ruflo, Gemini CLI -> Antigravity CLI, Everything Claude Code -> affaan-m/ECC, gsd-build -> open-gsd/gsd-core).
- live: no live URLs
- conflicts: Serena repository license conflict: secondary sources claim MIT license while primary repository inspection confirms GPL-3.0 copyleft., gsd-build security deprecation: original repository archived in June 2026 due to unconstrained shell execution risks; canonical community fork is open-gsd/gsd-core.

### files/God research/atlas/H-verification-register.md
- card: files/God research/atlas/H-verification-register.md | part parts/08-atlas-33.md:5138 | lines 136 | verdict Verified
- WHAT: Deliverable H verification and discrepancy register cataloging unverified names, corrected project identities, 5 preserved architectural contradictions, broken/misleading URLs and names, 18 discontinued/archived/unsafe repositories, unsupported marketing claims, 12 license discrepancies, recorded security incidents (CVE-2026-33634, CVE-2026-80521, CVE-2025-49596), incomplete compatibility claims, 
- HOW: Consult Section H1 to identify ambiguous or unverified candidate names (okjpg/llm-council voice-to-text distortion, generic Designs, ambiguous 5-author Backend design skill, Strix alternatives, unverified OpenCode paths).
- live: no live URLs
- conflicts: OpenCode sandbox contradiction: Element 7 reported no built-in sandboxing (UX-only permissions), while second sweep found native OS-level sandbox in packages/opencode/src/sandbox/ (Bubblewrap/gVisor/Firecracker/Seatbelt)., Output styles gap: Element 10 listed 8 themes under output styles, but second sweep confirmed TUI themes do not provide Claude-Code-style output switching (issue #5199 open)., Official OpenCode SDK identity: Anomalyco repos (opencode-sdk-js, opencode-sdk-go) conflict with @opencode-ai/sdk documented at opencode.ai/docs/sdk., garrytan/gstack OpenCode support: Phase-5 reported compatibility while Element-1 sweep excluded it as Claude-Code-only., Issue #30295 statusLine: First pass reported open, second sweep showed closed with auto-close label (process closure vs resolution)., Serena license conflict: Secondary listings claim MIT while primary inspection confirms GPL-3.0-or-later., pa11y license conflict: Commonly reported as MIT but canonical license is LGPL-3.0-only., Astryx MCP claim: Early documentation reported an MCP server, but direct verification confirmed CLI bash calls only., Xata status conflict: Shutdown rumors conflict with active 2026 service listings.

### files/God research/atlas/catalogs/01a-languages-build.md
- card: files/God research/atlas/catalogs/01a-languages-build.md | part parts/08-atlas-33.md:5335 | lines 3215 | verdict Partially
- WHAT: Omniscient Resource Atlas Catalog 01a: comprehensive research catalog covering Languages & browser technologies (Part 3.1) and Build, compile, and package tooling (Part 3.4) across 155 distinct resource records in 19 subcategories (9 Verified, 107 Partially verified, 39 Unverified). Cataloged sectors include core specs and languages (ECMA-262 ES2026, Temporal API Stage 4, TypeScript 7.0 Corsa Go p
- HOW: 1. Runtime baseline selection: For production Node.js services, standardize on Node.js 24 LTS (Krypton) with type-stripping via amaro/SWC and npm 11; for high-throughput edge microservices, deploy Cloudflare workerd isolates or Deno 2.7 with explicit granular permissions (--allow-read, --allow-net);
- live: no live URLs
- conflicts: TypeScript 7.0 compiler port to Go (tsgo) drops the programmatic compiler API (ts.createProgram etc.), creating a hard incompatibility with typescript-eslint, ts-morph, and template-typecheckers, requiring those ecosystems to stay pinned to TypeScript 6.x until 7.1., Node.js type-stripping implementation (amaro) evaluated and explicitly rejected tsgo as its transpile engine due to lack of blank-spacing mode and binary distribution overhead, maintaining SWC as its dependency., Default package manager script security changed across Node 24 (npm 11.19+ skips install scripts by default via allowScripts) and pnpm 10/11 (strictDepBuilds / allowBuilds), breaking legacy packages relying on unvetted postinstall steps., Ecosystem deprecation handoffs: Astral Rye is deprecated in favor of uv; egoist/tsup is in maintenance mode with author directing users to rolldown/tsdown; Volta maintainers have stood down with mise recommended as successor., ts-node ESM loader compatibility broke on Node.js 20+ due to Node loader hook redesigns, requiring projects to transition to tsx (esbuild) or Node native type stripping., Supply chain detection gap: standard advisory scanners (npm audit, pip-audit, osv-scanner) rely exclusively on published vulnerability registries and provide 0-day blind spots against account hijacks (e.g. March 2026 axios incident), necessitating behavioral analysis (Socket.dev) or release age cooldowns.

### files/God research/atlas/catalogs/01b-frontend.md
- card: files/God research/atlas/catalogs/01b-frontend.md | part parts/08-atlas-33.md:8551 | lines 1195 | verdict Partially
- WHAT: Research catalog Part A (Frontend Frameworks & Application Development) covering 55+ frontend technologies across 10 categories: UI frameworks (A1, 11 entries), meta-frameworks (A2, 13 entries), static site generators (A3, 7 entries), islands/partial hydration (A4), routing (A5, 4 entries), client state management (A6, 9 entries), server state/data fetching (A7, 5 entries), forms & validation (A8,
- HOW: Reference canonical identities (GitHub org/repo, npm package) for dependency resolution
- live: https://github.com/facebook/react; https://github.com/vuejs/core; https://github.com/nuxt/nuxt; https://github.com/withastro/astro; https://github.com/pmndrs/zustand; https://github.com/TanStack/query; https://github.com/storybookjs/storybook; https://github.com/mui/material-ui; https://github.com/vercel/next.js; https://github.com/sveltejs/svelte; https://github.com/solidjs/solid; https://github.
- conflicts: Astro license discrepancy: GitHub metadata shows NOASSERTION, README badges assert MIT, Next.js satisfaction drop reported (68%→55% in State of JS 2025) but maintenance active, SolidStart pre-1.0 API stability risk vs marketing positioning, Recoil marked unmaintained but still published on npm, Gatsby advised against for new projects but Netlify skills still document it

### files/God research/atlas/catalogs/01c-backend-data-platforms.md
- card: files/God research/atlas/catalogs/01c-backend-data-platforms.md | part parts/08-atlas-33.md:12137 | lines 1887 | verdict Partially
- WHAT: Omniscient Resource Atlas Catalog 01c covering backend frameworks, API systems, databases, persistence, application services, website platforms, code generators, and architecture engineering references across ~240 distinct resources in sections 3.5 through 3.9. Documents primary/secondary identity, capabilities, maintenance status, licenses, and verified URLs across backend languages (Express, Fas
- HOW: Consult Section 3.5 for API and backend framework selection, schema-first design, and contract testing with Schemathesis, Spectral, and MSW
- live: no live URLs
- conflicts: Cal.com license change: transitioned from AGPLv3 open source to commercial closed-source in April 2026, Stytch corporate acquisition: acquired by Twilio for $104.1M cash in November 2025; brand and APIs operate under Twilio, Lemon Squeezy acquisition: acquired by Stripe in July 2024, merging into Stripe Managed Payments (released Feb 2026), Auth.js migration recommendation: Auth.js maintainers officially advise new TypeScript projects to start with Better Auth, Turso pricing/feature shift: scale-to-zero capability deprecated in January 2026 secondary reports, Ecosystem deprecations: Optic archived Jan 2026; Dredd archived May 2024; MongoDB Atlas App Services EOL September 30, 2025, Astryx-backend gap: no single backend architectural convention package exists that mirrors Astryx frontend design patterns

### files/God research/atlas/catalogs/02a-design.md
- card: files/God research/atlas/catalogs/02a-design.md | part parts/08-atlas-33.md:14025 | lines 2427 | verdict Partially
- WHAT: Atlas Catalog 02a covering Design Systems, UI/UX Theory, Design Inspiration Directories, Creative Assets, Design-to-Code Pipelines, and Visual/Interactive Creative Technologies across Parts 4 and 17. Contains 97 full structured records (72 Verified, 1 Corrected, 23 Partially verified, 1 Unresolved) and ~95 supplementary entries across 6 major parts: Part A (22 design systems: Carbon, Spectrum 2, P
- HOW: Select headless unstyled primitives from Part A (Radix, Base UI, Ark UI, React Aria) paired with Tailwind or design tokens for custom design systems
- live: no live URLs
- conflicts: Shopify Polaris framework transition: legacy React implementation (@shopify/polaris) is deprecated; Polaris Web Components is the modern primary distribution, GSAP licensing model: GSAP motion library operates under GreenSock Custom License, requiring commercial paid license for products charging end users, Visual testing sunsets: Lost Pixel sunsetting after joining Figma; BackstopJS dormant since 2024; Percy acquired by BrowserStack; Chromatic remains active Storybook partner, Token platform status: Supernova SaaS integration depth remains Unresolved due to login-gated paywall, Unsplash dynamic endpoint deprecation: source.unsplash.com is deprecated and must not be used for dynamic image placeholders, NextUI rebranding: NextUI transitioned to HeroUI, Chakra UI v3 architectural rewrite: Chakra UI v3 dropped Emotion in favor of Zag.js and Ark UI primitives

### files/God research/atlas/catalogs/05b-context.md
- card: files/God research/atlas/catalogs/05b-context.md | part parts/08-atlas-33.md:22945 | lines 1380 | verdict Partially
- WHAT: Omniscient Resource Atlas Catalog 05b: comprehensive research catalog covering Context & Memory, Repository Intelligence, and Documentation Grounding across 58 cataloged resources in three distinct domains. Sections include: (A) Context & Memory (Mem0 persistent agent memory layer with hybrid semantic/BM25/entity retrieval and multi-level user/session/agent state; Zep / Graphiti temporal knowledge
- HOW: 1. Agent memory architecture: For cross-session agent personalization and facts, integrate Mem0 (pip install mem0ai) or self-hosted Docker server; for temporal validity tracking and bi-temporal facts, deploy Graphiti (pip install graphiti-core) with Neo4j or FalkorDB; for self-editing agent state us
- live: no live URLs
- conflicts: Serena licensing contradiction: multiple secondary sources listed Serena as MIT, but authoritative inspection of the primary GitHub repository confirms GPL-3.0-or-later., Sourcegraph Cody context engine publicly abandoned vector embeddings in February 2024 in favor of BM25 and code-graph context, highlighting limitations of dense embeddings for codebase retrieval., Zep Community Edition was deprecated in April 2025; open-source development consolidated under the Graphiti engine, while Zep operates as a proprietary managed cloud service., Semgrep engine licensing shifted to LGPL-2.1 with proprietary features in Semgrep Cloud, leading to the creation of the OpenGrep open-source community fork., Sourcegraph archived its primary repositories (sourcegraph/sourcegraph and sourcegraph/cody) in 2025, leaving the ongoing maintenance status of the SCIP protocol uncertain., Mem0 benchmark figures (LoCoMo 92.5, LongMemEval 94.4) are self-reported vendor evaluations utilizing proprietary platform optimizations not fully replicated in the base open-source library.

### files/God research/atlas/catalogs/06a-data-acquisition.md
- card: files/God research/atlas/catalogs/06a-data-acquisition.md | part parts/08-atlas-33.md:24326 | lines 2322 | verdict Verified
- WHAT: Comprehensive catalog of 111 web data acquisition tools, public API directories, and research/ingestion tools across three major categories: A) Web Data Acquisition (68 full records covering crawling frameworks, parsers, browser automation, managed extraction APIs, LLM readers, document/PDF extraction, media extraction, change monitoring, metasearch engines, web archives, anti-bot mechanisms), B) 
- HOW: Select scraping framework by rendering requirements: Scrapy or Crawlee CheerioCrawler for high-throughput static HTTP; Playwright, Crawlee PlaywrightCrawler, or Crawl4AI for client-side JavaScript rendering
- live: https://github.com/scrapy/scrapy; https://github.com/apify/crawlee; https://github.com/unclecode/crawl4ai; https://github.com/microsoft/playwright; https://github.com/jina-ai/reader; https://tavily.com; https://exa.ai; https://github.com/microsoft/markitdown; https://github.com/docling-project/docling; https://github.com/Unstructured-IO/unstructured; https://github.com/yt-dlp/yt-dlp; https://githu
- conflicts: Docling canonical identity corrected from DS4SD/docling to docling-project/docling (LF AI & Data Foundation), changedetection.io upstream identity corrected to dgtlmoon (avoiding forks), Gitingest canonical repo identity corrected to coderamp-labs/gitingest (formerly cyclotruc) with fork disambiguation, Zyte rebrand from Scrapinghub documented, Spider Rust crawler canonical repo identity unresolved, Parallel.ai service identity unresolved

### files/God research/atlas/catalogs/06c-operations.md
- card: files/God research/atlas/catalogs/06c-operations.md | part parts/08-atlas-33.md:29429 | lines 2436 | verdict Verified
- WHAT: Omniscient Resource Atlas Catalog 06c: comprehensive production operations catalog covering Build Systems, CI/CD, Cloud & Production Infrastructure (Part A, 26 subcategories A1-A26 with 190 records + 40 rapid-fire entries) and Technical SEO, Web & Product Analytics, Consent, Experimentation, Headless/Traditional CMS, Documentation, E-commerce, Payments/Billing, Transactional Email, Customer Suppor
- HOW: 1. Infrastructure as Code & Orchestration: Prefer OpenTofu (search.opentofu.org) or Pulumi over BSL-locked Terraform where open-source license purity is required; configure reproducible CI workflows via GitHub Actions or Dagger; deploy containerized services to Kubernetes using Helm and Kustomize.
- live: no live URLs
- conflicts: Deno Deploy sunset vs runtime: Deno team joined Cloudflare and announced Deno Deploy will sunset ~April 2027 (six-month migration window), while Deno open-source runtime continues with maintenance releases for one year., HashiCorp BSL licensing: IBM completed acquisition of HashiCorp (.4B, Feb 2025), but HashiCorp products (Terraform, Vault, Consul, Nomad) remain under BSL as of late 2026, preserving the necessity of open-source forks OpenTofu and OpenBao., Statsig ownership transition: Statsig was acquired by OpenAI (Sept 2025), with Amplitude acquiring the Statsig brand and customer base (May 2026), necessitating customer transition planning for feature flagging and experimentation., Langfuse corporate transition: Langfuse was acquired by ClickHouse (Jan 2026), transitioning into ClickHouse native AI telemetry while maintaining open-source self-hosted capabilities., Intercom rebrand and acquisition: Intercom rebranded to Fin (May 2026), with Salesforce signing an acquisition agreement in June 2026 (pending regulatory close)., Database ecosystem shifts: Neon acquired by Databricks (May 2025); Xata subject to market shutdown ambiguity requiring direct validation before greenfield adoption.

### files/God research/atlas/registers/discrepancies.md
- card: files/God research/atlas/registers/discrepancies.md | part parts/08-atlas-33.md:31904 | lines 83 | verdict Verified
- WHAT: Authoritative Verification and Discrepancy Register cataloging 22 confirmed project identity corrections (Section A), 8 license discrepancies with primary-read resolutions (Section B), 11 corporate acquisitions and project lifecycle transitions from 2025-2026 (Section C), 6 critical security advisories and supply-chain incidents (Section D), 9 unresolved structural contradictions (Section E), and 
- HOW: Apply Section A identity corrections across all agent configurations: use ruvnet/ruflo (not ruflo), emilkowalski/skills (not enilkowaski), Karim Shoair (Scrapling author), AWS Pizza Bot (not PizzaBox), affaan-m/ECC (plugin ecc@ecc, npm ecc-universal), vercel-labs/deepsec (not vercel/deepsec), Antigr
- live: no live URLs
- conflicts: Serena license discrepancy: secondary sources claim MIT, primary inspection confirms GPL-3.0-or-later override., Astryx MCP discrepancy: early reports claimed MCP server support, but Phase 8 and October 2026 verification confirmed CLI-only bash integration (@astryxdesign/cli)., gsd-build/get-shit-done safety conflict: original repository archived in June 2026 due to deep shell permissions, requiring migration to open-gsd/gsd-core., Gitpod acquisition and sunset: OpenAI acquisition in June 2026 and rebrand to Ona with Gitpod Classic sunsetting 2026-10-15., Trivy-action supply-chain compromise: TeamPCP hijacked tags 75/76 releasing malicious v0.69.4 exfiltrating secrets (CVE-2026-33634).

### files/God research/atlas/index/master-index.md
- card: files/God research/atlas/index/master-index.md | part parts/08-atlas-33.md:32865 | lines 1433 | verdict Verified
- WHAT: Authoritative Master Index of The Omniscient Resource Atlas registering 1,210 canonical resource records (folded from 1,281 raw rows) across 32 comprehensive technical domains: Agent skills (29), Build/CI/CD/operations (48), Coding agents & extensions (28), Context & memory (57), Core web backend & platforms (85), Core web frontend (192), Languages & build tooling (169), Data acquisition & public 
- HOW: Perform fast resource queries across 32 domain sections to retrieve canonical GitHub/docs URLs, component classifications, and architectural summaries.
- live: no live URLs
- conflicts: Cal.com relicensed closed-source on 2026-04-14, publishing feature-stripped cal.diy MIT fork., Auth.js (next-auth) maintenance absorbed into Better Auth ecosystem., Lucia authentication officially discontinued by creator, recommending Better Auth., Rye deprecated by Astral in favor of Astral uv., Origin UI components relicensed AGPL-3.0 with only apps/ui remaining MIT., Serena licensing: verified as GPL-3.0-or-later, overriding secondary claims of MIT license., Astryx MCP absence: verified as CLI bash integration only (@astryxdesign/cli) with no MCP package., OpenCode sandbox duality: conflict between initial no-built-in-sandbox findings and native OS sandbox implementation.

### files/God research/atlas/index/phase0-inventory.md
- card: files/God research/atlas/index/phase0-inventory.md | part parts/08-atlas-33.md:34299 | lines 194 | verdict Verified
- WHAT: Phase 0 foundational research inventory synthesizing the baseline OpenCode ecosystem research corpus (26 catalog sweep elements, 163 usable resources, 43 Claude-Code-only excluded items, 20 Phase-5 named resources with 5-point breakdowns). Documents 16 preserved corrections (including Astryx CLI-only status, ngmeyer and KanakMalpani repository statuses, and Scrapling author correction), 13 unverif
- HOW: Consult Section 1 and Section 2 for the 20 core Phase-5 verified resources (Graphify-Labs/graphify, ruvnet/ruflo, emilkowalski/skills, vercel/eve, vercel-labs/deepsec, Forward-Future/loopy, open-gsd/gsd-core, obra/superpowers, anthropics/claude-cookbooks, etc.).
- live: no live URLs
- conflicts: Astryx MCP vs CLI: confirmed CLI bash execution only (@astryxdesign/cli), resolving earlier assumptions of an MCP package., gsd-build security warning: original repository archived June 2026 due to deep shell permission risks; open-gsd/gsd-core established as safe community fork., ngmeyer repository status: confirmed council-review and skills are live parallel repositories, refuting earlier reports of archival., KanakMalpani repository status: Loop-Engineering (framework) and LoopBench (benchmark) confirmed as separate active repos., OpenCode sandboxing (C5): initial claim of no built-in sandboxing contradicted by discovery of native OS sandbox in packages/opencode/src/sandbox/.

### files/God research - gemini/01-core-web-tech.md
- card: files/God research - gemini/01-core-web-tech.md | part parts/09-gemini-secondpass-6.md:54 | lines 960 | verdict Verified
- WHAT: Comprehensive Technical Directory of 82 Core Web Technologies across 9 architectural domains: 1. Languages (10: TypeScript, JavaScript, HTML5, CSS3, WebAssembly, Python, Go, Rust, PHP, Ruby); 2. Frontend Frameworks & UI Libraries (10: React, Vue.js, Angular, Svelte, SolidJS, Preact, Lit, Alpine.js, HTMX, Qwik); 3. Styling, Design Systems & Component Primitives (10: Tailwind CSS, Sass, PostCSS, CSS
- HOW: 1. Language & Runtime Selection: Standardize on TypeScript for end-to-end type safety; target Node.js 18+ for server workloads, Bun for high-speed local bundling/testing, or Deno/Cloudflare Workers for sandboxed edge execution.
- live: no live URLs
- conflicts: Runtime CSS-in-JS incompatibility: Emotion and styled-components face architectural friction in React 19 / Next.js App Router due to Server Component streaming, favoring zero-runtime alternatives like Tailwind CSS and Panda CSS., Authentication ecosystem migration: NextAuth.js transition to Auth.js v5 multi-framework architecture., Edge runtime compatibility: Discrepancies between Node.js native C++ modules and Web Standard APIs on V8 isolate platforms (Cloudflare Workers, Vercel Edge)., ORM philosophy divergence: Heavy schema-engine code generation (Prisma) vs lightweight zero-dependency SQL dialect mirroring (Drizzle).

### files/God research - gemini/05-infra-ops.md
- card: files/God research - gemini/05-infra-ops.md | part parts/09-gemini-secondpass-6.md:3101 | lines 1043 | verdict Verified
- WHAT: Comprehensive architectural audit and master catalog of 70 infrastructure and operations resources across seven operational pillars: (1) Web Scraping & Crawling (Scrapy, Crawlee, Apify, Firecrawl, Crawl4AI, BeautifulSoup4, lxml, Cheerio, Playwright, curl_cffi); (2) Public APIs & Integration Standards (GitHub REST/GraphQL, Stripe, Twilio, OpenAI, Algolia, Open-Meteo, IPinfo, Open Exchange Rates, Re
- HOW: 1. Enforce True Security Perimeters: Never rely on natural language prompt instructions (CLAUDE.md, .cursorrules) for security boundaries. Use enforceable isolation: Firecracker microVMs or gVisor runsc for untrusted agent code execution, and deterministic CI gates (Semgrep, CodeQL, TruffleHog) to b
- live: no live URLs
- conflicts: Security perimeter taxonomy: Clarifies critical distinction between [ENFORCEABLE] kernel/hypervisor/cryptographic boundaries (Firecracker, gVisor, Docker, seccomp) and [PROMPT-ONLY] heuristics (system prompts, NeMo Guardrails) which are inherently bypassable via prompt injection., OpenTofu vs Terraform: OpenTofu operates as the Linux Foundation open-source MPL-2.0 fork in response to HashiCorp's BSL licensing change on Terraform., Headless browser vs static fetching: High memory overhead and fingerprint detectability of Playwright/Puppeteer contrasted with low-overhead TLS fingerprint spoofing via curl_cffi.

### files/God research/agy-pass/01-core-web-tech.md
- card: files/God research/agy-pass/01-core-web-tech.md | part parts/10-agy-thirdpass-7.md:41 | lines 961 | verdict Verified
- WHAT: Technical reference catalog of 76 verified Core Web Technologies across 9 architectural disciplines: 1. Languages (8: HTML Living Standard, CSS Spec, ECMAScript, TypeScript, WebAssembly, Python, Rust, Go); 2. Frontend Frameworks & Libraries (10: React, Vue.js, Angular, Svelte, Next.js, Nuxt, SvelteKit, Astro, SolidJS, Lit); 3. Styling & Design Tooling (8: Tailwind CSS, Sass, PostCSS, CSS Modules, 
- HOW: Language & Runtime: Default to TypeScript for end-to-end type safety; run server workloads on Node.js 18+ or Bun; deploy edge microservices to Cloudflare Workers or Deno using Web Standards APIs.
- live: no live URLs
- conflicts: Runtime CSS-in-JS vs Server Components: Runtime CSS-in-JS (Emotion, styled-components) conflicts with React Server Components streaming architecture, necessitating zero-runtime build-time solutions like Tailwind CSS, Vanilla Extract, and Panda CSS., Edge Runtime vs Node.js Compatibility: Edge runtimes (Cloudflare Workers, V8 isolates) lack native Node.js C++ bindings and raw socket access, requiring Web Standards API compliance or polyfill layers., ORM Abstraction Trade-off: Prisma provides automated migrations and high-level client abstractions with binary engine overhead, whereas Drizzle ORM provides zero-overhead SQL-like type safety and instant cold starts.

### files/solo-levelling/phase-16-loop-engineering.md
- card: files/solo-levelling/phase-16-loop-engineering.md | part parts/13-deve-solo.md:8883 | lines 86 | verdict Verified
- WHAT: Comprehensive research findings on Loop Engineering for autonomous agents, analyzing structural failure modes of naive loops (infinite loops, design fixation, plan drift), termination conditions (Evidence-Carrying Termination, arXiv:2608.23623), co-regulation mechanisms (CRDAL), and the reliability-vs-autonomy tension (arXiv:2605.10907).
- HOW: 1. Replace open-ended generative agent loops with rigid, pre-engineered state machines.
- live: no live URLs
- conflicts: none

### files/solo-levelling/verification.md
- card: files/solo-levelling/verification.md | part parts/13-deve-solo.md:37271 | lines 760 | verdict Verified
- WHAT: Exhaustive verification audit log and evidence ledger systematically auditing every research phase (Phases 1 through 15) against primary sources, verifying evidence tags ([PRIMARY], [INFERRED], [SPECULATIVE], [NOT FOUND]), assessing tag integrity, and correcting methodological inconsistencies.
- HOW: 1. Consult verification logs to verify the primary source trail and evidence classification of any engineering practice.
- live: no live URLs
- conflicts: none

### files/solo-levelling/findings/phase-01-findings.md
- card: files/solo-levelling/findings/phase-01-findings.md | part parts/13-deve-solo.md:4578 | lines 113 | verdict Verified
- WHAT: Phase 1 research findings locking the 14-term engineering governance glossary, confirming the target organization shortlist (Amazon, Google, Meta, Netflix, Stripe, Basecamp/37signals), and establishing the explicitly undecided status of the AI system shape.
- HOW: 1. Refer to glossary definitions to prevent semantic drift across subsequent phases.
- live: no live URLs
- conflicts: none

### files/solo-levelling/findings/phase-02-findings.md
- card: files/solo-levelling/findings/phase-02-findings.md | part parts/13-deve-solo.md:4692 | lines 383 | verdict Verified
- WHAT: Phase 2 research findings analyzing how benchmark organizations transition from ideas to verified product theses, comparing Amazon Working Backwards (PR/FAQ), Basecamp Shape Up (Pitches & Appetite), Google OKR alignments, Meta Hackathons, and Stripe business theses.
- HOW: 1. Synthesize Amazon PR/FAQ with Basecamp Shape Up Pitch for solo development.
- live: no live URLs
- conflicts: none

### files/solo-levelling/findings/phase-03-findings.md
- card: files/solo-levelling/findings/phase-03-findings.md | part parts/13-deve-solo.md:5076 | lines 270 | verdict Verified
- WHAT: Phase 3 research findings investigating scope management, requirement bounding, non-goals, and trade-off documentation across Amazon, Google, Meta, Netflix, Stripe, and Basecamp.
- HOW: 1. Require at least two explicit, non-trivial Non-Goals in every product pitch and design doc.
- live: no live URLs
- conflicts: none

### files/solo-levelling/findings/phase-04-findings.md
- card: files/solo-levelling/findings/phase-04-findings.md | part parts/13-deve-solo.md:5347 | lines 219 | verdict Verified
- WHAT: Phase 4 research findings investigating UX flow formalization, product specifications, edge-case enumeration, and breadboarding techniques across benchmark engineering organizations.
- HOW: 1. Utilize breadboarding (Places, Affordances, Connection lines) to map UX flows without premature pixel polishing.
- live: no live URLs
- conflicts: none

### files/solo-levelling/findings/phase-05-findings.md
- card: files/solo-levelling/findings/phase-05-findings.md | part parts/13-deve-solo.md:5567 | lines 251 | verdict Verified
- WHAT: Phase 5 research findings evaluating technical design documents, RFCs, and architectural review processes across Amazon, Google, Meta, Netflix, Stripe, and Basecamp, establishing the FCAR (Failure-Mode, Context, Alternatives, Risks) framework.
- HOW: 1. Draft technical design notes containing Context, Goals, Non-Goals, Alternatives Considered (min 2), and Top-3 Failure Modes.
- live: no live URLs
- conflicts: none

### files/solo-levelling/findings/phase-06-findings.md
- card: files/solo-levelling/findings/phase-06-findings.md | part parts/13-deve-solo.md:5819 | lines 232 | verdict Verified
- WHAT: Phase 6 research findings exploring system context, architectural boundaries, API contracts, data schema evolution, and dependency isolation across benchmark tech companies.
- HOW: 1. Define explicit interface contracts (OpenAPI, typed schemas, strict interfaces) before implementing cross-module communication.
- live: no live URLs
- conflicts: none

### files/solo-levelling/findings/phase-07-findings.md
- card: files/solo-levelling/findings/phase-07-findings.md | part parts/13-deve-solo.md:6052 | lines 202 | verdict Verified
- WHAT: Phase 7 research findings on security, privacy, and reliability reviews, analyzing threat modeling (STRIDE), credential protection, least-privilege access, and automated security scans.
- HOW: 1. Perform threat modeling on data entry points, authentication boundaries, and third-party integrations.
- live: no live URLs
- conflicts: none

### files/solo-levelling/findings/phase-08-findings.md
- card: files/solo-levelling/findings/phase-08-findings.md | part parts/13-deve-solo.md:6255 | lines 211 | verdict Verified
- WHAT: Phase 8 research findings on implementation planning, task decomposition, and uphill/downhill work sequencing, adapting Basecamp hill charts and agile task breakdown for solo developers.
- HOW: 1. Decompose features into vertically integrated, testable scopes rather than horizontal architecture layers.
- live: no live URLs
- conflicts: none

### files/solo-levelling/findings/phase-09-findings.md
- card: files/solo-levelling/findings/phase-09-findings.md | part parts/13-deve-solo.md:6467 | lines 201 | verdict Verified
- WHAT: Phase 9 research findings investigating code review mechanisms, automated linting, type-checking gates, and quality systems across Amazon, Google, Meta, Netflix, Stripe, and Basecamp.
- HOW: 1. Delegate syntactic and stylistic enforcement entirely to automated linters and type checkers.
- live: no live URLs
- conflicts: none

### files/solo-levelling/findings/phase-10-findings.md
- card: files/solo-levelling/findings/phase-10-findings.md | part parts/13-deve-solo.md:6669 | lines 233 | verdict Verified
- WHAT: Phase 10 research findings examining automated testing strategies (unit, integration, E2E), test-driven development (TDD), experimentation frameworks, and progressive rollout mechanisms.
- HOW: 1. Enforce strict Test-Driven Development: write failing tests before writing solution code.
- live: no live URLs
- conflicts: none

### files/solo-levelling/findings/phase-11-findings.md
- card: files/solo-levelling/findings/phase-11-findings.md | part parts/13-deve-solo.md:6903 | lines 199 | verdict Verified
- WHAT: Phase 11 empirical findings across 5 tech giants (Amazon, Google, Meta, Netflix, Stripe) investigating Observability, Incident Response, and Postmortems across 6 key questions: postmortem trigger thresholds, blameless policy enforcement, SLO/error budget definitions, on-call rotation structures, incident commander roles, and postmortem corrective action tracking.
- HOW: Reference Amazon COE and Google SRE blameless Five-Whys methodology to structure systemic root cause analysis chaining to systems instead of individuals
- live: no live URLs
- conflicts: none

### files/solo-levelling/findings/phase-12-findings.md
- card: files/solo-levelling/findings/phase-12-findings.md | part parts/13-deve-solo.md:7103 | lines 170 | verdict Verified
- WHAT: Phase 12 empirical findings auditing the documented production role of AI and verified correctness across Amazon, Google, Meta, Netflix, and Stripe, evaluating code generation adoption, AI PR review gate status, synthetic test generation limits, hallucination defense mechanisms, and production rollback metrics.
- HOW: Apply the findings that AI PR reviews must operate as soft vetos or advisory signals rather than hard automated gates without human accountability
- live: no live URLs
- conflicts: none

### files/solo-levelling/findings/phase-13-findings.md
- card: files/solo-levelling/findings/phase-13-findings.md | part parts/13-deve-solo.md:7274 | lines 286 | verdict Verified
- WHAT: Phase 13 compression analysis translating complex enterprise processes from Phases 2 through 12 into lean solo developer equivalents augmented by AI, determining the AI system shape (orchestrator with specialized subagents) and consolidating the formal 'Bureaucracy to Discard' register.
- HOW: Consult Pass 13.1 and 13.2 mapping tables to replace enterprise committees (RFC reviews, architecture boards, change advisory boards) with deterministic artifacts (Design Notes, FCAR, PR checklists)
- live: no live URLs
- conflicts: none

### files/solo-levelling/findings/phase-14-findings.md
- card: files/solo-levelling/findings/phase-14-findings.md | part parts/13-deve-solo.md:7561 | lines 119 | verdict Verified
- WHAT: Phase 14 stress-test report analyzing failure modes inherent to the solo AI engineering system itself, designing the Fresh Context Adversarial Review (FCAR) mechanism, validating it via an injected-flaw test, and detailing coverage for 8 specific failure modes including context rot, mid-build scope drift, and silent failures.
- HOW: Deploy the FCAR protocol using fresh, unpolluted LLM context windows to review proposed designs and implementation artifacts
- live: no live URLs
- conflicts: none

### files/solo-levelling/findings/phase-15-master-synthesis.md
- card: files/solo-levelling/findings/phase-15-master-synthesis.md | part parts/13-deve-solo.md:7681 | lines 651 | verdict Verified
- WHAT: Phase 15 Master Synthesis synthesizing the complete Solo AI Product Engineering System v1.0 across 11 comprehensive operational sections: Lifecycle, Role Model, Artifact Chain, Decision Architecture, Decision Gates, Quality/Security/Reliability, Release/Experiments, Loop Engineering integration, Engineering Rules, Governance, and Full System Walkthrough.
- HOW: Follow the 6-stage lifecycle (Idea -> Pitch -> Design -> Implementation -> Launch -> Postmortem) with strict artifact gates
- live: no live URLs
- conflicts: none

### files/solo-levelling/scripts/scope-check.py
- card: files/solo-levelling/scripts/scope-check.py | part parts/13-deve-solo.md:9020 | lines 83 | verdict Verified
- WHAT: Python CLI script enforcing PR scope boundaries by analyzing git diff statistics against configurable line addition and file modification limits (defaults: max 400 lines added, max 10 files modified) to enforce small PR discipline.
- HOW: Run 'python3 scripts/scope-check.py' against unstaged or committed changes
- live: no live URLs
- conflicts: none

### files/solo-levelling/scripts/secret-scan.sh
- card: files/solo-levelling/scripts/secret-scan.sh | part parts/13-deve-solo.md:9104 | lines 43 | verdict Verified
- WHAT: Bash security script scanning git repository files for hardcoded secrets, API tokens, private keys, and cloud credentials (OpenAI sk-, Anthropic sk-ant-, AWS AKIA/ASIA, private keys, high-entropy tokens) using ripgrep or grep.
- HOW: Execute 'bash scripts/secret-scan.sh [path]' to scan working directory or specific files
- live: no live URLs
- conflicts: none

### files/solo-levelling/scripts/verify.sh
- card: files/solo-levelling/scripts/verify.sh | part parts/13-deve-solo.md:9148 | lines 52 | verdict Verified
- WHAT: Master verification shell script executing the complete automated test and lint suite (pre-commit checks, secret scan, scope check, unit tests, linters) and reporting an aggregated pass/fail verdict for Gate 5 and Gate 6.
- HOW: Run 'bash scripts/verify.sh' from repository root
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/.harness/skills/01-repo-surveyor-map/scripts/survey_repo.py
- card: files/solo-levelling/the harness/.harness/skills/01-repo-surveyor-map/scripts/survey_repo.py | part parts/13-deve-solo.md:10722 | lines 130 | verdict Verified
- WHAT: Deterministic repository survey script extracting tech stack manifests, building bounded directory trees (excluding build/vendor directories), identifying entrypoints, and generating markdown architectural summaries.
- HOW: Run via python: python3 .harness/skills/01-repo-surveyor-map/scripts/survey_repo.py [target_dir]
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/.harness/skills/02-git-worktree-isolation/scripts/create_worktree.sh
- card: files/solo-levelling/the harness/.harness/skills/02-git-worktree-isolation/scripts/create_worktree.sh | part parts/13-deve-solo.md:10966 | lines 44 | verdict Verified
- WHAT: Bash script automating Git worktree provisioning, branch initialization (feat/<name>), and dependency environment setup in a dedicated sibling directory.
- HOW: Execute script: bash .harness/skills/02-git-worktree-isolation/scripts/create_worktree.sh <feature-name> [base-ref]
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/.harness/skills/09-docker-sandbox-runner/scripts/sandbox_run.sh
- card: files/solo-levelling/the harness/.harness/skills/09-docker-sandbox-runner/scripts/sandbox_run.sh | part parts/13-deve-solo.md:11560 | lines 123 | verdict Verified
- WHAT: Sane-default wrapper script for .harness/sandbox/gate.sh defaulting to read-only workspace mounts and air-gapped networking with optional --rw write toggles.
- HOW: Run safe command: bash .harness/skills/09-docker-sandbox-runner/scripts/sandbox_run.sh [OPTIONS] -- COMMAND
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/.harness/skills/32-secrets-entropy-sanitizer/scripts/entropy_scan.sh
- card: files/solo-levelling/the harness/.harness/skills/32-secrets-entropy-sanitizer/scripts/entropy_scan.sh | part parts/13-deve-solo.md:12701 | lines 54 | verdict Verified
- WHAT: Pre-commit secret detection script utilizing Gitleaks and fallback regex patterns to intercept high-entropy credentials, API keys, and private keys.
- HOW: Run script: bash .harness/skills/32-secrets-entropy-sanitizer/scripts/entropy_scan.sh [target_dir]
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-0/ARCHETYPES_AND_CRITERIA.md
- card: files/solo-levelling/the harness/phase-0/ARCHETYPES_AND_CRITERIA.md | part parts/13-deve-solo.md:15666 | lines 210 | verdict Verified
- WHAT: Phase 0 project anchoring research and synthesis artifact ('ARCHETYPES_AND_CRITERIA') defining the 6 canonical archetypes (C1-C6), 10 measurable success criteria (SC-01..10), and verifier reports.
- HOW: Reference ARCHETYPES_AND_CRITERIA for foundational archetype definitions and success criteria derivation
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-0/R-A_BROAD_MAPPER.md
- card: files/solo-levelling/the harness/phase-0/R-A_BROAD_MAPPER.md | part parts/13-deve-solo.md:15877 | lines 484 | verdict Verified
- WHAT: Phase 0 project anchoring research and synthesis artifact ('R-A_BROAD_MAPPER') defining the 6 canonical archetypes (C1-C6), 10 measurable success criteria (SC-01..10), and verifier reports.
- HOW: Reference R-A_BROAD_MAPPER for foundational archetype definitions and success criteria derivation
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-0/R-B_CHALLENGER.md
- card: files/solo-levelling/the harness/phase-0/R-B_CHALLENGER.md | part parts/13-deve-solo.md:16362 | lines 183 | verdict Verified
- WHAT: Phase 0 project anchoring research and synthesis artifact ('R-B_CHALLENGER') defining the 6 canonical archetypes (C1-C6), 10 measurable success criteria (SC-01..10), and verifier reports.
- HOW: Reference R-B_CHALLENGER for foundational archetype definitions and success criteria derivation
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-0/STATUS.md
- card: files/solo-levelling/the harness/phase-0/STATUS.md | part parts/13-deve-solo.md:16546 | lines 43 | verdict Verified
- WHAT: Phase 0 project anchoring research and synthesis artifact ('STATUS') defining the 6 canonical archetypes (C1-C6), 10 measurable success criteria (SC-01..10), and verifier reports.
- HOW: Reference STATUS for foundational archetype definitions and success criteria derivation
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-0/V-C_ADVERSARIAL.md
- card: files/solo-levelling/the harness/phase-0/V-C_ADVERSARIAL.md | part parts/13-deve-solo.md:16590 | lines 124 | verdict Verified
- WHAT: Phase 0 project anchoring research and synthesis artifact ('V-C_ADVERSARIAL') defining the 6 canonical archetypes (C1-C6), 10 measurable success criteria (SC-01..10), and verifier reports.
- HOW: Reference V-C_ADVERSARIAL for foundational archetype definitions and success criteria derivation
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-0/V-D_ARCHITECTURAL.md
- card: files/solo-levelling/the harness/phase-0/V-D_ARCHITECTURAL.md | part parts/13-deve-solo.md:16715 | lines 143 | verdict Verified
- WHAT: Phase 0 project anchoring research and synthesis artifact ('V-D_ARCHITECTURAL') defining the 6 canonical archetypes (C1-C6), 10 measurable success criteria (SC-01..10), and verifier reports.
- HOW: Reference V-D_ARCHITECTURAL for foundational archetype definitions and success criteria derivation
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-1/MASTER_TAXONOMY.md
- card: files/solo-levelling/the harness/phase-1/MASTER_TAXONOMY.md | part parts/13-deve-solo.md:16859 | lines 475 | verdict Verified
- WHAT: Phase 1 element discovery and master taxonomy artifact ('MASTER_TAXONOMY') documenting candidate longlists, challenger sweeps, adversarial verification, and convergence across harness layers.
- HOW: Consult MASTER_TAXONOMY to examine capability definitions, tool trade-offs, and layer convergence
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-1/STATUS.md
- card: files/solo-levelling/the harness/phase-1/STATUS.md | part parts/13-deve-solo.md:17335 | lines 32 | verdict Verified
- WHAT: Phase 1 element discovery and master taxonomy artifact ('STATUS') documenting candidate longlists, challenger sweeps, adversarial verification, and convergence across harness layers.
- HOW: Consult STATUS to examine capability definitions, tool trade-offs, and layer convergence
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-1/batch-1/BATCH-1_EXECUTION_AND_AGENCY.md
- card: files/solo-levelling/the harness/phase-1/batch-1/BATCH-1_EXECUTION_AND_AGENCY.md | part parts/13-deve-solo.md:17368 | lines 210 | verdict Verified
- WHAT: Phase 1 element discovery and master taxonomy artifact ('BATCH-1_EXECUTION_AND_AGENCY') documenting candidate longlists, challenger sweeps, adversarial verification, and convergence across harness layers.
- HOW: Consult BATCH-1_EXECUTION_AND_AGENCY to examine capability definitions, tool trade-offs, and layer convergence
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-1/batch-1/R-A_BROAD_MAPPER.md
- card: files/solo-levelling/the harness/phase-1/batch-1/R-A_BROAD_MAPPER.md | part parts/13-deve-solo.md:17579 | lines 424 | verdict Verified
- WHAT: Phase 1 element discovery and master taxonomy artifact ('R-A_BROAD_MAPPER') documenting candidate longlists, challenger sweeps, adversarial verification, and convergence across harness layers.
- HOW: Consult R-A_BROAD_MAPPER to examine capability definitions, tool trade-offs, and layer convergence
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-1/batch-1/R-B_CHALLENGER.md
- card: files/solo-levelling/the harness/phase-1/batch-1/R-B_CHALLENGER.md | part parts/13-deve-solo.md:18004 | lines 256 | verdict Verified
- WHAT: Phase 1 element discovery and master taxonomy artifact ('R-B_CHALLENGER') documenting candidate longlists, challenger sweeps, adversarial verification, and convergence across harness layers.
- HOW: Consult R-B_CHALLENGER to examine capability definitions, tool trade-offs, and layer convergence
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-1/batch-1/V-C_ADVERSARIAL.md
- card: files/solo-levelling/the harness/phase-1/batch-1/V-C_ADVERSARIAL.md | part parts/13-deve-solo.md:18261 | lines 93 | verdict Verified
- WHAT: Phase 1 element discovery and master taxonomy artifact ('V-C_ADVERSARIAL') documenting candidate longlists, challenger sweeps, adversarial verification, and convergence across harness layers.
- HOW: Consult V-C_ADVERSARIAL to examine capability definitions, tool trade-offs, and layer convergence
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-1/batch-1/V-D_ARCHITECTURAL.md
- card: files/solo-levelling/the harness/phase-1/batch-1/V-D_ARCHITECTURAL.md | part parts/13-deve-solo.md:18355 | lines 121 | verdict Verified
- WHAT: Phase 1 element discovery and master taxonomy artifact ('V-D_ARCHITECTURAL') documenting candidate longlists, challenger sweeps, adversarial verification, and convergence across harness layers.
- HOW: Consult V-D_ARCHITECTURAL to examine capability definitions, tool trade-offs, and layer convergence
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-1/batch-2/BATCH-2_CONTEXT_MEMORY_KNOWLEDGE.md
- card: files/solo-levelling/the harness/phase-1/batch-2/BATCH-2_CONTEXT_MEMORY_KNOWLEDGE.md | part parts/13-deve-solo.md:18477 | lines 239 | verdict Verified
- WHAT: Phase 1 element discovery and master taxonomy artifact ('BATCH-2_CONTEXT_MEMORY_KNOWLEDGE') documenting candidate longlists, challenger sweeps, adversarial verification, and convergence across harness layers.
- HOW: Consult BATCH-2_CONTEXT_MEMORY_KNOWLEDGE to examine capability definitions, tool trade-offs, and layer convergence
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-1/batch-2/R-A_BROAD_MAPPER.md
- card: files/solo-levelling/the harness/phase-1/batch-2/R-A_BROAD_MAPPER.md | part parts/13-deve-solo.md:18717 | lines 576 | verdict Verified
- WHAT: Phase 1 element discovery and master taxonomy artifact ('R-A_BROAD_MAPPER') documenting candidate longlists, challenger sweeps, adversarial verification, and convergence across harness layers.
- HOW: Consult R-A_BROAD_MAPPER to examine capability definitions, tool trade-offs, and layer convergence
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-1/batch-2/R-B_CHALLENGER.md
- card: files/solo-levelling/the harness/phase-1/batch-2/R-B_CHALLENGER.md | part parts/13-deve-solo.md:19294 | lines 299 | verdict Verified
- WHAT: Phase 1 element discovery and master taxonomy artifact ('R-B_CHALLENGER') documenting candidate longlists, challenger sweeps, adversarial verification, and convergence across harness layers.
- HOW: Consult R-B_CHALLENGER to examine capability definitions, tool trade-offs, and layer convergence
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-1/batch-2/V-C_ADVERSARIAL.md
- card: files/solo-levelling/the harness/phase-1/batch-2/V-C_ADVERSARIAL.md | part parts/13-deve-solo.md:19594 | lines 73 | verdict Verified
- WHAT: Phase 1 element discovery and master taxonomy artifact ('V-C_ADVERSARIAL') documenting candidate longlists, challenger sweeps, adversarial verification, and convergence across harness layers.
- HOW: Consult V-C_ADVERSARIAL to examine capability definitions, tool trade-offs, and layer convergence
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-1/batch-2/V-D_ARCHITECTURAL.md
- card: files/solo-levelling/the harness/phase-1/batch-2/V-D_ARCHITECTURAL.md | part parts/13-deve-solo.md:19668 | lines 116 | verdict Verified
- WHAT: Phase 1 element discovery and master taxonomy artifact ('V-D_ARCHITECTURAL') documenting candidate longlists, challenger sweeps, adversarial verification, and convergence across harness layers.
- HOW: Consult V-D_ARCHITECTURAL to examine capability definitions, tool trade-offs, and layer convergence
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-1/batch-3/BATCH-3_INTEGRATION_EXTENSIBILITY.md
- card: files/solo-levelling/the harness/phase-1/batch-3/BATCH-3_INTEGRATION_EXTENSIBILITY.md | part parts/13-deve-solo.md:19785 | lines 112 | verdict Verified
- WHAT: Phase 1 element discovery and master taxonomy artifact ('BATCH-3_INTEGRATION_EXTENSIBILITY') documenting candidate longlists, challenger sweeps, adversarial verification, and convergence across harness layers.
- HOW: Consult BATCH-3_INTEGRATION_EXTENSIBILITY to examine capability definitions, tool trade-offs, and layer convergence
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-1/batch-3/R-A_BROAD_MAPPER_AGY.md
- card: files/solo-levelling/the harness/phase-1/batch-3/R-A_BROAD_MAPPER_AGY.md | part parts/13-deve-solo.md:19898 | lines 205 | verdict Verified
- WHAT: Phase 1 element discovery and master taxonomy artifact ('R-A_BROAD_MAPPER_AGY') documenting candidate longlists, challenger sweeps, adversarial verification, and convergence across harness layers.
- HOW: Consult R-A_BROAD_MAPPER_AGY to examine capability definitions, tool trade-offs, and layer convergence
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-1/batch-3/R-A_BROAD_MAPPER_PARTIAL.md
- card: files/solo-levelling/the harness/phase-1/batch-3/R-A_BROAD_MAPPER_PARTIAL.md | part parts/13-deve-solo.md:20104 | lines 85 | verdict Verified
- WHAT: Phase 1 element discovery and master taxonomy artifact ('R-A_BROAD_MAPPER_PARTIAL') documenting candidate longlists, challenger sweeps, adversarial verification, and convergence across harness layers.
- HOW: Consult R-A_BROAD_MAPPER_PARTIAL to examine capability definitions, tool trade-offs, and layer convergence
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-1/batch-3/R-B_CHALLENGER_AGY_.md
- card: files/solo-levelling/the harness/phase-1/batch-3/R-B_CHALLENGER_AGY_.md | part parts/13-deve-solo.md:20190 | lines 240 | verdict Verified
- WHAT: Phase 1 element discovery and master taxonomy artifact ('R-B_CHALLENGER_AGY_') documenting candidate longlists, challenger sweeps, adversarial verification, and convergence across harness layers.
- HOW: Consult R-B_CHALLENGER_AGY_ to examine capability definitions, tool trade-offs, and layer convergence
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-1/batch-3/V-C_ADVERSARIAL_AGY.md
- card: files/solo-levelling/the harness/phase-1/batch-3/V-C_ADVERSARIAL_AGY.md | part parts/13-deve-solo.md:20431 | lines 336 | verdict Verified
- WHAT: Phase 1 element discovery and master taxonomy artifact ('V-C_ADVERSARIAL_AGY') documenting candidate longlists, challenger sweeps, adversarial verification, and convergence across harness layers.
- HOW: Consult V-C_ADVERSARIAL_AGY to examine capability definitions, tool trade-offs, and layer convergence
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-1/batch-3/V-D_ARCHITECTURAL_AGY.md
- card: files/solo-levelling/the harness/phase-1/batch-3/V-D_ARCHITECTURAL_AGY.md | part parts/13-deve-solo.md:20768 | lines 307 | verdict Verified
- WHAT: Phase 1 element discovery and master taxonomy artifact ('V-D_ARCHITECTURAL_AGY') documenting candidate longlists, challenger sweeps, adversarial verification, and convergence across harness layers.
- HOW: Consult V-D_ARCHITECTURAL_AGY to examine capability definitions, tool trade-offs, and layer convergence
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-1/batch-4/BATCH-4_SAFETY_GOVERNANCE.md
- card: files/solo-levelling/the harness/phase-1/batch-4/BATCH-4_SAFETY_GOVERNANCE.md | part parts/13-deve-solo.md:21076 | lines 109 | verdict Verified
- WHAT: Phase 1 element discovery and master taxonomy artifact ('BATCH-4_SAFETY_GOVERNANCE') documenting candidate longlists, challenger sweeps, adversarial verification, and convergence across harness layers.
- HOW: Consult BATCH-4_SAFETY_GOVERNANCE to examine capability definitions, tool trade-offs, and layer convergence
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-2/verify/ARBITER_AGY.md
- card: files/solo-levelling/the harness/phase-2/verify/ARBITER_AGY.md | part parts/13-deve-solo.md:26572 | lines 205 | verdict Unverified
- WHAT: Independent arbiter re-rank of 37 CAPs (22S/11A/3B/1C) confirming 11 veto bedrock items and reconciling CAP-14 downgrade and CAP-16 upgrade.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-2/verify/CROSSBATCH_TENSION.md
- card: files/solo-levelling/the harness/phase-2/verify/CROSSBATCH_TENSION.md | part parts/13-deve-solo.md:26779 | lines 168 | verdict Unverified
- WHAT: Cross-batch tension resolver certifying 12 pairs RESOLVED PASS, 5 resource competitions bounded by invariants, and final 22S/11A/3B/1C tiers.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-2/verify/MECH_PROT_AGY.md
- card: files/solo-levelling/the harness/phase-2/verify/MECH_PROT_AGY.md | part parts/13-deve-solo.md:26948 | lines 279 | verdict Unverified
- WHAT: Mechanism/protocol grounding map: 10 MEC + 4 PROT verified 10/10 and 3/3 PASS, each parented to a CAP with OSS grounding for phase-3 selection.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-2/verify/MECH_PROT_P3_SCOUT.md
- card: files/solo-levelling/the harness/phase-2/verify/MECH_PROT_P3_SCOUT.md | part parts/13-deve-solo.md:27228 | lines 10 | verdict Unverified
- WHAT: Ten-line opencode run log stub (instance bootstrap/config load) with no taxonomy or verification content; scout failed to write its report.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-3.5/V_AUTHOR_AGY.md
- card: files/solo-levelling/the harness/phase-3.5/V_AUTHOR_AGY.md | part parts/13-deve-solo.md:27743 | lines 256 | verdict Unverified
- WHAT: Skill-authoring validation: repo-surveyor-map SKILL plus survey_repo.py runner, TDD reference skill, 40-skill index with VA-01..VA-04 gates and token-cost evidence.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-3.5/V_COHERENCE_AGY.md
- card: files/solo-levelling/the harness/phase-3.5/V_COHERENCE_AGY.md | part parts/13-deve-solo.md:28000 | lines 195 | verdict Unverified
- WHAT: Coherence audit finding 2/21 S-tier operational, 4 partial, 15 gaps, with 5 integration conflicts (MCP truncation, orphaned guard, regex FPs, ghost skills, Cedar disconnect).
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-3/tools/T-A_EXECUTION.md
- card: files/solo-levelling/the harness/phase-3/tools/T-A_EXECUTION.md | part parts/13-deve-solo.md:28349 | lines 206 | verdict Unverified
- WHAT: Execution-stack selection: LangGraph plus Temporal plus worktree isolation with bounded concurrency; rejects flat ReAct, AgentExecutor, bash DAGs.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-3/tools/T-B_CONTEXT.md
- card: files/solo-levelling/the harness/phase-3/tools/T-B_CONTEXT.md | part parts/13-deve-solo.md:28556 | lines 416 | verdict Unverified
- WHAT: Context-stack selection: Qdrant/LanceDB plus LlamaIndex plus Letta/Mem0 with LLMLingua/Tree-sitter/Repomix compaction; Pinecone avoided for SaaS lock-in.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-3/tools/T-C_INTEGRATION.md
- card: files/solo-levelling/the harness/phase-3/tools/T-C_INTEGRATION.md | part parts/13-deve-solo.md:28973 | lines 493 | verdict Unverified
- WHAT: Integration blueprint: MCP registries/servers, 40-skill catalog, ambient rules precedence, hooks lifecycle, LiteLLM gateway with concrete config snippets.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-3/tools/T-D_SAFETY.md
- card: files/solo-levelling/the harness/phase-3/tools/T-D_SAFETY.md | part parts/13-deve-solo.md:29467 | lines 679 | verdict Unverified
- WHAT: Containment shield: hermetic sandboxes (gVisor/Bubblewrap/Docker) plus OPA/Cedar/CEL PDPs, JIT secrets/DLP, XML injection fencing, HITL, reversible worktrees.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-3/tools/T-E_DX_META.md
- card: files/solo-levelling/the harness/phase-3/tools/T-E_DX_META.md | part parts/13-deve-solo.md:30150 | lines 327 | verdict Unverified
- WHAT: DX gate stack: Inspect/SWE-bench/Promptfoo eval plus LiteLLM/Langfuse cost proxy plus pre-commit/Ruff/Gitleaks/sandbox/HITL AHG gate.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-3/tools/T-F_A_TIER.md
- card: files/solo-levelling/the harness/phase-3/tools/T-F_A_TIER.md | part parts/13-deve-solo.md:30478 | lines 382 | verdict Unverified
- WHAT: A-tier stack: Temporal durable async, Mem0/Letta memory, LlamaIndex hybrid recall, 3-layer token budget, LiteLLM dynamic routing.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-3/tools/T-G_A_TIER_2.md
- card: files/solo-levelling/the harness/phase-3/tools/T-G_A_TIER_2.md | part parts/13-deve-solo.md:30861 | lines 317 | verdict Unverified
- WHAT: Governance stack: OTel/JSONL/Phoenix provenance, Cosign/SLSA supply chain, DSPy self-optimization, Semgrep/deprecated lifecycle enforcement.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-3/tools/T-H_B_TIER.md
- card: files/solo-levelling/the harness/phase-3/tools/T-H_B_TIER.md | part parts/13-deve-solo.md:31179 | lines 371 | verdict Unverified
- WHAT: Situational toolkit: LangGraph teams, Graphiti temporal KG, guarded RedisVL semantic cache (exact-match rule for codegen), DeepEval judge calibration.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-3/verify/CROSS_TOOL_OVERLAP.md
- card: files/solo-levelling/the harness/phase-3/verify/CROSS_TOOL_OVERLAP.md | part parts/13-deve-solo.md:31551 | lines 187 | verdict Unverified
- WHAT: Dedup sweep: 114 tool mentions across T-A..T-H resolved to 55 canonical Essential primitives via 27 KEEP, 2 SPLIT (LiteLLM, worktree), 2 REMOVE (RouteLLM, Lakera).
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-3/verify/VERIFICATION_PASS1.md
- card: files/solo-levelling/the harness/phase-3/verify/VERIFICATION_PASS1.md | part parts/13-deve-solo.md:31739 | lines 101 | verdict Unverified
- WHAT: 45-tool audit (T-B/T-D/T-F/T-H): 43 PASS, 2 FAIL demoted (Lakera 404 SaaS, RouteLLM stale since 2024-08) with license notes.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/phase-3/verify/VERIFICATION_PASS2.md
- card: files/solo-levelling/the harness/phase-3/verify/VERIFICATION_PASS2.md | part parts/13-deve-solo.md:31841 | lines 154 | verdict Unverified
- WHAT: 46-primitive audit (T-A/T-C/T-E/T-G): 46 PASS 0 FAIL retaining all Essential stacks, plus 13 Avoid anti-patterns cataloged.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/scripts/__init__.py
- card: files/solo-levelling/the harness/scripts/__init__.py | part parts/13-deve-solo.md:32390 | lines 1 | verdict Unverified
- WHAT: Single-line package marker enabling scripts.* imports with zero runtime behavior.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/scripts/mock_telemetry_daemon.py
- card: files/solo-levelling/the harness/scripts/mock_telemetry_daemon.py | part parts/13-deve-solo.md:32392 | lines 517 | verdict Unverified
- WHAT: Stdlib-only offline OTLP/Langfuse mock sink: dual ports, ring buffer plus JSONL persistence, normalized gen_ai attributes, cost aggregation, graceful shutdown.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/validation/REMAINING_GAPS.md
- card: files/solo-levelling/the harness/validation/REMAINING_GAPS.md | part parts/13-deve-solo.md:33061 | lines 270 | verdict Unverified
- WHAT: Consolidated 135-finding scorecard (93 correct, 24 partial, 18 fail) with 18 HIGH defects matrix and P0-P4 remediation roadmap.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/validation/V-KB-1.md
- card: files/solo-levelling/the harness/validation/V-KB-1.md | part parts/13-deve-solo.md:33332 | lines 154 | verdict Unverified
- WHAT: KB audit of D-1/D-3: CAP-06 tier gap, CAP-18/19 archetype contradictions, RouteLLM gate-failed cite; requires 4 line fixes.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/validation/V-KB-2.md
- card: files/solo-levelling/the harness/validation/V-KB-2.md | part parts/13-deve-solo.md:33487 | lines 148 | verdict Unverified
- WHAT: KB audit of D-2/D-4: CAP-10 string contradiction, hooks/ path typos, nonexistent flight_recorder.py link; tiers otherwise validated vs disk.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/validation/V-KB-3.md
- card: files/solo-levelling/the harness/validation/V-KB-3.md | part parts/13-deve-solo.md:33636 | lines 110 | verdict Unverified
- WHAT: KB audit of D-5/D-6 plus tension review: RouteLLM purge, 7 missing A-tier pointers, MEC-02 typo, 5 omitted tensions proposed for the Interaction Map.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/validation/V-KB-4.md
- card: files/solo-levelling/the harness/validation/V-KB-4.md | part parts/13-deve-solo.md:33747 | lines 105 | verdict Unverified
- WHAT: Tracking-drift FAIL verdict: plan 0/137 checked, stale update hash, ISSUES false opens, AGENTS abandoned; lists missing Phase-4 deliverables.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/validation/V-OB-1.md
- card: files/solo-levelling/the harness/validation/V-OB-1.md | part parts/13-deve-solo.md:33853 | lines 92 | verdict Unverified
- WHAT: Observability check confirming V1 guard blocks, all 10 frictions, and the force-push ordering fix with residual refspec bypass matrix.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/validation/V-OB-2.md
- card: files/solo-levelling/the harness/validation/V-OB-2.md | part parts/13-deve-solo.md:33946 | lines 94 | verdict Unverified
- WHAT: Hook-subsystem grades: pre_tool_guard B+ with bypass inventory, hooks.json A- with quoting hazards, post_tool_linter A, exit codes compliant.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/validation/V-OB-3.md
- card: files/solo-levelling/the harness/validation/V-OB-3.md | part parts/13-deve-solo.md:34041 | lines 154 | verdict Unverified
- WHAT: REJECT verdicts on Cedar (illegal syntax, Class3 deadlock), presets (prefix injection), gate.sh (ro-bind, tmpfs shadowing, missing hardening) with line cites.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/validation/V-OB-4.md
- card: files/solo-levelling/the harness/validation/V-OB-4.md | part parts/13-deve-solo.md:34196 | lines 159 | verdict Unverified
- WHAT: Subagent/workflow/config audit: agents PASS, two workflow YAMLs FAIL on nested quotes, config duplicate drift risk; block-scalar fix prescribed.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/validation/V-OB-5.md
- card: files/solo-levelling/the harness/validation/V-OB-5.md | part parts/13-deve-solo.md:34356 | lines 92 | verdict Unverified
- WHAT: Materialization census: 8/12 subsystems materialized, skills index partial (5 concrete plus 35 stubs), root bridges missing; runnable as substrate, not daemon.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/validation/V-OB-6.md
- card: files/solo-levelling/the harness/validation/V-OB-6.md | part parts/13-deve-solo.md:34449 | lines 122 | verdict Unverified
- WHAT: Skill audit: index.json valid-but-partial (40 IDs, 5 dirs), all 5 SKILL frontmatters valid, survey_repo.py functional stdlib-only; 35 stubs to generate.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/validation/V-SYN-1.md
- card: files/solo-levelling/the harness/validation/V-SYN-1.md | part parts/13-deve-solo.md:34572 | lines 269 | verdict Unverified
- WHAT: Consolidated 135-finding synthesis mirror of the validation audit with full #1-135 table and phase roadmap.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/validation/V-SYN-2.md
- card: files/solo-levelling/the harness/validation/V-SYN-2.md | part parts/13-deve-solo.md:34842 | lines 123 | verdict Unverified
- WHAT: 17-gap prioritized matrix (3 Critical, 5 High, 5 Med, 4 Low) with 4-sprint fix plan: security, governance, materialization, dogfooding.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/validation/V-TO-1.md
- card: files/solo-levelling/the harness/validation/V-TO-1.md | part parts/13-deve-solo.md:34966 | lines 196 | verdict Unverified
- WHAT: Tool audit of 17 execution tools: 16 PASS plus worktrunk link correction; flags ghost SDK 404 header-vs-body conflict and metric drift.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/validation/V-TO-2.md
- card: files/solo-levelling/the harness/validation/V-TO-2.md | part parts/13-deve-solo.md:35163 | lines 165 | verdict Unverified
- WHAT: Tool audit of 16 context tools all PASS with renames verified; flags missing pgvector profile and LLMLingua maintenance caveat.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/validation/V-TO-3.md
- card: files/solo-levelling/the harness/validation/V-TO-3.md | part parts/13-deve-solo.md:35329 | lines 156 | verdict Unverified
- WHAT: Skill-catalog audit: 40 skills real across 8 domains, 5 materialized validated, progressive-disclosure index confirmed zero-bloat.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/validation/V-TO-4.md
- card: files/solo-levelling/the harness/validation/V-TO-4.md | part parts/13-deve-solo.md:35486 | lines 118 | verdict Unverified
- WHAT: Safety-tool audit distinguishing mechanical sandbox from semantic guard correctly; Rebuff demoted to Optional as stagnant, fencing preferred.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/validation/V-TO-5.md
- card: files/solo-levelling/the harness/validation/V-TO-5.md | part parts/13-deve-solo.md:35605 | lines 152 | verdict Unverified
- WHAT: DX-tool audit: 12/12 HTTP200 valid across Inspect, SWE-bench, Promptfoo, Langfuse, LiteLLM, Gitleaks, OTel, Phoenix, Sigstore stacks.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/validation/V-TO-6.md
- card: files/solo-levelling/the harness/validation/V-TO-6.md | part parts/13-deve-solo.md:35758 | lines 162 | verdict Unverified
- WHAT: A/B-tier tool audit demoting RouteLLM, Lakera, and KuzuDB to Avoid with LiteLLM/XML-fencing/Graphiti replacements and version evidence.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/validation/V-TO-7.md
- card: files/solo-levelling/the harness/validation/V-TO-7.md | part parts/13-deve-solo.md:35921 | lines 93 | verdict Unverified
- WHAT: URL-validity sweep 49/50 live: confirms Lakera 404 and RouteLLM staleness, fixes Playwright slug erratum, locks 55-tool deduped catalog.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/validation/V-TO-8.md
- card: files/solo-levelling/the harness/validation/V-TO-8.md | part parts/13-deve-solo.md:36015 | lines 114 | verdict Unverified
- WHAT: P3-30 gate PASS: 37 CAPs honor tiers plus veto, dedup sound, 100% on-disk concordance for agents/MCP/Cedar/hooks/telemetry/workflows/skills.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/validation/V-TX-1.md
- card: files/solo-levelling/the harness/validation/V-TX-1.md | part parts/13-deve-solo.md:36130 | lines 132 | verdict Unverified
- WHAT: Taxonomy audit of archetypes and success criteria: C1/C3/C4 splits needed, embedded/firmware dropped, SC-02/SC-06/SC-08 refactored.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/validation/V-TX-2.md
- card: files/solo-levelling/the harness/validation/V-TX-2.md | part parts/13-deve-solo.md:36263 | lines 125 | verdict Unverified
- WHAT: Taxonomy certification for CAP-01..08: level hygiene PASS, hub-spoke/mesh and dynamic/static distinctions confirmed, no fabrications.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/validation/V-TX-3.md
- card: files/solo-levelling/the harness/validation/V-TX-3.md | part parts/13-deve-solo.md:36389 | lines 109 | verdict Unverified
- WHAT: Taxonomy audit of CAP-09..16: separation sound, CAP-12 scoped to idempotent caching, KL math corrected to Lagrangian penalty form.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/validation/V-TX-4.md
- card: files/solo-levelling/the harness/validation/V-TX-4.md | part parts/13-deve-solo.md:36499 | lines 87 | verdict Unverified
- WHAT: Integration/safety certification for CAP-17..25: MCP/skills/rules/hooks/gateway/sandbox/AuthZ all VALID with strict level hygiene.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/validation/V-TX-5.md
- card: files/solo-levelling/the harness/validation/V-TX-5.md | part parts/13-deve-solo.md:36587 | lines 74 | verdict Unverified
- WHAT: Ontology certification for CAP-25..37 plus MEC-01..10 and PROT-01..03: 100% WHAT/HOW/CONTRACT hygiene, zero fabrications.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/validation/V-TX-6.md
- card: files/solo-levelling/the harness/validation/V-TX-6.md | part parts/13-deve-solo.md:36662 | lines 109 | verdict Unverified
- WHAT: Master-table audit: CONDITIONAL PASS with B4-17 replayability restore required and 48-to-54 cardinality fix plus CAP-20 layer alignment.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/validation/V-TX-7.md
- card: files/solo-levelling/the harness/validation/V-TX-7.md | part parts/13-deve-solo.md:36772 | lines 122 | verdict Unverified
- WHAT: Ranking-traceability audit: 92% traceable, Harm-4 exemptions documented, CAP-16 to S and CAP-12 to C fixes yielding 22S/11A/3B/1C.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/validation/V-TX-8.md
- card: files/solo-levelling/the harness/validation/V-TX-8.md | part parts/13-deve-solo.md:36895 | lines 104 | verdict Unverified
- WHAT: Merge/kill audit locking 5 merges, 4 kills, and 4 cross-ecosystem translations with zero bad merges and fencing equivalences.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/solo-levelling/the harness/validation/VALIDATION_AUDIT.md
- card: files/solo-levelling/the harness/validation/VALIDATION_AUDIT.md | part parts/13-deve-solo.md:37000 | lines 270 | verdict Unverified
- WHAT: Canonical 135-row audit (93/24/18, 68.9% strict, 86.7% resolvable) with 18 HIGH matrix and phase-aligned remediation roadmap.
- HOW: Read the local file in full before citing its claims
- live: no live URLs
- conflicts: none

### files/deve/Taskfile.yml
- card: files/deve/Taskfile.yml | part parts/13-deve-solo.md:39691 | lines 80 | verdict Verified
- WHAT: Task runner (Taskfile v3) defining the harness commands: verify (lint+test+secret-scan), test (pytest scripts -x -q), lint (flake8 or ruff fallback), secret-scan, sandbox, skills-list (enumerates the 9 workflows + FCAR), fcar (fresh-context reminder), and new-project (scaffolds projects/<name>/ from templates).
- HOW: Install go-task, then run targets: `task verify`, `task test`, `task lint`, `task secret-scan`, `task sandbox -- <cmd>`, `task fcar -- <artifact>`, `task new-project -- <name>`.
- live: no live URLs
- conflicts: new-project copies only pitch-template.md and build-log-template.md, not prfaq/design-note; yet CLAUDE.md/.cursorrules say to initialize with pitch, prfaq and design-note - the scaffold is incomplete versus the documented protocol., Requires the external go-task binary; scripts/verify.sh duplicates the same checks for environments without it.

### files/deve/os/release-experiments.md
- card: files/deve/os/release-experiments.md | part parts/13-deve-solo.md:40256 | lines 30 | verdict Verified
- WHAT: Release and experimentation practice: the 6-step default deploy procedure with a pre-committed rollback threshold and a 10-minute monitor window; the A/B protocol (hypothesis/metric/sample-size before results; run to completion; ship only on success); and headless-pipeline adaptations mapping PR/FAQ, UX flows, auth test, load test, monitoring and A/B onto non-user-facing workloads.
- HOW: Pre-commit the rollback threshold in the launch checklist before deploying.
- live: no live URLs
- conflicts: The A/B protocol mandates predefining MDE and sample size, but no repo tooling or template captures those fields.

### files/deve/os/roles.md
- card: files/deve/os/roles.md | part parts/13-deve-solo.md:40287 | lines 48 | verdict Verified
- WHAT: Human/AI delegation model: human-only decisions (appetite, circuit-breaker, corrective actions, reversibility, high-stakes implementation, waivers), AI-assisted (drafts + human approval), AI-first-human-approved (style review, postmortem draft), automated (lint, CI tests, deploy metric gate, scope gate, pre-tool guard), and the 9 named workflows with AI/human roles.
- HOW: Decide for each task whether it is human-only, AI-assisted, AI-first, or automated.
- live: no live URLs
- conflicts: roles.md names 'Deployment metric gate' and 'Scope gate check' as automated (matching workflows), but the human/AI split for FCAR is not explicitly placed in any of the four delegation buckets.

### files/deve/scripts/spend-log.sh
- card: files/deve/scripts/spend-log.sh | part parts/13-deve-solo.md:40487 | lines 29 | verdict Verified
- WHAT: Token-spend logger: appends date,model,tokens,cost to .harness/telemetry/spend.csv (creating a header if missing) and, after each append, sums today's cost with awk and warns on stderr when it reaches the 80% ($8.00 of $10) daily budget threshold.
- HOW: Run `bash scripts/spend-log.sh <model> <tokens> [cost]` after an AI call.
- live: no live URLs
- conflicts: It only warns at 80% and never hard-stops; litellm-config declares a hard stop at 100% that this script cannot enforce without the proxy., It hardcodes the $10 / 80% threshold, duplicating the router's global_limits values; the two can drift.

### files/deve/scripts/test_pre_tool_guard.py
- card: files/deve/scripts/test_pre_tool_guard.py | part parts/13-deve-solo.md:40517 | lines 171 | verdict Verified
- WHAT: pytest suite (24 cases) for pre_tool_guard.py: verifies block reasons and via-main exit codes for curl|bash, wget|bash, rm -rf /etc, force-push variants, ASIA, sk-/ghp_, AKIA, chmod +x, curl|python, curl -fsSL, rm quoted-force and unquoted-secret patterns; verifies allow cases (ls -la, echo) and write_file allow; and verifies bad-JSON fail-open returns 0. Secret-like fixtures are assembled from fr
- HOW: Run `python3 -m pytest scripts/test_pre_tool_guard.py -q` (or via task test).
- live: no live URLs
- conflicts: Test count discrepancy: the module docstring says '12+ cases' and the header lists ~11 categories, but the node-id cache reports 24 cases for this file; the docstring undercounts the suite.

### files/deve/scripts/test_scope_check.py
- card: files/deve/scripts/test_scope_check.py | part parts/13-deve-solo.md:40689 | lines 193 | verdict Verified
- WHAT: pytest suite (24 cases) for scope-check.py: overlap detection, stopword-only overlap passing, the documented synonym false-negative, missing-section behavior (default fails / tiny passes), numbered/star bullets, Non-Goals heading variants, case-insensitivity, punctuation stripping, heading-boundary extraction and main() integration (conflict exit 1, pass exit 0, missing pitch exit 1).
- HOW: Run `python3 -m pytest scripts/test_scope_check.py -q` (or via task test).
- live: no live URLs
- conflicts: The suite explicitly asserts the synonym false-negative as intended behavior, documenting that the automated scope gate cannot catch semantic scope creep.

### files/builders-playbook/product_engineering/report/01-executive-findings.md
- card: files/builders-playbook/product_engineering/report/01-executive-findings.md | part parts/14-bp-report.md:69 | lines 94 | verdict Verified
- WHAT: The 30 most important executive findings across 20 product engineering research streams, synthesized into six thematic clusters: AI productivity ledger (F1-F6), failure modes and countermeasures (F7-F13), three AI domains distinction (F14-F16), deployment and incident discipline (F17-F21), lifecycle defect origin and economics (F22-F27), and missing topics gap analysis (F28-F30).
- HOW: Consult the 30 executive findings before architecting AI-enabled engineering workflows or adopting agent tooling.
- live: no live URLs
- conflicts: Developer perception of +20-24% speedup vs measured METR RCT showing 19% slowdown on familiar complex codebases., Token price collapse (~300x) vs enterprise LLM spend tripling due to iterative response refinement.

### files/builders-playbook/product_engineering/report/03-product-lifecycle.md
- card: files/builders-playbook/product_engineering/report/03-product-lifecycle.md | part parts/14-bp-report.md:300 | lines 206 | verdict Verified
- WHAT: Comprehensive 12-stage iterative product engineering lifecycle (Problem discovery, Ideation/prioritisation, Validation, Spec, Architecture, Foundations, Build, Test, Deploy, Operate, Improve, Adopt) featuring condensed stage checklists and a 9-gate quality system.
- HOW: Operate product development as a closed feedback loop where production signals continually inform backlog and specs.
- live: no live URLs
- conflicts: High line coverage (100%) vs low mutation score (63%), demonstrating that running code does not prove fault detection., Stated developer velocity speedup vs increased downstream pull request review latency.

### files/builders-playbook/product_engineering/report/04-company-case-studies.md
- card: files/builders-playbook/product_engineering/report/04-company-case-studies.md | part parts/14-bp-report.md:507 | lines 121 | verdict Verified
- WHAT: Forensic case study synthesis across 16 major tech organizations (Google, Microsoft, Meta, Amazon, NVIDIA, OpenAI, Anthropic, GitHub, Stripe, Shopify, Uber, Netflix, Spotify, Airbnb, Cursor, Replit), documenting contradictions between public narratives and forensic evidence alongside 26 deduplicated transferable lessons.
- HOW: Treat control-plane modifications as production deployments subject to feature flags, canary rollouts, and out-of-band recovery.
- live: no live URLs
- conflicts: Spotify squad model marketed as universal agile blueprint vs original Kniberg/Ivarsson disclaimer stating it was an ephemeral snapshot not to be copied., Cursor marketed as model-first innovation vs CEO admission that OpenAI models serve only ~5% of traffic, proving value resides in workflow and harness., Public engineering excellence narratives vs forensic evidence of unflagged null-pointer changes and hardcoded admin credentials.

### files/builders-playbook/product_engineering/report/08-functional-completeness.md
- card: files/builders-playbook/product_engineering/report/08-functional-completeness.md | part parts/14-bp-report.md:1008 | lines 113 | verdict Verified
- WHAT: Methodology for systematic functional completeness auditing and demo honesty verification, establishing the closed-inventory principle, a 16-class element inventory, a 4-tier severity framework (S1-S4), automated crawler boundaries, and an 8-point demo authenticity scorecard.
- HOW: Enumerate a closed inventory across all 16 element classes (routes, navigation, forms, modals, uploads, auth, payments, etc.) before running QA checks.
- live: no live URLs
- conflicts: High automated scanner issue coverage (~57% by volume) vs low coverage of WCAG success criteria (~30-40%), showing automation misses semantic accessibility., Agent self-reported green test runs vs vacuous assertions created to satisfy exit code 0.

### files/builders-playbook/product_engineering/report/11-testing-quality-deployment-ops.md
- card: files/builders-playbook/product_engineering/report/11-testing-quality-deployment-ops.md | part parts/14-bp-report.md:1373 | lines 140 | verdict Verified
- WHAT: Testing, quality gates, deployment, and production operations framework: test-type catalog (unit, integration, contract, E2E, visual, accessibility, load, security, exploratory), Google size-based framing (small, medium, large), mutation testing as adequacy check (killing mutants vs vacuous line coverage), flaky test triage and root causes (async wait 45%, concurrency 20%, test-order 12%), contrac
- HOW: Run mutation testing on changed code in PRs and full analysis nightly, targeting ~80% coverage with headroom rather than vanity 100%.
- live: no live URLs
- conflicts: 70/20/10 test pyramid ratio vs modern microservice systems where contract and component tests form a thick middle, Agent self-certification of green tests vs mutation analysis revealing assertion-free tests

### files/builders-playbook/product_engineering/report/12-business-viability.md
- card: files/builders-playbook/product_engineering/report/12-business-viability.md | part parts/14-bp-report.md:1514 | lines 131 | verdict Verified
- WHAT: Business viability, adoption, and AI product unit economics framework: AARRR pirate metrics lifecycle diagnostics, onboarding/activation benchmarks, pricing and monetization models (freemium drag, tiered subscription, usage-based recovery of inference costs), standard unit economics (LTV:CAC >= 3:1, CAC payback < 12 months, fully loaded cost-to-serve), the AI token paradox (falling token prices vs
- HOW: Diagnose customer conversion drop-offs across AARRR stages and invest growth resources in the lowest-converting bottleneck stage first.
- live: no live URLs
- conflicts: Headline vendor automation claims (67-90%) vs independent aggregate median tier-1 automation rate (41%), Resolution vs deflection: counting unassisted customer drop-offs inflates perceived support automation by 20-40 points

### files/builders-playbook/product_engineering/report/13-bottleneck-analysis.md
- card: files/builders-playbook/product_engineering/report/13-bottleneck-analysis.md | part parts/14-bp-report.md:1646 | lines 146 | verdict Verified
- WHAT: Delivery economics and bottleneck shift analysis: empirical evaluation across 12 delivery dimensions demonstrating that AI accelerates active coding (historically only ~15% of lead time) while shifting the binding constraint downstream to specification, review, testing, CI pipelines, security gates, and maintenance. Comprehensive critique of 7 major productivity studies (METR RCT showing experienc
- HOW: Use value-stream mapping to measure active work time versus wait time across all stages before investing in coding acceleration.
- live: no live URLs
- conflicts: Developer perception of +20% speedup vs measured METR RCT showing 19% slowdown on familiar complex codebases, Increased PR throughput (+24% to +98%) vs increased review wait time (4.6x longer) and rising change failure rates (+23.5% to +30%)

### files/builders-playbook/product_engineering/report/19-missing-topics.md
- card: files/builders-playbook/product_engineering/report/19-missing-topics.md | part parts/14-bp-report.md:2783 | lines 185 | verdict Partially
- WHAT: Evidence-grounded gap analysis of 11 critical engineering topics omitted from conventional product-engineering frameworks, ranked by Failure weight, Lifecycle breadth, Actionability, and Evidence strength: T1 Platform engineering & DevEx (Spotify Backstage, golden paths vs portals), T2 AI-era review economy & seniority composition (Keypup review tax, Stanford junior employment decline), T3 Org des
- HOW: Treat developer workflow as a product: build golden-path templates and service catalogs rather than ticket-based portals to reduce cognitive load.
- live: no live URLs
- conflicts: Short-term cost reduction from junior hiring freezes vs long-term senior talent pipeline depletion, Internal AI adoption mandates vs Goodhart gaming where engineers burn tokens to protect ratings

### files/builders-playbook/product_engineering/research/discovery/01-problem-discovery.md
- card: files/builders-playbook/product_engineering/research/discovery/01-problem-discovery.md | part parts/15-bp-core-research.md:1 | lines 240 | verdict Verified
- WHAT: Problem Discovery and Opportunity Identification framework: eight evidence channels (story-based customer interviews, workflow observation, support ticket clustering, behavioral analytics, competitor teardowns, market/regulatory shifts, dogfooding, emerging tech); five core distinctions separating real problems from mirages (problem vs interesting idea, root cause vs symptom, user demand vs assump
- HOW: Conduct story-based interviews focusing exclusively on past behavior rather than hypothetical opinions (The Mom Test discipline).
- live: no live URLs
- conflicts: Founder conviction and compliments vs empirical commitment signals, Synthetic user modeling vs real human customer research

### files/builders-playbook/product_engineering/research/discovery/02-ideation-prioritisation.md
- card: files/builders-playbook/product_engineering/research/discovery/02-ideation-prioritisation.md | part parts/15-bp-core-research.md:242 | lines 207 | verdict Verified
- WHAT: Idea Generation and Prioritization discipline: eight grounded generation methods (customer workarounds, Jobs-to-be-Done with Ulwick's Outcome-Driven Innovation opportunity algorithm, Opportunity Solution Trees, design thinking, behavioral analytics, competitor teardowns, technical spikes, AI-assisted divergent brainstorming); nine evaluation dimensions (user value, reach, differentiation, feasibil
- HOW: Anchor all candidate solutions to a validated opportunity on an Opportunity Solution Tree (OST) traced directly to a desired business outcome.
- live: no live URLs
- conflicts: Algorithmic mathematical prioritization (RICE formulaic rankings) vs subjective qualitative two-way door decision making (Torres Opportunity Solution Trees), Customer feature requests vs underlying Job-To-Be-Done desired outcomes

### files/builders-playbook/product_engineering/research/discovery/03-validation.md
- card: files/builders-playbook/product_engineering/research/discovery/03-validation.md | part parts/15-bp-core-research.md:450 | lines 164 | verdict Verified
- WHAT: Solution Validation methodology: definition and taxonomy of validation methods (solution-stage interviews, landing page smoke tests, fake doors, concierge MVPs, Wizard of Oz tests, throwaway prototypes, paid pilots, technical spikes, pricing tests, usability research); commitment hierarchy (money > costly non-monetary commitment > behavior > stated intent > compliments); Sean Ellis PMF benchmark (
- HOW: Select the cheapest validation experiment that directly targets the current riskiest assumption (value, usability, feasibility, or viability).
- live: no live URLs
- conflicts: MVP as small test of demand vs MVP as smaller version of final production build, Survey-stated willingness to pay vs behavioral currency exchange

### files/builders-playbook/product_engineering/research/domain-a/01-research-planning.md
- card: files/builders-playbook/product_engineering/research/domain-a/01-research-planning.md | part parts/15-bp-core-research.md:705 | lines 73 | verdict Verified
- WHAT: AI-Assisted Product Research and Planning practices (Domain A, Area 1): engineering workflows for competitive and landscape research using agent skill cards (tool caps, citation enforcement, anti-hallucination rules); automated roadmap generation pipelines (analytics/tickets/RSS -> structured prompt -> DataFrame -> Slack); 5-rung evidence ladder governance (synthetic LLM ideation assigned to Rung 
- HOW: Equip research agents with versioned skill cards that enforce hard tool caps (e.g., 8 rounds) and mandatory citation constraints ('never invent URLs').
- live: no live URLs
- conflicts: Unconstrained AI brainstorming vs strict evidence-ladder governance requiring zero engineering capital on Rung 1

### files/builders-playbook/product_engineering/research/domain-a/02-requirements-specifications.md
- card: files/builders-playbook/product_engineering/research/domain-a/02-requirements-specifications.md | part parts/15-bp-core-research.md:779 | lines 77 | verdict Verified
- WHAT: AI-Assisted Requirements and Technical Specifications discipline (Domain A, Area 2): structured PRD workflows across four entry points (Shape from idea, Audit for coherence, Change for tracing updates, Recover from existing codebase); formal evidence states (VERIFIED, DECLARED, INFERRED, OPEN, PLANNED); 13-stage PRD generation pipelines; agent-enforced PRD discipline (mandatory clarifying question
- HOW: Execute brownfield spec recovery by auditing code, tests, and configurations into explicit evidence states (VERIFIED by test vs INFERRED by logic) before writing change requirements.
- live: no live URLs
- conflicts: Specification of functional requirements (WHAT/WHY) vs AI coding agents eagerly inserting implementation details (HOW)

### files/builders-playbook/product_engineering/research/domain-a/03-ux-research-design.md
- card: files/builders-playbook/product_engineering/research/domain-a/03-ux-research-design.md | part parts/15-bp-core-research.md:857 | lines 72 | verdict Verified
- WHAT: AI-Assisted UX Research and Interface Design (Domain A, Area 3): in-tool design assistance capabilities (Figma AI/Make general availability July 2025, First Draft agentic entry points, in-file layer renaming, asset search, content rewriting); prompt-to-screen exploration workflows (Paper/Uizard/Google Stitch for blank-canvas exploration, followed by production reconstruction in Figma); automated U
- HOW: Use generative prompt-to-UI tools during the blank-canvas phase to explore multiple layout variations rapidly (<45 minutes).
- live: no live URLs
- conflicts: High visual polish in AI screen generation vs underlying absence of coherent interaction logic and edge-case handling

### files/builders-playbook/product_engineering/research/domain-a/04-prototyping-frontend.md
- card: files/builders-playbook/product_engineering/research/domain-a/04-prototyping-frontend.md | part parts/15-bp-core-research.md:930 | lines 70 | verdict Verified
- WHAT: AI-Assisted Prototyping and Frontend Generation benchmark and practices (Domain A, Area 4): comparative analysis of frontend builders (v0 component generator with shadcn/ui conventions, Bolt.new WebContainer in-browser dev environment, Lovable full-stack Supabase integrator); measured 40-45% security vulnerability rate in generated code (missing input sanitization, exposed API keys, absent row-lev
- HOW: Select prototyping tools based on architectural boundaries: v0 for clean, reusable UI components; Bolt for full in-browser dev server environments; Lovable for quick Supabase database scaffolding.
- live: no live URLs
- conflicts: High visual quality and functional appearance of vibe-coded apps vs 40-45% measured security vulnerability rate

### files/builders-playbook/product_engineering/research/domain-a/06-testing-debugging-review.md
- card: files/builders-playbook/product_engineering/research/domain-a/06-testing-debugging-review.md | part parts/15-bp-core-research.md:1096 | lines 79 | verdict Verified
- WHAT: AI Testing, Debugging, and Code Review analysis (Domain A, Area 6): production code review benchmarks (16,017 PR evaluation showing precision vs recall tradeoffs across Greptile, CodeRabbit, Copilot); vendor benchmark divergence and methodology sensitivity; the 'AI review tax' (AI PRs are 2-3x larger, shifting bottlenecks from writing to senior engineer review, with 38.5% of AI code merging unrevi
- HOW: Configure automated code review tools based on precision/recall posture: choose high-precision tools (Greptile) to reduce reviewer fatigue or broader coverage tools (CodeRabbit) with noise suppression enabled.
- live: no live URLs
- conflicts: Claims of accelerated delivery via AI generation vs bottleneck shift to senior engineer code review ('AI review tax'), Agent claims of 100% test pass rates vs agents weakening assertions or mocking databases to game exit code 0

### files/builders-playbook/product_engineering/research/domain-a/07-security-quality-assurance.md
- card: files/builders-playbook/product_engineering/research/domain-a/07-security-quality-assurance.md | part parts/15-bp-core-research.md:1176 | lines 70 | verdict Verified
- WHAT: Security and Quality Assurance of AI-Generated Code (Domain A, Area 7): multi-study convergence on the measured insecurity of AI-generated code (Veracode 2025/2026 showing 45% insecure code generation across 150+ models with Java worst at 71.5%; Cobalt AI formal Z3 verification showing 55.8% vulnerability rate with commercial scanners missing 97.8% of findings; Symbiotic Security finding 4.4x more
- HOW: Treat all AI-generated code as untrusted-by-default; newer model releases and larger sizes do not inherently solve code insecurity.
- live: no live URLs
- conflicts: Vendor claims of model safety vs empirical security studies showing stable 45-56% vulnerability generation across 2 years of model releases, Model generation capabilities (55.8% vulnerable) vs model review capabilities (78.7% catch rate)

### files/builders-playbook/product_engineering/research/domain-a/09-monitoring-incident-response.md
- card: files/builders-playbook/product_engineering/research/domain-a/09-monitoring-incident-response.md | part parts/15-bp-core-research.md:1317 | lines 76 | verdict Verified
- WHAT: AI-Assisted Monitoring and Incident Response (Domain A, Area 9): three-layer taxonomy of AI operational tooling (Alert correlation via classical AIOps for high-volume event dedup; Postmortem generation from existing artifacts; Agentic investigation using interactive tool calls to gather real-time evidence like HolmesGPT/K8sGPT); architectural failure modes of stateless LLMs in incidents (suggestin
- HOW: Deploy classical AIOps/ML upstream to handle carrier-scale event correlation, alert deduplication, and noise reduction before paging engineers or agents.
- live: no live URLs
- conflicts: Vendor marketing claiming fully autonomous AI SRE incident remediation vs practitioner requirement for least-privilege read-only agents and mandatory human sign-off

### files/builders-playbook/product_engineering/research/domain-a/10-documentation-maintenance.md
- card: files/builders-playbook/product_engineering/research/domain-a/10-documentation-maintenance.md | part parts/15-bp-core-research.md:1394 | lines 67 | verdict Verified
- WHAT: AI-Assisted Documentation and Ongoing Maintenance practices (Domain A, Area 10): documentation as source code for AI agents (Microsoft ISE first-party practice: dating docs, linking ADRs, keeping info in-repo, treating doc drift as a CI bug); DoGBench empirical benchmark on agent-authored documentation (1,267 submissions revealing 45.5% task-completion gaps, 36.6% technical inaccuracies, and 6.1% 
- HOW: Treat repository documentation as source code for agents: maintain dates on long-lived docs, link to in-repo ADRs, and explicitly encode negative operational rules.
- live: no live URLs
- conflicts: Vendor claims that AI automatically keeps documentation updated vs DoGBench benchmark showing 45.5% completion gaps and 6.1% fabricated APIs

### files/builders-playbook/product_engineering/research/domain-b/01-llm-features.md
- card: files/builders-playbook/product_engineering/research/domain-b/01-llm-features.md | part parts/15-bp-core-research.md:1638 | lines 79 | verdict Verified
- WHAT: Customer-Facing LLM Product Features (Domain B, Area 1): core architecture pattern of 'brain vs body' separation (probabilistic LLM reasoning separated from deterministic execution workers, exemplified by Notion AI database agents); real product cases (Duolingo Max with Explain My Answer and Roleplay; Notion AI's discovery that simpler prompts beat complex schemas; Intercom Fin Apex purpose-traine
- HOW: Enforce the brain vs body architectural split: let the LLM interpret user intent and propose actions, but execute all mutations and database updates through deterministic code.
- live: no live URLs
- conflicts: Vendor claims of general-purpose frontier model superiority vs measured real-world success of purpose-trained small models on narrow tasks, Syntactic JSON schema conformance vs semantic correctness of generated values

### files/builders-playbook/product_engineering/research/domain-b/02-rag.md
- card: files/builders-playbook/product_engineering/research/domain-b/02-rag.md | part parts/15-bp-core-research.md:1718 | lines 75 | verdict Verified
- WHAT: Retrieval-Augmented Generation (RAG) in Production Products (Domain B, Area 2): end-to-end RAG architecture; analysis of production failure modes (the demo-to-production gap, small-data ANN approximation errors, silent quality decay from 90% to 60% without error logs, document lifecycle drift, ingestion pipeline failures); the Glean enterprise platform case (hybrid search, knowledge graphs, real-t
- HOW: Structure chunking around document semantics (headings, tables) and combine keyword (BM25) with vector search to catch exact identifiers and technical codes.
- live: no live URLs
- conflicts: Fine-tuning models for enterprise knowledge vs query-time retrieval-augmented generation (RAG), High demo accuracy on static test sets vs production quality collapse under dynamic document updates

### files/builders-playbook/product_engineering/research/domain-b/03-ai-assistants.md
- card: files/builders-playbook/product_engineering/research/domain-b/03-ai-assistants.md | part parts/15-bp-core-research.md:1794 | lines 92 | verdict Verified
- WHAT: Customer-Facing AI Assistants as Products (Domain B, Area 3): action-taking assistant architectures; the definitive Klarna two-act case study (Act 1: Feb 2024 launch handling 2.3M chats with 700-agent workload equivalence; Act 2: May 2025 reversal where CEO acknowledged excessive cost-cutting degraded quality, leading to rehiring human agents for complex escalations, disputed transactions, and bra
- HOW: Automate routine high-volume queries with AI while deliberately maintaining well-staffed human escalation paths for complex, emotional, or high-stakes interactions.
- live: no live URLs
- conflicts: Short-term cost reduction metrics (resolution speed, headcount equivalence) vs long-term customer trust, escalation satisfaction, and brand equity, Corporate legal defense of chatbots as independent entities vs judicial rulings establishing company liability for AI statements

### files/builders-playbook/product_engineering/research/domain-b/04-recommendations.md
- card: files/builders-playbook/product_engineering/research/domain-b/04-recommendations.md | part parts/15-bp-core-research.md:1887 | lines 77 | verdict Verified
- WHAT: Recommendation and Ranking Systems in Production Products (Domain B, Area 4): classical three-stage recommender funnel (candidate retrieval ~10ms via two-tower embeddings and ANN search -> heavy multi-objective neural ranking ~30ms -> business-rule reranking and diversity enforcement ~10ms within a 50-100ms total budget); deep case study of Netflix (multi-retriever fan-out, multi-objective complet
- HOW: Structure recommender pipelines as multi-stage funnels to balance candidate pool size against strict sub-100ms serving latency budgets.
- live: no live URLs
- conflicts: Optimizing purely for click probability (clickbait) vs optimizing for balanced long-term completion and satisfaction, Open-ended conversational recommendation vs catalog-constrained ranking

### files/builders-playbook/product_engineering/research/domain-b/05-ai-search-extraction.md
- card: files/builders-playbook/product_engineering/research/domain-b/05-ai-search-extraction.md | part parts/15-bp-core-research.md:1965 | lines 75 | verdict Verified
- WHAT: AI Search and Information Extraction Products (Domain B, Area 5): architecture of AI search engines (retrieval infrastructure as the primary determinant of quality and cost, Perplexity Photon case rebuilding indexing in Rust for 160ms p50 / 230ms p95 latency and 68% cost reduction, Algolia architectural constraints-first pattern); negative evidence in AI search (Google AI Overviews surfacing satir
- HOW: Treat retrieval infrastructure as the core product engine in AI search, prioritizing low-latency index formats and bounded candidate traversal over model scaling.
- live: no live URLs
- conflicts: Retrieval infrastructure as the primary driver of search quality and latency vs model parameter scaling, General vision LLMs for extraction vs specialized two-stage OCR pipelines

### files/builders-playbook/product_engineering/research/domain-b/06-multimodal.md
- card: files/builders-playbook/product_engineering/research/domain-b/06-multimodal.md | part parts/15-bp-core-research.md:2041 | lines 93 | verdict Verified
- WHAT: Multimodal Product Capabilities (Domain B, Area 6): vision and voice engineering patterns (cascaded STT -> LLM -> TTS vs native speech-to-speech models, temporal cross-modal synchronization, multimodal RAG sending original images to VLMs, specialized OCR vs general VLMs); cost and latency economics ($0.30-$0.80 per fully multimodal 5-minute call, sub-800ms latency budgets for conversational voice)
- HOW: Design multimodal systems with independent latency budgets, cost accounting, and graceful degradation paths for each modality (e.g., fall back to text if voice fails).
- live: no live URLs
- conflicts: Chained multimodal pipelines (STT -> LLM -> TTS: debuggable, cheaper) vs native speech-to-speech models (low latency, conversational prosody, higher cost), Stage demo impact in AI hardware vs real-world daily utility and battery/thermal constraints

### files/builders-playbook/product_engineering/research/domain-b/09-cost-latency-reliability.md
- card: files/builders-playbook/product_engineering/research/domain-b/09-cost-latency-reliability.md | part parts/15-bp-core-research.md:2317 | lines 98 | verdict Verified
- WHAT: Inference Economics, Latency Budgets, and Reliability Engineering (Domain B, Area 9): cost drivers of LLM applications (compounding turn history, agent loop multiplication, long-context RAG); the 9-technique cost optimization stack ordered by implementation complexity (prompt prefix caching 60-90% savings, batch APIs 50%, output length constraints 15-30%, model routing 40-70%, semantic caching 31-
- HOW: Instrument granular cost attribution per feature, tenant, and team before undertaking any optimization effort.
- live: no live URLs
- conflicts: Perceived speedup from streaming tokens vs actual compute duration and cost, Cost minimization via aggressive model downgrades vs task accuracy and regression rates

### files/builders-playbook/product_engineering/research/domain-b/10-security-ops.md
- card: files/builders-playbook/product_engineering/research/domain-b/10-security-ops.md | part parts/15-bp-core-research.md:2416 | lines 122 | verdict Verified
- WHAT: Security and Production Operations for AI Products (Domain B, Area 10): Part A Security: threat model of direct and indirect prompt injection ('lethal trifecta' of tool access, memory, and autonomous action); chronological incident catalog (Bing Sydney, Samsung confidential data leak, Chevy $1 Tahoe, DPD bot, ChatGPT memory exploit, Notion PDF exfiltration, CVE-2025-32711 EchoLeak zero-click exfil
- HOW: Treat all external retrieved content (web pages, PDFs, emails, tool descriptions) as untrusted user data, enforcing strict separation from developer instructions.
- live: no live URLs
- conflicts: Natural language prompt-level safety instructions vs empirical ease of injection bypass without deterministic architectural barriers, Logging comprehensive debugging traces vs customer privacy and PII protection requirements

### files/builders-playbook/product_engineering/research/domain-c/01-customer-support.md
- card: files/builders-playbook/product_engineering/research/domain-c/01-customer-support.md | part parts/15-bp-core-research.md:3236 | lines 103 | verdict Verified
- WHAT: Organisational AI Customer Support framework: 3-layer architecture (grounded knowledge layer, front-line resolver bot, agent-assist copilot); documented real-world case studies (Klarna's massive support automation and subsequent May 2025 human re-hiring reversal; Air Canada's Moffatt v. Air Canada tribunal loss establishing corporate liability for chatbot hallucinations; Cursor's Sam bot inventing
- HOW: Deploy support bots with a mandatory, visible human exit ('talk to a person') on low confidence or customer distress.
- live: no live URLs
- conflicts: Vendor headline resolution claims (67-90%) vs independent benchmark reality (41% median), Chatbot deflection metrics vs true end-to-end customer issue resolution, Cost-cutting staffing reductions vs preserving essential human escalation capacity

### files/builders-playbook/product_engineering/research/domain-c/02-research-knowledge-management.md
- card: files/builders-playbook/product_engineering/research/domain-c/02-research-knowledge-management.md | part parts/15-bp-core-research.md:3340 | lines 88 | verdict Verified
- WHAT: Organisational AI Research & Knowledge Management architecture: enterprise multi-stage RAG pipeline (connector ingestion, semantic chunking, dual lexical/dense hybrid retrieval, cross-encoder reranking, strict citation generation); documented cases (Bayer's life sciences enterprise search across 40 disparate systems, Morgan Stanley's wealth management CoPilot achieving 98% adoption, McKinsey's Lil
- HOW: Enforce strict user-identity permission trimming at query time so RAG never surfaces documents the requesting user cannot access.
- live: no live URLs
- conflicts: Broad internal knowledge access vs strict organizational access control and confidentiality boundaries, Semantic vector similarity matching vs exact keyword precision for internal technical jargon

### files/builders-playbook/product_engineering/research/domain-c/03-internal-operations.md
- card: files/builders-playbook/product_engineering/research/domain-c/03-internal-operations.md | part parts/15-bp-core-research.md:3429 | lines 88 | verdict Verified
- WHAT: Organisational AI for Internal Operations: 'internal front door' IT/HR service desk architecture (employee portal, ticket classification/routing, onboarding orchestration, ops staff copilot); rollout philosophy treating AI agents like new hires (gradual trust and verification); documented cases (City of Raleigh public-sector IT service desk with ServiceNow, Siemens enterprise onboarding, Dell IT t
- HOW: Treat internal operational bots as junior staff: start with read-only FAQ and summary roles before granting automated write or provisioning access.
- live: no live URLs
- conflicts: Anticipated operational labor savings vs added workload spent verifying and fixing AI-generated IT/HR errors, Automated self-service efficiency vs employee isolation during critical onboarding milestones

### files/builders-playbook/product_engineering/research/domain-c/04-sales-customer-success.md
- card: files/builders-playbook/product_engineering/research/domain-c/04-sales-customer-success.md | part parts/15-bp-core-research.md:3518 | lines 92 | verdict Verified
- WHAT: AI Automating Sales & Customer Success operations: Section A Sales Prospecting & Outreach (AI SDR tooling, automated enrichment, sequence drafting, signal-based outreach, Gong State of Revenue 2025 findings showing 29% sales growth and 11% GTM efficiency for AI adopters alongside plans for increased hiring, spam-filter reputation collapse, domain blacklisting); Section B Customer Success & Retenti
- HOW: Deploy AI outreach with strict volume caps, high domain separation, and custom messaging to protect primary domain deliverability.
- live: no live URLs
- conflicts: High-volume AI outreach efficiency vs email domain deliverability and prospect trust destruction, Algorithmic customer health scores vs real-world customer churn risk

### files/builders-playbook/product_engineering/research/domain-c/05-analytics-reporting.md
- card: files/builders-playbook/product_engineering/research/domain-c/05-analytics-reporting.md | part parts/15-bp-core-research.md:3611 | lines 86 | verdict Verified
- WHAT: Organisational AI Analytics & Reporting: analysis of two architectural postures—Posture A (chat on top of uncurated BI/SQL, highly unreliable) vs Posture B (NL querying backed by a governed semantic layer like Cube/dbt/LookML, reliable); definitions of NL-to-SQL, semantic models, Spider 2.0 enterprise text-to-SQL benchmarks, and InfoWorld's 'almost-right tax'; documented corporate cases (ThoughtSp
- HOW: Enforce Posture B: always place a strictly governed semantic layer (Cube, dbt, LookML) between LLMs and raw database tables.
- live: no live URLs
- conflicts: Unrestricted natural language query flexibility vs strict data governance and metric definition consistency, Syntactically valid SQL generation vs semantically correct business metric calculation

### files/builders-playbook/product_engineering/research/domain-c/06-administrative-processes.md
- card: files/builders-playbook/product_engineering/research/domain-c/06-administrative-processes.md | part parts/15-bp-core-research.md:3698 | lines 92 | verdict Verified
- WHAT: Organisational AI Administrative Processes: back-office automation across accounts payable, expense management, insurance claims, and compliance paperwork; standard AP/claims pipeline (capture, extraction, validation, PO matching, straight-through processing, exception routing); definitions of IDP (intelligent document processing), RPA, and 2-way/3-way PO matching; documented cases (Siemens AP aut
- HOW: Enforce strict 3-way matching (invoice to PO to receiving report) before releasing straight-through payments.
- live: no live URLs
- conflicts: Maximizing straight-through processing throughput vs preventing invoice fraud and accounting errors, High benchmark accuracy on synthetic/digital documents vs brittle real-world scan extraction

### files/builders-playbook/product_engineering/research/domain-c/07-engineering-coordination.md
- card: files/builders-playbook/product_engineering/research/domain-c/07-engineering-coordination.md | part parts/15-bp-core-research.md:3791 | lines 87 | verdict Verified
- WHAT: Organisational AI for Engineering Coordination: AI automating the operational overhead around engineering (incident triage, on-call coordination, standup summarization, cross-team routing, status communication); distinguishes alerting (detecting smoke) from triage (interpreting and preparing response); documented cases (incident.io AI incident summaries, Rootly automated postmortem generation, Pag
- HOW: Use AI as an incident recorder and summarizer (drafting timelines, gathering relevant logs and PR links) rather than an autonomous commander.
- live: no live URLs
- conflicts: Rapid incident status broadcasting vs accuracy of early root-cause assessments, Automated runbook suggestion speed vs risk of executing destructive remediation steps

### files/builders-playbook/product_engineering/research/domain-c/08-business-workflows.md
- card: files/builders-playbook/product_engineering/research/domain-c/08-business-workflows.md | part parts/15-bp-core-research.md:3879 | lines 85 | verdict Verified
- WHAT: Organisational AI Repetitive Business Workflows framework: agentic multi-step workflow automation (procurement approvals, employee lifecycle sequences, data reconciliation, scheduled reporting, cross-system synchronization); foundational concepts (agentic workflows, guardrails, iteration caps, blast radius); production safety controls (iteration caps of 5-15 steps, pre-action dry-run simulations, 
- HOW: Enforce strict iteration caps (e.g. max 10 steps) and execution timeouts to prevent infinite loops and runaway API costs.
- live: no live URLs
- conflicts: Autonomous agent multi-step flexibility vs compounding error decay across long tool chains, Fast unattended execution vs human oversight latency on irreversible business actions

### files/builders-playbook/product_engineering/research/spec-arch/01-requirements-specs.md
- card: files/builders-playbook/product_engineering/research/spec-arch/01-requirements-specs.md | part parts/15-bp-core-research.md:4120 | lines 198 | verdict Verified
- WHAT: Requirements, Product Specification & Scope Engineering framework (§6): operational definition of a spec as a buildable contract across PM, design, engineering, testing, and AI agent consumers; empirical findings establishing requirements failures as 40-60% of all software defects; complete 14-section anatomy of a production spec; discipline for writing durable requirements (quantified metrics, bo
- HOW: Structure every specification with all 14 mandatory sections, including explicit non-goals, invariants, and edge case behaviors.
- live: no live URLs
- conflicts: Agile 'working software over comprehensive documentation' dogma vs empirical reality of 40-60% defects originating from missing requirements, Natural language narrative specs vs structured machine-verifiable constraints required by AI coding agents

### files/builders-playbook/product_engineering/research/spec-arch/02-architecture-decisions.md
- card: files/builders-playbook/product_engineering/research/spec-arch/02-architecture-decisions.md | part parts/15-bp-core-research.md:4319 | lines 181 | verdict Verified
- WHAT: Architecture & Technical Planning decision framework (§9): ADR (Architecture Decision Record) discipline in docs/adrs/; two-way vs one-way door decision criteria; principle of deciding on pain rather than fashion; three comprehensive comparative trade-off matrices: Matrix 1 (Monolith vs Modular Monolith vs Microservices—evaluating team size, deploy cadence, failure domains, distributed tracing cos
- HOW: Document every significant technical decision in a written ADR capturing context, options considered, trade-offs, consequences, and reversibility.
- live: no live URLs
- conflicts: Premature microservices fashion vs operational complexity and distributed tracing overhead, Pure eventual consistency vs business requirements for transactional ACID guarantees

### files/builders-playbook/product_engineering/research/spec-arch/03-repo-foundations.md
- card: files/builders-playbook/product_engineering/research/spec-arch/03-repo-foundations.md | part parts/15-bp-core-research.md:4501 | lines 113 | verdict Verified
- WHAT: Repository Foundations & Development Conventions engineering guide (§10): thesis framing foundations as defect prevention with cost paid once ('if absence produced the same incident twice, it is overdue'); Section 1 Essential Day-1 Foundations (one repo per deployable, protected main branch, mandatory blocking CI status checks, automated deterministic lint/formatting, strict static typechecking, s
- HOW: Configure branch protection on main immediately: block direct pushes, require passing CI checks (build, test, lint, typecheck, secret scan), and prohibit force-pushes.
- live: no live URLs
- conflicts: Speed of unconstrained development vs upfront repository hygiene and blocking CI gates, Premature complex infrastructure investment vs essential day-1 defect prevention controls

### files/builders-playbook/product_engineering/research/ux-states/01-polish-details.md
- card: files/builders-playbook/product_engineering/research/ux-states/01-polish-details.md | part parts/15-bp-core-research.md:4705 | lines 245 | verdict Verified
- WHAT: UX Polish Details Framework (§18): comprehensive catalog of small details that make software products feel complete and trustworthy; guiding principle of proportionality (auditing context, task frequency, and user impact rather than bloat); structured across five core domains: Section A Interaction & State Completeness (the 4 distinct empty states, loading skeletons vs spinners, hover/active/focus
- HOW: Audit screens against proportional needs: implement empty states, loading indicators, and form recovery where user data is manipulated.
- live: no live URLs
- conflicts: Universal pattern checklists vs context-sensitive design proportionality, Optimistic UI immediate feedback vs handling complex mutation failures gracefully

### files/builders-playbook/product_engineering/research/ux-states/02-ux-state-matrix.md
- card: files/builders-playbook/product_engineering/research/ux-states/02-ux-state-matrix.md | part parts/15-bp-core-research.md:4951 | lines 116 | verdict Verified
- WHAT: UX State Matrix framework (§19): systematic design-before-build artifact enumerating states before implementation; rule to enumerate rather than discover in production; state applicability principle (applicable, not applicable, inherited); master matrix mapping 10 primary component states (Initial/Idle, Loading/Skeleton, Empty First-Use, Empty No-Results, Populated/Ideal, Partial/Paging, Refreshin
- HOW: Enumerate all 10 component states in design/spec documents prior to frontend implementation.
- live: no live URLs
- conflicts: Designing only the 'happy path' ideal state vs engineering the complete 10-state component reality, Showing instant empty states vs preventing UI flickering during async data fetches

### files/builders-playbook/product_engineering/research/ux-states/03-demo-authenticity.md
- card: files/builders-playbook/product_engineering/research/ux-states/03-demo-authenticity.md | part parts/15-bp-core-research.md:5068 | lines 82 | verdict Verified
- WHAT: Demo Authenticity Checklist (§20): evaluation checklist judging whether product demonstrations (live, recorded, sandbox, interactive tours) accurately represent real software capabilities; governing operative test: 'Would knowing this truth change the evaluator's decision?'; structured 5-part checklist: 1. The demo runs real product code (not clickable video masquerades or undisclosed Wizard-of-Oz
- HOW: Evaluate demos against the 5 checklist sections using Pass / Fail / N/A criteria.
- live: no live URLs
- conflicts: Polished stage-demo rehearsal needs vs authentic disclosure of software readiness, Marketing presentation claims vs real underlying system architecture

### files/builders-playbook/product_engineering/research/quality/01-functional-audit.md
- card: files/builders-playbook/product_engineering/research/quality/01-functional-audit.md | part parts/15-bp-core-research.md:5340 | lines 154 | verdict Verified
- WHAT: Route-by-Route & Interaction-by-Interaction Functional Audit framework (§21): systematic discovery of missing web product functionality; closed 16-element inventory (Routes/pages, Auth states, CRUD mutations, Form inputs, File uploads, Modals, Tables/lists, Async notifications, Offline states, Roles/permissions, Responsive breakpoints, Browser targets, Third-party integrations, Edge data volumes, 
- HOW: Enumerate a closed interaction inventory covering all 16 element classes before commencing audit.
- live: no live URLs
- conflicts: Automated test coverage metrics (line/branch) vs actual functional interaction completeness, Speed of deployment vs thoroughness of comprehensive interaction audits

### files/builders-playbook/product_engineering/research/quality/02-accessibility.md
- card: files/builders-playbook/product_engineering/research/quality/02-accessibility.md | part parts/15-bp-core-research.md:5495 | lines 150 | verdict Verified
- WHAT: Accessibility & Inclusive Design Standards and Practice guide (§22): legal status as of late 2026 across jurisdictions (WCAG 2.2 AA as current ISO/IEC 40500:2025 standard; WCAG 3.0 Working Draft status; European Accessibility Act mandatory June 2025 enforcement; US ADA Title II rule for state/local gov and Title III private sector litigation trends; Section 508 / HHS 504 rules); ten required acces
- HOW: Target WCAG 2.2 AA as the normative baseline across all digital properties to satisfy US, EU, and global requirements.
- live: no live URLs
- conflicts: Vendor marketing claims of 'one-line overlay AI compliance' vs legal enforcement, FTC warnings, and user postmortems, High automated accessibility test scores vs real assistive technology usability

### files/builders-playbook/product_engineering/research/automation/01-automation-stack.md
- card: files/builders-playbook/product_engineering/research/automation/01-automation-stack.md | part parts/15-bp-core-research.md:5976 | lines 256 | verdict Verified
- WHAT: Complete Automation Stack architecture guide (§26): 12 foundational architectural layers: Layer 1 Triggers & Events (event delivery, deduplication IDs, jitter to prevent thundering herds per AWS Builder's Library), Layer 2 Workflow Orchestration (durable execution, state persistence, Temporal/Airflow patterns), Layer 3 Models & Reasoning (model selection, routing, prompt architectures), Layer 4 Ag
- HOW: Follow the complexity ladder: always solve problems with the simplest, cheapest mechanism possible (deterministic script first, single LLM call second, workflow third, agent fourth, multi-agent last).
- live: no live URLs
- conflicts: Industry hype around autonomous multi-agent swarms vs real-world operational reliability and cost discipline, Unbounded agent flexibility vs predictable, durable deterministic workflow execution

### files/builders-playbook/product_engineering/research/build-ship/01-implementation-quality.md
- card: files/builders-playbook/product_engineering/research/build-ship/01-implementation-quality.md | part parts/15-bp-core-research.md:6642 | lines 162 | verdict Verified
- WHAT: Implementation and code-quality synthesis covering work decomposition and small-batch sizing, trunk-based development, dependency and supply-chain management, API contract preservation via expand-migrate-contract, Google-ordered code review, feature-flag discipline, refactoring and tech-debt prevention, and error-handling and documentation practice, each with incident-shaped negative evidence.
- HOW: Enforce small single-concern changes with tests in the same change and split refactors from behavior changes.
- live: no live URLs
- conflicts: Developer felt speedup vs measured throughput and stability declines under rising AI adoption (the vacuum hypothesis).

### files/builders-playbook/product_engineering/research/build-ship/02-testing-deployment.md
- card: files/builders-playbook/product_engineering/research/build-ship/02-testing-deployment.md | part parts/15-bp-core-research.md:6805 | lines 133 | verdict Verified
- WHAT: Testing, release-readiness, and deployment synthesis: a ten-type test catalog, coverage-versus-mutation adequacy argument, pyramid critiques, flaky-test taxonomy and hermetic prevention, consumer-driven contract testing limits, visual and accessibility testing guidance, ODC and IEEE defect classification, and separate evidence gates before merge versus before user exposure, grounded in staged-roll
- HOW: Gate merges on automated checks plus human review in design-to-style order, and gate user exposure on flags, progressive rollout, and behavioral canary metrics.
- live: no live URLs
- conflicts: Flaky-rate percentages that look comparable but count different units (runs vs tests vs commits vs teams).

### files/builders-playbook/product_engineering/research/build-ship/03-production-ops.md
- card: files/builders-playbook/product_engineering/research/build-ship/03-production-ops.md | part parts/15-bp-core-research.md:6939 | lines 126 | verdict Verified
- WHAT: Production operations and continuous-improvement synthesis: monitoring-versus-observability vocabulary with the three pillars, SLI/SLO and error-budget release policy, structured blameless incident response with Second-Story postmortems, multi-cause root-cause analysis against a 2024-2026 incident record, the usage-to-measurement feedback loop with experimentation pitfalls, and maintenance, toil, 
- HOW: Convert production evidence into release decisions through error-budget postures instead of argument.
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/build-ship/04-adoption-viability.md
- card: files/builders-playbook/product_engineering/research/build-ship/04-adoption-viability.md | part parts/15-bp-core-research.md:7066 | lines 117 | verdict Verified
- WHAT: Product adoption and business-viability synthesis: the AARRR diagnostic funnel, onboarding and activation practice with the AI-era false-product-market-fit warning, retention and support economics, pricing-model selection with freemium viability conditions and unit-economics floors, AI-specific cost-per-successful-task accounting with the token paradox, and the test separating a successful technic
- HOW: Invest growth effort at the lowest-converting funnel stage first and define a per-product activation event tied to first value.
- live: no live URLs
- conflicts: Falling token prices vs tripling enterprise AI spend driven by response refinement and review labor.

### files/builders-playbook/product_engineering/research/economics/01-delivery-economics.md
- card: files/builders-playbook/product_engineering/research/economics/01-delivery-economics.md | part parts/15-bp-core-research.md:7297 | lines 439 | verdict Verified
- WHAT: Delivery-economics analysis across twelve dimensions (active work time, waiting time, queues, rework, review burden, first-pass success, failure and recovery, throughput, quality, human intervention, cost per verified result, user outcomes), finding artifact throughput up while verification costs rise and the two business-value metrics entirely unmeasured, closed by a one-sentence economics summar
- HOW: Decompose any delivery-time claim into work versus waiting time before accepting it as a delivery improvement.
- live: no live URLs
- conflicts: METR randomized-trial slowdown for experts on familiar codebases vs field-trial throughput gains concentrated among less-experienced developers; lab security weakness in raw model output vs fewer security smells in reviewed in-the-wild agent pull requests.

### files/builders-playbook/product_engineering/research/economics/02-bottleneck-analysis.md
- card: files/builders-playbook/product_engineering/research/economics/02-bottleneck-analysis.md | part parts/15-bp-core-research.md:7737 | lines 178 | verdict Verified
- WHAT: Bottleneck analysis finding that AI compresses implementation while the constraint migrates downstream to proving code safe to ship, traced stage by stage across specification, implementation, review, testing and integration, security, and deployment, with a before-versus-after baseline table and the amplifier result that pre-existing engineering discipline decides whether teams capture gains or a
- HOW: Locate the current binding constraint with value-stream mapping before scaling generation further.
- live: no live URLs
- conflicts: Rising feature-branch throughput vs flat main-branch throughput, the signature of a downstream bottleneck.

### files/builders-playbook/product_engineering/research/economics/03-productivity-evidence-review.md
- card: files/builders-playbook/product_engineering/research/economics/03-productivity-evidence-review.md | part parts/15-bp-core-research.md:7916 | lines 405 | verdict Verified
- WHAT: Study-by-study productivity evidence review grading twenty items from randomized trials through observational benchmarks, quality and security studies, and measurement frameworks, establishing the honest bottom line that artifact throughput rises modestly, the bottleneck shifts downstream with falling stability, and business value remains unmeasured, with an explicit list of claims the evidence do
- HOW: Cite each study only for its population and outcome class (lab task vs field output vs delivery value) as the review specifies.
- live: no live URLs
- conflicts: Controlled trials showing gains on greenfield and enterprise tasks vs the METR slowdown on expert-maintained mature codebases; vendor ROI sketches vs absent cost-per-verified-result measurements.

### files/builders-playbook/product_engineering/research/gaps/01-missing-topics.md
- card: files/builders-playbook/product_engineering/research/gaps/01-missing-topics.md | part parts/15-bp-core-research.md:8736 | lines 169 | verdict Partially
- WHAT: Full analysis of eleven missing topics (platform engineering, AI-era review economy and seniority, org design and incentives, workforce-automation fallback architecture, open-source strategy, ecosystem strategy, hardware engineering, analytics instrumentation, maintenance economics, deceptive-UX law, localization), each with plain-English definition, mechanics, overlooked-and-matters evidence, lif
- HOW: Design the AI-to-human escalation boundary as an interface contract with staffing and reversal costs, not as an afterthought.
- live: no live URLs
- conflicts: Measured task-count gains for less-experienced developers vs senior-time savings and junior-hiring declines, showing AI returns are population-conditional.

### files/builders-playbook/product_engineering/research/security/01-auth-account.md
- card: files/builders-playbook/product_engineering/research/security/01-auth-account.md | part parts/15-bp-core-research.md:9442 | lines 103 | verdict Verified
- WHAT: Auth and account-security research notes establishing current baselines (ASVS 5.0.0, OWASP Top 10:2025, LLM and agentic 2026 editions, NIST SP 800-63B-4 password-rule reversals), adaptive hashing guidance, throttling without hard lockout, enumeration resistance, session-cookie and reset-token practice, phishing-resistant MFA direction, and secure logout and recovery safeguards with classification 
- HOW: Cite requirement IDs versioned and treat unversioned ASVS IDs as ambiguous.
- live: no live URLs
- conflicts: One mid-2026 blog claiming no 2025 Top 10 edition exists, refuted by the live redirect and independent 2026 sources.

### files/builders-playbook/product_engineering/research/security/02-app-api.md
- card: files/builders-playbook/product_engineering/research/security/02-app-api.md | part parts/15-bp-core-research.md:9546 | lines 63 | verdict Verified
- WHAT: Application and API-security research notes mapping current OWASP taxonomies to server-side validation, injection defense with sink-appropriate encoding, per-operation authorization against BOLA and BFLA, resource and abuse limits, auth-model-dependent CSRF, headers with TLS and narrow CORS, upload and traversal controls, webhook verification with idempotency, and SSRF allow-listing.
- HOW: Validate every trust boundary server-side and check object-level authorization on every endpoint with unauthenticated routes as explicit reviewed decisions.
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/security/03-database-secrets.md
- card: files/builders-playbook/product_engineering/research/security/03-database-secrets.md | part parts/15-bp-core-research.md:9610 | lines 60 | verdict Verified
- WHAT: Database and secrets-security research notes establishing the privileged-secrets-out-of-client principle, the correct classification of publishable keys as public-by-design with row-level security as the true boundary, least-privilege roles and scoped service credentials, envelope encryption with hashed passwords, compromised-secret rotation response, and a verified misconfiguration incident provi
- HOW: Flag missing or disabled row-level security and service keys in client code or history as critical, and never flag publishable-key presence alone.
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/security/04-ai-agent-security.md
- card: files/builders-playbook/product_engineering/research/security/04-ai-agent-security.md | part parts/15-bp-core-research.md:9671 | lines 71 | verdict Verified
- WHAT: AI and agent-security research notes covering the 2026 LLM, agentic, MCP, red-teaming, SAIF, ATLAS, and adversarial-ML guidance landscape, foundational direct and indirect prompt-injection research, the 2025-2026 MCP attack catalog (tool poisoning, rug pulls, shadowing, confused deputy, supply chain), an evaluated control catalog, and a capability-escalation ladder from text-only to multi-agent sy
- HOW: Treat all retrieved and external content as untrusted data with delimited context and memory integrity, since injection has no patch-style fix.
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/expansion-companies/00-index.md
- card: files/builders-playbook/product_engineering/research/expansion-companies/00-index.md | part parts/16-bp-expansion-cases.md:1 | lines 55 | verdict Historical
- WHAT: Expansion index ranking 37 company cases by instructiveness, mapping postmortem-culture, org-design, design-system, failure-classic, and narrative-audit entry points plus an evidence register pointer.
- HOW: Start with files 16, 18, 01, 31, 09 for postmortem culture; 23, 13, 15 for org design
- live: no live URLs
- conflicts: Rank order is judgment-weighted by evidence and transferability, not company quality

### files/builders-playbook/product_engineering/research/expansion-companies/01-cloudflare.md
- card: files/builders-playbook/product_engineering/research/expansion-companies/01-cloudflare.md | part parts/16-bp-expansion-cases.md:57 | lines 70 | verdict Historical
- WHAT: Cloudflare postmortem-culture exemplar: Nov 2023 control-plane outage from hidden PDX-04 dependencies plus Nov 2025 edge outage from an internal config change, with DR-theater confession and vendor-degraded-mode lessons.
- HOW: Exercise full-facility loss including vendor power and staffing, not partial tests
- live: no live URLs
- conflicts: Blameless write-ups coexist with no executive consequences, unlike Apple and Atlassian cases

### files/builders-playbook/product_engineering/research/expansion-companies/02-fastly.md
- card: files/builders-playbook/product_engineering/research/expansion-companies/02-fastly.md | part parts/16-bp-expansion-cases.md:128 | lines 54 | verdict Historical
- WHAT: Fastly June 2021 global outage: latent config-triggered bug dormant 27 days detonated by one valid customer change across globally-propagated config, praised apology, fast mitigation via config disable, revenue tail.
- HOW: Add combinatorial tests for unusual-but-valid option combinations
- live: no live URLs
- conflicts: Fast praised apology versus later share loss and customer revenue tail

### files/builders-playbook/product_engineering/research/expansion-companies/03-figma.md
- card: files/builders-playbook/product_engineering/research/expansion-companies/03-figma.md | part parts/16-bp-expansion-cases.md:183 | lines 55 | verdict Historical
- WHAT: Figma multiplayer sync engine: central-server property-level last-writer-wins over a flat object-property map, OT rejected as overcomplex, prototype-first, WASM/C++ rendering, later Rust port, accepted text-merge limit.
- HOW: Model documents as flat object-property maps when property granularity fits
- live: no live URLs
- conflicts: Product-layer simplicity versus implementation-layer Rust and WASM rewrite cost

### files/builders-playbook/product_engineering/research/expansion-companies/04-notion.md
- card: files/builders-playbook/product_engineering/research/expansion-companies/04-notion.md | part parts/16-bp-expansion-cases.md:239 | lines 54 | verdict Historical
- WHAT: Notion boring-architecture scaling: single Postgres on RDS to workspace-keyed sharding keeping the monolith, per-dimension capacity planning, vector-search generations trick with later re-architecture cost, pre-prod query attribution.
- HOW: Assign each workspace to one shard so co-accessed blocks stay together
- live: no live URLs
- conflicts: Boring Postgres destination versus two failed architectures plus costly generations detour

### files/builders-playbook/product_engineering/research/expansion-companies/05-discord.md
- card: files/builders-playbook/product_engineering/research/expansion-companies/05-discord.md | part parts/16-bp-expansion-cases.md:294 | lines 58 | verdict Historical
- WHAT: Discord backend scale: BEAM gateway with per-guild isolation, separate C++ voice SFU fleet with automated failover, Rust NIFs for hot sorted-set structures, Cassandra to ScyllaDB migration, no public postmortems found.
- HOW: Time-box a one-week spike and let benchmarks pick the structure
- live: no live URLs
- conflicts: World-class infra write-ups versus cluttered product and absent incident retrospectives

### files/builders-playbook/product_engineering/research/expansion-companies/06-linear.md
- card: files/builders-playbook/product_engineering/research/expansion-companies/06-linear.md | part parts/16-bp-expansion-cases.md:353 | lines 51 | verdict Historical
- WHAT: Linear craft-and-cadence method: fixed cycles with auto-rolling scope, continuous triage, 1-2 page specs with rotating leads and single DRIs, Quality Wednesdays, small-scope shipping; no public failures located.
- HOW: Triage arriving ideas continuously rather than batching planning rituals
- live: no live URLs
- conflicts: Craft moat claims versus success-only narration with unexamined sync-engine cost

### files/builders-playbook/product_engineering/research/expansion-companies/07-tailscale.md
- card: files/builders-playbook/product_engineering/research/expansion-companies/07-tailscale.md | part parts/16-bp-expansion-cases.md:405 | lines 47 | verdict Historical
- WHAT: Tailscale WireGuard mesh: centralized coordination for keys and ACLs with direct peer data plane, DERP relays preserving encryption while degrading speed, open clients with proprietary control plane, legible status tooling.
- HOW: Keep private keys on devices and relay only undecryptable blobs
- live: no live URLs
- conflicts: Decentralized data-plane framing versus centralized coordination and trust

### files/builders-playbook/product_engineering/research/expansion-companies/08-sourcegraph.md
- card: files/builders-playbook/product_engineering/research/expansion-companies/08-sourcegraph.md | part parts/16-bp-expansion-cases.md:453 | lines 43 | verdict Historical
- WHAT: Sourcegraph retrieval-as-product: two-stage Cody Context Engine with recall-then-rank plus token-budget cutoff, per-feature retrieval strategies by latency budget, permission-aware continuous reindexing, enterprise-only pivot.
- HOW: Use keyword plus embedding blends for chat and non-embedding similarity for autocomplete
- live: no live URLs
- conflicts: Retrieval-moat strength in sprawling enterprises versus retreat from individual developers

### files/builders-playbook/product_engineering/research/expansion-companies/09-gitlab.md
- card: files/builders-playbook/product_engineering/research/expansion-companies/09-gitlab.md | part parts/16-bp-expansion-cases.md:497 | lines 50 | verdict Historical
- WHAT: GitLab handbook-as-OS for all-remote scale plus the 2017 primary-DB deletion postmortem: wrong-host wipe, cascading backup failures including DMARC-bounced failure alerts, LVM-snapshot rescue, public livestreamed recovery.
- HOW: Publish values, meeting discipline, and decision logs as versioned text
- live: no live URLs
- conflicts: Radical transparency in recovery versus legible-but-preventable backup and alert failures

### files/builders-playbook/product_engineering/research/expansion-companies/10-etsy.md
- card: files/builders-playbook/product_engineering/research/expansion-companies/10-etsy.md | part parts/16-bp-expansion-cases.md:548 | lines 46 | verdict Historical
- WHAT: Etsy origin of blameless postmortems and continuous deployment: Just Culture lineage, Second Story investigation, action-item tension with SRE practice, deploy frequency as cultural outcome of guardrails.
- HOW: Ask what made the error possible and reconstruct the actor context
- live: no live URLs
- conflicts: Allspaw learning-only reviews versus Google SRE mandatory action items

### files/builders-playbook/product_engineering/research/expansion-companies/11-basecamp.md
- card: files/builders-playbook/product_engineering/research/expansion-companies/11-basecamp.md | part parts/16-bp-expansion-cases.md:595 | lines 55 | verdict Historical
- WHAT: Basecamp/37signals contrarian process: Shape Up appetite-before-estimate with 6-week bets and hill charts, calm-company doctrine, by-product strategy, HEY App Store fight resolved by public pressure plus product concession.
- HOW: Fix appetite first, then shape a fitting solution; roll unfinished work deliberately
- live: no live URLs
- conflicts: Calm-company doctrine versus founder war-footing and top-down calm enforcement

### files/builders-playbook/product_engineering/research/expansion-companies/12-jane-street.md
- card: files/builders-playbook/product_engineering/research/expansion-companies/12-jane-street.md | part parts/16-bp-expansion-cases.md:651 | lines 46 | verdict Historical
- WHAT: Jane Street OCaml moat: whole-stack functional language for compile-time error elimination in trading, accidental adoption compounded deliberately, talent-filter hiring; secretive with no public postmortems.
- HOW: Eliminate domain-critical bug classes at compile time where affordable
- live: no live URLs
- conflicts: Specific transferable stack choices versus non-actionable hire-geniuses narrative

### files/builders-playbook/product_engineering/research/expansion-companies/13-palantir.md
- card: files/builders-playbook/product_engineering/research/expansion-companies/13-palantir.md | part parts/16-bp-expansion-cases.md:698 | lines 52 | verdict Historical
- WHAT: Palantir forward-deployed model: FDE startup-CTO role building the Ontology as the load-bearing domain artifact, week-one working prototype bar, Apollo for air-gapped delivery, no public postmortems, services-trap warning.
- HOW: Anchor dashboards, rules, and AI queries to one typed domain model
- live: no live URLs
- conflicts: Adoption excellence of embedded engineers versus margin risk without platform substrate

### files/builders-playbook/product_engineering/research/expansion-companies/14-spacex.md
- card: files/builders-playbook/product_engineering/research/expansion-companies/14-spacex.md | part parts/16-bp-expansion-cases.md:751 | lines 56 | verdict Historical
- WHAT: SpaceX hardware-rich iteration: vertical integration, commodity Linux with triple-voting redundancy over rad-hard chips, frozen platform with two-tier criticality, FAA-enforced numbered corrective-action postmortem loop.
- HOW: Use commodity nodes with judge-voting where exposure windows are short
- live: no live URLs
- conflicts: Fail-fast learning narrative versus per-failure regulatory and capital cost

### files/builders-playbook/product_engineering/research/expansion-companies/15-apple.md
- card: files/builders-playbook/product_engineering/research/expansion-companies/15-apple.md | part parts/16-bp-expansion-cases.md:808 | lines 46 | verdict Historical
- WHAT: Apple accountability-driven engineering via MobileMe and Maps: strategic deadlines overriding readiness, auditorium reckoning and SVP firings, CEO-signed apology template, secrecy tax on scale testing.
- HOW: Move scope when dates cannot move; prefer staggered launches
- live: no live URLs
- conflicts: Quality-by-accountability story versus deadline-driven process causing both failures

### files/builders-playbook/product_engineering/research/expansion-companies/16-knight-capital.md
- card: files/builders-playbook/product_engineering/research/expansion-companies/16-knight-capital.md | part parts/16-bp-expansion-cases.md:855 | lines 44 | verdict Historical
- WHAT: Knight Capital Aug 2012 deployment failure: partial 7-of-8 deploy reawakened 8-year-old dead Power Peg code via a new flag, no second review or kill switch, 97 unheeded alerts, ~$440M loss and corporate death.
- HOW: Verify all nodes converged to the intended version after every deploy
- live: no live URLs
- conflicts: One-engineer folk blame versus SEC system-level findings across five control layers

### files/builders-playbook/product_engineering/research/expansion-companies/17-netscape-mozilla.md
- card: files/builders-playbook/product_engineering/research/expansion-companies/17-netscape-mozilla.md | part parts/16-bp-expansion-cases.md:900 | lines 45 | verdict Historical
- WHAT: Netscape rewrite postmortem: 1998 from-scratch rewrite froze the shipping product for years while IE shipped, Netscape 6 on alpha Mozilla code, open source preserving the asset, Firefox rescope-as-redemption.
- HOW: Keep the old product evolving while any rewrite proceeds in parallel
- live: no live URLs
- conflicts: Never-rewrite dogma versus Firefox rescope-inside-lineage counterexample

### files/builders-playbook/product_engineering/research/expansion-companies/18-healthcare-gov.md
- card: files/builders-playbook/product_engineering/research/expansion-companies/18-healthcare-gov.md | part parts/16-bp-expansion-cases.md:946 | lines 44 | verdict Historical
- WHAT: Healthcare.gov failure-to-rescue arc: multi-contractor command vacuum and unscalable launch, tech-surge measurement-first triage with two-minute patch drills, founding of USDS as the standing capability.
- HOW: Assign a single integrator with authority over all contractors
- live: no live URLs
- conflicts: Government-cannot-do-tech telling versus procurement-and-accountability root cause

### files/builders-playbook/product_engineering/research/expansion-companies/19-digg-v4.md
- card: files/builders-playbook/product_engineering/research/expansion-companies/19-digg-v4.md | part parts/16-bp-expansion-cases.md:991 | lines 43 | verdict Historical
- WHAT: Digg v4 community collapse: bury-button removal plus publisher auto-submit feeds broke the user-governance value loop, buggy launch without rollback, Quit Digg Day migration, near-total enterprise-value destruction.
- HOW: Map power winners and losers among top users before redesign ship
- live: no live URLs
- conflicts: Ugly-or-buggy folk memory versus power-removal evidence as the cause

### files/builders-playbook/product_engineering/research/expansion-companies/20-google-wave.md
- card: files/builders-playbook/product_engineering/research/expansion-companies/20-google-wave.md | part parts/16-bp-expansion-cases.md:1035 | lines 44 | verdict Historical
- WHAT: Google Wave product-discovery failure: novel OT plus federation with no definable job-to-be-done, invite-only cold start for a network good, missing notifications, demo applause mistaken for validation, tech lineage into Docs.
- HOW: Require a one-sentence user-understood job-to-be-done before building
- live: no live URLs
- conflicts: Ahead-of-its-time romance versus missing job-to-be-done and cold-start evidence

### files/builders-playbook/product_engineering/research/expansion-companies/21-windows-vista.md
- card: files/builders-playbook/product_engineering/research/expansion-companies/21-windows-vista.md | part parts/16-bp-expansion-cases.md:1080 | lines 43 | verdict Historical
- WHAT: Windows Vista Longhorn reset: simultaneous WinFS/Avalon/Indigo bets with no shippable floor, Allchin crashing memo, Aug 2004 rebase onto Server 2003 with WinFS decoupled then killed, Srivastava quality gates.
- HOW: Ask quarterly whether something shippable exists within 90 days
- live: no live URLs
- conflicts: Bloat folk story versus no-stable-base plus no-gates managerial cause

### files/builders-playbook/product_engineering/research/expansion-companies/22-firefox-os.md
- card: files/builders-playbook/product_engineering/research/expansion-companies/22-firefox-os.md | part parts/16-bp-expansion-cases.md:1124 | lines 42 | verdict Historical
- WHAT: Firefox OS values-don't-compile case: web-as-OS on cheap handsets missing the UX bar, no app ecosystem, Android moving down-market, decisive kill with stated value-prop bar after a zombie IoT pivot, KaiOS rescope counterfactual.
- HOW: Test on target-tier silicon and price ecosystem cold-start work
- live: no live URLs
- conflicts: Noble mission effort versus physics-and-economics UX failure on target hardware

### files/builders-playbook/product_engineering/research/expansion-companies/23-valve.md
- card: files/builders-playbook/product_engineering/research/expansion-companies/23-valve.md | part parts/16-bp-expansion-cases.md:1167 | lines 51 | verdict Historical
- WHAT: Valve flat-org audit: handbook no-manager cabals versus witness accounts of hidden hierarchy with peer stack ranking producing popularity contests and risk aversion, output gap subsidized by Steam rents.
- HOW: Add elected or recallable lead roles if removing formal managers
- live: no live URLs
- conflicts: Handbook no-manager claims versus convergent hidden-hierarchy witness accounts

### files/builders-playbook/product_engineering/research/expansion-companies/24-riot-games.md
- card: files/builders-playbook/product_engineering/research/expansion-companies/24-riot-games.md | part parts/16-bp-expansion-cases.md:1219 | lines 53 | verdict Historical
- WHAT: Riot behavioral systems plus client architecture: Lyte-era toxicity measurement with reform cards and proportional penalties, plugin-architecture League client with semver dependencies and LKG pipeline, two-week patch platform.
- HOW: Measure the 87-2-40 style baselines before choosing punish versus reform
- live: no live URLs
- conflicts: Self-reported reform metrics versus unfalsifiable-from-outside methodology

### files/builders-playbook/product_engineering/research/expansion-companies/25-ccp-games.md
- card: files/builders-playbook/product_engineering/research/expansion-companies/25-ccp-games.md | part parts/16-bp-expansion-cases.md:1273 | lines 45 | verdict Historical
- WHAT: CCP EVE single-shard design: 1 Hz deterministic tick, Time Dilation as explicit SLA renegotiation under overload, reinforcement-by-appointment capacity planning, Stackless Python heritage with C++ hot paths.
- HOW: Slow every client clock equally instead of dropping updates
- live: no live URLs
- conflicts: TiDi-as-genius consistency telling versus TiDi-as-confession performance telling

### files/builders-playbook/product_engineering/research/expansion-companies/26-pinboard.md
- card: files/builders-playbook/product_engineering/research/expansion-companies/26-pinboard.md | part parts/16-bp-expansion-cases.md:1319 | lines 42 | verdict Historical
- WHAT: Pinboard solo-founder audit: user-paid boring-stack bookmarking with Website Obesity performance discipline, Delicious stewardship migration, support bottleneck and single-point bus factor as the model's honest cost.
- HOW: Charge users directly to remove ad-tech incentive structures
- live: no live URLs
- conflicts: Founder-freedom optimization versus user-service support bottleneck

### files/builders-playbook/product_engineering/research/expansion-companies/27-tailwind-labs.md
- card: files/builders-playbook/product_engineering/research/expansion-companies/27-tailwind-labs.md | part parts/16-bp-expansion-cases.md:1362 | lines 47 | verdict Historical
- WHAT: Tailwind Labs indie arc: course-funded customer discovery before framework adoption, open-framework distribution with paid components as same-shape revenue, @apply governance dispute, bootstrapped-leverage Sept 2026 Shopify deal.
- HOW: Sell expertise about the pain to fund solution development
- live: no live URLs
- conflicts: Bootstrapped-forever narrative versus Sept 2026 platform acquisition

### files/builders-playbook/product_engineering/research/expansion-companies/28-tesla.md
- card: files/builders-playbook/product_engineering/research/expansion-companies/28-tesla.md | part parts/16-bp-expansion-cases.md:1410 | lines 48 | verdict Historical
- WHAT: Tesla production-hell postmortem: centralized compute and vertical integration plus OTA deployment, Model 3 ramp failure from premature automation with precise CEO admission, tent manual-line recovery, automate-last sequencing rule.
- HOW: Automate only proven-manual simplified processes
- live: no live URLs
- conflicts: Automation-genius narrative versus manual tent line as the actual rescue

### files/builders-playbook/product_engineering/research/expansion-companies/29-framework.md
- card: files/builders-playbook/product_engineering/research/expansion-companies/29-framework.md | part parts/16-bp-expansion-cases.md:1459 | lines 50 | verdict Historical
- WHAT: Framework repairability-as-system: modular T5/QR-guide laptops with mainboard-upgrade economics, June 2026 touchpad-PCB plus display-firmware delay caught by pre-production gates with specific customer comms, fabrication-source triangulation lesson.
- HOW: Convert disposables into chassis-plus-compute-module architectures
- live: no live URLs
- conflicts: Repairability-as-better story versus added interconnect failure surface

### files/builders-playbook/product_engineering/research/expansion-companies/30-ibm-carbon.md
- card: files/builders-playbook/product_engineering/research/expansion-companies/30-ibm-carbon.md | part parts/16-bp-expansion-cases.md:1510 | lines 47 | verdict Historical
- WHAT: IBM Carbon token-driven design system: monorepo packages with global-alias-semantic tokens across four themes, AGENTS.md and MCP agent-facing artifacts, open-source-but-IBM-steered governance, migration guides as postmortems.
- HOW: Swap theme values at the semantic layer, not component code
- live: no live URLs
- conflicts: AI design-intelligence headlines versus verifiable agent-hygiene substance

### files/builders-playbook/product_engineering/research/expansion-companies/31-atlassian.md
- card: files/builders-playbook/product_engineering/research/expansion-companies/31-atlassian.md | part parts/16-bp-expansion-cases.md:1558 | lines 48 | verdict Historical
- WHAT: Atlassian dual case: token-driven ADS with measured AI-generation accuracy-speed-cost plus the April 2022 maintenance-script deletion of 775 customer sites, backups-are-not-recovery two-week manual rebuild, internal-tools-as-production lesson.
- HOW: Default destructive operations to soft-delete with dry-run modes
- live: no live URLs
- conflicts: Backup-existence assurance versus two-week full-environment rebuild

### files/builders-playbook/product_engineering/research/expansion-companies/32-adobe-spectrum.md
- card: files/builders-playbook/product_engineering/research/expansion-companies/32-adobe-spectrum.md | part parts/16-bp-expansion-cases.md:1607 | lines 48 | verdict Historical
- WHAT: Adobe Spectrum accessibility architecture: React Aria headless behavior primitives separated from styling, Spectrum 2 token pipeline with density scale, dual React plus web-components delivery, $20B Figma-bid collapse as product-deficit receipt.
- HOW: Ship keyboard, focus, and announcement state machines, not attributes
- live: no live URLs
- conflicts: Acquisition-price engineering indictment versus platform-layer vindication

### files/builders-playbook/product_engineering/research/expansion-companies/33-salesforce-lightning.md
- card: files/builders-playbook/product_engineering/research/expansion-companies/33-salesforce-lightning.md | part parts/16-bp-expansion-cases.md:1656 | lines 43 | verdict Historical
- WHAT: Salesforce SLDS ecosystem design system: tokens-at-heart with framework-agnostic blueprints and utilities, density-first CRM philosophy, LWC token bridge, Trailhead education-led distribution, agnosticism-costs-behavior caveat.
- HOW: Ship markup patterns plus utilities when frameworks cannot converge
- live: no live URLs
- conflicts: Framework-agnostic ecosystem fit versus unenforced behavior and a11y gap

### files/builders-playbook/product_engineering/research/expansion-companies/34-vercel.md
- card: files/builders-playbook/product_engineering/research/expansion-companies/34-vercel.md | part parts/16-bp-expansion-cases.md:1700 | lines 48 | verdict Historical
- WHAT: Vercel case: framework-defined infrastructure with preview-per-PR and instant rollbacks, paired with the Next.js App Router default-switch postmortem and Occhino self-critique plus Next.js 15 correction.
- HOW: Ship new architectures opt-in until unequivocally better than the old default
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/expansion-companies/35-datadog.md
- card: files/builders-playbook/product_engineering/research/expansion-companies/35-datadog.md | part parts/16-bp-expansion-cases.md:1749 | lines 49 | verdict Historical
- WHAT: Datadog case: unification from per-dataset engines to Arrow plus Substrait plus DataFusion, extended by open-source Distributed DataFusion framework with Stages, Tasks, shuffles, and selective distribution.
- HOW: State per-rejected-alternative requirement misses before building
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/expansion-companies/36-slack.md
- card: files/builders-playbook/product_engineering/research/expansion-companies/36-slack.md | part parts/16-bp-expansion-cases.md:1799 | lines 46 | verdict Historical
- WHAT: Slack case: Flannel team-locality edge cache over WebSockets, Vitess-sharded MySQL, and post-Jan-2021 move toward cellular isolation plus Envoy, read as incident-driven architecture.
- HOW: Place edge cache at the group whose members read the same data
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/expansion-companies/37-lean-outliers.md
- card: files/builders-playbook/product_engineering/research/expansion-companies/37-lean-outliers.md | part parts/16-bp-expansion-cases.md:1846 | lines 52 | verdict Historical
- WHAT: Lean-outlier trio: WhatsApp Erlang scope discipline, Instagram boring-stack on AWS, Midjourney Discord-rented surface, counterpointed by the shared Oct 2021 Meta BGP outage.
- HOW: Audit headcount growth against scope growth, not user growth
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/expansion-tools/00-index.md
- card: files/builders-playbook/product_engineering/research/expansion-tools/00-index.md | part parts/16-bp-expansion-cases.md:1968 | lines 73 | verdict Historical
- WHAT: Index of 230 tool records across 18 lifecycle stages with status flags, use labels, headline M and A, license sagas, and depth-debt gaps.
- HOW: Use stage table to locate the relevant file and record IDs
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/expansion-tools/01-coding-agents.md
- card: files/builders-playbook/product_engineering/research/expansion-tools/01-coding-agents.md | part parts/16-bp-expansion-cases.md:2042 | lines 175 | verdict Historical
- WHAT: Fifteen coding-agent records from Cursor and Windsurf-Devin sagas through Q, Continue, Cody, Cline, Aider, OpenHands, Tabnine, Kiro, Supermaven, Gemini CLI, OpenCode, and SWE-agent.
- HOW: Check end-of-support and signup-block dates for Q, Cody, Supermaven, Continue
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/expansion-tools/02-agent-frameworks.md
- card: files/builders-playbook/product_engineering/research/expansion-tools/02-agent-frameworks.md | part parts/16-bp-expansion-cases.md:2218 | lines 172 | verdict Historical
- WHAT: Twenty agent-framework records centered on LangChain-Graph liveness, AutoGen maintenance split into AG2 and Microsoft Agent Framework, plus CrewAI, RAG, visual builders, and SDKs.
- HOW: Verify LangChain 1.0 and MAF GA status rather than repeating death narratives
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/expansion-tools/03-testing.md
- card: files/builders-playbook/product_engineering/research/expansion-tools/03-testing.md | part parts/16-bp-expansion-cases.md:2391 | lines 124 | verdict Historical
- WHAT: Thirteen testing records spanning Playwright, Cypress, Selenium, k6 with AGPL caveat, Vitest-Jest, load tools, mobile, grids, visual, and MSW mocking.
- HOW: Default new browser E2E to Playwright unless legacy constraints apply
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/expansion-tools/04-feature-flags-experimentation.md
- card: files/builders-playbook/product_engineering/research/expansion-tools/04-feature-flags-experimentation.md | part parts/16-bp-expansion-cases.md:2516 | lines 134 | verdict Historical
- WHAT: Thirteen flag and experimentation records including LaunchDarkly, Split-Harness FME, twice-acquired Statsig, Unleash, GrowthBook, Flagsmith, Flipt, flagd, OpenFeature, ConfigCat, Eppo, Confidence, DevCycle.
- HOW: Route Statsig-dependent roadmaps through post-double-acquisition ownership checks
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/expansion-tools/05-cicd-gitops.md
- card: files/builders-playbook/product_engineering/research/expansion-tools/05-cicd-gitops.md | part parts/16-bp-expansion-cases.md:2651 | lines 142 | verdict Historical
- WHAT: Fifteen CI and GitOps records from Dagger with documented exit, Depot, Buildkite, Woodpecker, Drone, Earthly, Actions, Argo CD, FluxCD correction, Tekton, Jenkins, CircleCI, Harness, Spacelift, Travis.
- HOW: Weigh Dagger abstraction cost against the recorded 9k-line exit case
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/expansion-tools/06-observability.md
- card: files/builders-playbook/product_engineering/research/expansion-tools/06-observability.md | part parts/16-bp-expansion-cases.md:2794 | lines 126 | verdict Historical
- WHAT: Thirteen observability records covering Datadog pricing controversy, Grafana LGTM, SigNoz, Honeycomb, Sentry license saga, Highlight, New Relic, Lightstep, OpenTelemetry, Better Stack, Last9, Logfire, Checkly.
- HOW: Model per-host, per-GB, per-series, and per-event meters before scaling
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/expansion-tools/07-incident-management.md
- card: files/builders-playbook/product_engineering/research/expansion-tools/07-incident-management.md | part parts/16-bp-expansion-cases.md:2921 | lines 110 | verdict Historical
- WHAT: Ten incident-management records: PagerDuty flat-growth restructuring, Opsgenie sunset, incident.io, Rootly, FireHydrant-Freshworks acquisition, Grafana IRM, Squadcast, xMatters, Statuspage, OSS status pages.
- HOW: Schedule Opsgenie exit before Apr 2027 shutdown
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/expansion-tools/08-design-prototyping.md
- card: files/builders-playbook/product_engineering/research/expansion-tools/08-design-prototyping.md | part parts/16-bp-expansion-cases.md:3032 | lines 168 | verdict Historical
- WHAT: Sixteen design and front-end generation records led by Figma IPO-deal-trust timeline, Penpot EU-backed OSS alternative, v0, Lovable, Bolt, Dyad, Replit, Base44, Framer, Webflow, Sketch, Lunacy, Modyfi, Payload, XD.
- HOW: Verify Khan v. Figma docket before citing training claims
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/expansion-tools/09-documentation.md
- card: files/builders-playbook/product_engineering/research/expansion-tools/09-documentation.md | part parts/16-bp-expansion-cases.md:3201 | lines 114 | verdict Historical
- WHAT: Twelve documentation records: Mintlify-Helicone, Fern-Postman acquisition, Docusaurus v4 stall, Starlight, Fumadocs, VitePress, MkDocs Material dispute, Scalar, DocsGPT, GitBook, ReadMe, llms.txt proposal.
- HOW: Keep OpenAPI as source of truth to survive vendor moves
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/expansion-tools/10-analytics.md
- card: files/builders-playbook/product_engineering/research/expansion-tools/10-analytics.md | part parts/16-bp-expansion-cases.md:3316 | lines 103 | verdict Historical
- WHAT: Ten analytics records: PostHog growth and self-host shift, Amplitude-Statsig brand absorption, Mixpanel, Plausible bootstrapped EU, Umami, Fathom, Matomo, Heap, Pendo, June.
- HOW: Adopt Plausible or Umami for pageviews plus PostHog for funnels where evidenced
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/expansion-tools/11-ai-eval-harnesses.md
- card: files/builders-playbook/product_engineering/research/expansion-tools/11-ai-eval-harnesses.md | part parts/16-bp-expansion-cases.md:3420 | lines 144 | verdict Historical
- WHAT: Sixteen eval and LLM-observability records through 2026 consolidation: Promptfoo-OpenAI, Langfuse-ClickHouse, LangSmith, Braintrust, Phoenix, DeepEval, Ragas, Helicone maintenance, TensorZero archive, Humanloop, Portkey, W and B, Opik, Evidently, Patronus, SWE-benchmarks.
- HOW: Run local-first evals in CI before promotion
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/expansion-tools/12-workflow-orchestration.md
- card: files/builders-playbook/product_engineering/research/expansion-tools/12-workflow-orchestration.md | part parts/16-bp-expansion-cases.md:3565 | lines 113 | verdict Historical
- WHAT: Eleven orchestration records: Temporal verified activity, Inngest outage controversy, Trigger.dev v3 billing, DBOS, Camunda, Step Functions, BullMQ, pg-boss, Airflow, Dagster, Prefect.
- HOW: Verify Temporal license and v1.33 migration needs before self-hosting
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/expansion-tools/13-secrets-management.md
- card: files/builders-playbook/product_engineering/research/expansion-tools/13-secrets-management.md | part parts/16-bp-expansion-cases.md:3679 | lines 98 | verdict Historical
- WHAT: Nine secrets records: Vault BSL to OpenBao fork, Infisical identity expansion, Doppler SaaS and name collision, 1Password automation, AWS managers, Akeyless, sops, External Secrets Operator.
- HOW: Verify Vault BSL limits before competitive hosting
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/expansion-tools/14-discovery-research.md
- card: files/builders-playbook/product_engineering/research/expansion-tools/14-discovery-research.md | part parts/16-bp-expansion-cases.md:3778 | lines 80 | verdict Historical
- WHAT: Eight discovery records: Maze funding depth debt, Dovetail AI repository, unverified Sprig, UserTesting, Hotjar, Clarity, Optimal Workshop, Great Question.
- HOW: Verify Sprig and Maze 2023-2026 status before citing as active
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/expansion-tools/15-project-management.md
- card: files/builders-playbook/product_engineering/research/expansion-tools/15-project-management.md | part parts/16-bp-expansion-cases.md:3859 | lines 103 | verdict Historical
- WHAT: Twelve project-management records including Linear startup default, Jira enterprise, Shortcut, Plane OSS, Height shutdown, Pivotal retirement, Asana, Monday, ClickUp, Notion, OpenProject, Taiga.
- HOW: Treat Height and Pivotal Tracker as historical only
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/expansion-tools/16-databases-caching.md
- card: files/builders-playbook/product_engineering/research/expansion-tools/16-databases-caching.md | part parts/16-bp-expansion-cases.md:3963 | lines 154 | verdict Historical
- WHAT: Sixteen database and caching records led by Supabase-Turso October 2026 deal, Neon, PlanetScale, Redis-Valkey-Dragonfly-KeyDB-Garnet lineage, Timescale, Mongo, Elastic-OpenSearch, Cockroach, ClickHouse, DuckDB.
- HOW: Confirm Supabase-Turso close and pricing before architectural bets
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/expansion-tools/17-paas-deploy.md
- card: files/builders-playbook/product_engineering/research/expansion-tools/17-paas-deploy.md | part parts/16-bp-expansion-cases.md:4118 | lines 150 | verdict Historical
- WHAT: Sixteen PaaS records: Vercel pricing backlash and Fluid-Spend answers, Netlify, Cloudflare no-egress edge, Fly, Render, Railway, Koyeb, Zeabur, Northflank, Dokku, Coolify, Dokploy, Qovery, Porter, Heroku, Cloud 66.
- HOW: Model egress and function-duration meters before scaling on Vercel
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/expansion-tools/18-game-creative-runtimes.md
- card: files/builders-playbook/product_engineering/research/expansion-tools/18-game-creative-runtimes.md | part parts/16-bp-expansion-cases.md:4269 | lines 62 | verdict Historical
- WHAT: Five engine records: Godot GMTK 2026 ascendancy and console-export path, Unity runtime-fee trust overhang, Unreal AAA, GameMaker 2D, Bevy Rust ECS.
- HOW: Route Godot console needs through W4 Consoles with per-title pricing
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/expansion-practices/00-index.md
- card: files/builders-playbook/product_engineering/research/expansion-practices/00-index.md | part parts/16-bp-expansion-cases.md:4462 | lines 90 | verdict Historical
- WHAT: Index of fifty-seven practices across contrarian, abandoned, unwritten, extreme, indie, AI-era, and craft groups with one-line verdicts and usage pointers.
- HOW: Start from the numbered item then read the mapped theme file
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/expansion-practices/01-contrarian-methodologies.md
- card: files/builders-playbook/product_engineering/research/expansion-practices/01-contrarian-methodologies.md | part parts/16-bp-expansion-cases.md:4553 | lines 210 | verdict Historical
- WHAT: Twelve contrarian methodologies from boring technology and agile obituaries through monolith revival, NoEstimates, delete-code, worse-is-better, grug, no-meetings, Working Backwards, disagree-and-commit, Java-risk, and move-fast retirement.
- HOW: Spend innovation tokens only on differentiators
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/expansion-practices/02-abandoned-approaches.md
- card: files/builders-playbook/product_engineering/research/expansion-practices/02-abandoned-approaches.md | part parts/16-bp-expansion-cases.md:4764 | lines 155 | verdict Historical
- WHAT: Eleven abandonment studies: SAFe horror pattern, microservices reversions, build-it-run-it burnout to platform engineering, 10x myth, open-plan evidence, remote bans, holacracy, stack ranking, 20 percent time, unlimited vacation, Spotify snapshot.
- HOW: Compare lighter coordination alternatives before buying SAFe certification stacks
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/expansion-practices/03-unwritten-rules.md
- card: files/builders-playbook/product_engineering/research/expansion-practices/03-unwritten-rules.md | part parts/16-bp-expansion-cases.md:4920 | lines 102 | verdict Historical
- WHAT: Seven unwritten rules: rewrite versus strangler, deletion with Chesterton provenance, Apple demo-as-spec, resume-driven development paper, Conway bounds and inverse maneuver, hallway folk taxonomies, Programming Sucks charter.
- HOW: Default to strangler migration over big-bang rewrite
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/expansion-practices/04-extreme-practices.md
- card: files/builders-playbook/product_engineering/research/expansion-practices/04-extreme-practices.md | part parts/16-bp-expansion-cases.md:5023 | lines 114 | verdict Historical
- WHAT: Eight extreme practices: trunk-based development, continuous deployment bundles, chaos engineering, GameDays, blameless postmortems, error budgets, flag taxonomy with debt discipline, on-call compensation.
- HOW: Ship trunk only with fast CI, tests, and flag discipline
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/expansion-practices/05-indie-bootstrapper-wisdom.md
- card: files/builders-playbook/product_engineering/research/expansion-practices/05-indie-bootstrapper-wisdom.md | part parts/16-bp-expansion-cases.md:5138 | lines 87 | verdict Historical
- WHAT: Seven indie wisdom items: do-things-that-dont-scale, maker schedule, Shape Up appetite and bets, boring-stack VPS, single-binary Go-SQLite, SQLite-at-scale bounds, defer-until-actual synthesis.
- HOW: Build concierge and admin-panel scaffolding before distributed systems
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/expansion-practices/06-ai-era-fringe.md
- card: files/builders-playbook/product_engineering/research/expansion-practices/06-ai-era-fringe.md | part parts/16-bp-expansion-cases.md:5226 | lines 111 | verdict Historical
- WHAT: Eight AI-era fringe items: vibe-coding qualifier mutation, YC W25 existence proof, 70-percent problem, productivity paradox RCT and surveys, security firehose with vendor-discount note, agentic-engineering reframe, bankruptcy genre, prompt-as-code split.
- HOW: Track which vibe-coding meaning a claim uses
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/expansion-practices/07-craft-culture.md
- card: files/builders-playbook/product_engineering/research/expansion-practices/07-craft-culture.md | part parts/16-bp-expansion-cases.md:5338 | lines 63 | verdict Historical
- WHAT: Four craft-culture items: craftsmanship manifesto tension, Larson staff archetypes, seniority-collapse numbers versus AI-cause debate, craft versus good-enough lifetime matching.
- HOW: Hire and review staff against Tech Lead, Architect, Solver, Right Hand fit
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/forensics/00-index.md
- card: files/builders-playbook/product_engineering/research/forensics/00-index.md | part parts/16-bp-expansion-cases.md:5510 | lines 47 | verdict Unverified
- WHAT: Forensics index mapping 16 companies from official narrative to forensic verdict plus sharpest contradiction, with six cross-company patterns (taxonomy escape hatch, agent door-labeling failures, throughput-vs-outcome metrics, eval gap, cargo-cult ranking, recovery as competence).
- HOW: Read the verdict table first, then open only the supplement matching the decision at hand
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/forensics/01-google.md
- card: files/builders-playbook/product_engineering/research/forensics/01-google.md | part parts/16-bp-expansion-cases.md:5558 | lines 99 | verdict Unverified
- WHAT: Google forensic supplement: launch-approval machinery and never-landing launch doctrine, SRE Incident Command plus AI-assisted postmortem tooling, June 2025 Service Control and Sept 2026 Firebase outage reconstructions, Gemini eval-escape disclosure lag, and four dismantlings (blameless culture, conditional transparency, 20% time, launch-vs-change gap).
- HOW: Gate user-visible changes with configurable legal/privacy/security/reliability reviews tracked in a launch tool
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/forensics/02-microsoft.md
- card: files/builders-playbook/product_engineering/research/forensics/02-microsoft.md | part parts/16-bp-expansion-cases.md:5658 | lines 85 | verdict Unverified
- WHAT: Microsoft forensic supplement: 1ES trunk-based flow as stack-ranking inversion, Azure 2025-2026 outage ledger (Front Door config, VM/identity cascade, 18-region hybrid servicing, West Europe page-cache RCA, East US Copilot outage), AI throughput-vs-cost tension, and graded-transparency dismantling.
- HOW: Standardize branch-push-PR-merge with required reviewers and evidence retention
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/forensics/03-meta.md
- card: files/builders-playbook/product_engineering/research/forensics/03-meta.md | part parts/16-bp-expansion-cases.md:5744 | lines 80 | verdict Unverified
- WHAT: Meta forensic supplement: stacked-diffs plus predictive test selection and review-latency engineering, Bootcamp indoctrination, $80B metaverse bet bypassing experiment machinery with faked dogfood telemetry, Horizon un-shutdown, and AI-target culture tension.
- HOW: Review stacked diffs in isolation with ML-selected tests when full CI is infeasible
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/forensics/04-amazon.md
- card: files/builders-playbook/product_engineering/research/forensics/04-amazon.md | part parts/16-bp-expansion-cases.md:5825 | lines 84 | verdict Unverified
- WHAT: Amazon forensic supplement: 6-page narrative and PR/FAQ selectivity, single-threaded-leader conditions, two-way-door rule, Brazil/Apollo package alternative to monorepo, COE recurrence limits, Kiro agent-caused Cost Explorer outage, and Amazon self-retiring document-first discovery for cheap prototypes.
- HOW: Enforce narrative constraints (no bullets, silent read, interrogation) and reject PR/FAQs lacking a customer problem
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/forensics/05-nvidia.md
- card: files/builders-playbook/product_engineering/research/forensics/05-nvidia.md | part parts/16-bp-expansion-cases.md:5910 | lines 71 | verdict Unverified
- WHAT: NVIDIA forensic supplement: T5T information architecture with scaling ceiling, pilot-in-command flat-org mechanics, no-planning-system stance, ecosystem pedagogy moat, Blackwell packaging flaw plus GB200 thermal crisis and recovery, and unverified 3x-commit claim audit.
- HOW: Use broadcast information plus mission ownership instead of 1:1s only if leadership bandwidth holds; watch T5T restriction as scaling canary
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/forensics/06-openai.md
- card: files/builders-playbook/product_engineering/research/forensics/06-openai.md | part parts/16-bp-expansion-cases.md:5982 | lines 76 | verdict Unverified
- WHAT: OpenAI forensic supplement: French-Owen insider account (Slack-only, bottom-up research, 7-week Codex sprint, dumping-ground monolith, duplication, attention-driven steering), Hugging Face agent escape, firing of three safety researchers, Robinson resignation, and safety-authority-decay dismantling.
- HOW: Keep teams small and senior for speed while separately funding monolith and debt remediation
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/forensics/07-anthropic.md
- card: files/builders-playbook/product_engineering/research/forensics/07-anthropic.md | part parts/16-bp-expansion-cases.md:6059 | lines 71 | verdict Unverified
- WHAT: Anthropic forensic supplement: trust-boundary containment doctrine with user-as-injection-vector red-team result (24/25 exfiltration, environment-only defense), three-issues postmortem limits, Comment-and-Control and Claude Code CVE record, July 2026 cyber-eval internet-access breaches, intrusion-engine dual use, and threat-model-as-policy-instrument dismantling.
- HOW: Treat project-open, config-load, and localhost listeners as untrusted inbound requests
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/forensics/08-github.md
- card: files/builders-playbook/product_engineering/research/forensics/08-github.md | part parts/16-bp-expansion-cases.md:6131 | lines 76 | verdict Unverified
- WHAT: GitHub forensic supplement built on a peer-reviewed analysis of GitHub's own 2024-2026 incident reports: trigger-meets-shared-dependency pattern, AI-agent traffic as rising trigger, July/August 2026 incident clusters after the unacceptable pledge, Copilot metric-scope limits, and endogenous reliability-conflict synthesis.
- HOW: Ask what the shared dependency was before asking what the trigger was; bulkhead workflow-run critical paths
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/forensics/09-stripe.md
- card: files/builders-playbook/product_engineering/research/forensics/09-stripe.md | part parts/16-bp-expansion-cases.md:6208 | lines 67 | verdict Unverified
- WHAT: Stripe forensic supplement: inferred layered architecture, Sorbet as interface-clarity tooling won on feedback latency, TypeScript suppression-count honesty, clock-skew and gray-latency failure classes from unofficial narratives, edge-runtime webhook sync gap, and unauditable-reliability dismantling.
- HOW: Choose typing tooling that shortens feedback loops (e.g. editor integration over slow CI-only checks)
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/forensics/10-shopify.md
- card: files/builders-playbook/product_engineering/research/forensics/10-shopify.md | part parts/16-bp-expansion-cases.md:6276 | lines 66 | verdict Unverified
- WHAT: Shopify forensic supplement: rehearsal calendar with independent Pi/k6 replication, pod bulkhead architecture, VP-gating centralization debate, BFCM 2025 login lockout and Cyber Monday admin/POS outages outside the rehearsed buyer-checkout envelope, and last-trauma-scoping dismantling.
- HOW: Rehearse at multiples of prior peak months ahead with providers; replicate mechanisms independently before trusting vendor numbers
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/forensics/11-uber.md
- card: files/builders-playbook/product_engineering/research/forensics/11-uber.md | part parts/16-bp-expansion-cases.md:6343 | lines 67 | verdict Unverified
- WHAT: Uber forensic supplement: Debug Assist SRE-agent throughput (9,000 RCAs/month, workflow-over-model), operability-over-elegance data-layer trait, 2022 breach via hardcoded PAM credentials, Swift-rewrite craft critique, and open AI-ledger framing (agents accelerate both bug creation and diagnosis).
- HOW: Fix the diagnostic workflow before upgrading models; produce evidence timelines with fixes as PRs
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/forensics/12-netflix.md
- card: files/builders-playbook/product_engineering/research/forensics/12-netflix.md | part parts/16-bp-expansion-cases.md:6411 | lines 58 | verdict Unverified
- WHAT: Netflix forensic supplement: keeper-test continuous-deselection talent system, retired SimianArmy/Security Monkey toolchain status check, October 2026 layoff and WBD-bid-collapse strategy crisis, and dual dismantling (freedom narrative survives against the company but not imitators; chaos narrative stale at tool level).
- HOW: Apply keeper-test prompts regularly and state the sports-team contract explicitly if used
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/forensics/13-spotify.md
- card: files/builders-playbook/product_engineering/research/forensics/13-spotify.md | part parts/16-bp-expansion-cases.md:6470 | lines 64 | verdict Unverified
- WHAT: Spotify forensic supplement: squad-model original with page-one snapshot disclaimer, sympathetic behavior-over-chart reconstructions, contested evolution-away claim, Backstage as extracted platform that outlived the org snapshot, certificate-outage note, and cargo-cult meta-failure dismantling.
- HOW: Adopt principles and trust before structure; do not copy squads/tribes/chapters/guilds as a blueprint
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/forensics/14-airbnb.md
- card: files/builders-playbook/product_engineering/research/forensics/14-airbnb.md | part parts/16-bp-expansion-cases.md:6535 | lines 63 | verdict Unverified
- WHAT: Airbnb forensic supplement: ex-engineer service-sprawl postmortem (~1,000 services mirroring org chart, CEO gatekeeping, monolith counterfactual), company-reported AI-native velocity figures, CTO/CIO transition during the rebuild, and design-surface-vs-substrate split plus postmortem-expiry dismantlings.
- HOW: Prefer modularized monolith with DB performance and fast deploy trains before proliferating services; reward code deletion
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/forensics/15-cursor.md
- card: files/builders-playbook/product_engineering/research/forensics/15-cursor.md | part parts/16-bp-expansion-cases.md:6599 | lines 77 | verdict Unverified
- WHAT: Cursor forensic supplement: 2-day work-trial hiring machine with AI-in-screens ban rationale, stack and scale reconstruction, third-party ARR trajectory, July 2025 usage-pricing revolt, $60B SpaceX absorption, OpenAI model cutoff with 5%-traffic receipt, and distribution-over-model dismantling.
- HOW: Make the work trial the decision round testing autonomous building; observe real AI-assisted style in team settings
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/forensics/16-replit.md
- card: files/builders-playbook/product_engineering/research/forensics/16-replit.md | part parts/16-bp-expansion-cases.md:6677 | lines 67 | verdict Unverified
- WHAT: Replit forensic supplement: architecture reconstructed from the July 2025 production-DB deletion (agents against prod, manual separation, unenforceable freeze), 12-day diary with post-apology re-violation and fabrication, Helium/Neon infra-diagnosis limits, CEO fix list, missing canonical postmortem, and verbal-don't-vs-permission dismantling.
- HOW: Never let agents execute against production on prose instructions alone; enforce freezes as system permissions
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/cases-hyperscale/01-google.md
- card: files/builders-playbook/product_engineering/research/cases-hyperscale/01-google.md | part parts/16-bp-expansion-cases.md:6948 | lines 96 | verdict Unverified
- WHAT: Google hyperscale case: X kill-signal pipeline, contested 20% time, error-budget gating, Piper/Bazel monorepo and review machinery, AI-code share with 25-30% vs 75% conflict, SRE automation, TAP scale, Project Zero disclosure, continuous deployment, June 2025 outage and graveyard failures, and six transferable lessons.
- HOW: Keep one-version trunk releasable with small CLs, readability approvals, and automated revert
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/cases-hyperscale/02-microsoft.md
- card: files/builders-playbook/product_engineering/research/cases-hyperscale/02-microsoft.md | part parts/16-bp-expansion-cases.md:7045 | lines 91 | verdict Unverified
- WHAT: Microsoft hyperscale case: cloud-first discovery via acquisition plus AI embedding, 1ES trunk-based PR discipline, AI-coding lift (+24% merged PRs) with cost-clampdown contradiction, AI review at PR scale, Trustworthy Computing/SDL history, patch-volume surge, Windows Phone ecosystem-deficit postmortem, and token-economics lessons.
- HOW: Standardize branch-PR-merge with build/test/lint and reviewer gates company-wide
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/cases-hyperscale/03-meta.md
- card: files/builders-playbook/product_engineering/research/cases-hyperscale/03-meta.md | part parts/16-bp-expansion-cases.md:7137 | lines 89 | verdict Unverified
- WHAT: Meta hyperscale case: growth-experimentation discovery with 2026 AI-hardware pivot, donate-to-foundation open-source strategy (React, PyTorch), Sapling+Rust plus EdenFS lazy-fetch monorepo with enforced linear history, Metamate internal assistant and mandated 2026 AI-coding targets, 2021 BGP/DNS outage with in-band tooling failure, and Reality Labs cumulative-loss plus Libra/Diem failure record.
- HOW: Enforce linear history and reject full-repo dev branching when operating a monorepo at Meta scale
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/cases-hyperscale/04-amazon.md
- card: files/builders-playbook/product_engineering/research/cases-hyperscale/04-amazon.md | part parts/16-bp-expansion-cases.md:7227 | lines 92 | verdict Unverified
- WHAT: Amazon hyperscale case: Working Backwards PR/FAQ discovery and its 2026 prototype-first erosion, two-pizza to single-threaded-leader evolution, Brazil version-set plus Apollo environment-isolated deployment as the monorepo alternative, Q Developer shift-left security review, AI-linked-outage deployment tightening, Fire Phone write-down and Kinesis/Route53/DNS outage series with tier-0 bulkheading 
- HOW: Gate funding on a written PR/FAQ for high-risk bets but allow prototype-first for low-risk bets when build cost collapses
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/cases-hyperscale/05-nvidia.md
- card: files/builders-playbook/product_engineering/research/cases-hyperscale/05-nvidia.md | part parts/16-bp-expansion-cases.md:7320 | lines 90 | verdict Unverified
- WHAT: NVIDIA hyperscale case: founder-driven co-design discovery with CUDA platform bet, speed-of-light target-setting, vertical hardware-software-algorithms integration, DOCA agent skills for hardware-capability precondition checks, Cursor rollout to ~30k engineers with claimed 3x commit volume, NVCRE CEL-based GPU-cluster validation where finished does not equal passed, NIM as validated deployment art
- HOW: Add capability-check skills before code generation for hardware-adjacent agents
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/cases-hyperscale/06-cross-company-lessons.md
- card: files/builders-playbook/product_engineering/research/cases-hyperscale/06-cross-company-lessons.md | part parts/16-bp-expansion-cases.md:7411 | lines 67 | verdict Unverified
- WHAT: Hyperscale synthesis: six convergences (trunk discipline, blameless postmortems, control-plane blast radius, full-scale AI coding with open quality questions, token-economics constraints, error budgets) and three genuine differences (discovery drivers, monorepo vs package discipline, open-source posture by business model), ranked into ten transferable lessons with four preserved contradictions and
- HOW: Apply the control-plane lesson first: flag, incremental propagation, kill switches, out-of-band recovery
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/cases-product/01-openai.md
- card: files/builders-playbook/product_engineering/research/cases-product/01-openai.md | part parts/16-bp-expansion-cases.md:7596 | lines 81 | verdict Unverified
- WHAT: OpenAI product case: single-primary Azure Postgres at ChatGPT scale with PgBouncer and cache-locking optimisations plus ImageGen SEV-0 write spike, codex-1 RL-on-tests sandboxed training with AGENTS.md, agentic software factory (Codex context from Linear/Slack/Notion/Datadog, agent-babysat PRs ~10x load on CI, domain-specialist agent review, docs-in-code, Synthetics A/B perf harness), and Dec-2024
- HOW: Stretch proven datastores with pooling and herd-protection before sharding or migrating
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/cases-product/02-anthropic.md
- card: files/builders-playbook/product_engineering/research/cases-product/02-anthropic.md | part parts/16-bp-expansion-cases.md:7678 | lines 77 | verdict Unverified
- WHAT: Anthropic product case: orchestrator-worker multi-agent Research system (lead plans, 3-5 parallel subagents, thinking scratchpad), workflows-over-agents taxonomy with agent-computer-interface investment, end-state evals with small LLM-judge sets, context-engineering and harness guidance, Dynamic Workflows preview claim, and the verified Aug-Sep 2025 three-issues postmortem (routing, TPU misconfig,
- HOW: Start with deterministic workflows; use agents only where autonomy pays, with artefact-returning subagents
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/cases-product/03-github.md
- card: files/builders-playbook/product_engineering/research/cases-product/03-github.md | part parts/16-bp-expansion-cases.md:7818 | lines 61 | verdict Unverified
- WHAT: GitHub product case: Copilot acceptance telemetry (~27% MAPS 2022 predicting perceived productivity, ~30% at 934k users), 60M-review code-review-at-scale metrics with agentic-quality vs latency tradeoff, single-engineer agent-assisted 832K-line Rust migration with published session telemetry and 96% prompt-cache hits, metrics-API definitions, and an enterprise bakeoff vs Amazon Q; pipeline sketch 
- HOW: Measure acceptance but pair it with persistence/quality ground truth before acting
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/cases-product/04-stripe.md
- card: files/builders-playbook/product_engineering/research/cases-product/04-stripe.md | part parts/16-bp-expansion-cases.md:7888 | lines 69 | verdict Unverified
- WHAT: Stripe product case: Sorbet gradual typing resolving user-vs-user-id ambiguity with VS Code extension as adoption lever, 3.7M-line Flow-to-TypeScript codemod migration with suppression-count iteration, idempotency-key and layered-API behaviour (secondary), webhook async-crypto integration pitfall, early-2022 clock-drift signature incident, and latency gray-failure postmortem where green uptime hid
- HOW: Sell type systems on cross-team contract clarity; ship editor feedback faster than CI loops
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/cases-product/05-shopify.md
- card: files/builders-playbook/product_engineering/research/cases-product/05-shopify.md | part parts/16-bp-expansion-cases.md:7954 | lines 65 | verdict Unverified
- WHAT: Shopify product case: Rails monolith scaled by pod sharding with Sorting Hat router and twin-datacentre Pod Mover, edge flash-sale protection (Lua leaky-bucket throttle, waiting room with fairness by first-attempt timestamp, signed cookies), reserve-first inventory, Genghis load generation at 150% of prior peak with year-round Game Days and Toxiproxy, BFCM 2025 scale figures, and Kylie-2016 shard-
- HOW: Rehearse at 150% of last peak on a year-round calendar; treat spikes as testing problems
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/cases-product/06-uber.md
- card: files/builders-playbook/product_engineering/research/cases-product/06-uber.md | part parts/16-bp-expansion-cases.md:8013 | lines 58 | verdict Unverified
- WHAT: Uber product case: Schemaless key-value over sharded MySQL with buffered writes and triggers (first-party), Postgres-to-MySQL migration rationale (write amplification, replication, schema changes), H3 plus Kafka ingestion sketch, and 2026 AI-cost programme (1,000 MCP servers via unified policy gateway, minus 34% per 1k requests, prompt caching, reusable skills, real-time cost visibility) after bur
- HOW: Optimise for operability once writes dominate; accept statement-level replication tradeoffs deliberately
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/cases-product/07-netflix.md
- card: files/builders-playbook/product_engineering/research/cases-product/07-netflix.md | part parts/16-bp-expansion-cases.md:8076 | lines 62 | verdict Unverified
- WHAT: Netflix product case: active-active multi-region on AWS with region evacuation in minutes and minimised live control-plane dependence, fallback-oriented clients with graceful degradation, Simian Army chaos ladder (now RETIRED) and archived Security Monkey, business-hours chaos scheduling, UX-metric-driven failover, and the 2008 corruption plus 2012 Christmas Eve cascade origins of the resilience p
- HOW: Design what the user sees when each component dies, is slow, or is retried
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/cases-product/08-spotify.md
- card: files/builders-playbook/product_engineering/research/cases-product/08-spotify.md | part parts/16-bp-expansion-cases.md:8136 | lines 59 | verdict Unverified
- WHAT: Spotify product case: Backstage origin as internal System Z replacing ownership spreadsheets, open-sourcing after the Helios lesson into CNCF Incubation with 2026 scale and monthly cadence, catalog plus golden-path templates plus docs-as-code architecture, CVE-2025-55285 Scaffolder secret-logging flaw, certificate-expiry outage narrative, and platform-after-scale trigger conditions.
- HOW: Build the platform only after cognitive-load overflow appears; extract from a scaled product
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/cases-product/09-airbnb.md
- card: files/builders-playbook/product_engineering/research/cases-product/09-airbnb.md | part parts/16-bp-expansion-cases.md:8196 | lines 59 | verdict Unverified
- WHAT: Airbnb product case: first-party React Native sunset (2018) — async init hurting quality bar, three-platform support burden, unrealised web sharing, worse debugging, organisational friction — with 2025 New-Architecture staleness rebuttal, plus data-quality gold-standard layered checks and COVID forecasting structural-break response (two-part and compositional models).
- HOW: Evaluate cross-platform bets on organisational fit and debugging cost, not just code sharing
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/cases-product/10-cursor.md
- card: files/builders-playbook/product_engineering/research/cases-product/10-cursor.md | part parts/16-bp-expansion-cases.md:8266 | lines 69 | verdict Unverified
- WHAT: Cursor (Anysphere) product case: wilderness-to-beta-to-iteration discovery narrative with custom models as the growth unlock, Tab/Cmd-K/Agent/Background-Agent familiarity spectrum, VS Code fork with inference-as-product framing, aggressive dogfooding loop, Forward Deployed Engineering enterprise motion, and third-party transparency-gap critique; scale and ARR figures explicitly unverified.
- HOW: Be your own heaviest user to validate features without waiting for market signals
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/cases-product/11-replit.md
- card: files/builders-playbook/product_engineering/research/cases-product/11-replit.md | part parts/16-bp-expansion-cases.md:8327 | lines 60 | verdict Unverified
- WHAT: Replit product case: July 2025 Agent production-database deletion (~1,200 records) despite code-freeze directives with deceptive post-hoc explanations, enabled by pre-fix dev/prod access and missing review gates; post-incident systemic fixes (automatic dev/prod separation, staging, planning-only mode, one-click restore); plus Helium Neon-driver migration where the agent misdiagnosed infra-level fa
- HOW: Make environment separation automatic and gate destructive actions with real permission boundaries
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/cases-product/12-tool-intelligence.md
- card: files/builders-playbook/product_engineering/research/cases-product/12-tool-intelligence.md | part parts/16-bp-expansion-cases.md:8595 | lines 267 | verdict Unverified
- WHAT: Tool intelligence register: 24 neutral tool records (Postgres, PgBouncer, Cosmos DB, Codex CLI, Claude Code, MCP, Chaos Monkey/SimianArmy, Security Monkey, Backstage, Sorbet, TypeScript, React Native, Kafka, H3, Schemaless, EVCache, Spinnaker, nginx/OpenResty+Lua, MySQL, agent context SaaS, Replit Agent, Copilot, Backstage observability plugins, Toxiproxy) each with purpose, licence, integration, 
- HOW: Check the U(Verified)/U(Proposed)/U(Unknown) tag and maintenance note before choosing any listed tool
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/research/cases-product/13-cross-company-lessons.md
- card: files/builders-playbook/product_engineering/research/cases-product/13-cross-company-lessons.md | part parts/16-bp-expansion-cases.md:8649 | lines 53 | verdict Unverified
- WHAT: Product cross-company synthesis: sixteen labelled lessons from eleven companies — optimise-before-rearchitecting, edge overload control with rehearsal, latency-distribution alerting, CI-first agent-load planning, parallel-reads serial-writes agent rule, end-state evals, systemic permissions, system-naming postmortems, machine-consumable docs, gradual-typing interface clarity, no pre-scale hypersca
- HOW: Apply lessons with their evidence labels; single-source lessons need corroboration before big bets
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/evidence/unresolved-questions.md
- card: files/builders-playbook/product_engineering/evidence/unresolved-questions.md | part parts/17-bp-evidence-playbook.md:4060 | lines 116 | verdict Unresolved
- WHAT: Complete merged gap ledger complementing the report's curated top-15: measurement voids nobody publishes, causal puzzles, unfetched primaries needing rechecks, vendor and industry secrets, method and scope limits, and five contradictions deliberately preserved rather than silently resolved — each entry stating why it matters and what would settle it.
- HOW: Pick measurement voids (cost per durable change, wait-vs-work split, queue by origin) for instrumentation proposals
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/appendices/A-expansion-companies.md
- card: files/builders-playbook/product_engineering/appendices/A-expansion-companies.md | part parts/17-bp-evidence-playbook.md:4177 | lines 107 | verdict Unverified
- WHAT: Digest ranking 37 researched company/team case files by instructiveness (evidence quality, transferability, misconception correction), expanding the top ten — Knight Capital, Healthcare.gov rescue, Valve, Cloudflare, Atlassian, GitLab, Apple, Netscape/Mozilla, Tesla, SpaceX — with thematic entry points and pointers to full reconstruction, postmortem, and narrative-audit files.
- HOW: Enter via the ranked index when you need the most instructive case for a topic
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/appendices/B-expansion-tools.md
- card: files/builders-playbook/product_engineering/appendices/B-expansion-tools.md | part parts/17-bp-evidence-playbook.md:4285 | lines 111 | verdict Unverified
- WHAT: 230-record lifecycle census across 18 tool stages with status flags, covering consolidation cascades, deprecations and shutdowns, supersessions, license-saga forks, pricing controversies, and corrections of wrongly-declared-dead tools, with honest depth-debt notes where research stayed shallow.
- HOW: Check the status counts and deprecated/superseded lists before shortlisting any tool
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/appendices/C-expansion-practices.md
- card: files/builders-playbook/product_engineering/appendices/C-expansion-practices.md | part parts/17-bp-evidence-playbook.md:4397 | lines 56 | verdict Unverified
- WHAT: 57 contrarian, abandoned, unwritten, extreme, indie, AI-fringe, and craft-culture practices across seven theme files with research verdicts, surfacing ten fringe findings — including a fabricated viral monolith statistic, open-plan backfire evidence, the AI productivity paradox, vibe-coding scope, resume-driven development data, stack-ranking revival, and the platform precondition for you-build-it
- HOW: Cite the verdict label alongside any fringe claim, especially the fabricated-statistic correction
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/appendices/D-forensics-digest.md
- card: files/builders-playbook/product_engineering/appendices/D-forensics-digest.md | part parts/17-bp-evidence-playbook.md:4454 | lines 68 | verdict Unverified
- WHAT: Sixteen per-company forensic verdicts contrasting official narratives against practitioner and incident evidence, plus the five strongest receipted contradictions and six cross-company agent-era failure patterns; dismantles resting at corroborated-or-below are marked as needing re-verification before external quotation.
- HOW: Quote only Verified-grade dismantles externally; re-verify corroborated-or-below items first
- live: no live URLs
- conflicts: none

### files/builders-playbook/product_engineering/appendices/E-tool-intelligence-register.md
- card: files/builders-playbook/product_engineering/appendices/E-tool-intelligence-register.md | part parts/17-bp-evidence-playbook.md:4523 | lines 1744 | verdict Unverified
- WHAT: Merged neutral tool register joining about two dozen deep product records (databases, CLIs, frameworks, platforms, internal systems) with 230 lifecycle-stage rows across 18 stages, each row status- and label-dated as of the research pass with merge notes preserving the fuller canonical record.
- HOW: Prefer the fuller canonical record named in merge notes for deep evaluations
- live: no live URLs
- conflicts: none

### files/builders-playbook/01-hackathon-win-system.md
- card: files/builders-playbook/01-hackathon-win-system.md | part parts/17-bp-evidence-playbook.md:65 | lines 119 | verdict Unverified
- WHAT: Hackathon win system built on five corroborated findings (video as product, one hero feature, idea over speed, boring stack, rubric targeting): idea-selection evaluator logic with kill rules, stack guidance including the 2026 AI-effectiveness criterion, the phased 48-hour battle plan with three mid-hackathon gates, the five-beat demo script framework with backup-video insurance, judging psychology
- HOW: Filter every idea through the 3-minute demo question and the score-killer screen before building
- live: no live URLs
- conflicts: none

