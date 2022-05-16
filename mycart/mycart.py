from dis import disco
from itertools import product
from operator import add
import pymysql

billed_items={}

def add_Maincategory():
    con = pymysql.connect(host="localhost", port=3306,
                      user="root", password="123456", database="mycart")
    cur = con.cursor()
    print(id)
    main_name = input("Enter Maincategory name")

    cur.execute("insert into maincategory(name) values(%s)",(main_name))
    con.commit()
    con.close()
def add_Subcategory():
    con = pymysql.connect(host="localhost", port=3306,
                      user="root", password="123456", database="mycart")
    cur = con.cursor()
    print(id)
    sub_name = input("Enter Maincategory name")

    cur.execute("insert into subcategory(name) values(%s)",(sub_name))
    con.commit()
    con.close()
def add_Brand():
    con = pymysql.connect(host="localhost", port=3306,
                      user="root", password="123456", database="mycart")
    cur = con.cursor()
    print(id)
    br_name = input("Enter Maincategory name")

    cur.execute("insert into brnad(name) values(%s)",(br_name))
    con.commit()
    con.close()
def addItem_db():  
    con = pymysql.connect(host="localhost", port=3306,
                      user="root", password="123456", database="mycart")
    cur = con.cursor()
    print(id)           
    product_name = input("enter product name")
    product_price = int(input("enter product price"))
    maincategory=input("enter maincategoryt name")
    subcategory=input("enter  subcategory name")
    brand=input("enter brand name")
    query = cur.execute("insert into product(name,price,main_id,sub_id,brand_id) values(%s,%s,(SELECT id FROM maincategory where name=%s),(select id FROM subcategory where name=%s),(select id FROM brand where name=%s))",(product_name,  product_price, maincategory, subcategory, brand))
    con.commit()
    con.close()

def add_details_db():
    con = pymysql.connect(host="localhost", port=3306,
                      user="root", password="123456", database="mycart")
    cur = con.cursor()
    num = int(input("1.Add Maincategory \n2..Add Subcategory \n3..Add Brand \n4.Add Product"))
    if num==1:
        add_Maincategory()
    elif num==2:
        add_Subcategory()
    elif num==3:
        add_Brand()
    elif num==4:
        addItem_db()

def updatePrice_db():
    con = pymysql.connect(host="localhost", port=3306,
                      user="root", password="123456", database="mycart")
    cur = con.cursor()
    print(id)
    product_name = input("enter product name")
    product_price = int(input("enter product price"))
    cur.execute("update product set price=%s where name=%s",(product_price,product_name))
    con.commit()
    con.close()
def deleteProduct_db():
    con = pymysql.connect(host="localhost", port=3306,
                      user="root", password="123456", database="mycart")
    cur = con.cursor()
    print(id)
    id= int(input("enter product id"))
    cur.execute("DELETE FROM product WHERE id=%s",(id))
    con.commit()
    con.close()





def delete_item_to_details():
    product_name = int(input("enter product key "))
    billed_items.pop(product_name)
    show_billed_items()

def show_billed_items():
    global sum ,dis,total
    sum=0
    dis=500
    total=0
    
    con = pymysql.connect(host="localhost", port=3306,
                      user="root", password="123456", database="mycart")
    cur = con.cursor()
    sum=0
    for item in billed_items.values():
       
        print(f"product Name: {item[0]} \n price-per-unit:{item[2]} \nunit of product is :{item[1]}  \nprice of product:{item[3]} ")
        sum=sum+item[3]
    if sum>10000:
        total=sum-dis
        print("Total amount ",sum)
        print("discount:",dis)
        print("ToTal Billing Amount:",total)
    else:
        total=sum
        print("Total amount ",sum)
    num=int(input("1.Enter final bill \n2.Delete product"))
    if num==1:
        final_bill()
    elif num==2:
        delete_item_to_details()

def final_bill():
   
    for item in billed_items.values():
        print(f"product Name: {item[0]} \nPrice of product:{item[3]} ")
    print("ToTal Billing Amount:",total)
   

def add_item_to_details(): 
    id=0
    def nested():
        nonlocal id 
        if( id>0):
            con = pymysql.connect(host="localhost", port=3306,
                        user="root", password="123456", database="mycart")
            cur = con.cursor()
            product_nm = input("enter product name")
            qty=input("Enter number of Quanity fro Purchase")
            cur.execute("select price from product where name=%s",(product_nm))
            con.close()
            product=cur.fetchone()
            price=product[0]
            billed_items[id]=[product_nm,qty,price,int(qty)*price]
            id=id+1

        else:
            id=0
            con = pymysql.connect(host="localhost", port=3306,
                        user="root", password="123456", database="mycart")
            cur = con.cursor()
            product_nm = input("enter product name")
            qty=input("Enter number of Quanity fro Purchase")
            cur.execute("select price from product where name=%s",(product_nm))
            con.close()
            product=cur.fetchone()
            price=product[0]

            billed_items[id]=[product_nm,qty,price,int(qty)*price]
            id=id+1
        for item in billed_items.values():
            print(f"product Name: {item[0]}\nPrice-per-unit:{item[2]} \nUnit of product is :{item[1]}  \nPrice of product:{item[3]} ")
    nested()
    num=int(input("1.ENTER for shop More\n2. purchase"))
    if num==1:
          nested()
    else:
        show_billed_items()

    


    num=int(input("1.ENTER for shop More\n2. purchase"))
    if num==1:
       add_item_to_details()
    else:
        show_billed_items()
    



def admin():
    con = pymysql.connect(host="localhost", port=3306,
                      user="root", password="123456", database="mycart")
    cur = con.cursor()
    print(id)
    username = input("Enter your user name")
    password = input("Enter your Password")

    query = cur.execute("select * from admin")
    adm = cur.fetchall()

    if username == adm[0][1] and password == adm[0][2]:
        num = int(input("1.SELECT FOR PRODUCT DETAILES\n2.SELECT FOR ADD PRODUCT\n3.UPDATE DETAILS\n4.SELECT DELETE DETAILS"))
        if num==1:
            pass
        elif num==2:
            add_details_db()
        elif num==3:
            updatePrice_db()
        elif num==4:
            deleteProduct_db()
def select_item():
    con = pymysql.connect(host="localhost", port=3306,
                      user="root", password="123456", database="mycart")
    cur = con.cursor()
    query=cur.execute("select * from product")
    product=cur.fetchall()
    for i in product:
        row=i[0]
        print(f"{i[1]} price: {i[5]}")
    con.close()
    num=int(input("Enter 1 for BUY\n 2. exit"))
    if num==1:
        add_item_to_details()
    elif num==2:
        pass

def show():
    con = pymysql.connect(host="localhost", port=3306,
                      user="root", password="123456", database="mycart")
    cur = con.cursor()
    admin_page = int(input("Press 1 for admin \nPress 2 for User "))
    if admin_page == 1:
        admin()
    else:
        select_item()

show()    
