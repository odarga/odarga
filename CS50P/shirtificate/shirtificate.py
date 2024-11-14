from fpdf import FPDF

name = input("Name: ")

pdf = FPDF()
pdf.add_page()
pdf.set_y(20)
pdf.set_font("helvetica", "B", 50)
pdf.cell(text = "CS50 Shirtificate", center = True)
pdf.image("shirtificate.png", x=10, y=80, w = 190, h = 200)
pdf.set_y(150)
pdf.set_font("helvetica", "", 30)
pdf.set_text_color(255,255,255)
pdf.cell(text = f"{name} took CS50", center = True)
pdf.output("shirtificate.pdf")


"""
outputs, using fpdf2, a CS50 shirtificate in a file called shirtificate.pdf similar to this one for John Harvard, with these specifications:

The orientation of the PDF should be Portrait.
The shirt’s image should be centered horizontally.
The user’s name should be on top of the shirt, in white text.
All other details we leave to you. You’re even welcome to add borders, colors, and lines. Your shirtificate needn’t match John Harvard’s precisely. And no need to wrap long names across multiple lines.

Before writing any code, do read through fpdf2’s tutorial to learn how to use it. Then skim fpdf2’s API (application programming interface) to see all of its functions and parameters therefor.
"""
