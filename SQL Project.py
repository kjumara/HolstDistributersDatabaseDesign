import mysql.connector
from tabulate import tabulate
from easygui import *
from datetime import date
import datetime

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    #passwd="hiremath12",
    passwd="Henroy15MyBoy",
    database="databasesystemsprojectfall2020"
)

db_cursor = db_connection.cursor()

def printTable(tablename):
    db_cursor.execute("SELECT * FROM " + tablename)
    myresult = db_cursor.fetchall()
    for x in myresult:
        print(x)

def insertTerritory():

    tname = enterbox("Enter Territory Name", "Add New Territory")

    db_cursor.execute("SELECT MAX(tnum) FROM territory")
    strrow = str(db_cursor.fetchall())
    str1 = strrow.split(',')
    first = str1[0]
    tint = int(first[2:]) + 1

    inTerritory(tint, tname)
    transactions()

def inTerritory(territorynum, territoryname):
    tnum = int(territorynum)
    tsql = "INSERT INTO territory VALUES (%s,%s)"
    val = tnum, territoryname
    db_cursor.execute(tsql, val)

    db_connection.commit()

    print(db_cursor.rowcount, "record inserted.")

    printTable("territory")

def modifyTerritory():
    db_cursor.execute("SELECT tname FROM territory")
    myresult = db_cursor.fetchall()
    lista = str(myresult)
    lista = lista.split("'")
    count = 0
    listb = []
    for x in lista:
        count += 1
        if (count % 2 == 0):
            listb.append(x)

    title = "Modify Territory"
    msg = "Select Territory You Wish To Alter"
    tname = choicebox(msg, title, listb)
    
    tsql = "SELECT tnum FROM territory WHERE tname='" + tname + "'"
    db_cursor.execute(tsql)
    myresult = db_cursor.fetchone()
    tnum = myresult[0]
    
    newtname = enterbox("Enter New Territory Name", "Modify Territory", default=tname)
    
    tsql = "UPDATE territory SET tname=%s WHERE(tnum=%s)"
    val = (newtname, tnum)
    db_cursor.execute(tsql, val)

    db_connection.commit()

    print(db_cursor.rowcount, "record updated.")

    printTable("territory")

    transactions()

def insertVendor():
    msg = "Enter Vendor Information"
    title = "Add New Vendor"
    fieldNames = ["Name", "Address", "City", "State", "Zip Code"]
    fieldValues = multenterbox(msg, title, fieldNames)

    vname, vaddress, vcity, vstate, vzip = fieldValues

    db_cursor.execute("SELECT MAX(vnum) FROM vendor")
    strrow = str(db_cursor.fetchall())
    str1 = strrow.split(',')
    first = str1[0]
    vnum = int(first[2:]) + 1
    
    tsql = "INSERT INTO vendor VALUES (%s, %s, %s, %s, %s, %s)"
    val = (vnum, vname, vaddress, vcity, vstate, vzip)

    db_cursor.execute(tsql, val)
    db_connection.commit()

    print(db_cursor.rowcount, "record inserted.")

    printTable("vendor")

def modifyVendor():
    db_cursor.execute("SELECT vname FROM vendor")
    myresult = db_cursor.fetchall()
    lista = str(myresult)
    lista = lista.split("'")
    count = 0
    listb = []
    for x in lista:
        count += 1
        if (count % 2 == 0):
            listb.append(x)

    title = "Modify Vendor"
    msg = "Select Vendor You Wish To Alter"
    vname = choicebox(msg, title, listb)
    
    tsql = "SELECT vnum FROM vendor WHERE vname='" + vname + "'"
    db_cursor.execute(tsql)
    myresult = db_cursor.fetchone()
    vnum = myresult[0]

    msg = "Enter Vendor Information"
    title = "Update Vendor"
    messages = ["name", "address", "city", "state", "zip"]
    output = []
    for msg in messages:
        db_cursor.execute("SELECT v" + msg + " FROM vendor WHERE vnum=" + str(vnum))
        strforchoice = db_cursor.fetchall()
        choice1 = enterbox(msg, "Modify Vendor", default=strforchoice[0])
        output.append(choice1)
    
    vname, vaddr, vcity, vst, vzip = output
    tsql = "UPDATE vendor SET vname=%s, vaddress=%s, vcity=%s, vstate=%s, vzip=%s WHERE(vnum=%s)"
    val = (vname, vaddr, vcity, vst, vzip, vnum)
    db_cursor.execute(tsql, val)

    db_connection.commit()

    print(db_cursor.rowcount, "record updated.")

    printTable("vendor")

def insertCustomer():
    shipping = ynbox(msg='Is Shipping Address Different From Customer Address?',
                     title='Shipping Address', choices=('Yes', 'No'), image=None,
                     default_choice='Yes', cancel_choice='No')

    msg = "Enter Customer Information"
    title = "Add New Customer"

    if shipping:
        fieldnames = ["ID Number", "Name", "FL Address", "SL Address", "City", "State", "Zip", "FL Shipping Address",
                      "SL Shipping Address", "Shipping City", "Shipping State", "Shipping Zip", "Territory Number",
                      "Sales Rep Number", "Balance", "Credit Limit"]
        output = multenterbox(msg, title, fieldnames)

        cnum, name, faddr, saddr, city, st, zipc, sfaddr, ssaddr, scity, sst, szipc, tnum, snum, bal, cl = output

    else:
        fieldnames = ["ID Number", "Name", "FL Address", "SL Address", "City", "State", "Zip",
                      "Territory Number", "Sales Rep Number", "Balance", "Credit Limit"]
        output = multenterbox(msg, title, fieldnames)

        cnum, name, faddr, saddr, city, st, zipc, tnum, snum, bal, cl = output
        sfaddr = faddr
        ssaddr = saddr
        scity = city
        sst = st
        szipc = zipc

    tsql = "INSERT INTO customer_sales VALUES (%s, 0, %s, %s, 0, 0, 0, 0, %s)"
    val = (cnum, bal, cl, snum)

    db_cursor.execute(tsql, val)
    db_connection.commit()

    tsql = "INSERT INTO customer VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (cnum, name, faddr, saddr, city, st, zipc, sfaddr, ssaddr, scity, sst, szipc, tnum, snum)

    db_cursor.execute(tsql, val)
    db_connection.commit()

    db_cursor.execute("SELECT * FROM customer WHERE cnum=" + str(cnum))
    print(db_cursor.fetchall())

def modifyCustomer():
    db_cursor.execute("SELECT cnum, cname FROM customer")
    title = "Modify Sales Rep"
    msg = str(db_cursor.fetchall())
    dtext = "Enter number you wish to modify"

    output = enterbox(msg, title, dtext)

    tsql = "SELECT customer.cnum, cname, cfladdress, csladdress, ccity, cstate, czip,"
    tsql = tsql + " cstfladdress, cstsladdress, cstcity, cststate, cstzip,territorynum, salesrepnum, "
    tsql = tsql + "balance, creditlimit FROM customer INNER JOIN customer_sales "
    tsql = tsql + "ON customer.cnum = customer_sales.cnum WHERE (customer.cnum=%s);"
    srval = int(output)
    val = (srval,)
    db_cursor.execute(tsql, val)
    msg1 = str(db_cursor.fetchall())

    shipping = ynbox(msg='Is Shipping Address Different From Customer Address?',
                     title='Shipping Address', choices=('Yes', 'No'), image=None,
                     default_choice='Yes', cancel_choice='No')

    db_cursor.execute(tsql, val)
    msg = str(db_cursor.fetchall())

    if shipping:
        fieldnames = ["Name", "FL Address", "SL Address", "City", "State", "Zip", "FL Shipping Address",
                      "SL Shipping Address", "Shipping City", "Shipping State", "Shipping Zip", "Territory Number",
                      "Sales Rep Number", "Balance", "Credit Limit"]
        output = multenterbox(msg, title, fieldnames)

        name, faddr, saddr, city, st, zipc, sfaddr, ssaddr, scity, sst, szipc, tnum, snum, bal, cl = output

    else:
        fieldnames = ["Name", "FL Address", "SL Address", "City", "State", "Zip", "Territory Number",
                      "Sales Rep Number", "Balance", "Credit Limit"]
        output = multenterbox(msg, title, fieldnames)

        name, faddr, saddr, city, st, zipc, tnum, snum, bal, cl = output
        sfaddr = faddr
        ssaddr = saddr
        scity = city
        sst = st
        szipc = zipc

    tsql = "UPDATE customer_sales SET balance=%s, salesrepnum=%s, creditlimit=%s WHERE(cnum=%s)"
    val = (bal, snum, cl, srval)
    db_cursor.execute(tsql, val)
    db_connection.commit()

    tsql = "UPDATE customer SET cname=%s, cfladdress=%s, csladdress=%s, ccity=%s, cstate=%s, czip=%s, "
    tsql = tsql + "cstfladdress=%s, cstsladdress=%s, cstcity=%s, cststate=%s, cstzip=%s, territorynum=%s, "
    tsql = tsql + "salesrepno=%s WHERE(cnum=%s)"
    val = (name, faddr, saddr, city, st, zipc, sfaddr, ssaddr, scity, sst, szipc, tnum, snum, srval)

    db_cursor.execute(tsql, val)
    db_connection.commit()

    db_cursor.execute("SELECT * FROM customer WHERE cnum=" + str(srval))
    print(db_cursor.fetchall())

def insertSalesRep():
    msg = "Enter Sales Rep Information"
    title = "Add New Sales Rep"
    fieldNames = ["Sales Rep ID", "Name", "Address", "City", "State", "ZIP",
                  "Commission Rate", "Territory Number"]
    fieldValues = multenterbox(msg, title, fieldNames)
    srint, srname, sraddr, srcity, srstate, srzip, srcomm, tnum = fieldValues

    tsql = "INSERT INTO sales_rep_sales VALUES (%s,0,0,0,0,%s,%s)"
    val = (int(srint), float(srcomm), int(tnum),)
    db_cursor.execute(tsql, val)

    db_connection.commit()

    print(db_cursor.rowcount, "record inserted.")

    printTable("sales_rep_sales")

    tsql = "INSERT INTO sales_rep VALUES (%s,%s,%s,%s,%s,%s,%s)"
    val = (int(srint), srname, sraddr, srcity, srstate, int(srzip), int(tnum))
    db_cursor.execute(tsql, val)

    db_connection.commit()

    print(db_cursor.rowcount, "record inserted.")

    printTable("sales_rep_sales")

def modifySalesRep():
    db_cursor.execute("SELECT srnum, srname FROM sales_rep")
    title = "Modify Sales Rep"
    msg = str(db_cursor.fetchall())
    dtext = "Enter number you wish to modify"

    output = enterbox(msg, title, dtext)

    tsql = "SELECT sales_rep.srnum, srname, sraddress, srcity, srstate, srzip, tnum, srcomissionrate"
    tsql = tsql + " FROM sales_rep INNER JOIN sales_rep_sales "
    tsql = tsql + "ON sales_rep.srnum = sales_rep_sales.srnum WHERE (sales_rep.srnum=%s);"
    srval = int(output)
    val = (srval,)
    db_cursor.execute(tsql, val)
    msg = str(db_cursor.fetchall())
    fieldnames = ["Name", "Address", "City", "State", "Zip",
                  "Territory Number", "Commission Rate"]
    output = multenterbox(msg, title, fieldnames)

    name, addr, city, state, zipc, tnum, srcomm = output

    tsql = "UPDATE sales_rep SET srname=%s, sraddress=%s, srcity=%s, srstate=%s,"
    tsql = tsql + "srzip=%s,tno=%s WHERE(srnum=%s)"
    val = (name, addr, city, state, zipc, tnum, srval)
    db_cursor.execute(tsql, val)
    db_connection.commit()

    print(db_cursor.rowcount, "record updated.")

    tsql = "UPDATE sales_rep_sales SET tnum=%s, srcomissionrate=%s WHERE(srnum=%s)"
    val = (tnum, srcomm, srval)
    db_cursor.execute(tsql, val)
    db_connection.commit()

    print(db_cursor.rowcount, "record updated.")

    printTable("sales_rep")
    printTable("sales_rep_sales")

def insertPart():
    
    db_cursor.execute("SELECT MAX(prtnum) FROM part")
    strrow = str(db_cursor.fetchall())
    str1 = strrow.split(',')
    first = str1[0]
    partnumber = int(first[2:]) + 1
    
    msg = "Enter Part Information"
    title = "Add New Part"
    fieldNames = ["Description", "Price", "Units On Hand", "Reorder Point"]
    fieldValues = multenterbox(msg, title, fieldNames)

    partdescription, partprice, partunitsonhand, partreorderpoint = fieldValues

    tsql = "INSERT INTO part VALUES (%s, %s, %s, 0, 0, %s, 0, %s)"
    val = (partnumber, partdescription, partprice, partunitsonhand, partreorderpoint)

    db_cursor.execute(tsql, val)
    db_connection.commit()

    print(db_cursor.rowcount, "record inserted.")

    printTable("part")

def modifyPart():
    db_cursor.execute("SELECT prtdesc FROM part")
    myresult = db_cursor.fetchall()
    lista = str(myresult)
    lista = lista.split("'")
    count = 0
    listb = []
    for x in lista:
        count += 1
        if (count % 2 == 0):
            listb.append(x)

    title = "Modify Part"
    msg = "Select Part You Wish To Alter"
    prtdesc = choicebox(msg, title, listb)
    
    tsql = "SELECT prtnum FROM part WHERE prtdesc='" + prtdesc + "'"
    db_cursor.execute(tsql)
    myresult = db_cursor.fetchone()
    prtnum = myresult[0]

    title = "Update Part"
    msg = ["Desc", "Price", "Units On Hand", "Reorder Point"]
    output = []
    for msgs in msg:
        msgs = msgs.replace(" ","")
        db_cursor.execute("SELECT prt" + msgs + " FROM part WHERE prtnum=" + str(prtnum))
        strforchoice = db_cursor.fetchall()
        choice1 = enterbox(msgs, title, default=strforchoice[0])
        output.append(choice1)
    
    desc, price, uoh, rp = output

    tsql = "UPDATE part SET prtdesc=%s, prtprice=%s, prtunitsonhand=%s, prtreorderpoint=%s WHERE(prtnum=%s)"
    val = (desc, price, uoh, rp, prtnum)
    db_cursor.execute(tsql, val)

    db_connection.commit()

    print(db_cursor.rowcount, "record updated.")

    printTable("part")

def deleteFromTable(num, name, Tablename):
    title = "Alter " + Tablename
    db_cursor.execute("SELECT " + name + " FROM " + Tablename)
    myresult = db_cursor.fetchall()
    lista = str(myresult)
    lista = lista.split("'")
    count = 0
    listb = []
    for x in lista:
        count += 1
        if (count % 2 == 0):
            listb.append(x)

    title = "Delete " + Tablename
    msg = "Select " + Tablename
    tchoice = choicebox(msg, title, listb)
    print(tchoice)
    tsql = "SELECT " + num + " FROM " + Tablename + " WHERE " + name + " ='" + tchoice + "'"
    db_cursor.execute(tsql)
    myresult = db_cursor.fetchone()
    number = myresult[0]
    print(number)
    
    sql = "DELETE FROM " + Tablename + " WHERE (" + num + "=%s)"
    val = (int(number),)

    db_cursor.execute(sql, val)

    db_connection.commit()

    print(db_cursor.rowcount, "record deleted.")

    if Tablename == "sales_rep" or Tablename == "customer":
        sql = "DELETE FROM " + Tablename + "_sales WHERE (" + num + "=%s)"
        val = (int(number),)

        db_cursor.execute(sql, val)

        db_connection.commit()

    printTable(Tablename)

    transactions()

def alterTable(tblname):
    title = "Alter " + tblname

    msg = "Click for the type of Query"

    buttonlist = []
    button1 = "Add " + tblname

    button2 = "Modify " + tblname

    button3 = "Delete " + tblname

    button4 = "Return to Main Menu"

    buttonlist.append(button1)
    buttonlist.append(button2)
    buttonlist.append(button3)
    buttonlist.append(button4)

    reply = buttonbox(msg, title, buttonlist)

    if reply == "Add " + tblname:
        if tblname == "territory":
            insertTerritory()
        if tblname == "sales_rep":
            insertSalesRep()
        if tblname == "customer":
            insertCustomer()
        if tblname == "vendor":
            insertVendor()
        if tblname == "part":
            insertPart()
    if reply == "Modify " + tblname:
        if tblname == "territory":
            modifyTerritory()
        if tblname == "sales_rep":
            modifySalesRep()
        if tblname == "customer":
            modifyCustomer()
        if tblname == "vendor":
            modifyVendor()
        if tblname == "part":
            modifyPart()
    if reply == "Delete " + tblname:
        if tblname == "territory":
            deleteFromTable("tnum", "tname", tblname)
        if tblname == "sales_rep":
            deleteFromTable("srnum", tblname)
        if tblname == "customer":
            deleteFromTable("cnum", tblname)
        if tblname == "vendor":
            deleteFromTable("vnum", "vname", tblname)
        if tblname == "part":
            deleteFromTable("prtnum", "prtdesc", tblname)
    if reply == "Return to Main Menu":
        main()

def newPayment():
    db_cursor.execute("SELECT MAX(pynum) FROM payment")
    strrow = str(db_cursor.fetchall())
    str1 = strrow.split(',')
    first = str1[0]
    fr = int(first[2:]) + 1

    db_cursor.execute("SELECT cname FROM customer")
    myresult = db_cursor.fetchall()
    lista = str(myresult)
    lista = lista.split("'")
    count = 0
    listb = []
    for x in lista:
        count += 1
        if (count % 2 == 0):
            listb.append(x)

    title = "Make Payment"
    msg = "Select Customer Making Payment"
    cname = choicebox(msg, title, listb)
    
    tsql = "SELECT cnum FROM customer WHERE cname='" + cname + "'"
    db_cursor.execute(tsql)
    myresult = db_cursor.fetchone()
    cid = myresult[0]
    
    msg = "Enter Payment Information"
    title = "Add Payment"
    fieldNames = ["Day", "Month", "Year", "Amount"]
    fieldValues = multenterbox(msg, title, fieldNames)

    dy, mth, yr, amt = fieldValues
    date = yr + "-" + mth + "-" + dy
    print(date)
    
    tsql = "INSERT INTO payment VALUES (%s, %s, %s, %s)"
    val = (fr, date, amt, cid)
    db_cursor.execute(tsql, val)

    db_connection.commit()

    print(db_cursor.rowcount, "record updated.")

    printTable("payment")

    tsql = "UPDATE customer_sales SET balance=(balance-%s) WHERE(cnum=%s)"
    val = (amt, cid)
    db_cursor.execute(tsql, val)

    db_connection.commit()

    print(db_cursor.rowcount, "record updated.")

def enterOrder():
    db_cursor.execute("SELECT MAX(onum) FROM orders")
    strrow = str(db_cursor.fetchall())
    str1 = strrow.split(',')
    first = str1[0]    
    onum = int(first[2:]) + 1
    
    db_cursor.execute("SELECT cname FROM customer")
    myresult = db_cursor.fetchall()
    lista = str(myresult)
    lista = lista.split("'")
    count = 0
    listb = []
    for x in lista:
        count += 1
        if (count % 2 == 0):
            listb.append(x)

    title = "Enter Order"
    msg = "Select Customer"
    cname = choicebox(msg, title, listb)
    
    tsql = "SELECT cnum FROM customer WHERE cname='" + cname + "'"
    db_cursor.execute(tsql)
    myresult = db_cursor.fetchone()
    cid = myresult[0]
    
    db_cursor.execute("SELECT prtdesc FROM part")
    myresult = db_cursor.fetchall()
    lista = str(myresult)
    lista = lista.split("'")
    count = 0
    listb = []
    for x in lista:
        count += 1
        if (count % 2 == 0):
            listb.append(x)

    title = "Enter Order"
    msg = "Select Part"
    prtdesc = choicebox(msg, title, listb)
    
    tsql = "SELECT prtnum FROM part WHERE prtdesc='" + prtdesc + "'"
    db_cursor.execute(tsql)
    myresult = db_cursor.fetchone()
    prtnum = myresult[0]
    
    tsql = "SELECT PRTUNITSONHAND-PRTUNITSALLOCATED FROM part WHERE prtnum='" + str(prtnum) + "'"
    db_cursor.execute(tsql)
    myresult = db_cursor.fetchone()
    partrange = myresult[0]
    print(partrange)
    
    correctamount = False
    msg = "Maximum Available: " + str(partrange)
    listb = []
    for x in range(partrange): listb.append(x)
    
    title = "Enter Order"
    msg = "Select Amount of Parts"
    prtamt = choicebox(msg, title, listb)
    print(prtamt)
    
    msg = "Enter Order Information"
    title = "Add Order"
    fieldNames = ["Day", "Month", "Year", "Description"]
    fieldValues = multenterbox(msg, title, fieldNames)
    
    dy, mth, yr, desc = fieldValues
    
    tsql="SELECT prtnum, prtdesc, prtprice FROM part WHERE (prtnum= %s );"
    val = (prtnum,)
    db_cursor.execute(tsql, val)
    allfields = db_cursor.fetchone()
    partnumber, partdesc, price = allfields
    prices = "$" + str(price)
    
    title = "Confirm Price Per Unit"
    msg = "Part Number: " + str(partnumber) + "\nDescription: " + partdesc 
    msg = msg + "\nPrice : " + prices + "\n\n\nIs this the Quoted Price?"
    
    quoted = ynbox(msg, title)
    if quoted:
        qtdprice = float(price)
    else:
        title = "Quoted Price"
        msg = "Enter Quoted Price"
        qtdprice = float(enterbox(msg, title, price))
    
    date = yr + "-" + mth + "-" + dy
    
    db_cursor.execute("SELECT MAX(ocustponum) FROM orders WHERE (customernum=" + str(cid) + ")");
    currentponum = str(db_cursor.fetchone())
    currentponum = currentponum[:3]
    currentponum = currentponum[1:]
    if currentponum == "No":
        nextponum = 1
    else:
        nextponum = int(currentponum) + 1
    
    ordertotal = qtdprice * float(prtamt)
    tsql = "INSERT INTO orders VALUES (%s, %s, %s, %s, %s, 0, %s)"
    val = (onum, date, desc, nextponum, ordertotal, cid)
    db_cursor.execute(tsql, val)
    
    db_connection.commit()
    
    tsql = "INSERT INTO orderhaspart VALUES (%s, %s, %s, %s)"
    val = (onum, partnumber, prtamt, qtdprice)
    db_cursor.execute(tsql, val)
    
    db_connection.commit()
    printTable("orderhaspart")
    
    tsql = "UPDATE part SET prtunitsallocated=(prtunitsallocated+%s) WHERE(prtnum=%s)"
    val = (prtamt, partnumber)
    db_cursor.execute(tsql, val)

    db_connection.commit()
    
def transactions():
    # message for our window
    msg = "Transactions Menu"

    # choices which user can select
    choices = ["Alter Territory", "Alter Sales Rep", "Alter Customer", "Alter Vendor",
               "Alter Part", "Apply Payment", "Create Invoice", "Order Entry",
               "Return to Main Menu"]

    # mesaage / question to be asked
    msg = "Select any one option"

    # opening a choice box using our msg and choices
    reply = choicebox(msg, choices=choices)

    if reply == "Alter Territory":
        alterTable("territory")
    if reply == "Alter Sales Rep":
        alterTable("sales_rep")
    if reply == "Alter Customer":
        alterTable("customer")
    if reply == "Alter Vendor":
        alterTable("vendor")
    if reply == "Alter Part":
        alterTable("part")
    if reply == "Apply Payment":
        newPayment()
    if reply == "Create Invoice":
        newInvoice()
    if reply == "Order Entry":
        enterOrder()
    if reply == "Return to Main Menu":
        main()

def main():
    title = "Database Systems Final"

    msg = "Click for the type of Query"

    buttonlist = []

    button1 = "Transaction Queries"

    button2 = "Reporting Queries"

    button3 = "Month End Queries"

    buttonlist.append(button1)
    buttonlist.append(button2)
    buttonlist.append(button3)
    

    output = buttonbox(msg, title, buttonlist)
    
    if output == "Reporting Queries":
        reporting()
    elif output == "Transaction Queries":
        transactions()
    elif output == "Month End Queries":
        month_end()

main()

db_cursor.close()
db_connection.close()
