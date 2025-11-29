import asyncio
from langchain_openai import ChatOpenAI
from mcp_use import MCPAgent, MCPClient

async def main():
    # Configure MCP server
    config = {
        "mcpServers": {
	"sequential-thinking": {
		"command": "C:\\Program Files\\nodejs\\npx.cmd",
		"args": [
			"-y",
			"@modelcontextprotocol/server-sequential-thinking"
		]
	}}
    }

    client = MCPClient.from_dict(config)
    llm = ChatOpenAI(
        model="gpt-5-mini",
        base_url="http://localhost:4141/v1/",
        api_key="dummy"
    )
    agent = MCPAgent(llm=llm, client=client)

    result = await agent.run("List all my tools")
    print(result)

asyncio.run(main())