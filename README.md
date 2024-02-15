**Simple_python_app_ECL**


** This Python Flask application is designed to generate CPU load to demonstrate auto-scaling features of cloud environments. It includes a /stress endpoint that executes a CPU-intensive operation. **

**Prerequisites**

Python 3.6 or later
Flask

**Local Development Setup**

git clone <repository-url>
cd path-to-repository

**Virual env**

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


**Run the Application**:
flask run



**Packaging for AWS Elastic Beanstalk**
**Package Application**: 
Zip the application files (application.py, requirements.txt) excluding the virtual environment directory.

**Upload to S3**:
 Upload the zip file to an AWS S3 bucket.

**Deploy on Elastic Beanstalk**:
 Use the AWS Elastic Beanstalk Console or the EB CLI to create a new application version with the uploaded zip file and deploy it.