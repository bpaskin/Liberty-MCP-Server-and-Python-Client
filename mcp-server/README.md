### Liberty as an MCP Server

This module deploys a Jakarta EE WAR application on Open Liberty that exposes the same business logic through **two protocols simultaneously**:

| Protocol | Endpoint | Purpose |
|---|---|---|
| MCP (JSON-RPC 2.0) | `POST /mcp-server/mcp` | Tool invocation by AI agents |
| JAX-RS REST | `POST /mcp-server/services/generateRandomNumber/{min}/{max}` | Traditional HTTP clients |

---

#### How it works

The core logic lives in [`RandomNumber.java`](src/main/java/com/ibm/example/beans/RandomNumber.java), a plain CDI bean that uses `SecureRandom` to produce a number in a given range.

Two adapters expose that bean:

- **[`RandomNumberTool.java`](src/main/java/com/ibm/example/mcp/RandomNumberTool.java)** — annotated with `@Tool` and `@ToolArg` from `org.mcpjava.server.tools`. Liberty's `mcp-1.0` feature discovers this CDI bean at startup and registers it as an MCP tool with `name="RandomNumberGenerator"` and `title="Magical Random Number Generator"`.

- **[`RandomNumberService.java`](src/main/java/com/ibm/example/rest/RandomNumberService.java)** — a standard JAX-RS resource under `@ApplicationPath("/services")` (see [`RestApplication.java`](src/main/java/com/ibm/example/rest/RestApplication.java)).

---

#### What changed from the original version

| Area | Before | Now |
|---|---|---|
| **MCP API JAR** | `io.openliberty.mcp` — loaded from a local Liberty install path via `<systemPath>` in `pom.xml` | `org.mcpjava:mcp-server-api:1.0.0` — a proper Maven Central dependency with `scope=provided` |
| **`@Tool` / `@ToolArg` import** | `io.openliberty.mcp.annotations.Tool` / `ToolArg` | `org.mcpjava.server.tools.Tool` / `ToolArg` |
| **Liberty feature** | `mcpServer-1.0` | `mcp-1.0` (renamed in the release build) |
| **Jakarta EE version** | `jakarta.jakartaee-api:10.0.0` | `jakarta.jakartaee-api:11.0.0` |
| **Java source / target** | 21 | 25 |
| **`liberty-maven-plugin`** | 3.11.5, required `<installDirectory>` pointing to a local `wlp` folder | 3.12.3, no manual install path needed — Liberty is downloaded automatically |
| **`maven-war-plugin`** | 3.4.0 | 3.5.1 |
| **`pom.xml` properties** | Required `<wlp-dir-path>` and `<mcp-jar-version>` to be set manually | No environment-specific properties required |

The net result: the project now builds and runs with a plain `mvn liberty:run` — no pre-installed Liberty, no local JAR path, no manual property edits.

---

#### Running the server

```bash
mvn liberty:run
```

Liberty downloads itself, starts, and deploys the WAR. The server listens on:
- HTTP  → `http://localhost:9080`
- HTTPS → `https://localhost:9443`

To start and deploy separately (e.g. in a CI pipeline):

```bash
mvn liberty:start
mvn liberty:deploy
```

Once running, test with the [Python client](../mcp-client/README.md).
