import subprocess

def git_operations():
    try:
        # Step 1: Stage all changes
        print("Staging all changes...")
        subprocess.run(["git", "add", "."], check=True)

        # Step 2: Commit the changes with a message
        print("Committing changes...")
        commit_message = "Update scraped data and code"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        # Step 3: Push the changes to the remote repository
        print("Pushing changes to remote...")
        subprocess.run(["git", "push"], check=True)

        print("Git operations completed successfully.")

    except subprocess.CalledProcessError as e:
        print(f"Error during Git operations: {e}")
        print("Make sure your repository is properly initialized and connected to a remote.")

if __name__ == "__main__":
    git_operations()
