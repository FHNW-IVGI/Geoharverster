import re
from typing import Union

import geopandas as gpd
from fastapi import APIRouter

router = APIRouter()

@router.get("/getData")
async def getData(query: Union[str, None] = None):
    payload = re.split(r',|!|;', str(query))

    print(payload)
    return {"data": payload}
