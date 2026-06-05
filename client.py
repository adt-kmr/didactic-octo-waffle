import asyncio

from mcp import ClientSession
from mcp.client.stdio import stdio_client, StdioServerParameters


async def main():
    print("Client Started")

    server_params = StdioServerParameters(
        command="python",
        args=["server.py"]
    )

    async with stdio_client(server_params) as streams:

        read_stream, write_stream = streams

        async with ClientSession(
            read_stream,
            write_stream
        ) as session:

            print("Session created")

            # Handshake with the server
            await session.initialize()

            print("Server initialized")

            # Discover available tools
            tools = await session.list_tools()

            print("\nAvailable Tools:")
            print(tools)

            # Call add tool
            result = await session.call_tool(
                "add",
                {
                    "a": 5,
                    "b": 6
                }
            )

            print("\nTool Result:")
            print(result)


if __name__ == "__main__":
    asyncio.run(main())