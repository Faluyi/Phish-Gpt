import csv
from flask import Flask, request, render_template, send_from_directory
from datetime import datetime
import os 

app = Flask(__name__)
current_directory = os.path.dirname(os.path.abspath(__file__))
csv_directory = os.path.join(current_directory, 'data')

# Path to the CSV file
csv_file = './data/victim_details.csv'  # Replace with the path to your CSV file

@app.get('/')
def index():
    # Fetch the 'id' parameter from the URL (email address)
    email_address = request.args.get('id')
    print(email_address)

    # Search for the email address in the CSV file
    with open(csv_file, 'r', newline='') as file:
        reader = list(csv.reader(file))
        print(list(reader))
        del reader[0]
        for row in reader:
            print(row[0])
            if row[0] == email_address:  # Assuming email_address is in the first column
                name = row[1]  # Assuming name is in the second column
                print(name)               
                last_datetime_clicked = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                no_of_times_clicked = int(row[3]) + 1  # Assuming no_of_times_clicked is in the fourth column

                # Update the row with the new values
                row[2] = last_datetime_clicked  # Assuming last datetime clicked is in the third column
                row[3] = no_of_times_clicked

                # Write the updated data back to the CSV file
                with open(csv_file, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(['email_address', 'name', 'last_datetime_clicked', 'no_of_times_clicked'])  # Write the header row
                    writer.writerows(reader)

                # Render an HTML page with the victim's name and other details
                return render_template('index.html', name=name )

    # If the email address is not found in the CSV file
    return "Email address not found."


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    
    if request.method == 'POST':
        # Get data from the form
        email = request.form['email']
        name = request.form['name']
        

        # Append the new data to the CSV file
        with open(csv_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([email, name, 0, 0])
        return render_template('form.html')

    # Render the HTML template with the form
    return render_template('form.html')

@app.route('/admin/download_csv')
def download_csv():
    # Serve the CSV file
    return send_from_directory(directory=csv_directory, path='victim_details.csv', as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
