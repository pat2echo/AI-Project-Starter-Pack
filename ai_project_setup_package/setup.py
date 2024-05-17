from setuptools import setup, find_packages

setup(
    name='ai_project_setup',
    version='0.2.6',
    packages=find_packages(),
    description='A versatile utility package designed to streamline the setup of AI project structures while seamlessly integrating with Git repositories and Google Colab, simplifying the process of building collaborative AI projects.',
    long_description="""# AI Project Starter Pack
The AI Project Starter Pack is a meticulously structured directory and module framework designed for creating machine learning and data science projects. This starter pack aims to streamline the project setup process, helping data scientists and developers organize their code, data, and documentation efficiently. 

## GITHUB: https://github.com/pat2echo/AI-Project-Starter-Pack/

## Features
- **Project Structure Setup**: Quickly set up standardized project structures for AI projects.
- **Git Integration**: Seamlessly integrate with Git repositories for version control and collaboration.
- **Google Colab Integration**: Easily collaborate on projects using Google Colab notebooks.
- **Streamlined Workflow**: Simplify the process of building and managing collaborative AI projects.
- **Automation**: Automate repetitive tasks and streamline project management.
""",
    long_description_content_type='text/markdown',
    author='Patrick Ogbuitepu',
    author_email='pat2echo@gmail.com',
    keywords=['AI', 'utility package', 'project structure', 'Git integration', 'Google Colab integration', 'collaborative projects', 'ease of use', 'streamlined workflow', 'automation', 'project management', 'project', 'setup', 'structure', 'ai', 'artificial intelligence', 'research', 'data science', 'machine learning'],
    install_requires=[
        # Any dependencies the package might have, e.g.,
        # 'numpy', 'pandas'
    ]
)
