### Python MCP and REST Client

This client exercises the Liberty MCP server in four steps:

1. **Initialize** — sends an `initialize` handshake to establish an MCP session. The server returns an `Mcp-Session-Id` header that must be included on every subsequent MCP request.
2. **List tools** — calls `tools/list` and prints every MCP tool the server advertises.
3. **Invoke via MCP** — calls `tools/call` with tool name `"RandomNumberGenerator"` (registered title: `"Magical Random Number Generator"`) and arguments `minNumber=10`, `maxNumber=75`.
4. **Invoke via REST** — calls the plain JAX-RS endpoint `POST /mcp-server/services/generateRandomNumber/10/75` directly, bypassing MCP entirely.

Both the MCP path and the REST path hit the same underlying business logic ([`RandomNumber.java`](../mcp-server/src/main/java/com/ibm/example/beans/RandomNumber.java)), demonstrating that a single Liberty deployment can serve both AI agents and traditional HTTP clients simultaneously.

---

#### Prerequisites

- Python 3.10 or later
- The Liberty MCP server running at `http://localhost:9080` (see [mcp-server](../mcp-server/README.md))

---

#### Setup and run

```bash
# 1. Move into the client directory
cd mcp-client

# 2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies  (only `requests` is required)
pip install -r requirements.txt

# 4. Run the client
python3 main.py
```

The script prints the full JSON-RPC request and response for each call so you can see exactly what the MCP wire protocol looks like.
