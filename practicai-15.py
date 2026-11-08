import csv
from reportlab.pdfgen import canvas

with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Marks"])
    writer.writerow(["Joy", 85])

pdf = canvas.Canvas("report.pdf")
pdf.drawString(100, 750, "Student Report")
pdf.drawString(100, 720, "Name: Joy")
pdf.drawString(100, 690, "Marks: 85")
pdf.save()

print("PDF Report Created")