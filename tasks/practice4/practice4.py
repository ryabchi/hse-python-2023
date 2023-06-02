from typing import Any, Optional


def search_phone(content: Any, name: str) -> Optional[str]:

    if isinstance(content, dict):
        if "name" in content and content["name"] == name:
            return content["phone"]
        else:
            for elem in content.values():
                result=search_phone(elem, name)
                if result is not None:
                    return result

    elif isinstance(content, list):
        for elem in content:
            result = search_phone(elem, name)
            if result is not None:
                return result
   
    return None
