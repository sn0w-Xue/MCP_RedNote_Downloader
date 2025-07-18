<h1>🧩 MCP 服务器</h1>
<p><b>本地运行的</b> MCP 服务器, 配置如下</p>
<pre>
{
  "mcpServers": {
    "RedNote downloader": {
      "timeout": 600,
      "type": "stdio",
      "command": "uv",
      "args": [
        "run",
        "--project",
        "项目路径/tool",
        "项目路径/MCP_server.py"
      ]
    }
  }
}
</pre>
<p>目前提供 2 个 MCP Tool:</p>
<p>1. &nbsp <code>download_rednote_work</code>
<p>该工具用于下载小红书作品(图片、视频、LivePhoto), Agent 能自动识别该工具可以下载的小红书作品链接</p>
<p>请求示例为：<code>帮我下载这个链接的内容：http://xhslink.com/m/XXX</code></p>
<p>2. &nbsp <code>get_rednote_work_info</code>
<p>该工具用于获取小红书作品信息，包括收藏数量、评论数量、分享数量、点赞数量、作品标签、作品ID、作品链接、作品标题、作品描述、作品类型、发布时间、最后更新时间、时间戳、作者昵称、作者ID、作者链接、下载地址、动图地址等</p>
<p>请求示例为：<code>这个作品是谁发布的？点赞有多少？</code></p>
