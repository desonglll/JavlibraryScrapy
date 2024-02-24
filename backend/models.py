# -*- coding: utf-8 -*-
"""
File: models
Description: 
Author: mikeshinoda
Date: 2024/2/18
"""

# TODO: Add your code here
# FINISH: Add your code here
# FIXME: Add your code here
# models.py

from pydantic import BaseModel
from typing import List, Optional


class Cast(BaseModel):
    cast_id: Optional[str]
    cast: Optional[str]

    class Config:
        from_attributes = True


class Work(BaseModel):
    id: Optional[int]
    link: Optional[str]
    preview: Optional[str]
    title: Optional[str]
    serial_number: str
    release_date: Optional[str]
    length: Optional[str]
    director: Optional[str]
    maker: Optional[str]
    label: Optional[str]
    user_rating: Optional[str]
    genres: Optional[str]
    cast: Optional[str]
    cast_id: Optional[str]
    subscribed: Optional[str]
    watched: Optional[str]
    owned: Optional[str]
    preview_thumbs: Optional[str]

    class Config:
        from_attributes = True


class DateRange(BaseModel):
    start_date: str
    end_date: str


class ActorIDFilter(BaseModel):
    actor_ids: List[str]
