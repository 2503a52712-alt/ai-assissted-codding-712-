def suggest_commit_message(changes):
    changes = changes.lower()

    if "validation" in changes and "task" in changes:
        return "Add validation for task entries"
    if "complete" in changes and "task" in changes:
        return "Add task completion feature"
    if "calculator" in changes and "history" in changes:
        return "Add calculation history"
    if "bug" in changes or "fix" in changes:
        return "Fix program logic"

    return "Update application features"

change_description = input("Describe your code changes: ")
print("Suggested commit message:", suggest_commit_message(change_description))