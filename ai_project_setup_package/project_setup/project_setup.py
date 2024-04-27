import os

class ProjectSetup:
    def __init__(self, title, base_path=""):
        self.base_path = base_path
        self.title = title
        self.directory = ""
        self.clean_title = ""
        self.default_modules = {
            '__init__.py': None,  # Initializes the Python package
            'data': {
                '__init__.py': None,
                'loader.py': None,  # Data loading functionality
                'preprocess.py': None  # Data cleaning and preprocessing
            },
            'features': {
                '__init__.py': None,
                'builder.py': None  # Build and transform features
            },
            'ml_models': {
                '__init__.py': None,
                'train_model.py': None,  # Training scripts
                'predict_model.py': None  # Prediction scripts
            },
            'nn_models': {
                '__init__.py': None,
                'train_model.py': None,  # Training scripts
                'predict_model.py': None  # Prediction scripts
            },
            'utils': {
                '__init__.py': None,
                'helpers.py': None  # Helper functions
            },
            'visualization': {
                '__init__.py': None,
                'visualize.py': None  # Plotting and visualization functions
            }
        }

        self.default_directories = {
          "notebooks": {
              "exploratory_analysis.ipynb": None,
              "features_engineering.ipynb": None,
              "model_training.ipynb": None,
              "model_evaluation.ipynb": None,
              "explainable_ai.ipynb": None
          },
          "backup_notebooks": {},
          "tests": {
              "__init__.py": None,
              "test_data.py": None,
              "test_features.py": None,
              "test_models.py": None
          },
          "setup.py": None,
          "requirements.txt": None,
          "README.md": None
      }
    
    def clean_string(self, string):
        """Replace spaces with underscores in strings
        
        Parameters:
          string (str): String to be cleaned

        Returns:
          str: Lowercase cleaned string
        """
        return string.lower().strip().replace(" ", "_")

    def create_directory_and_files(self, path, structure):
        """Recursively creates directory and sub-directories"""
        for name, content in structure.items():
            real_path = os.path.join(path, name)
            if isinstance(content, dict):  # It's a directory
                self.ensure_directory_exists(real_path)
                self.create_directory_and_files(real_path, content)  # Recursively create contents
            else:  # It's assumed to be a file
                self.ensure_file_exists(real_path)

    def ensure_directory_exists(self, path):
      """Ensure that a directory exists; if it doesn't, create it."""
      if not os.path.exists(path):
          os.makedirs(path)
          print(f"Created directory: {path}")
      else:
          print(f"Directory already exists: {path}")

    def ensure_file_exists(self, path):
        """Ensure that a file exists; if it doesn't, create it as empty."""
        if not os.path.exists(path):
            open(path, 'a').close()  # Create an empty file
            print(f"Created file: {path}")
        else:
            print(f"File already exists: {path}")
    

    def new_project(self, project_directories={}):
        """Creates a project directory and sub-directories"""
        
        self.clean_title = self.clean_string(self.title)
        real_path = os.path.join(self.base_path, self.clean_title)

        directories = self.default_directories

        if project_directories != {}:
          directories = project_directories

        if "notebooks" in directories:
          directories["notebooks"][self.clean_title + ".ipynb"] = None

        self.ensure_directory_exists(real_path)
        self.directory = real_path

        self.create_directory_and_files(real_path, directories)

    def new_package(self, package_name, package_modules={}):
        """Generates all required directories and files for an AI project
        
        Parameters:
          package_name (str): Name of AI Project Package
          package_modules (dict): A dictionary containing sub-directories and files in the module. Keys should include:
            'directory1' (str): Name of sub-directory. If sub-directory then value is dictionary
            'file1' (str): Name of file. If file is None
            ... additional directories or files ...

        Returns:
          none: Returns Nothing
        """
        clean_package_name = self.clean_string(package_name)
        real_path = os.path.join(self.directory, clean_package_name)

        modules = self.default_modules

        if package_modules != {}:
          modules = package_modules
        
        self.ensure_directory_exists(real_path)
        self.create_directory_and_files(real_path, modules)
