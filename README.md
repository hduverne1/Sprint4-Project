# Car Advertisement Dashboard

## Project Description
This project is a web application dashboard that provides visualizations and analysis of car advertisement data. It is built using Streamlit, Pandas, and Plotly Express.

## Running the App Locally
1. Clone the repository:
git clone https://github.com/hduverne1/Sprint4-Project.git
2. Navigate to the project directory:
cd your-repo-name
3. Install the required packages:
pip install -r requirements.txt
4. Run the app:
streamlit run app.py

## Live Application
You can view the live application here: [US Vehicle Advertisement Listings](https://sprint4-project-ys66.onrender.com)

# Car Sales Dashboard

This project is a web application dashboard for visualizing car sales data. It is built using Streamlit, Pandas, and Plotly Express. The dashboard provides interactive visualizations to explore the dataset and gain insights into car sales trends.

## Features

- **Interactive Histogram**: Visualize the distribution of car prices.
- **Scatter Plot**: Explore the relationship between car price and odometer reading.
- **Filter Option**: Use a checkbox to filter and display cars with prices above $10,000.

## Technologies Used

- **Streamlit**: For building the web application.
- **Pandas**: For data manipulation and analysis.
- **Plotly Express**: For creating interactive visualizations.

## How to Run Locally

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/hduverne1/Sprint4-Project.git
   cd your-repo-name
Set Up a Virtual Environment:

python -m venv myenv
source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
Install Dependencies:

pip install -r requirements.txt
Run the Application:

streamlit run app.py
Open in Browser:

The application will open in your default web browser. If not, navigate to http://localhost:8501 in your browser.
Contributing
Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

License
This project is licensed under the MIT License - see the LICENSE file for details.


### Final Steps

1. **Test Locally:**
   - Run your application locally using the command:
     ```bash
     streamlit run app.py
     ```
   - Ensure everything works as expected and make any necessary adjustments.

2. **Commit and Push Changes:**

Open your terminal and navigate to your project directory.
Stage all your changes:
git add .
Commit Your Changes:

Commit your changes with a meaningful message:
git commit -m "Add Streamlit dashboard with EDA visualizations"
Push to GitHub:

Push your changes to your GitHub repository:

git push origin main
Replace main with the name of your branch if you're using a different branch.

Verify on GitHub

Go to your GitHub repository and verify that all your files, including app.py, EDA.ipynb, and README.md, are present and updated.

Prepare for Deployment on Render
Since your project files are now on GitHub, you can proceed to deploy your application on Render. Make sure your repository is linked to your Render account, and follow Render's instructions to deploy a Streamlit application.

Additional Tips

Requirements File: Ensure you have a requirements.txt file listing all the Python packages your project depends on. You can generate this file with:

pip freeze > requirements.txt
Continuous Testing: As you develop your application, continue testing locally with streamlit run app.py to ensure everything functions correctly before pushing changes.

Iterate and Improve: Use feedback from your project reviewer to make improvements. It's common to go through several iterations, so don't hesitate to refine your application based on feedback.