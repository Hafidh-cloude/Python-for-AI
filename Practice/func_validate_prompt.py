def validate_prompt(prompt_text):
    if len(prompt_text) < 10:
        return "Prompt terlalu pendek! Minimal 10 karakter."
    elif "hack" in prompt_text:
        return "Prompt ditolak: Mengandung kata sensitif!"
    else:
        return "Prompt valid! Siap dikirim ke model AI"


prompt = input("Masukkan prompt Anda: ")
status = validate_prompt(prompt)
print(status)
