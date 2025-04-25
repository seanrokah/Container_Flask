# Flask DevOps Container

A simple containerized Flask application with a clean UI.

## Setup Instructions

### Prerequisites
- Docker installed on your machine
- Git (optional)

### Running the Application

1. **Clone or download this repository**
   ```
   git clone https://github.com/seanrokah/Container_Flask.git
   cd Flask_Devops_Container
   ```

2. **Build the Docker image**
   ```
   docker build -t flask-container .
   ```

3. **Run the container**
   ```
   docker run -p 5000:5000 flask-container
   ```

4. **Access the application**
   Open your browser and navigate to [http://localhost:5000](http://localhost:5000)

## Project Structure
- `app.py` - Main Flask application
- `requirements.txt` - Python dependencies
- `index.html` - Welcome page
- `Dockerfile` - Docker configuration

## Development

To make changes to the application:

1. Modify the files as needed
2. Rebuild the Docker image
3. Run the container again

## Troubleshooting

- If you can't access the application, make sure ports are correctly mapped
- Check Docker logs for any errors: `docker logs <container_id>`