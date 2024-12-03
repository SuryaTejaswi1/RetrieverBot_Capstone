
import subprocess

def git_operations():
            try:
                # Stage the CSV files
                subprocess.run([
                    "git", "add",
                    "dil_scraped_data.csv",
                    "isss_scraped_data.csv",
                    "research_data.csv",
                ], check=True)

                # Force add scraping_log.log
                subprocess.run(["git", "add", "-f", "scraping_log.log"], check=True)

                # Commit the changes
                subprocess.run(["git", "commit", "-m", "Update scraped data files"], check=True)

                # Push to the remote repository
                subprocess.run(["git", "push"], check=True)

                print("CSV files pushed to Git successfully.")
            except subprocess.CalledProcessError as e:
                print(f"Error during Git push: {e}")


if __name__ == "__main__":
    git_operations()
