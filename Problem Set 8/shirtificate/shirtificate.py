from fpdf import FPDF
class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 24)
        self.cell(0, 10, "CS50 Shirtificate", ln=True, align="C")

    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")

    def add_shirt(self, name):
        self.image("shirtificate.png", x=0, y=60, w=self.w)
        self.set_xy(0, 140)
        self.set_font("helvetica", "B", 32)
        self.set_text_color(255, 255, 255)
        self.cell(0, 10, name, align="C")


name = input("Name: ")
pdf = PDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.add_shirt(name)
pdf.output("shirtificate.pdf")
