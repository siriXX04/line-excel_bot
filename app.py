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
                        
                        ws.append([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), branch, status, detail])
                        
                        wb.save(EXCEL_FILE)
                        print("✅ บันทึกลง Excel สำเร็จ!")
                    else:
                        print(f"❌ ไม่พบไฟล์ Excel ชื่อ: {EXCEL_FILE}")
