from ultralytics import YOLO

# Model dosyasının (best.pt) yolunu belirtin
model = YOLO("path/to/best.pt")

# Tespit yapmak istediğiniz resmin yolunu belirtin
results = model.predict("path/to/your/image.jpg")

# Tespit sonuçlarını görselleştirme (isteğe bağlı)
for result in results:
    boxes = result.boxes  # Tespit edilen nesnelerin kutuları
    for box in boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        label = result.names[int(box.cls[0])]
        confidence = box.conf[0]
        print(f"Etiket: {label}, Güven Skoru: {confidence:.2f}, Kutu: {x1}, {y1}, {x2}, {y2}")

    im_array = result.plot() # Görüntü üzerinde kutuların çizildiği sonuç
    # Görüntüyü göstermek için:
    from PIL import Image
    im = Image.fromarray(im_array[..., ::-1]) # Renkleri RGB'ye çevir
    im.show() # Görüntüyü göster (örneğin Jupyter Notebook üzerinde)
    im.save("output_image.jpg")