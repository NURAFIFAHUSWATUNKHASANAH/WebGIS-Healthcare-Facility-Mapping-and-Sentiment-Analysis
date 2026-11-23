from datetime import datetime
from model.model_komentar import ModelKomentar
from config.sentimen_prediction import predict_sentiment

class ControllerKomentar:

    def simpan(id_faskes, komentar):

        try:
            sentimen = predict_sentiment(komentar)

            print("=" * 60)
            print("Komentar :", komentar)
            print("Prediksi :", sentimen)
            print("=" * 60)

        except Exception as e:
            print("ERROR PREDIKSI :", e)

            # fallback jika model gagal
            sentimen = "positif"

        data = {
            "id_faskes": id_faskes,
            "komentar": komentar,
            "sentimen": sentimen,
            "created_at": datetime.now()
        }

        return ModelKomentar.insert(data)
    
    @staticmethod
    def get_all():

        return ModelKomentar.get_all()


    @staticmethod
    def delete(id):

        return ModelKomentar.delete(id)
    
    @staticmethod
    def get_statistik(id_faskes):
        return ModelKomentar.get_statistik(id_faskes)