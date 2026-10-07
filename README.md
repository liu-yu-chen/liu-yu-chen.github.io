# Liu YuChen / 刘雨辰 — 个人网站

本地完成的 Hugo 个人网站，使用你提供的 Tella 模板定制。包含个人介绍、研究分享、相册、随心感想四个板块，以及完整的中英文版本。左上角标识为 **LYC**，品牌姓名为 **Liu YuChen**，中文正文姓名为 **刘雨辰**。

## 预览

双击 `preview.cmd`，然后访问：

- 英文：<http://localhost:1313/>
- 中文：<http://localhost:1313/zh/>

如果已经有预览服务器正在运行，不必重复打开。终端中按 `Ctrl+C` 可以停止预览。需要 Hugo，本机已安装并验证的版本为 **0.121.2 extended**；网站不需要安装 Node、npm 或 Tailwind。

## 上传方式一：直接上传静态网站（最简单）

1. 解压 `delivery/Liu-YuChen-GitHub-Pages.zip`。
2. 建立或使用 GitHub 个人网站仓库：`你的GitHub用户名.github.io`。
3. 将解压后的**全部内容**上传至仓库根目录。根目录应直接有 `index.html`、`zh/`、`css/`、`images/`、`files/`、`js/` 等，不能再套一层文件夹。保留 `.nojekyll` 隐藏文件。
4. 在仓库 **Settings → Pages → Build and deployment** 中选择 **Deploy from a branch**，选择 `main` 分支与 `/ (root)`，保存。
5. 等待 GitHub Pages 部署完成，再访问它显示的网址。

这个 ZIP 是构建好的静态网页，不包含源码工作流；采用这一方式时无需启用 GitHub Actions。以后修改内容后运行 `build.cmd`，将 `public/` 内的最新网页重新上传。

## 上传方式二：上传源码，由 GitHub 自动构建

1. 解压 `delivery/Liu-YuChen-Website-Source.zip`，将全部内容上传到仓库根目录，包含隐藏的 `.github/` 文件夹。
2. 确认默认分支为 `main`。如果用其他分支，修改 `.github/workflows/pages.yml` 的 `on.push.branches`。
3. 在 **Settings → Pages** 将 Source 设为 **GitHub Actions**。
4. 在 **Actions** 找到 `Build and deploy personal website`。如没有自动运行，点击 **Run workflow**。
5. 工作流会使用本地已验证的 Hugo 版本构建两种语言、检查输出，再发布到 Pages。以后更新 Markdown 并上传，网站就会重新构建。

工作流遵循 [Hugo 官方 GitHub Pages 部署文档](https://gohugo.io/host-and-deploy/host-on-github-pages/) 和 [GitHub 自定义 Pages 工作流说明](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)。工作流自动使用仓库提供的实际部署地址；最近发布状态请查看仓库 Actions。

两种上传方式**选择一种即可**。源码方式不要把 `public/` 上传到仓库。

## 网站地址

根据当前文件夹名，默认 `baseURL` 为 `https://liu-yu-chen.github.io/`。这不是对你 GitHub 账号的验证。如果实际用户名、仓库地址或域名不同，请先在 `hugo.toml` 修改 `baseURL`，再运行 `build.cmd`。静态 ZIP 默认用于个人网站仓库根路径；项目仓库的 `/仓库名/` 子路径需要用正确 `baseURL` 重新构建。

## 后续修改位置

| 内容 | 英文 | 中文 |
| --- | --- | --- |
| 个人介绍 | `content/en/about.md` | `content/zh/about.md` |
| 研究分享 | `content/en/research/` | `content/zh/research/` |
| 相册 | `content/en/gallery/` | `content/zh/gallery/` |
| 随心感想 | `content/en/notes/` | `content/zh/notes/` |
| 导航、按钮和通用文字 | `i18n/en.json` | `i18n/zh.json` |

研究分享现有五个双语项目：生活方式与抑郁症状网络、基于主体建模文献分析、胃癌与GIST基因筛选、宫颈癌转录组与生存分析，以及厦门新能源汽车市场调研。图表按所提供材料中的数值绘制；页面同时说明相关样本口径、方法和局限。尤其对自陈调查的数据质量、报告中未达到显著性的结果和样本数未对齐的问题作了标注。项目报告与研究中的探索结果不应理解为临床验证或因果结论。

每个项目详情页包括数据来源表、分析流程、方法、结果及解释与局限，并提供页面内跳转目录。共 21 个图表面板，每种语言各一版：包括偏相关与敏感性对照、主题分布、差异表达计数、模块交集、Cox 风险比及置信区间、词频和 LDA 主题卡片等。图表数据与流程文字在 `data/research_charts.json`，渲染位于 `layouts/partials/research-chart.html`；Markdown 中的 `{{< research-results >}}` 将图表放在结果部分。计算得到的补充值均注明来源与口径。

- 首页两张大图与文案：`data/hero.json`。
- 四个社交链接：`data/social.json`。
- 站点名称、邮箱和基础设置：`hugo.toml`。
- 视觉样式：`assets/css/site.css`。
- 照片及图片：`static/images/`。
- 下载用简历：`static/files/CV.pdf`。

英文位于根路径，中文位于 `/zh/`。同一篇中英文文章使用**相同相对文件名**，语言按钮就会自动跳到对应版本。例如英文 `content/en/notes/a-small-thought.md` 对应中文 `content/zh/notes/a-small-thought.md`。

## 添加随心感想

新建 `content/zh/notes/a-small-thought.md`，例如：

```toml
+++
title = '一次旅行后的想法'
date = '2026-10-07'
description = '在这里写一句真实的文章简介。'
draft = false
+++

在这里写正文。可以使用 Markdown 标题、列表、链接和图片。
```

在 `content/en/notes/` 添加同名英文文件。`draft = true` 的文章不会发布，`hugo server -D` 可以预览草稿。

## 添加相册

1. 把自己的照片放进 `static/images/albums/`，建议压缩至单张约 500 KB–1 MB，并移除不想公开的照片元数据。
2. 新建 `content/zh/gallery/my-trip.md`：

```toml
+++
title = '我的旅行'
date = '2026-10-07'
description = '写下真实的地点与回忆。'
cover = 'images/albums/photo-01.jpg'
draft = false
[[photos]]
src = 'images/albums/photo-01.jpg'
caption = '第一张照片的说明'
[[photos]]
src = 'images/albums/photo-02.jpg'
caption = '第二张照片的说明'
+++

在这里写相册介绍。

{{< photos >}}
```

3. 添加 `content/en/gallery/my-trip.md` 对应英文版。相册列表会自动显示封面；点击照片可放大，按 Escape 或关闭按钮返回。

相册和随心感想现在是明确的空状态，没有虚构你的照片或经历。首页的风景与建筑照片来自提供的 Tella 模板，仅作装饰。研究卡片与爱好配图是装饰性矢量插画，不是研究结果或个人照片。

## 构建与检查

```powershell
hugo --minify
python scripts/check_site.py
```

需要重新生成两个交付 ZIP 时，运行 `python scripts/package_site.py`。它会先构建和检查，再生成静态网站包、源码包与 SHA-256 校验值，全程只操作本地文件。

`check_site.py` 仅使用 Python 标准库，检查生成页面、站内链接、静态资源、锚点、语言互链、翻译键、简历副本和 `.nojekyll`。`delivery/VERIFICATION.md` 记录本次验证结果。GitHub 实际发布仍需在上传后检查 Actions 或 Pages 的结果。

## 模板与内容来源

Tella 模板位于 `themes/tella-master/`，保留原始 MIT 许可证。根目录的 Hugo layouts 覆盖模板的页面与样式；首页继续使用模板的 Splide 轮播与所附装饰照片。原模板的示例公司内容没有发布到网站。

专业经历来自提供的 `CV.pdf`，家乡、爱好和社交链接来自本次补充。研究内容作为项目经历介绍，进行中的工作已明确标注，没有添加未经提供的论文、DOI、代码链接、准确率或研究成果。联系区域展示邮箱，原始 CV 下载文件完整保留。
