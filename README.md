# Welcome to My First Scraper project

#Description
This Python script scrapes the GitHub trending repositories page (https://github.com/trending), extracts relevant information for each repository (developer name, repository name, and number of stars), and saves it to a CSV file (github_trends.csv).

#Installation
Clone the repository:
git clone <repository-url>
cd <repository-name>
Install dependencies:
pip install requests beautifulsoup4

#Usage
Run the script:
Ensure Python is installed on your system. 
Navigate to the directory where the script is saved and execute the following command:
python github_trending_scraper.py
Output:
The script will fetch the GitHub trending page, extract data, transform it into a structured format, and save it to github_trends.csv in the current directory.
The CSV file will contain columns: "Developer Name", "Repository Name", and "Number of Stars", with each row corresponding to a trending repository on GitHub.
Notes
Dependencies: The script requires requests and beautifulsoup4 libraries, which can be installed via pip.
File Handling: The script uses basic file handling with open() and close() to write data to github_trends.csv. Ensure the script has write permissions in the directory where it is executed.
Error Handling: Error handling is minimal in this version. Ensure network connectivity and the stability of the GitHub trending page structure to avoid potential issues.