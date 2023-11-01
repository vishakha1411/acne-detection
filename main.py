from ultralytics import YOLO
model=YOLO("C:\\Users\\VishakhaPC\\PycharmProjects\\pythonProject7\\best (2).pt")
results=model.predict(source='0',show=True)
print(results)