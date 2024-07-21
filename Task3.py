#Reportlab is a Python library that create documents 

from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

#add Serial number, Date , Item name , Item Price to create a bill or receipt
Items_purchased = [
    [ "S.no.", "Date" , "Item name", "Price (in Rs.)" ],
    ["1","24/06/2024","TextBook","550.00/-"],
    [ "2", "24/06/2024", "TextCopy", "120.00/-"],
    [ "3", "24/06/2024", "Diary","100.00/-"],
    [ "4", "24/06/2024", "Pen Packet","250.00/-"],
    [ "5","24/06/2024", "Files","250.00/-"],
    [ "Sub Total", "","","1270.00/-"],
    [ "Discount", "","","-170.00/-"],
    [ "Total", "","","1100.00/-"],
]

#define pdf function and styles
bill_generate= SimpleDocTemplate( "Receipt.pdf" , pagesize = A4 )
styles = getSampleStyleSheet()
title_style = styles[ "Heading1" ]

title_style.alignment = 1

#the title of Payment Receipt
title = Paragraph( "Stationary Requirements" , title_style ) 

#Table of Bill
style = TableStyle(
    [
        ( "BOX" , ( 0, 0 ), ( -1, -1 ), 1 , colors.black ),
        ( "GRID" , ( 0, 0 ), ( 5 , 5 ), 1 , colors.black ),
        ( "BACKGROUND" , ( 0, 0 ), ( 4, 0 ), colors.darkgrey),
        ( "TEXTCOLOR" , ( 0, 0 ), ( -1, 0 ), colors.white ),
        ( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ),
        ( "BACKGROUND" , ( 0 , 1 ) , ( -1 , -1 ), colors.wheat ),
    ]
)

table_representation = Table( Items_purchased, style = style )
#A Payment Receipt is created.
bill_generate.build([ title , table_representation ]) 

print("\nReceipt is Generated . \n Thank You !!!\n")