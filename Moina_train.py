#train Moina
from ultralytics import YOLO

model = YOLO('yolov8n.pt')

# Training.
results = model.train(
   data='C:/Users/yasik/anaconda3/envs/fish_detection/Lib/site-packages/ultralytics/data/Moina_custom_data.yaml',
   imgsz=512,
   epochs=50,
   batch=16,
   name='yolov8n_custom'
   )
