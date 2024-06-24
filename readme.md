# Phishing Email Generator

This project is a Python-based tool for generating convincing phishing email templates using OpenAI's GPT (Generative Pre-trained Transformer) models. The tool aims to create realistic phishing emails that can be used for educational purposes, security testing, or awareness campaigns.

## Installation

To install and set up the project, follow these steps:

1. Navigate to the project directory:

cd phishing_simulation_tool


2. Run the installation batch file:

install.bat


This batch file will install the required Python packages specified in `requirements.txt`.

## Usage

After the installation, you can use the tool to generate phishing emails. Follow these steps:

1. Run the run batch file:
run.bat
![genphish](https://github.com/Faluyi/Phish-Gpt/assets/83612442/f2860236-9cee-478f-b8c6-4943f76e688e)

## Local Configuration

You can customize various parameters of the phishing email generation process, such as the target name, malicious link, and company name. These parameters can be adjusted directly in the `email_generator.py` script.

To add more target mail addresses and names, navigate to ./src/data. Open the csv file named "email_addresses.csv" and input the email address and name in the appropriate column. Finally, save and close the file.

## Web application configuration
For every email address and name added locally, there is a need to add them to the csv file in web application project folder.
To do this, navigate to https://genphish.onrender.com/admin, input the email address and name in the appropriate input fields and submit.
To download the csv file for reporting purposes, navigate to https://genphish.onrender.com/admin/download_csv, this will automatically download the csv fie upon navigation.
The csv file has four columns: the email address, the name, the last_clicked datetime, and the no of clicks.


## Contributing

Contributions are welcome! If you'd like to contribute to the project, feel free to open an issue or submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

