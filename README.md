# AI Project Starter Pack
The AI Project Starter Pack is a meticulously structured directory and module framework designed for creating machine learning and data science projects. This starter pack aims to streamline the project setup process, helping data scientists and developers organize their code, data, and documentation efficiently. 

# Features
- **Project Structure Setup:** Quickly set up standardized project structures for AI projects.
- **Git Integration:** Seamlessly integrate with Git repositories for version control and collaboration.
- **Google Colab Integration:** Easily collaborate on projects using Google Colab notebooks.
- **Streamlined Workflow:** Simplify the process of building and managing collaborative AI projects.
- **Automation:** Automate repetitive tasks and streamline project management.
- **AI based Guidiance:** Provide guide & assistance on core AI concepts to engineers

# How it Works
## 1. Install the package  
   `pip install ai-project-setup`  

## 2. Create your new AI Project and Package (one-time operation)
```
import project_setup as ps

# Create an instance of a new AI ProjectSetup
proj = ps.ProjectSetup("ExampleProject", "./example")

# Create the project structure
proj.new_project()

# Optionally, add a specific package within the project
proj.new_package("example_package")
```

# Output: Project Directory Structure
```
Name_of_project/
│
├── name_of_package/          # Main package directory
│   ├── __init__.py         # Initializes the Python package
│   ├── data/               # Modules for data handling
│   │   ├── __init__.py
│   │   ├── loader.py       # Data loading functionality
│   │   └── preprocess.py   # Data cleaning and preprocessing
│   │
│   ├── features/           # Feature engineering
│   │   ├── __init__.py
│   │   └── builder.py      # Build and transform features
│   │
│   ├── ml_models/          # ML models
│   │   ├── __init__.py
│   │   ├── train_model.py  # Training scripts
│   │   └── predict_model.py# Prediction scripts
│   │
│   ├── utils/              # Utility functions
│   │   ├── __init__.py
│   │   └── helpers.py      # Helper functions
│   │
│   └── visualization/      # Visualization tools
│       ├── __init__.py
│       └── visualize.py   # Plotting and visualization functions
│
├── notebooks/              # Jupyter notebooks for specific activities
|   └── main.ipynb		   #Complete project
│   └── exploratory_analysis.ipynb
|   └── features_engineering.ipynb
|   └── model_training.ipynb
|   └── model_evaluation.ipynb
|   └── explainable_ai.ipynb
|
├── backup_notebooks/              # Auto copied from google drive
|   └── backup_main.ipynb  
|   …
|
├── tests/                  # Test suite
│   ├── __init__.py
│   ├── test_data.py
│   ├── test_features.py
│   └── test_models.py
│
├── setup.py                # Setup file for package installation
├── requirements.txt        # Dependencies
└── README.md               # Project overview
```

## 3. Coding in Google Colab
- [Get your git account tokens and setup your secrets in google colab](https://github.com/pat2echo/AI-Project-Starter-Pack/blob/main/docs/how%20to%20setup%20secrets.md)   
- Optionally, you can pass your credentials when initializing the class as shown below:
```
git = psgit.GitClone(vc_repo=GIT_REPO_URL, vc_user=GIT_USER, vc_token=GIT_ACCESS_TOKEN)
```

- Import Package and Clone Repo, by default your google drive will be mounted as a temporary working space to hold contents of the github repo
```
import git_clone as psgit
git = psgit.GitClone()
```

-- Optionally, if using branching strategy, although this is not advised. [You can checkout this article on continuous integration if you desire greater efficiency](https://medium.com/@pat2echo/dare-to-get-rapid-feedback-continuous-development-deployment-strategy-8516df6e9e26)
```
import git_clone as psgit
git = psgit.GitClone(branch_name=GIT_BRANCH_NAME)
```

- Write Your Code and Manage Files in Google Drive
- When writing your code you can easily access the directory path of your repo files, using:
```
print(git.git_dir)
%cd {git.git_dir}
%ls
```
- When done writing codes, commit your changes back to your repo
```
git.commit_and_push()
```

# Join our Exciting Open-Source AI Project!

We need diverse skills such as strategic planning, project management, coding, documentation, research, and more. Your expertise can make a real impact!

Send us a email to [ai@d1kit.com](mailto:ai@d1kit.com) 

Not ready to dive in? Support us by watching the repo and staying updated.

Thank you for your interest and support!
