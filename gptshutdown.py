import os
import tkinter as tk
from tkinter import messagebox

def shutdown():
    time_unit = time_var.get()
    try:
        x = int(time_entry.get())
        if time_unit == "h":
            os.system(f"shutdown /s /t {x * 3600}")
            messagebox.showinfo("Shutdown", f"จะปิดเครื่องใน {x} ชั่วโมง")
        elif time_unit == "m":
            os.system(f"shutdown /s /t {x * 60}")
            messagebox.showinfo("Shutdown", f"จะปิดเครื่องใน {x} นาที")
        elif time_unit == "s":
            os.system(f"shutdown /s /t {x}")
            messagebox.showinfo("Shutdown", f"จะปิดเครื่องใน {x} วินาที")
    except ValueError:
        messagebox.showerror("Error", "กรุณาใส่จำนวนเป็นตัวเลข")

def cancel_shutdown():
    os.system("shutdown /a")
    messagebox.showinfo("Cancel", "ยกเลิกการปิดเครื่องเรียบร้อยแล้ว")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("Shutdown Timer")

# สร้างตัวเลือกเวลา
time_var = tk.StringVar(value="h")

tk.Label(root, text="เลือกหน่วยเวลา:").pack()
tk.Radiobutton(root, text="ชั่วโมง (h)", variable=time_var, value="h").pack(anchor="w")
tk.Radiobutton(root, text="นาที (m)", variable=time_var, value="m").pack(anchor="w")
tk.Radiobutton(root, text="วินาที (s)", variable=time_var, value="s").pack(anchor="w")

# สร้างช่องใส่จำนวนเวลา
tk.Label(root, text="ใส่จำนวนเวลา:").pack()
time_entry = tk.Entry(root)
time_entry.pack()

# สร้างปุ่มสำหรับตั้งเวลาปิดเครื่องและยกเลิกการปิดเครื่อง
tk.Button(root, text="ตั้งเวลาปิดเครื่อง", command=shutdown).pack(pady=10)
tk.Button(root, text="ยกเลิกการปิดเครื่อง", command=cancel_shutdown).pack()

# เริ่มต้นหน้าต่าง
root.mainloop()
