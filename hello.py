def greet(name: str) -> str:
    """返回一句问候语。"""
    return f"Hello, {name}!"


def farewell(name: str) -> str:
    """返回一句告别语。"""
    return f"Goodbye, {name}!"


if __name__ == "__main__":
    print(greet("Open Source"))
    print(farewell("Open Source"))