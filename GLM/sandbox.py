import json
import pandas as pd
import orjson
from rapidjson import dumps, loads
import numpy as np
from datetime import date, datetime

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, pd.DataFrame):
            return obj.to_json()
        if isinstance(obj, pd.Series):
            return obj.to_json()
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, (datetime, date)):
            return obj.isoformat()
        else:
            return json.JSONEncoder.default(self, obj)


df = pd.DataFrame([[1],[3]], columns=['a'])

q = {'c': 1, 'd': df}

qs = json.dumps(q,cls=CustomEncoder)
q2 = json.dumps(df,cls=CustomEncoder)

print('hej')

