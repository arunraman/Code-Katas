import json



def compareJsons():
    a = json.loads("""
    {
        "errors": [
            {"error": "invalid", "field": "email"},
            {"error": "required", "field": "name"}
        ],
        "success": false
    }
    """)

    b = json.loads("""
    {
        "success": false,
        "errors": [
            {"error": "required", "field": "name"},
            {"error": "invalid", "field": "email"}
        ]
    }
    """)
    if ordered(a) == ordered(b):
        return True
    else:
        return False

def ordered(obj):
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj

print compareJsons()