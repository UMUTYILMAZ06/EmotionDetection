# EmotionDetection

Bu proje, ses verisi kullanarak kişinin duygusunu tahmin etmeyi amaçlayan bir Makine Öğrenmesi uygulamasıdır. Python ile geliştirilmiş ve önceden eğitilmiş bir model (.pkl) kullanılarak duygular sınıflandırılmaktadır.

##  Proje Dosyaları

- `app_voice.py`: Ses girişini alıp modele veren ana uygulama dosyası.
- `emotion_classifier_model.pkl`: Eğitilmiş duygu sınıflandırma modeli (pickle formatında).
- `vectorizer.pkl`: Ses verisinden özellik çıkartmak için kullanılan önceden eğitilmiş vektörleştirici.
- `emotion_dataset.csv`: Modelin eğitildiği veri kümesi.
- `main.ipynb`: Veri ön işleme, model eğitimi ve analizlerin yapıldığı Jupyter Notebook dosyası.

## Gereksinimler

Proje çalıştırılmadan önce aşağıdaki kütüphanelerin yüklü olması gerekmektedir:

```bash
pip install numpy pandas scikit-learn soundfile librosa
