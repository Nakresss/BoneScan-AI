# Kemik Kanseri Tespit Sistemi

Bu proje, eğitilmiş bir YOLOv8 modeli kullanarak röntgen görüntülerinde kemik kanserini tespit etmeyi amaçlar.

## Proje Tanımı

Bu proje, kemik kanseri teşhisinde doktorlara yardımcı olmak amacıyla geliştirilmiştir. YOLOv8 derin öğrenme modeli kullanılarak eğitilmiş bir model ile röntgen görüntülerindeki kemik kanseri belirtileri tespit edilmektedir. Bu sistem, kemik kanserinin erken teşhisine katkıda bulunarak tedavi sürecinin etkinliğini artırmayı hedeflemektedir.
![istatistik](https://github.com/user-attachments/assets/861487c6-81c5-4398-92bd-73bdaa562c9b)
![istatistik (2)](https://github.com/user-attachments/assets/59e1fc3c-c36f-4cc6-bf18-33f03ce2e44c)
![tesbit](https://github.com/user-attachments/assets/073528c1-e7f9-4757-bb08-0963dc7c70e6)

## Kullanılan Teknolojiler

- **Programlama Dili:** Python
- **Derin Öğrenme Kütüphanesi:** Ultralytics YOLOv8
- **Görüntü İşleme Kütüphanesi:** OpenCV (isteğe bağlı)
- **Temel Veri İşleme:** NumPy
- **Görselleştirme:** PIL (Python Imaging Library) veya Matplotlib

## Kurulum

1.  **Python Kurulumu:** Sisteminizde Python'ın kurulu olduğundan emin olun.
2.  **Gerekli Kütüphanelerin Kurulumu:** Aşağıdaki komut ile gerekli kütüphaneleri yükleyebilirsiniz:

    ```bash
    pip install ultralytics numpy pillow
    ```

## Kullanım

1.  **Model Dosyasını Yerleştirin:** Eğitim sonucunda elde ettiğiniz `best.pt` dosyasını proje dizinine yerleştirin.
2.  **Resimleri Yerleştirin:** Tespit etmek istediğiniz röntgen görüntülerini proje dizinine yerleştirin.
3.  **Kodları Çalıştırın:** Aşağıdaki örnek kodu kullanarak kemik kanseri tespitini gerçekleştirebilirsiniz:

    ```python
    from ultralytics import YOLO
    from PIL import Image
    import numpy as np

    # Model dosyasının yolunu belirtin
    model = YOLO("best.pt")

    # Tespit yapmak istediğiniz resmin yolunu belirtin
    image_path = "test_image.jpg"  # Resmin adını değiştirin

    # Tespit işlemini gerçekleştirin
    results = model.predict(image_path)

    # Tespit sonuçlarını işleyin ve görselleştirin
    for result in results:
        boxes = result.boxes
        if boxes:
            print(f"Tespit Edilen Nesne Sayısı: {len(boxes)}")

            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                label = result.names[int(box.cls[0])]
                confidence = box.conf[0]
                print(f"Etiket: {label}, Güven Skoru: {confidence:.2f}, Kutu: {x1}, {y1}, {x2}, {y2}")
            
            # Görüntüyü çizdir ve kaydet
            im_array = result.plot()
            im = Image.fromarray(im_array[..., ::-1])
            im.save("output_image.jpg")
            print("Tespit Sonuçları output_image.jpg olarak kaydedildi.")
        else:
            print("Tespit Edilen Bir Nesne Bulunmamaktadır")
    ```

4.  **Sonuçları Görüntüleyin:** Kod çalıştırıldığında, tespit sonuçları konsolda yazdırılacak ve üzerine tespit kutuları çizilmiş `output_image.jpg` dosyası oluşturulacaktır.

## Proje Dosya Yapısı

kemik_kanseri_tespit/
├── best.pt # Eğitilmiş YOLOv8 modeli
├── test_image.jpg # Test için kullanılan röntgen görüntüsü
├── main.py # Tespit işlemini gerçekleştiren python kodu
└── README.md # Proje açıklaması ve kullanım kılavuzu


## Katkıda Bulunma

Bu proje açık kaynak olarak geliştirilmiştir ve katkılarınızı memnuniyetle karşılar. Katkıda bulunmak için lütfen aşağıdaki adımları takip edin:

1.  Projenin bir kopyasını fork edin.
2.  Kendi geliştirmelerinizi ve iyileştirmelerinizi yapın.
3.  Çekme isteği (Pull Request) göndererek katkılarınızı sunun.

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Lisans dosyası için `LICENSE` dosyasına bakınız.

## Uyarı

Bu sistem, kemik kanseri teşhisi için yardımcı bir araç olarak tasarlanmıştır ve tek başına teşhis koyma yeteneğine sahip değildir. Kesin teşhis ve tedavi için lütfen bir doktora başvurun.

Projenin Adım Adım Açıklaması:

Proje Dizini Oluştur: Bilgisayarında kemik_kanseri_tespit adında bir klasör oluştur.

best.pt Dosyasını Koy: Eğittiğin best.pt dosyasını bu klasöre yerleştir.

Röntgen Görüntülerini Koy: Tespit yapacağın röntgen görüntülerini (örneğin, test_image.jpg) bu klasöre yerleştir.

main.py Oluştur: Aşağıdaki Python kodunu main.py adında bir dosya olarak oluştur ve proje dizinine kaydet:

from ultralytics import YOLO
from PIL import Image
import numpy as np

# Model dosyasının yolunu belirtin
model = YOLO("best.pt")

# Tespit yapmak istediğiniz resmin yolunu belirtin
image_path = "test_image.jpg"  # Resmin adını değiştirin

# Tespit işlemini gerçekleştirin
results = model.predict(image_path)

# Tespit sonuçlarını işleyin ve görselleştirin
for result in results:
    boxes = result.boxes
    if boxes:
      print(f"Tespit Edilen Nesne Sayısı: {len(boxes)}")
    
      for box in boxes:
          x1, y1, x2, y2 = map(int, box.xyxy[0])
          label = result.names[int(box.cls[0])]
          confidence = box.conf[0]
          print(f"Etiket: {label}, Güven Skoru: {confidence:.2f}, Kutu: {x1}, {y1}, {x2}, {y2}")
          
      # Görüntüyü çizdir ve kaydet
      im_array = result.plot()
      im = Image.fromarray(im_array[..., ::-1])
      im.save("output_image.jpg")
      print("Tespit Sonuçları output_image.jpg olarak kaydedildi.")
    else:
      print("Tespit Edilen Bir Nesne Bulunmamaktadır")

