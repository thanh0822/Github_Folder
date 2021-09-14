from fpdf import FPDF

class CustomPDF(FPDF):

    def header(self):
        # Set up a logo
        self.image('logo.jpg', 10, 8, 33)
        self.set_font('Arial', 'B', 10)

        # Add an address
        self.cell(50)
        self.cell(0, 5, 'CONG TY TNHH A VIET NAM', ln=1)
        self.cell(58)
        self.cell(0, 5, 'Dia chi: Tang 15, Thap A, Toa nha A,', ln=1)
        self.cell(60)
        self.cell(0, 5, '5321 Kim Ma, Ngoc Khanh, Ba Dinh, Ha Noi', ln=1) 
        self.cell(60)
        self.cell(0, 5, 'Tel: (+84-4) 6272 6600 -- Fax: (+84-4) 3771 4781', ln=1) 
        # Line break
        self.ln(8)
        self.cell(40)
        self.cell(0, 5, 'BANG TONG HOP CHIET KHAU THUONG MAI TREN DOANH SO', ln=1) 
        self.cell(60)
        self.cell(0, 5, 'CUA DAI LY BAN LE THANG 01/2019', ln=1) 

    def footer(self):
        self.set_y(-10)

        self.set_font('Arial', 'I', 8)

        # Add a page number
        page = 'Page ' + str(self.page_no()) + '/{nb}'
        self.cell(0, 10, page, 0, 0, 'C')

def create_pdf(pdf_path):
    data = [['','','', 'Thông tin tổng đại lý'],
            ['','','Tên', 'Cong ty TNHH Thang Lai'],
            ['','','Mã', '17000'],
            ]
    data1 = [['STT','MA','TEN DAI LY', 'SO LUONG TB MOI','THANH TIEN(VND)'],
                ['1','6501','Pham Khac Tuy rat Dep trai lai con hoc gioi', '100','45000'],
                ['2','6502','ABC', '200','90000'],
                ['2','6502','ABC', '200','90000'],
                ['2','6502','ABC', '200','90000'],
                ['3','6503','CONG TY TNHH THIET BI VA CONG NGHE NGOC ANH', '200','90000'],
                ['','','', 'Tong tien gop','225000']
            ]
    data4 = [['','NGUOI LAP BIEU','','KE TOAN TRUONG'],
                ['','','',''],
                ['','','',''],
                ['','','',''],
                ['','','',''],
                ['','','','NGUYEN THI TO HAO']
                ]           
    d2='CÔNG TY TNHH ATM VIỆT NAM'
    d1='CONG TY TNHH ATM TINH VIET NAM'
    d3='Địa chỉ: Tầng 15, Tháp A, Tòa Nhà B,'
    d31='Dia chi: Tang 15, Tháp A, Tòa Nhà B'
    pdf = FPDF()
    # Create the special value {nb}
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('DejaVu', '', 12)
    pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
    pdf.set_font('DejaVu', '', 14)
    pdf.image('logo.jpg', x=10, y=8, w=20)
    pdf.set_font('DejaVu', '', 10)
    pdf.cell(200, 5, txt=d2, ln=1, align="C")
    pdf.set_font('DejaVu', '', 8)
    pdf.cell(200, 5, txt=d31, ln=1, align="C")
    pdf.cell(200, 5, txt="521 Kim Ma, Ngoc Khanh, Ba Dinh, Ha Noi.", ln=1, align="C")
    pdf.cell(200, 5, txt="Tel: (+84-4) 6272 6600 -- Fax: (+84-4) 3771 4781", ln=1, align="C")
    pdf.ln(8)
    pdf.set_font('DejaVu', '', 12)
    pdf.cell(200, 5, txt='BANG TONG HOP CHIET KHAU THUONG MAI TREN DOANH', ln=1, align="C")
    pdf.cell(200, 5, txt='SO CUA DAI LY BAN LE THANG 1/2019', ln=1, align="C")
    pdf.ln(8)
    pdf.set_font('DejaVu', '', 10)
    col_width = pdf.w / 4.5
    row_height = pdf.font_size
    for row in data:
        for item in row:
            pdf.cell(col_width, row_height*1,txt=item, border=0)
        pdf.ln(row_height*1)
    pdf.cell(20, 5, txt='Ngay xuat:', ln=1, align="C")
    pdf.ln(8)
    col_width = pdf.w / 5.5
    col_width1 = col_width*1/3
    col_width2 = col_width*1/3
    col_width3 = col_width+col_width*2/3+col_width*2/3
    row_height = pdf.font_size
    i=0
    for row in data1:
        i=i+1
        if i==1:
            j=0
            for item in row:
                pdf.set_font('Times', 'B', 10)
                j=j+1
                if j==1:
                    pdf.cell(col_width1, row_height*1.4,txt=item, border=1,ln = 0, align = 'C', fill = False, link = '')
                else:
                    if j==3:
                        pdf.cell(col_width3, row_height*1.4,txt=item, border=1,ln = 0, align = 'C', fill = False, link = '')
                    else:
                        if j==2:
                            pdf.cell(col_width2, row_height*1.4,txt=item, border=1,ln = 0, align = 'C', fill = False, link = '')
                        else:
                            pdf.cell(col_width, row_height*1.4,txt=item, border=1,ln = 0, align = 'C', fill = False, link = '')
        else:
            j=0
            for item in row:
                pdf.set_font('Times', '', 10)
                j=j+1
                if j==1:
                    pdf.cell(col_width1, row_height*1.4,txt=item, border=1, align = 'C', fill = False)
                else:
                    if j==3:
                        pdf.cell(col_width3, row_height*1.4,txt=item, border=1, align = 'L', fill = False)
                    else:
                        if j==2:
                            pdf.cell(col_width2, row_height*1.4,txt=item, border=1, align = 'C', fill = False)
                        else:
                            pdf.cell(col_width, row_height*1.4,txt=item, border=1, align = 'R', fill = False)
        pdf.ln(row_height*1.4)
    line_no = 1
    pdf.ln(8)
    pdf.set_font('DejaVu', '', 10)
    col_width = pdf.w / 4.5
    row_height = pdf.font_size
    for row in data4:
        for item in row:
            pdf.cell(col_width, row_height*1,txt=item, border=0)
        pdf.ln(row_height*1)
#   for i in range(50):
#       pdf.cell(0, 10, txt="Line #{}".format(line_no), ln=1)
#       line_no += 1        
    pdf.output(pdf_path)

if __name__ == '__main__':
    create_pdf('header_footer.pdf')