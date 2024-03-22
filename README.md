# Reviews Classification Using DistilBERT
- [Endpoints](http://localhost:8118/docs) (FastAPI, Transformer)
- [UI](http://localhost:8000) (Streamlit)

## Docker Installation

- Step 1: Build
```# command
git clone https://github.com/liemkg1234/reviews-analysis
cd reviews-analysis
make build-cpu # or 'build-gpu' if you want
```

- Step 2: Download Model
```
make download_model
```

- Step 3: Start Server
```
make start
```

## Demo
![Demo](/reports/demo.png "Demo")

- Report at: ```/reports/report.pdf```

## Contact
```
liemkg1234@gmail.com
```