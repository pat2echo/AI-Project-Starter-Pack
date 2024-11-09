# How to Set-up Secrets (Git and Google Colab Setup Guide)

## Table of Contents
- [Part 1: Creating a GitHub Account and Token](#part-1-creating-a-github-account-and-token)
- [Part 2: Creating a GitLab Account and Token](#part-2-creating-a-gitlab-account-and-token)
- [Part 3: Setting Up Google Colab Secrets](#part-3-setting-up-google-colab-secrets)
- [Safety Tips](#safety-tips)

## Part 1: Creating a GitHub Account and Token

### 1. Create GitHub Account
- Go to github.com
- Click "Sign Up"
- Enter your email address
- Create a password
- Choose a username
- Verify your email address

### 2. Get Your GitHub Token
- Click your profile picture (top right)
- Click "Settings"
- Scroll to "Developer settings" (bottom of left menu)
- Click "Personal access tokens" then "Tokens (classic)"
- Click "Generate new token"
- Give your token a name like "AI_Project"
- Select scopes: check "repo" and "workflow"
- Click "Generate token"
- IMPORTANT: Copy and save your token immediately. You won't see it again!

## Part 2: Creating a GitLab Account and Token

### 1. Create GitLab Account
- Go to gitlab.com
- Click "Register now"
- Fill in your details
- Verify your email

### 2. Get Your GitLab Token
- Click your profile picture
- Click "Preferences"
- Click "Access Tokens" (left menu)
- Give your token a name
- Select scopes: check "api", "read_repository", "write_repository"
- Click "Create personal access token"
- IMPORTANT: Copy and save your token immediately

## Part 3: Setting Up Google Colab Secrets

### 1. Open Google Colab
- Go to colab.research.google.com
- Sign in with your Google account

### 2. Store Your Git Secrets
Add this code to a new cell:

```python
from google.colab import userdata

# For GitHub
userdata.set('GITHUB_TOKEN', 'your-github-token-here')
userdata.set('GITHUB_USERNAME', 'your-github-username')
userdata.set('GITHUB_EMAIL', 'your-github-email')

# For GitLab
userdata.set('GITLAB_TOKEN', 'your-gitlab-token-here')
userdata.set('GITLAB_USERNAME', 'your-gitlab-username')
userdata.set('GITLAB_EMAIL', 'your-gitlab-email')
```

### 3. Test Your Secrets
Add this code to a new cell:

```python
from google.colab import userdata

# Test GitHub
print("GitHub Username:", userdata.get('GITHUB_USERNAME'))
print("GitHub Email:", userdata.get('GITHUB_EMAIL'))
print("GitHub Token exists:", bool(userdata.get('GITHUB_TOKEN')))

# Test GitLab
print("GitLab Username:", userdata.get('GITLAB_USERNAME'))
print("GitLab Email:", userdata.get('GITLAB_EMAIL'))
print("GitLab Token exists:", bool(userdata.get('GITLAB_TOKEN')))
```

## Safety Tips
1. Never share your tokens with anyone
2. Never put tokens directly in your code
3. If you accidentally expose a token, delete it immediately and create a new one
4. Store tokens securely - consider using a password manager

Remember: Your Google Colab secrets are tied to your Google account and will persist across sessions, but you may need to remount your Google Drive each time you start a new session.
