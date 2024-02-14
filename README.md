## :danger: New Version !!! :danger:

->
-> https://github.com/desonglll/scrapyJAV
->

## 🖥️ Javlibrary 爬虫

### 🌟 介绍

🎥 `Javlibrary 爬虫` 是一个利用 `Scrapy` 框架创建的项目，目的是从 [JavLibrary](https://www.javlibrary.com/)
网站中抓取日本成人视频的资料。从这个项目里，你可以获得如演员信息、作品详细、评分、评论数、导演、制片商和标签等数据。

### 🗄️ 数据库结构

[数据库示意图](https://dbdiagram.io/)

```
Table movies {
  id integer [primary key, increment]
  serial_number varchar(255) [unique]
  title text
  actor_id text
  release_date date
  comments integer
  reviews integer
  preview text
  link text
  maker varchar(255)
  length integer
  director varchar(255)
  label varchar(255)
  user_rating float
  genres text
  cast text
  magnet_link text
  online_missav text
}
Table actors{
  actor_id text
  actor_name text
}
Ref: movies.actor_id > actors.actor_id
Ref: movies.cast > actors.actor_name
```

### 🛠️ 使用方法

🔧 确保你已安装必要的依赖，例如 `Scrapy` 和 `pymysql`。
🌐 使用科学上网，面对403错误时可以尝试切换到韩国或台湾的代理节点。
❌ 请不在 GitHub Actions 中设置任务，因为 JavLibrary 有封锁 GitHub IP 的措施。
🌹 在项目根目录，新建一个`python`环境

```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

如果你使用的是pycharm，别忘记修改python的解释器为本地的env。

✏️ 修改 `config.arguments` 文件，按需配置。
- 填入想要爬取的演员 ID。例如 `https://www.javlibrary.com/cn/vl_star.php?list&mode=&s=ae5q6&page=1` 的 `ae5q6`。
- `reference` 提供了演员数据的 json 格式供参考。
- 通过 `magnet_file = [2, 10]` 来调整磁力链的大小区间。
📂 根据需要选择数据库类型并修改 `javlibrary_crawer.settings.ITEM_PIPELINES` 以及相关的数据库配置。

执行下列命令：

```
python main.py
```

然后是 FastApi 的部分：

```
cd api
python fast.py
```

🎉 爬取的数据会储存到你配置的数据库中！

### ⚠️ 注意事项

🚫 确保你有合法权利访问目标网站。
🐢 过于频繁的爬取可能导致 IP 被封，建议在 `settings.py` 中适当设置延迟。
📜 遵守网站的 `robots.txt` 及相关法律法规。

### 🤝 贡献

🙌 欢迎你的提问和合作，一起让这个项目变得更好！

### 📜 许可证

这个项目采用 MIT 许可证。详情请查看 [LICENSE](LICENSE) 文件。

---

希望这篇 README 可以帮到你！如有任何问题或建议，都可以告诉我哦！🙋‍♂️

### 📖 参考文献

Torrent

[https://onejav.com/](https://onejav.com/)

### 🌠 星级历史

[![Star History Chart](https://api.star-history.com/svg?repos=desonglll/javlibrary_crawler&type=Date)](https://star-history.com/#desonglll/javlibrary_crawler&Date)
