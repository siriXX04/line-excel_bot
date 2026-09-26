from flask import Flask, request
from datetime import datetime
import openpyxl
import os

app = Flask(__name__)

# *** สำคัญ: เปลี่ยนชื่อไฟล์ตรงนี้ให้ตรงกับชื่อไฟล์ Excel ที่คุณอัปโหลดลง GitHub ***
EXCEL_FILE = "LP_Report.xlsx" 

@app.route("/")
def home():
    return "LINE Bot Running"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    for event in data.get("events", []):
        if event.get("type") == "message":
            if event["message"]["type"] == "text":
                msg = event["message"]["text"]
                
                if msg.startswith("#ตรวจ"):
                    branch = ""
                    status = ""
                    detail = ""
                    
                    # แยกข้อมูลจากข้อความ LINE
                    for line in msg.split("\n"):
                        if line.startswith("สาขา:"):
                            branch = line.replace("สาขา:", "").strip()
                        elif line.startswith("สถานะ:"):
                            status = line.replace("สถานะ:", "").strip()
                        elif line.startswith("รายละเอียด:"):
                            detail = line.replace("รายละเอียด:", "").strip()
                    
                    # แสดงใน Log เพื่อตรวจสอบ
                    print(f"ได้รับข้อมูล: สาขา={branch}, สถานะ={status}, รายละเอียด={detail}")
                    
                    # นำข้อมูลบันทึกลงไฟล์ Excel
                    if os.path.exists(EXCEL_FILE):
                        wb = openpyxl.load_workbook(EXCEL_FILE)
                        ws = wb.active
                        
                        # เพิ่มข้อมูลลงในแถวใหม่ (เรียงคอลัมน์ตามที่คุณออกแบบไว้ เช่น วันที่, สาขา, สถานะ, รายละเอียด)
                        # คุณสามารถสลับตำแหน่งในวงเล็บก้ามปู [...] ได้ตามคอลัมน์ใน Excel ของคุณเลยครับ
                        ws.append([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), branch, status, detail])
                        
                        wb.save(EXCEL_FILE)
                        print("✅ บันทึกลง Excel สำเร็จ!")
                    else:
                        print(f"❌ ไม่พบไฟล์ Excel ชื่อ: {EXCEL_FILE}")
                        
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
