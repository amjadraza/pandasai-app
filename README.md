<h1 align="center">
📖PANDASAI APP
</h1>

An App to interact with Pandas Dataframes using Generative AI (LLMs). This app is built using `streamlit`
as front end and using [`pandasai`](https://github.com/gventuri/pandas-ai) a higher level python wrapper to make dataframes conversational.

`pandasai` made available `openai`, `HuggingFace` and `Azure` APIs for Generative AI capabilities. 
User can configure their choice of Platform for backend.  

## 🔧 Features

- Upload csv 📁(csv) and ask questions about the uploaded Data.
- Ask Questions about the data
- Interact with your data like a Human

## 💻 Running Locally

1. Clone the repository📂

```bash
git clone https://github.com/amjadraza/pandasai-app.git
```

2. Install dependencies with [Poetry](https://python-poetry.org/) and activate virtual environment🔨

```bash
poetry install
poetry shell
```

3. Run the Streamlit server🚀

```bash
cd pandasai_app
streamlit run main.py 
```

Run App using Docker
--------------------
This project includes `Dockerfile` to run the app in Docker container.

Build the docker container

``docker  build -t pandasai-app .``

1. Run the docker container directly 

``docker run -d --name pai_app -p 8501:8501 pandasai-app``

2. Run the docker container using docker-compose (Recommended)

``docker-compose up``

## 🚀 Upcoming Features

- [ ] Add support for more models (e.g.HuggingFace, Azure.).
- [ ] Adding Functionality of Plotting.
- [ ] Some Generic insights on Uploaded Data (e.g Shape, head etc)
- [x] Adding Docker Support to run the App in Docker
- [ ] Deploying App on Google App Engine

## Report Feedbacks

As `pandasai` is in active developments as well as LLMs sometime go south. 
Please report your feedbacks for improvements. 

## DISCLAIMER

The Pandasai app (hereinafter referred to as "the App") is provided for informational purposes only. 
The creators and authors of the App make no representations or warranties of any kind, 
express or implied, about the completeness, accuracy, reliability, suitability, 
or availability of the App or the information, products, services, 
r related graphics contained in the App.

We do not store any of data or API keys. Users can refresh Keys as part of Best Practices.

This disclaimer is subject to change without notice. It is your responsibility to review this disclaimer periodically 
for any updates or changes.