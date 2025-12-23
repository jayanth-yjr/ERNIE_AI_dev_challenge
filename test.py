# See https://www.paddleocr.ai/latest/version3.x/pipeline_usage/PaddleOCR-VL.html to installation

from paddleocr import PaddleOCRVL
pipeline = PaddleOCRVL()
output = pipeline.predict("./dataset/test_pdf.pdf")
for res in output:
	res.print()
	res.save_to_markdown(save_path="output")