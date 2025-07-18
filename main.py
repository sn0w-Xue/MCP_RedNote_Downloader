from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent / "tool"))

from fastmcp import FastMCP
from typing import Annotated
from pydantic import Field
import json
from source.module import Settings
from source.application import XHS
from source.translation import _, switch_language


mcp = FastMCP(
    name='RedNote Downloader',
    instructions="""
        This server provides tools for downloading works from RedNote.
        A URL containing any of the following strings is a RedNote work URL:
            1. www.xiaohongshu.com
            2. xhslink.com
        Call the download_work_from_rednote() function to download the work via its URL.
    """,
)


async def download_tool(url: str, download: bool):
    async with XHS(**Settings().run()) as xhs:
        if not url:
            msg = _("提取小红书作品链接失败")
        else:
            if data := await xhs._XHS__deal_extract(
                    url,
                    download,
                    None,
                    None,
                    None,
                    True,
                    None,
                    None,
            ):
                if download:
                    msg = _(
                        f"下载小红书作品【{data['作品标题']}】成功, 如果需要进一步获取该作品信息可以继续使用该作品的 URL 调用 MCP Server:RedNote Downloader 的 get_rednote_work_info 工具")
                else:
                    msg = _("获取小红书作品信息成功: " + json.dumps(data, ensure_ascii=False))
            else:
                if download:
                    msg = _("下载小红书作品失败")
                else:
                    msg = _("获取小红书作品信息失败")
    return msg


@mcp.tool(
    name='download_rednote_work',
    description="""
        Download works from RedNote using the work's URL.
        The works include pictures, videos, and LivePhotos.
    """,
    tags=['download', 'RedNote']
)
async def download_work_from_rednote(
        url: Annotated[str, Field(description='The URL of the work.')]
) -> str:
    return await download_tool(url, True)


@mcp.tool(
    name='get_rednote_work_info',
    description="""
       Retrieve RedNote post information, including:
        - Favorites count
        - Comments count
        - Shares count
        - Likes count
        - Work tags
        - Work ID
        - Work URL
        - Work title
        - Work description
        - Work type
        - Publication time
        - Last update time
        - Timestamp
        - Author nickname
        - Author ID
        - Author URL
        - Download link
        - Animated image URL
        - And other relevant details

        It is crucial to note the following: The Download link in the data returned by this MCP tool cannot be used as the "url" input for the download_rednote_work tool. If you intend to use the download_rednote_work tool to download the work, you must use the original URL entered by the user.
    """,
    tags=['info', 'RedNote']
)
async def get_rednote_work_info(
        url: Annotated[str, Field(description='The URL of the work.')]
) -> str:
    return await download_tool(url, False)



if __name__ == '__main__':
    mcp.run()
