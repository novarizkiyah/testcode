from pathlib import Path
import json

path = Path("number.json")
contents = path.read_text()
numbers = json.loads(contents)

print(f"I know your favorite number! It's {numbers}")