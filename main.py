import tkinter as tk
from tkinter import ttk, messagebox
import requests

def get_money():
    try:
        miktar=float(para_entry.get())
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli sayı giriniz.")
        return

    from_currency = doviz_combobox.get()
    to_currency = cevrilen_doviz_combobox.get()

    if from_currency == to_currency:
        messagebox.showinfo("Bilgi","Aynı para birimini seçtiniz")
        return

    api_key = "fca_live_SHcnQIYH4OB6k8GnTNrJAqhMoUsZXl7k34Ie1ejt"
    url = f"https://api.freecurrencyapi.com/v1/latest?apikey={api_key}&base_currency={from_currency}"

    try:
        response = requests.get(url)
        data = response.json()

        if "data" not in data or to_currency not in data["data"]:
            messagebox.showerror("Hata","API dan geçerli veri alınamadı.")
            return

        kur=data["data"][to_currency]
        sonuc=miktar*kur

        result_label.config(text=f"{miktar:.2f} {from_currency} = {sonuc:.2f} {to_currency}")

    except Exception as e:
        messagebox.showerror("Hata",f"Bir hata oluştu: {e}")



root = tk.Tk()
root.title("Currency Converter")
root.geometry("450x400")

doviz_listesi = ["USD", "EUR", "GBP", "TRY", "JPY"]

tk.Label(root, text="Dönüştürmek İstediğiniz Tutar:").grid(row=0, column=0, padx=10, pady=10)
para_entry = tk.Entry(root)
para_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Döviz Cinsi").grid(row=1, column=0, padx=10, pady=10)
doviz_combobox = ttk.Combobox(root, values=doviz_listesi, state="readonly")
doviz_combobox.grid(row=1, column=1, padx=10, pady=10)
doviz_combobox.current(0)

tk.Label(root, text="Çevrilecek Döviz Cinsi").grid(row=2, column=0, padx=10, pady=10)
cevrilen_doviz_combobox = ttk.Combobox(root, values=doviz_listesi, state="readonly")
cevrilen_doviz_combobox.grid(row=2, column=1, padx=10, pady=10)
cevrilen_doviz_combobox.current(1)

get_doviz_btn = tk.Button(root, text="Çevir", command=get_money)
get_doviz_btn.grid(row=3, column=1, padx=10, pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=4, column=0, columnspan=2, pady=20)




root.mainloop()

