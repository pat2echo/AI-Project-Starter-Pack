import os
import shutil
from datetime import datetime
import re
import subprocess

try:
  from google.colab import userdata
  from google.colab import drive
except Exception as e:
      print("You are not using Google Colab. You must specify values for\n1. GIT_USER (leave blank if using github)\n2. GIT_ACCESS_TOKEN\n3. GIT_REPO_URL")

GIT_USER = ''
GIT_ACCESS_TOKEN = ''
GIT_REPO_URL = ''

class GitClone:
    def __init__(self, mount_google_drive=True, vc_repo='', vc_user='', vc_token=''):
        self.vc_repo = vc_repo
        self.vc_user = vc_user
        self.vc_token = vc_token
        self.content_dir = 'content'
        self.base_dir = f'/{self.content_dir}/'
        self.no_error = True

        self.url, self.dirname, self.user_email, self.user_name = self.get_repo_data(vc_repo, vc_user, vc_token)
        
        if self.no_error and mount_google_drive:
          self.base_dir = self.mount_gdrive(self.base_dir)

        if self.no_error:
          self.clone_repo(self.url, self.dirname, self.base_dir)
          
        if self.no_error:
          self.branch_name = self.get_git_branch_name()

    def mount_gdrive(self, base_dir):
      """Mount google drive, git repo will be cloned into google drive

      Parameters:
        base_dir (str): Base/Root Directory Path. E.g In google colab its usually /content/

      Returns:
        str: Base/Root Directory
      """
      error = ''
      mount_path = f'/{self.content_dir}/drive'
      if os.path.exists(mount_path):
        print(f"Google Drive seems to be mounted at {mount_path}")
      else:
        try:
          drive.mount(mount_path)
        except Exception as e:
          error = f"An error occurred when mounting google drive: {e}\nYou can disable this option by setting GitClone(mount_google_drive=False)"

      if error == '':
        if os.path.exists(f'{mount_path}/MyDrive'):
          base_dir = f'{mount_path}/MyDrive'
        else:
          error = "Google Drive mount failed!"

      if error: print(error)

      return base_dir
    
    def is_valid_email(self, email):
        """Regular expression pattern for validating email addresses
        
        Parameters:
          email (str): Email Address

        Returns:
          bool: True if email is valid
        """
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        if re.match(pattern, email):
            return True
        else:
            return False

    def get_repo_data(self, vc_repo='', vc_user='', vc_token=''):
      """Validate and return connection details to the remote git repository

      Parameters:
        vc_repo (str): URL of remote git repository
        vc_user (str): Token Name (Gitlab), if using Github leave this blank
        vc_token (str): Personal Access Token (PAT) to git repository

      Returns:
        set: Set of (Git URL with Auth. Credentials, Directory Name after cloning the repository, Git Email Address, Git Username)
      """
      error = ''
      url = ''
      dirname = ''
      user_email = ''
      user_name = ''

      try:
          user_email = userdata.get('email')
      except Exception as e:
          error = f"An error occurred: {e}"
          print(error, "You can also define this value as a secret")
          user_email = input("Tell us your git email address: ")
          if self.is_valid_email(user_email):
            error = ''
          else:
            error += f"\nEmail address provided is invalid: {user_email}"

      # if error == '': 
      #   try:
      #       user_email = userdata.get('username')
      #   except Exception as e:
      #       error = f"An error occurred: {e}"
      #       print(error, "You can also define this value as a secret")
      #       user_name = input("Tell us your git username: ")
      #       if user_name != '':
      #         error = ''
      #       else:
      #         error += f"\nUsername provided is invalid: {user_name}"

      if error == '':
        if vc_repo == '':
          try:
            vc_repo = userdata.get('url')
          except Exception as e:
            error = f"An error occurred: {e}"

      if error == '':
        if vc_token == '':
          try:
            vc_user = userdata.get('token_name')
            vc_token = userdata.get('token')
          except Exception as e:
            error = f"An error occurred: {e}"
            error += "\n\nIf you are using Google Colab:"
            error += "\n1. Simply ensure that this line works: from google.colab import userdata"
            error += "\n2. Ensure that you have defined your secrets in colab. More Info on secrets required: https://github.com/pat2echo/AI-Project-Starter-Pack/blob/main/docs/how%20to%20setup%20secrets.md"
            error += "\n\nAlternatively, you can pass parameters [vc_repo, vc_user, vc_token] directly to the function"

      if error == '':
        if vc_repo.startswith("http") and vc_repo.endswith(".git"):
          repo_part = vc_repo.split('://')
          url = f'{repo_part[0]}://{vc_user}:{vc_token}@{repo_part[1]}'
          if vc_user != '':
            url = f'{repo_part[0]}://{vc_user}:{vc_token}@{repo_part[1]}'
          else:
            url = f'{repo_part[0]}://{vc_token}@{repo_part[1]}'

          repo_part = vc_repo.split('/')
          dirname = repo_part[-1].replace('.git','')
        else:
          error = f"Invalid repo url {vc_repo}, url must start with [http://...] or [https://...] and end with [.git]"

      if error:
        print(error)
        self.no_error = False

      return url, dirname, user_email, user_name


    def clone_repo(self, url, dir, base_dir):
      """Clone git repository and display contents of the newly cloned repo

      Parameters:
        url (str): Git URL with Auth. Credentials
        dir (str): Directory Name after cloning the repository
        base_dir (str): Base/Root Directory Path. E.g In google colab its usually /content/

      Returns:
        none: Returns Nothing
      """
      error = ''
      user_dir = base_dir
      if url.startswith("http") and url.endswith(".git"):
        if os.path.exists(user_dir):
            os.chdir(user_dir)
            git_dir = os.path.join(user_dir,dir)
            if os.path.exists(git_dir):
              print(f"\033[91mIMPORTANT! Directory {git_dir} already exists\033[0m")
              confirm = input(f"The directory {git_dir} already exists.\nAre you sure you want to delete the directory '{git_dir}' and all its contents and re-clone it? (yes/no): ")
              if confirm.lower() == 'yes':
                  shutil.rmtree(git_dir)
              else:
                  error = f"User aborted the Clone Operation because the directory exists"
              
            if error == '':
              #!git clone {url}
              subprocess.run(["git", "clone", url])
            
            if os.path.exists(git_dir):
              os.chdir(dir)
              print('List files: ', os.listdir())
            else:
              error = f"Failed to Clone Repo: Directory {git_dir} does not exists"
              self.no_error = False
        else:
            error = f"Directory {user_dir} does not exists"
            self.no_error = False
      else:
        error = f"Invalid repo url, url must start with [http://...] or [https://...] and end with [.git]"
        self.no_error = False

      if error: print(error)
    
    def get_git_branch_name(self):
      """Run the git branch command and capture the output
      
      Returns:
        str: Name of current git branch
      """
      error = ''
      branch_name = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).decode().strip()
      ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
      branch_name = ansi_escape.sub('', branch_name)

      # branch_name = ''
      # try:
      #     branch_output = !git branch
      #     # Find the line with an asterisk (*) indicating the current branch
      #     for line in branch_output:
      #         if line.startswith('*'):
      #             # Extract the branch name (remove the asterisk)
      #             branch_name = line[1:].strip()
      #             # Regular expression pattern for ANSI escape codes
      #             ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
      #             branch_name = ansi_escape.sub('', branch_name)

      # except Exception as e:
      #     error = f"Error: Unable to get Git branch: {e}"

      if error: 
        print(error)
        self.no_error = False

      return branch_name

    def commit_and_push(self, commit_message=''):
      """Save (commit) and push changes to git repository

      Parameters:
        commit_message (str): Describe the changes that you have made

      Returns:
        none: Returns Nothing
      """
      #!git config --global user.email {self.user_email}
      subprocess.run(["git", "config", "--global", "user.email", self.user_email])

      #!git config --global user.name {self.user_email}
      subprocess.run(["git", "config", "--global", "user.name", self.user_name])

      #!git config --global user.name {self.user_name}
      #!git add . 
      subprocess.run(["git", "add", "."])

      commit_msg = input("Enter your commit message that describes the changes that you have made to the files: ")
      if commit_msg == '':
        commit_msg = f'Commit at {datetime.now()}'
      #!git commit -m "{commit_msg}"
      subprocess.run(["git", "commit", "-m", commit_msg])
      #!git remote set-url origin {self.url}
      subprocess.run(["git", "remote", "set-url", "origin", self.url])
      #!git push origin {self.branch_name}
      subprocess.run(["git", "push", "origin", self.branch_name])


