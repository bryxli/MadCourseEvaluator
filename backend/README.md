# MadCourseEvaluator Back End Web API

The back end web API for our MadCourseEvaluator application is built using Python3 and Flask. The API is hosted on AWS EC2 and is accessible at [http://3.145.22.97/](http://3.145.22.97/), the front end React application is hosted with Netlify and is accessible at [https://madgers.netlify.app/](https://madgers.netlify.app/).

## Running the API Locally

### 1. Create a python virtual environment, activate it, then install the dependencies.

Make sure you have python3 and pip3 installed on your machine before running the following commands.

If you do not have virtualenv installed, run `pip3 install virtualenv` in your terminal before running the following commands.

```bash
python3 -m venv venv             # create a virtual environment
source venv/bin/activate         # activate the virtual environment
pip3 install -r requirements.txt # install all dependencies
```

### 2. Run the API

```bash
flask run
```