# Reviews Analysis Using DistilBERT
- [Endpoints](http://localhost:8118/docs) (FastAPI, Transformer)
- [UI](http://localhost:8000) (Streamlit)

## Docker Installation

- Step 1: Build
```# command
git clone https://github.com/liemkg1234/reviews-analysis
cd reviews-analysis
make build
```

- Step 2: Download Model
  - Go [here](https://www.kaggle.com/datasets/liemkg1234/distilbert-imdb-finetuned)
  - Download & unzip with folder name is ```distilbert_imdb```
  - Copy ```distilbert_imdb``` into ```/models```


- Step 3: Start Server
```
make start
```

## Test Results
- Result at: ```/eval/eval_distilbert_imdb.csv```
```
- Accuracy: 0.92656
- Precision: 0.9265
- Recall: 0.9265
- F1: 0.926
```

## Demo
![Demo](/reports/demo.png "Demo")
## APIs
![APIs](/reports/APIs.png "APIs")
- Report at: ```/reports/Review-Analysis.pdf```

## Contact
```
liemkg1234@gmail.com
```