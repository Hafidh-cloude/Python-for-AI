def check_model_status(accuracy):
    if accuracy >= 0.80:
        return "Model Siap Deploy"
    else:
        return "Model Perlu Retraining"


accuracy_score = float(input("Masukkan akurasi model (dalam desimal): "))

status_model = check_model_status(accuracy_score)
print(status_model)
