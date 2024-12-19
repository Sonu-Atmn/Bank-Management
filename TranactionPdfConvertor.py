import shelve
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate,Paragraph,Table,TableStyle,Spacer
def print_trnsaction(id):
    
    with shelve.open(r'bankdata\AccountFile') as actfile:
            customer=actfile[id]     
    filename=str(customer.name)+str("transactions.pdf")
    bank_name="Lena bank"
    acc_no=customer.account_number
    cust_name=customer.name

    transactions=customer.passbook
    print(transactions)      
    t1=["Transcations","Date","Closing Balance"]
    transactions=[t1]+transactions[-25:]

    pdf=SimpleDocTemplate(f"pdfs\\{filename}")
    styles=getSampleStyleSheet()
    content=[]
    bank_para=Paragraph(f"<b> {bank_name}</b>",styles["Title"])
    content.append(bank_para)

    content.append(Spacer(1,12))
    customer_para=Paragraph(f"<b>Account Number:</b> {acc_no}<br/><b>Customer Name:</b> {cust_name}",styles["Normal"])
    content.append(customer_para)
    content.append(Spacer(1,20))





    style=TableStyle([('BACKGROUND',(0,0),(-1,0),colors.grey),
                    ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
                    ('ALIGN',(0,0),(-1,-1),'CENTER'),
                    ('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),
                    ('BOTTOMPADDING',(0,0),(-1,0),12),
                    ('BACKGROUND',(0,1),(-1,-1),colors.beige),
                    ('GRID',(0,0),(-1,-1),1,colors.black)])

    table=Table(transactions,colWidths=[150,200,100])
    table.setStyle(style)

    content.append(table)
    pdf.build(content)
    print("Request Completed Succesfully!")
    input()