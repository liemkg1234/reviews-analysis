from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, validator, Field

app = FastAPI()


# Schema
class ReviewRequest(BaseModel):
    text: str = Field(..., example="It actually pains me to say it, but this movie was horrible on every level. The blame does not lie entirely with Van Damme as you can see he tried his best, but let's face it, he's almost fifty, how much more can you ask of him? I find it so hard to believe that the same people who put together Undisputed 2; arguably the best (western) martial arts movie in years, created this. Everything from the plot, to the dialog, to the editing, to the overall acting was just horribly put together and in many cases outright boring and nonsensical. Scott Adkins who's fight scenes seemed more like a demo reel, was also terribly underused and not even the main villain which is such a shame because 1) He is more than capable of playing that role and 2) The actual main villain was not only not intimidating at all but also quite annoying. Again, not blaming Van Damme. I will always be a fan, but avoid this one.")

    @validator('text')
    def validate_text(cls, v):
        if not v:
            response = {
                "status_code": 400,
                "message": "[text] is required",
                "data": {},
            }
            raise response
        return v


# Controller
@app.post("/analysis-review")
def analysis_review(review: ReviewRequest):
    """"""

    class_predicted = predict_analysis_review(review.text)
    response = {
        "status_code": 200,
        "message": "",
        "data": class_predicted,
    }
    return JSONResponse(content=response, status_code=200)


# Service
import torch
from optimum.onnxruntime import ORTModelForSequenceClassification
from transformers import AutoTokenizer

model_interface = "models/distilbert_imdb/distilbert_imdb_onnx_quantized"
tokenizer = AutoTokenizer.from_pretrained(model_interface)
model = ORTModelForSequenceClassification.from_pretrained(model_interface, use_cache=False)


def predict_analysis_review(text: str) -> dict:
    """
    Predict analysis review

    """
    id2label = {0: "NEGATIVE", 1: "POSITIVE"}

    # Predict
    encoded_input = tokenizer(text, return_tensors='pt')
    output = model(**encoded_input)

    probabilities = torch.softmax(output.logits, dim=1)
    class_id = torch.argmax(probabilities, dim=1).item()
    confidence = probabilities[0, class_id].item()

    return {"class_id": class_id, "class": id2label[class_id], "confidence": confidence}
