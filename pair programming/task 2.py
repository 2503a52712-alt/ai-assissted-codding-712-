import subprocess

def run_git(*arguments):
    subprocess.run(["git", *arguments], check=True)

# Initialize the repository and create the main branch
run_git("init")
run_git("branch", "-M", "main")

# Create and switch to a feature branch
run_git("switch", "-c", "add-todo-features")

# After adding your AI-assisted code, stage and commit it
run_git("add", ".")
run_git("commit", "-m", "Add task validation and completion")

# Switch back to main and merge the feature branch
run_git("switch", "main")
run_git("merge", "add-todo-features")