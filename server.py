from mcp.server.fastmcp import FastMCP


mcp = FastMCP("DemoServer")
@mcp.tool()
def add(a:int, b:int)-> int:
    return a+b

@mcp.tool()
def multiply(c:int, d:int)-> int:
    return c*d



@mcp.tool()
def greet(name:str):
    return f"Hello {name}"


if __name__ == "__main__":
    mcp.run()


    