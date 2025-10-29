import json
import requests

MCP_SERVER_URL = "http://localhost:9080/mcp-server/mcp"  
REST_SERVER_URL = "http://localhost:9080/mcp-server/services/generateRandomNumber"  

def list_tools():
    # Build JSON-RPC 2.0 request
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/list"
    }

    headers = {
        "Content-Type": "application/json"
    }

    print("→ Sending request to MCP server...")
    print(json.dumps(payload, indent=2))

    # Send HTTP POST request
    response = requests.post(MCP_SERVER_URL, headers=headers, data=json.dumps(payload))

    if response.status_code != 200:
        print(f"HTTP error {response.status_code}: {response.text}")
        return

    # Parse JSON response
    data = response.json()
    print("\n← Received response:")
    print(json.dumps(data, indent=2))

    # Extract and display tools
    if "result" in data and "tools" in data["result"]:
        print("\nAvailable tools:")
        for tool in data["result"]["tools"]:
            print(f" - {tool['name']}: {tool.get('description', '')}")
    else:
        print("\nNo tools found or unexpected response structure.")

def getRandomNumber():
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": "Random Number Generator",
            "arguments": {
                "minNumber": 10,
                "maxNumber": 75
            }
        }
    }

    headers = {
        "Content-Type": "application/json"
    }

    print("..................................")
    print("→ Sending request to MCP server...")
    print(json.dumps(payload, indent=2))

    # Send HTTP POST request
    response = requests.post(MCP_SERVER_URL, headers=headers, data=json.dumps(payload))

    if response.status_code != 200:
        print(f"HTTP error {response.status_code}: {response.text}")
        return

    # Parse JSON response
    data = response.json()
    print("\n← Received response:")
    print(json.dumps(data, indent=2))

    # Extract and display results
    if "result" in data and "content" in data["result"]:
        print("\nYour Random Number is: ")
        for tool in data["result"]["content"]:
            print(f"{tool['text']}")
    else:
        print("\nError or Error parsing response.")

def getRandomNumberREST():
    payload = {}
    
    headers = {
        "Content-Type": "application/json"
    }

    print("..................................")
    print("→ Sending request to REST server...")
    print(json.dumps(payload, indent=2))

    response = requests.post(REST_SERVER_URL + "/10/75" , headers=headers, data=json.dumps(payload))

    if response.status_code != 200:
        print(f"HTTP error {response.status_code}: {response.text}")
        return

    # Parse JSON response
    data = response.json()
    print("\n← Received response:")
    print(json.dumps(data, indent=2))

if __name__ == "__main__":
    list_tools()
    getRandomNumber()
    getRandomNumberREST()