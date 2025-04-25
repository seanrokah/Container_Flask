# Flask DevOps Container - Contribution

## Maintainer Information

This project is currently maintained solely by the original author. No external contributions are being accepted at this time.

## Development Notes

### Local Setup

```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

### Docker Setup

```
docker build -t flask-container .
docker run -p 5000:5000 flask-container
```

## Contact

If you have any questions or find issues with this project, please contact the maintainer directly.