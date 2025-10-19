from datetime import datetime

def data_hoje():
    return datetime.now().strftime("%d/%m/%Y")

# print(f"A data de hoje é {data_hoje()}")