# MCP

By transport/provider.

### files/God research/B-category-catalogs/10-mcp.md
- card: files/God research/B-category-catalogs/10-mcp.md | part parts/05-firstpass-B-catalogs.md:3855 | lines 784 | verdict Verified
- WHAT: Master Model Context Protocol (MCP) ecosystem catalog (split 1/2 covering spec architecture, Tier 1/2/3 SDKs, official reference servers, and major vendor servers). Details MCP Specification 2026-07-28 stateless request/response core (retired initialize/Mcp-Session-Id, per-request _meta, server/discover, Mcp-Method/Mcp-Name headers, ttlMs/cacheScope caching, MRTR input_required, Tasks/MCP Apps ext
- HOW: 1. Spec & Protocol Migration: Implement or migrate to MCP Specification 2026-07-28 stateless core using per-request _meta (protocolVersion, clientInfo, clientCapabilities) and server/discover; handle 12-month deprecation window for roots/sampling/logging and legacy initialize handshake.
- live: no live URLs
- conflicts: Protocol version transition: Spec 2026-07-28 retires initialize handshake and Mcp-Session-Id in favor of stateless per-request _meta, but provides 12-month backwards compatibility for 2025-11-25 clients., TypeScript SDK package migration: Monolithic @modelcontextprotocol/sdk v1.x is deprecated and split into @modelcontextprotocol/server and @modelcontextprotocol/client in v2., SDK Tier parity discrepancy: Tier 1 SDKs (TS, Python, Go, C#, Rust, Ruby) implement full 2026-07-28 conformance (discovery, MRTR, header routing, caching), whereas Tier 2 (Java) and Tier 3 (Swift, Kotlin, PHP) lag on cutting-edge spec extensions., GitHub MCP server privilege defaults: Ships by default with full write/exec tools; requires explicit /readonly URL path modifier or X-MCP-Readonly:true header and restricted X-MCP-Toolsets to prevent accidental repository mutations.

### files/God research/atlas/catalogs/04-mcp.md
- card: files/God research/atlas/catalogs/04-mcp.md | part parts/08-atlas-33.md:18697 | lines 2846 | verdict Verified
- WHAT: Comprehensive Workstream #8 master catalog of MCP servers, external tools, development frameworks, and protocol interoperability (82 primary records, 12 archived reference servers, and 10 protocol alternatives). Covers Section 1: MCP Specification (JSON-RPC 2.0 open protocol, host/client/server architecture, 2025-11-25 Final and 2026-07-28 stateless core with per-request _meta, OAuth 2.1 / OIDC di
- HOW: 1. Protocol and Spec Compliance: Target MCP 2025-11-25 Final for stable conformant implementations or migrate to 2026-07-28 stateless core using per-request _meta capabilities and server/discover, observing the 12-month deprecation lifecycle for legacy initialize/Mcp-Session-Id.
- live: no live URLs
- conflicts: Protocol version transition: Spec 2026-07-28 retires stateful initialize handshake and Mcp-Session-Id in favor of stateless per-request _meta, but maintains 12-month backwards compatibility for 2025-11-25 clients., TypeScript SDK package restructuring: Monolithic @modelcontextprotocol/sdk v1.x is legacy/deprecated and split into @modelcontextprotocol/server and @modelcontextprotocol/client in v2., Reference server maintenance: 12 original reference servers in modelcontextprotocol/servers are marked archived/historical, replaced by vendor-maintained packages or standalone community tools., Astryx and CLI tool boundaries: Documented that certain UI design tools lack native MCP servers and require direct CLI invocations instead., Community database security posture: db_mcp_gateway wraps archived reference servers with credentials stored in JSON config files, presenting high blast radius compared to read-only native implementations like qore-mcp.

### files/solo-levelling/.harness/mcp/tools.yaml
- card: files/solo-levelling/.harness/mcp/tools.yaml | part parts/13-deve-solo.md:246 | lines 99 | verdict Verified
- WHAT: Model Context Protocol (MCP) tool interface schema definitions declaring 5 typed governance and artifact management tools: 'create_artifact' (typed project artifacts: prfaq, pitch, design-note, launch-checklist, postmortem, build-log), 'check_non_goals' (validates proposed task against non-goals list), 'evaluate_against_rubric' (runs FCAR against locked rubric in fresh context), 'monitor_metric' (
- HOW: Use as the schema contract when implementing or exposing MCP server endpoints for the harness.
- live: no live URLs
- conflicts: Defines tool schema definitions only without executable server implementations or stdio/SSE transport configurations.

### files/solo-levelling/the harness/.harness/mcp/mcp_servers.json
- card: files/solo-levelling/the harness/.harness/mcp/mcp_servers.json | part parts/13-deve-solo.md:10035 | lines 68 | verdict Verified
- WHAT: Model Context Protocol server configuration defining standardized local servers for filesystem access (src, tests, docs), git operations, Context7 live documentation, Postgres read-only queries, Playwright browser automation, and memory graph.
- HOW: Configure in agent environment settings to expose MCP tools to agent sessions
- live: no live URLs
- conflicts: none

### files/deve/.harness/mcp/tools.yaml
- card: files/deve/.harness/mcp/tools.yaml | part parts/13-deve-solo.md:38321 | lines 99 | verdict Verified
- WHAT: MCP tool specification for artifact and governance automation: five tools with JSON parameter/return schemas - create_artifact, check_non_goals, evaluate_against_rubric (FCAR), monitor_metric (rollback threshold), and create_postmortem.
- HOW: Expose these as MCP tools to the agent runtime, or implement them as local functions with matching schemas.
- live: no live URLs
- conflicts: No MCP server/client or transport config exists in the repo, so workflows referencing these actions have no runtime binding., Workflow ai_action skill names do not match the mcp tool names (see workflow cards).

