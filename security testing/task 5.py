import json
from pathlib import Path


DATA_FILE = Path("user_data.json")


def save_user_data(data: dict) -> None:
    temporary_file = DATA_FILE.with_suffix(".tmp")

    with temporary_file.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)
        file.write("\n")

    temporary_file.replace(DATA_FILE)


def load_user_data() -> dict:
    if not DATA_FILE.exists():
        return {}

    with DATA_FILE.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, dict):
        raise ValueError("User data must be a JSON object.")

    return data


if __name__ == "__main__":
    sample_data = {
        "username": "asha",
        "preferences": {
            "theme": "light",
            "notifications": True
        }
    }

    save_user_data(sample_data)
    print("Saved user data.")

    loaded_data = load_user_data()
    print(json.dumps(loaded_data, indent=2))