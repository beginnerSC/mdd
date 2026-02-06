# Minimal Dash Dashboard

A simple Plotly Dash dashboard ready for Docker deployment on Render [here](https://mdd-xql8.onrender.com/).

## Local Development

### Install dependencies
```bash
poetry install
```

### Run locally
```bash
poetry run python -m mdd.app
```

Visit `http://localhost:8050` in your browser.

## Docker Deployment

### One-Time Setup 

* Download and install [Docker Desktop for Windows](https://docs.docker.com/desktop/setup/install/windows-install/) with default settings, and reboot
* Verify installation:
```bash
docker --version
docker run hello-world
```
* Change image location to D drive: In the UI click Settings > Resources > Disk image location


### Build the Docker image locally
```bash
docker build -t dash-app .
```

### Run locally in Docker
```bash
docker run -p 8050:8050 dash-app
```

Visit `http://localhost:8050` to verify.

## Deploy to Render

1. **Push to GitHub** - Commit and push this repository to GitHub
2. **Create Render service**:
   - Go to [Render Dashboard](https://dashboard.render.com)
   - Click "New +" > "Web Service"
   - Connect your GitHub repository
   - Select this repo
3. **Configure**:
   - Name: `dash-dashboard` (or your choice)
   - Environment: Docker
   - Region: Choose closest to you
   - Plan: Free tier
4. **Deploy** - Click "Create Web Service"

Render will automatically build and deploy your Docker image. Your app will be live at `https://<your-service-name>.onrender.com`

## Deploy Jupyter to Render

* There are prebuilt Docker image on [Jupyter Docker Stack](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html)
* Render Dashboard > New > Web Service > Existing Image set to jupyter/base-notebook:latest
* Choose a Name and Region
* Environment Variables
   * JUPYTER_TOKEN: YOUR_PASSWORD
   * PORT: 8888

## Project Structure

```
.
├── Dockerfile              # Container configuration
├── pyproject.toml          # Poetry dependencies and config
├── poetry.lock             # Locked dependency versions
├── mdd/
│   ├── __init__.py
│   └── app.py             # Main Dash application
└── README.md
```
