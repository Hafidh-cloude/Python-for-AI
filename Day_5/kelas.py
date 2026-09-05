# Tanpa class

document1_name = "Rag.pdf"
document1_score = 0.93

document2_name = "Vector.pdf"
document2_score = 0.89
# Jika ada 100 dokumen akan berantakan

# Class berguna untuk template


class AIConfig:
    model_name = "GPT-Light"  # Variabel = "Object"
    max_token = 512

    def get_status():  # Function
        return "Berhasil"


print(f"Nama Model: {AIConfig.model_name}")
print(f"Max Tokens: {AIConfig.max_token}")

status = AIConfig.get_status()
print(f"Status {status}")
