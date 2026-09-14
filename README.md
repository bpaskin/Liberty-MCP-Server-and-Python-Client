### Using Liberty as an MCP Server and Python Client to Test

---

This example demonstrates the versatility of Open Liberty as a [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server. The same business logic is exposed through **two protocols at once**:

- **MCP (JSON-RPC 2.0)** — so AI agents and LLM tool-use frameworks can discover and invoke it as a named tool.
- **JAX-RS REST** — so traditional HTTP clients continue to work unchanged.

The server is a Jakarta EE 11 WAR deployed on Liberty. The client is written in Python and exercises both endpoints to show that both paths reach the same underlying logic.

---

#### What changed from the original version

The original example required a manually downloaded Liberty beta and a locally installed `wlp` directory. The MCP annotations and feature name were also from a pre-release internal package. The current version removes all of that:

| Area | Before | Now |
|---|---|---|
| **Liberty install** | Manual download of beta ZIP, `<installDirectory>` in `pom.xml` | Downloaded automatically by `liberty-maven-plugin` |
| **MCP API** | `io.openliberty.mcp` JAR referenced by `<systemPath>` | `org.mcpjava:mcp-server-api:1.0.0` Maven dependency (`scope=provided`) |
| **Annotation package** | `io.openliberty.mcp.annotations` | `org.mcpjava.server.tools` |
| **Liberty feature** | `mcpServer-1.0` | `mcp-1.0` |
| **Jakarta EE** | 10 | 11 |
| **Java** | 21 | 25 |

---

#### Structure

```
mcp-server/   ← Liberty WAR: MCP + REST endpoints
mcp-client/   ← Python script: exercises both endpoints
```

#### Steps

1. [Liberty MCP + REST server](mcp-server/README.md)
2. [Python client](mcp-client/README.md)
