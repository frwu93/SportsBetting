# SportsBetting

## Project Setup Guide

### 1️⃣ Setting Up a Virtual Environment (venv)

A virtual environment allows you to manage dependencies for your Python project in an isolated environment.

#### **Step 1: Create a Virtual Environment**

1. Open a terminal or command prompt (can do this in VSCode).
2. Navigate to your project directory:
   ```sh
   cd /path/to/your/project
   ```
3. Run the following command to create a virtual environment named `.venv`:
   ```sh
   python -m venv venv
   ```

#### **Step 2: Activate the Virtual Environment**
- **On Windows (Command Prompt)**:
  ```sh
  venv\Scripts\activate
  ```
- **On Windows (PowerShell)**:
  ```sh
  venv\Scripts\Activate.ps1
  ```
- **On macOS/Linux**:
  ```sh
  source venv/bin/activate
  ```

Once activated, your terminal should show a `(venv)` prefix.

#### **Step 3: Install Dependencies**
Install the required dependencies from the `requirements.txt` file:
```sh
pip install -r requirements.txt
```

### 2️⃣ Setting Up a Virtual Environment (venv)

The .env file stores environment variables like API keys and database credentials. We should not be sharing this in GitHub, but rather should each have our local version with our own API keys.

#### **Step 1: Create a Virtual Environment**

In terminal, in the project's root directory, create a new file named .env:
```sh
touch .env
```

#### **Step 2: Add Environment Variables**
Open .env in a VSCode and define your variables:
```sh
API_KEY=your_api_key_here
```
There is an .env.example file in the repository to show you what this looks like.

### 3️⃣ Test your NBA API Token

Run the `test_nba_api.py` file with the following command:
```sh
python test_nba_api.py
```
If that doesn't work, replace it with:
```sh
python3 test_nba_api.py
```

### 4️⃣ Create your own branch and start working
Follow naming conventions of `name/feature`. For example, `franklin/add_players`.

## Git Basics

## Cloning a Repository
If you haven't already cloned the repository, use the following command:
```sh
git clone <repository_url>
```
Example:
```sh
git clone https://github.com/yourusername/your-repository.git
```

## Pulling Changes from Remote Repository
To fetch the latest changes from the remote repository and merge them into your local branch:
```sh
git pull origin <branch_name>
```
Example:
```sh
git pull origin main
```

## Adding and Committing Changes
After making changes to your files, you need to add and commit them:
1. Stage the changes:
   ```sh
   git add .
   ```
2. Commit the changes with a message:
   ```sh
   git commit -m "Your commit message"
   ```

## Pushing Changes to Remote Repository
To push your committed changes to the remote repository:
```sh
git push origin <branch_name>
```
Example:
```sh
git push origin main
```

## Checking Status and Logs
- Check the current status of your repository:
  ```sh
  git status
  ```
- View commit history:
  ```sh
  git log --oneline
  ```

## Creating and Switching Branches
- Create a new branch:
  ```sh
  git branch <new_branch_name>
  ```
- Switch to the new branch:
  ```sh
  git checkout <new_branch_name>
  ```
- Alternatively, create and switch in one command:
  ```sh
  git checkout -b <new_branch_name>
  ```

## Merging Branches
To merge changes from another branch into the current branch:
```sh
git merge <branch_name>
```
Example:
```sh
git merge feature-branch
```

  




