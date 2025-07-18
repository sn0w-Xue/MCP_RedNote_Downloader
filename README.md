<h1>🧩 MCP 服务器</h1>
<p><b>本地运行的</b> MCP 服务器, 提供 Agent 通过 URL 下载小红书图片、视频和 LivePhoto 和获取作品信息的能力，感谢 <a href="https://github.com/JoeanAmier">JoeanAmier</a> 开源维护的 <a href="https://github.com/JoeanAmier/XHS-Downloader">XHS-Downloader</a> 项目.
<h2>安装教程</h2>
</p>
<p>1. &nbsp 克隆本项目代码到本地：<code>git clone --recurse-submodules --depth=1 git@github.com:sn0w-Xue/MCP_RedNote_Downloader.git</code></p>
<p>2. &nbsp 同步项目环境依赖：<code>cd tool && uv sync && uv add fastmcp</code></p>
<p>3. &nbsp 配置 MCP 服务器：</p>
<p>MacOS / Linux</p>
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
        "项目路径/main.py"
      ]
    }
  }
}
</pre>
<p>Windows</p>
<pre>
{
  "mcpServers": {
    "RedNote downloader": {
      "disabled": false,
      "timeout": 600,
      "type": "stdio",
      "command": "cmd",
      "args": [
        "/c",
        "uv",
        "run",
        "--project",
        "项目路径/tool",
        "项目路径/main.py"
      ]
    }
  }
}
</pre>
<h2>使用教程</h2>
<p>目前提供 2 个 MCP Tool:</p>
<p>1. &nbsp <code>download_rednote_work</code>
<p>&nbsp&nbsp&nbsp&nbsp该工具用于下载小红书作品(图片、视频、LivePhoto), Agent 能自动识别该工具可以下载的小红书作品链接</p>
<p>&nbsp&nbsp&nbsp&nbsp请求示例为：<code>帮我下载这个链接的内容：http://xhslink.com/m/XXX</code></p>
<p>2. &nbsp <code>get_rednote_work_info</code>
<p>&nbsp&nbsp&nbsp&nbsp该工具用于获取小红书作品信息，包括收藏数量、评论数量、分享数量、点赞数量、作品标签、作品ID、作品链接、作品标题、作品描述、作品类型、发布时间、最后更新时间、时间戳、作者昵称、作者ID、作者链接、下载地址、动图地址等</p>
<p>&nbsp&nbsp&nbsp&nbsp请求示例为：<code>这个作品是谁发布的？点赞有多少？</code></p>
