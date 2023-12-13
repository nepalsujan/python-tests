import subprocess
import sys

def git_add_commit_push(commit_message):
    try:
        # Git add all changes
        subprocess.run(["git", "add", "."], check=True)

        # Git commit with the provided message
        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        # Git push to the current branch
        subprocess.run(["git", "push", "origin", subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"]).decode().strip()], check=True)

        print("Git add, commit, and push successful!")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py 'Commit Message'")
        sys.exit(1)

    commit_message = sys.argv[1]
    git_add_commit_push(commit_message)
