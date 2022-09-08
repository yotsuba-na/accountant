#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Literal

from fastapi import FastAPI


app = FastAPI()


@app.get('/', response_model=Literal['OK'])
def index():
  return 'OK'


if __name__ == '__main__':
  import uvicorn

  uvicorn.run("main:app", host="localhost", port=8080, log_level="info")
