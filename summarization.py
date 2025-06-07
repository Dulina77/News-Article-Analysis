from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=0)   #device = 0 makes the program run on the GPU 

def summarize_article(content, max_length=150, min_length=40):
    try:
        summary = summarizer(content, max_length=max_length, min_length=min_length, do_sample=False)
        return summary[0]['summary_text']
    except Exception:
        print(f"Summarization Failed {Exception}")
        return False