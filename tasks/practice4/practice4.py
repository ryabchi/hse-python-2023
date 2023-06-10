from typing import Any, Optional


def search_phone(content: Any, name: str) -> Optional[str]:
    if isinstance(content, dict):
        if 'name' in content and content['name'] == name and 'phone' in content:
            return content['phone']
        for _, value in content.items():
            result = search_phone(value, name)
            if result:
                return result
    elif isinstance(content, list):
        for item in content:
            result = search_phone(item, name)
            if result:
                return result

    return None
