from summarizer import summarize

text = """
Artificial intelligence (AI) is transforming industries by automating tasks,
improving decision-making, and enabling new capabilities. Machine learning models
can analyze data at massive scale and uncover patterns that were previously
impossible for humans to detect.
"""

print("Original text:\n", text)
print("\nSummary:\n", summarize(text))
