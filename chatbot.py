from transformers import pipeline

# โหลดโมเดลพรีเทรนด์สำหรับการวิเคราะห์ข้อความ (Text Classification)
classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

def chat_with_model():
    print("Chatbot : Hello! You can type a message, and I'll tell you what it's about.")
    while True:
        user_input = input("You : ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot : bye!")
            break
        
        # วิเคราะห์ข้อความด้วยโมเดล
        result = classifier(user_input)
        
        # แสดงผลลัพธ์
        label = result[0]['label']
        confidence = result[0]['score']
        print(f"Chatbot : I think you're talking about {label} (Confidence: {confidence:.2f})")

if __name__ == "__main__":
    chat_with_model()