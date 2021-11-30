# BioPlatform

## version 2.0.1

- 更新时间：11.17，主要涉及文件：SQL_Todo.py,  main.py

- 数据库相关论文查询api更改，由 **/papers?dbname=**更改为**/papers/db?name=**

- 新增论文搜索API: **/papers/search?wd=**

  - 暂提供MySQL数据库端的模糊查询
  - 不支持搜索空内容，空内容会返回404
  - 搜索速度较慢

- 删除论文查询结果中的Affiliations

  

