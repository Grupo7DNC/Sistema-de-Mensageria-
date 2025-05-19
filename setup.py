from setuptools import setup, find_packages

setup(
    name="airflow_custom_modules",
    version="1.0.0",
    description="Módulos customizados para Airflow",
    packages=find_packages(where="plugins"),  # Procura pacotes na pasta plugins
    package_dir={"": "plugins"},             # Define plugins/ como raiz
    install_requires=[
        "pymongo>=4.6.2",
        "pandas>=2.0.3",
        "apache-airflow-providers-mongo>=3.0.0"
    ],
    python_requires=">=3.8",
)