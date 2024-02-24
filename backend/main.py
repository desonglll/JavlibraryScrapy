# -*- coding: utf-8 -*-
"""
File: main
Description: 
Author: mikeshinoda
Date: 2024/2/18
"""
from typing import List

# TODO: Add your code here
# FINISH: Add your code here
# FIXME: Add your code here
# main.py

from fastapi import FastAPI, Query, Path
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from db_operations import fetch_data_from_db, get_works_table_count
from models import Work, Cast

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 定义路由
@app.get("/api/works_table_count")
def get_works_table_count_route():
    # 获取 works_table 的条目数
    count = get_works_table_count()
    return {"works_table_count": count}


@app.get("/api/works", response_model=List[Work])
def get_works(page: int = Query(default=1, ge=1), per_page: int = Query(default=10, ge=1, le=102),
              cast_id: str = Query(default="%"), cast: str = Query(default="%")):
    # 计算起始索引
    start_index = (page - 1) * per_page

    # 使用参数化查询构建 SQL 查询字符串
    query = "SELECT * FROM works_table WHERE genres LIKE %s AND cast_id LIKE %s AND cast LIKE %s AND genres NOT LIKE %s ORDER BY release_date DESC, serial_number DESC LIMIT %s, %s"
    genre_like = '%单体%'
    genre_not_like = '%VR%'
    works_data = fetch_data_from_db(query, (genre_like, cast_id, cast, genre_not_like, start_index, per_page))
    return works_data


@app.get("/api/works/{id}", response_model=Work)
def get_work(id: int = Path(..., title="The ID of the work")):
    query = "SELECT * FROM works_table WHERE id = %s"
    work_data = fetch_data_from_db(query, (id,))
    if work_data:
        return work_data[0]  # 返回查询到的第一条数据
    else:
        return {"error": "Work not found"}  # 如果未找到作品，返回错误信息


@app.get("/api/actors", response_model=List[Cast])
def get_actors():
    query = """SELECT
    DISTINCT cast_id,
    SUBSTRING_INDEX(cast, ' ', 1) AS cast
FROM
    works_table
WHERE
    LENGTH(cast) - LENGTH(REPLACE(cast, ' ', '')) = 0;
"""
    actors_data = fetch_data_from_db(query)
    return actors_data


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
