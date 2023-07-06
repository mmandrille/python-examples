import logging
import torch

# Global
logger = logging.getLogger(__name__)


# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
model.conf = 0.30  # NMS confidence threshold
model.iou = 0.45  # NMS IoU threshold
model.agnostic = False  # NMS class-agnostic
model.multi_label = False  # NMS multiple labels per box
model.classes = [0]  # (optional list) filter by class, i.e. = [0, 15, 16]
model.max_det = 1000  # maximum number of detections per image
model.amp = False  # Automatic Mixed Precision (AMP) inference


# Image
im = 'https://ultralytics.com/images/zidane.jpg'


# Inference
results = model(im)
logger.info(results.pandas().xyxy[0])
results.show()
