import mysql.connector
from tabulate import tabulate
from easygui import *
from datetime import date
import datetime

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="hiremath12",
    #passwd="Henroy15MyBoy",
    database="databasesystemsprojectfall2020"
)

db_cursor = db_connection.cursor()
#########################################################################################
#                                                                                       #
#                           REPORTING                                                   #
#                                                                                       #
#                                                                                       #
#########################################################################################

def reportTerList():
    db_cursor.execute("SELECT territory.TNUM, territory.TNAME,\
                      sales_rep.SRNUM, sales_rep.SRNAME,\
                      sales_rep.SRADDRESS, sales_rep.SRCITY,\
                      sales_rep.SRSTATE, sales_rep.SRZIP \
                      FROM territory \
                      INNER JOIN sales_rep \
                      ON territory.TNUM = sales_rep.TNO \
                      ORDER BY territory.TNUM, territory.TNAME")
    result = db_cursor.fetchall()

    print("Sales Rep in Territories")
    print(tabulate(result, headers=["Territory Number", "Territory Name", "Sales Rep Number",
                                    "Sales Rep Name", " Sales Rep Address Line 1",
                                    "City", "State", "Zip"], tablefmt='orgtbl'))
    db_cursor.execute("SELECT sales_rep.SRNUM, sales_rep.SRNAME, customer.cnum,\
                       customer.cname, customer.cfladdress, customer.csladdress, \
                       customer.ccity, customer.cstate, customer.czip \
                       FROM sales_rep \
                       INNER JOIN customer \
                       ON sales_rep.SRNUM = customer.salesrepno \
                       ORDER BY sales_rep.SRNUM, sales_rep.SRNAME")
    result = db_cursor.fetchall()
    print("Customers by Sales Rep")
    print(tabulate(result, headers=["Sales Rep Number", "Sales Rep Name", "Customer Number",
                                    "Customer Name", " Customer Address Line 1", "Address Line 2",
                                    "City", "State", "Zip"], tablefmt='orgtbl'))

    with open('Territory_Info.txt', 'w') as f:
        f.write("Sales Rep in Territories\n")
        f.write(tabulate(result, headers=["Territory Number", "Territory Name", "Sales Rep Number",
                                  "Sales Rep Name", " Sales Rep Address Line 1",
                                  "City", "State", "Zip"], tablefmt='orgtbl')+"\n")
        f.write("Customers by Sales Rep\n")
        f.write(tabulate(result, headers=["Sales Rep Number", "Sales Rep Name", "Customer Number",
                                    "Customer Name", " Customer Address Line 1", "Address Line 2",
                                    "City", "State", "Zip"], tablefmt='orgtbl')+"\n")
    f.close()

    reporting()

def reportCustMasterList():
    db_cursor.execute("SELECT customer.cnum,\
                       customer.cfladdress, customer.csladdress, \
                       customer.ccity, customer.cstate, customer.czip, \
                       customer.cstfladdress, customer.cstsladdress, customer.cstcity,\
                       customer.cststate, customer.cstzip, sales_rep.SRNUM, sales_rep.SRNAME, \
                       sales_rep.SRADDRESS, sales_rep.SRCITY, sales_rep.SRSTATE, sales_rep.SRZIP, \
                       territory.TNUM, territory.TNAME \
                       FROM ((customer \
                       INNER JOIN sales_rep \
                       ON customer.salesrepno = sales_rep.SRNUM) \
                       INNER JOIN territory \
                       ON customer.territorynum = territory.TNUM) \
                       ORDER BY customer.cnum")
    results = db_cursor.fetchall()
    print("Customer Master List")
    print(tabulate(results, headers=["Customer Number", "Customer Address Line 1", "Customer Address line 2",
                                     "City", "State", "Zip", "Ship to Address Line 1", "Address line 2",
                                     "City", "State", "Zip", "Sales Rep Number", "Sales Rep Name", "Sales Rep Address",
                                     "City", "State", "ZIP", "Territory Number", "Territory Name"], tablefmt="orgtbl"))

    with open('Customer_Master_List.txt', 'w') as f:
        f.write("Customer Master List\n")
        f.write(tabulate(results, headers=["Customer Number", "Customer Address Line 1", "Customer Address line 2",
                                     "City", "State", "Zip", "Ship to Address Line 1", "Address line 2",
                                     "City", "State", "Zip", "Sales Rep Number", "Sales Rep Name", "Sales Rep Address",
                                     "City", "State", "ZIP", "Territory Number", "Territory Name"], tablefmt="orgtbl")+"\n")
    f.close()

    reporting()

def reportCustOpenOrders():
    db_cursor.execute("SELECT orders.customernum, orders.onum, orderhaspart.prtnum, \
                       orders.odesc, orders.odate, orderhaspart.numordered, \
                       orderhaspart.quotedprice \
                       FROM orders \
                       INNER JOIN orderhaspart \
                       ON orders.onum = orderhaspart.onum \
                       ORDER BY orders.customernum")

    results = db_cursor.fetchall()

    print("Customer Open Orders")
    print(tabulate(results, headers=["Customer Number", "Order Number", "Item Number", "Description",
                                     "Date Ordered", "Quantity", "Price"], tablefmt="orgtbl", floatfmt=".2f"))

    with open('Customer_Open_Orders.txt', 'w') as f:
        f.write("Customer Open Orders\n")
        f.write(tabulate(results, headers=["Customer Number", "Order Number", "Item Number", "Description",
                                     "Date Ordered", "Quantity", "Price"], tablefmt="orgtbl", floatfmt=".2f")+"\n")
    f.close()

    reporting()

def reportItemOpenOrders():
    db_cursor.execute("SELECT orderhaspart.prtnum,orders.customernum, orders.onum, \
                       orders.odesc, orders.odate, orderhaspart.numordered, \
                       orderhaspart.quotedprice \
                       FROM orderhaspart \
                       INNER JOIN orders \
                       ON orderhaspart.onum = orders.onum \
                       ORDER BY orderhaspart.prtnum")

    results = db_cursor.fetchall()

    print("Item Open Orders")
    print(tabulate(results, headers=["Item Number", "Customer Number", "Order Number", "Description",
                                     "Date Ordered", "Quantity", "Price"], tablefmt="github", floatfmt=".2f"))

    with open('Item_Open_Orders.txt', 'w') as f:
        f.write("Customer Open Orders\n")
        f.write(tabulate(results, headers=["Item Number", "Customer Number", "Order Number", "Description",
                                     "Date Ordered", "Quantity", "Price"], tablefmt="github", floatfmt=".2f")+"\n")
    f.close()

    reporting()

def reportDailyInvoice():
    db_cursor.execute("SELECT DISTINCT invoice.ishipdate\
                       FROM invoice")
    dates = db_cursor.fetchall()
    count = 0
    with open('Daily_Invoice.txt', 'w') as f:
        for i in dates:
            db_cursor.execute("SELECT invoice.inum, \
                                customer.cnum, customer.cname, invoice.ishipcharge,\
                                invoice.total \
                                FROM invoice \
                                INNER JOIN orders \
                                ON invoice.orderno = orders.onum \
                                INNER JOIN customer \
                                ON orders.customernum = customer.cnum \
                                WHERE invoice.ishipdate = (%s) \
                                ORDER BY invoice.inum", (i))

            results = db_cursor.fetchall()
            date_string = str(i).replace("(datetime.date(", "")
            date_string = date_string.replace("),)", "")
            date_string = date_string.replace(",", "/")

            count += 1
            print(
                    date_string + "        " + "HOLT DISTRUBUTORS DAILY INVOICE REGISTER" + "         " + "Page " + str(count))
            print(tabulate(results, headers=["Invoice Number", "Customer Number", "Customer Name", "Sales Amount", "Total"],
                       tablefmt="github", floatfmt=".2f"))

            f.write(date_string + "        " + "HOLT DISTRUBUTORS DAILY INVOICE REGISTER" + "         " + "Page " + str(count) + "\n")
            f.write(tabulate(results, headers=["Invoice Number", "Customer Number", "Customer Name", "Sales Amount", "Total"],
                       tablefmt="github", floatfmt=".2f")+"\n")
    f.close()

    reporting()

def reportMonthlyInvoice():
    db_cursor.execute("SELECT DISTINCT EXTRACT(MONTH FROM invoice.ishipdate)\
                       FROM invoice")
    dates = db_cursor.fetchall()
    count = 0
    print(dates)
    with open('Monthly_Invoice.txt', 'w') as f:
        for i in dates:
            db_cursor.execute("SELECT invoice.inum, \
                       customer.cnum, customer.cname, invoice.ishipcharge,\
                       invoice.total \
                       FROM invoice \
                       INNER JOIN orders \
                       ON invoice.orderno = orders.onum \
                       INNER JOIN customer \
                       ON orders.customernum = customer.cnum \
                       WHERE EXTRACT( MONTH FROM invoice.ishipdate) = (%s) \
                       ORDER BY invoice.inum", (i))

            results = db_cursor.fetchall()
            date_string = str(i).replace("(", "")
            date_string = date_string.replace(",)", "")

            count += 1
            print(date_string + "th Month" + "        " + "HOLT DISTRUBUTORS DAILY INVOICE REGISTER" + "         " + "Page " + str(
                    count))
            print(tabulate(results, headers=["Invoice Number", "Customer Number", "Customer Name", "Sales Amount", "Total"],
                       tablefmt="github", floatfmt=".2f"))

            f.write(date_string + "th Month" + "        " + "HOLT DISTRUBUTORS DAILY INVOICE REGISTER" + "         " + "Page " + str(
                    count)+"\n")
            f.write(tabulate(results, headers=["Invoice Number", "Customer Number", "Customer Name", "Sales Amount", "Total"],
                       tablefmt="github", floatfmt=".2f")+"\n")
    f.close()

    reporting()

def reportStockStatus():
    db_cursor.execute("SELECT * FROM part")

    results = db_cursor.fetchall()

    result = []
    with open('Stock_Status.txt', 'w') as f:
        for i in results:
            y = list(i)
            if y[5] <= y[7]:
                y[7] = str(y[7]) + "*"
                print(y[7])
            i = tuple(y)
            result.append(i)
        print(tabulate(result,
                   headers=["Part Number", "Description", "Price", "TD", "YTD", "Units on Hand", "Units Allocated",
                            "Reorder Point"], tablefmt="github", floatfmt=".2f"))
        f.write(tabulate(result,
                   headers=["Part Number", "Description", "Price", "TD", "YTD", "Units on Hand", "Units Allocated",
                            "Reorder Point"], tablefmt="github", floatfmt=".2f")+"\n")
    f.close()

    reporting()

def reorderPointList():
    db_cursor.execute("SELECT * FROM part")

    results = db_cursor.fetchall()

    result = []
    with open('Reorder_Point_List.txt', 'w') as f:
        for i in results:
            y = list(i)
            if y[5] < y[7]:
                y[7] = str(y[7]) + "*"
                print(y[7])
                i = tuple(y)
                result.append(i)

        print(tabulate(result,
                headers=["Part Number", "Description", "Price", "TD", "YTD", "Units on Hand", "Units Allocated",
                        "Reorder Point"], tablefmt="github", floatfmt=".2f"))
        f.write(tabulate(result,
                   headers=["Part Number", "Description", "Price", "TD", "YTD", "Units on Hand", "Units Allocated",
                            "Reorder Point"], tablefmt="github", floatfmt=".2f")+"\n")
    f.close()

    reporting()

def reportVendorList():
    db_cursor.execute("SELECT * FROM vendor")

    vendors = db_cursor.fetchall()
    with open('Vendor_List.txt', 'w') as f:
        for i in vendors:
            vnum = i[0]
            print("Vendor Number: ", i[0])
            print("Vendor Name: ", i[1])
            print("Address: ", i[2] + " ,", i[3])
            print(i[4] + ",", i[5])
            db_cursor.execute("SELECT VNUM, PRTNUM, VPRICE, MINQUANTITY, EXPECTEDTIME FROM supplies WHERE VNUM = (%s)",
                                (i[0],))
            supplies = db_cursor.fetchall()
            print(tabulate(supplies, headers=["Vendor Number", "Part Number", "VPRICE", "Mininum Quantity", "Expected By"],
                        tablefmt="github", floatfmt=".2f"))
            f.write("Vendor Number: " + str(i[0]))
            f.write("\nVendor Name: " + str(i[1]))
            f.write("\nAddress: " + str(i[2]) + " ," + str(i[3]))
            f.write("\n" + str(i[4]) + "," + str(i[5]) + "\n")
            f.write(tabulate(supplies, headers=["Vendor Number", "Part Number", "VPRICE", "Mininum Quantity", "Expected By"],
                        tablefmt="github", floatfmt=".2f")+"\n")
    f.close()

    reporting()

def reportDailyCash():
    db_cursor.execute("SELECT DISTINCT pydate FROM payment")
    dates = db_cursor.fetchall()

    with open('Daily_Cash.txt', 'w') as f:
        for i in dates:
            db_cursor.execute("SELECT payment.pynum, payment.customer, customer.cname, payment.pyamt \
                               FROM payment \
                               INNER JOIN customer \
                               ON payment.customer = customer.cnum\
                               WHERE pydate = (%s)", (i))
            results = db_cursor.fetchall()
            date_string = str(i).replace("(datetime.date(", "")
            date_string = date_string.replace("),)", "")
            date_string = date_string.replace(",", "/")
            print(date_string + "        " + "HOLT DISTRIBUTORS DAILY CASH RECIEPTS")
            print(tabulate(results, headers=["Payment No.", "Customer Number", "Customer Name", "Payment Amount"],
                           tablefmt="github", floatfmt=".2f"))
            f.write(date_string + "        " + "HOLT DISTRIBUTORS DAILY CASH RECIEPTS\n")
            f.write(tabulate(results, headers=["Payment No.", "Customer Number", "Customer Name", "Payment Amount"],
                           tablefmt="github", floatfmt=".2f")+"\n")
    f.close()

    reporting()

def reportMonthlyCash():
    db_cursor.execute("SELECT DISTINCT MONTH(pydate) FROM payment")
    months = db_cursor.fetchall()

    with open('Monthly_Cash.txt', 'w') as f:
        for i in months:
            db_cursor.execute("SELECT payment.pynum, payment.customer, customer.cname, payment.pyamt \
                               FROM payment \
                               INNER JOIN customer \
                               ON payment.customer = customer.cnum\
                               WHERE MONTH (pydate) = (%s)", (i))
            results = db_cursor.fetchall()
            date_string = str(i).replace("(", "")
            date_string = date_string.replace(",)", "")
            print(date_string + "        " + "HOLT DISTRIBUTORS DAILY CASH RECIEPTS")
            print(tabulate(results, headers=["Payment No.", "Customer Number", "Customer Name", "Payment Amount"],
                           tablefmt="github", floatfmt=".2f"))
            f.write(date_string + "        " + "HOLT DISTRIBUTORS DAILY CASH RECIEPTS\n")
            f.write(tabulate(results, headers=["Payment No.", "Customer Number", "Customer Name", "Payment Amount"],
                           tablefmt="github", floatfmt=".2f")+"\n")
    f.close()

    reporting()

def reportCustMail():
    db_cursor.execute("SELECT cstfladdress, csladdress, cstcity, \
                      cststate, cstzip \
                      FROM customer")
    stamp = db_cursor.fetchall()
    with open('Customer_Mail.txt', 'w') as f:
        for i in stamp:
            print("")
            print("Address: ", i[0])
            print(i[1])
            print(str(i[2]) + " ," + str(i[3]) + " ," + str(i[4]))
            print("")

            f.write("\n")
            f.write("Address: " + i[0]+"\n")
            f.write(str(i[1])+"\n")
            f.write(str(i[2]) + " ," + str(i[3]) + " ," + str(i[4])+"\n")
            f.write("\n")

    f.close()

    reporting()

def reportStatements():
    today = date.today()
    month = today.month
    today = today.strftime("%m/%d/%y")

    db_cursor.execute("SELECT customer.cnum, customer.cname,\
                      customer.cfladdress, customer.csladdress,\
                      customer.ccity, customer.cstate, customer.czip, \
                      sales_rep.SRADDRESS, sales_rep.SRCITY, sales_rep.SRSTATE,\
                      sales_rep.SRZIP \
                      FROM customer\
                      INNER JOIN sales_rep\
                      ON customer.salesrepno = sales_rep.SRNUM")

    customer = db_cursor.fetchall()

    prev_balance = 0
    current_invoice = 0
    current_payment = 0
    current_balance = 0
    balance = 0
    for i in customer:
        print("                         " + "HOLT DISTRIBUTORS" + "                       " + today)
        print("                         " + i[7])
        print("                         " + i[8] + ", " + i[9] + " ", i[10])
        print("Customer Number: ", i[0])
        print(i[1])
        print(i[2])
        print(i[3])
        print(i[4] + ", " + i[5], i[6])

        db_cursor.execute("SELECT invoice.inum, invoice.ishipdate, invoice.total \
                          FROM invoice \
                          INNER JOIN orders \
                          ON invoice.orderno = orders.onum \
                          WHERE orders.customernum = (%s)", (i[0],))

        invoice = db_cursor.fetchall()
        invoices = []
        for voice in invoice:
            voice = list(voice)
            voice.append("invoice")
            invoices.append(voice)

        db_cursor.execute("SELECT payment.pynum, payment.pydate, pyamt \
                          FROM payment \
                          WHERE customer = (%s)", (i[0],))

        payment = db_cursor.fetchall()
        payments = []
        for pay in payment:
            pay = list(pay)
            pay.append("payment")
            payments.append(pay)

        all_transactions = payments + invoices
        reciept = []
        for transaction in all_transactions:
            if (transaction[1].month < 11):
                if transaction[3] == "payment":
                    prev_balance = prev_balance - transaction[2]
                elif transaction[3] == "invoice":
                    prev_balance = prev_balance + transaction[2]
            elif (transaction[1].month == 11):
                if transaction[3] == "payment":
                    current_payment += transaction[2]
                    current_balance = current_balance - transaction[2]
                elif transaction[3] == "invoice":
                    current_invoice += transaction[2]
                    balance = balance + transaction[2]

                amount = transaction.pop(2)
                transaction.append(amount)
                transaction.append(balance)
                reciept.append(transaction)
        current_balance = prev_balance + current_invoice - current_payment
        db_cursor.execute("SELECT CREDITLIMIT FROM customer_sales\
                                          WHERE CNUM = (%s)", (i[0],))
        credit_limit = float(db_cursor.fetchall()[0][0])
        reciept_bottom = [[credit_limit, prev_balance, current_invoice, current_payment, current_balance]]
        print(tabulate(reciept, headers=["Inv/Pay Number", "Date", "Type",
                                         "Amount", "Balance"], tablefmt="github", floatfmt=".2f"))
        print(tabulate(reciept_bottom, headers=["Credit Limit", "Prev Balance", "Current Invoice",
                                                "Current Payment", "Current Balance"],
                       tablefmt="github", floatfmt=".2f"))

        with open ('Monthly_Statements.txt', 'w') as f:
            for i in customer:
                f.write("\n                         " + "HOLT DISTRIBUTORS" + "                       " + today)
                f.write("\n                         " + str(i[7]))
                f.write("\n                         " + str(i[8]) + ", " + str(i[9]) + " " + str(i[10]))
                f.write("\nCustomer Number: " + str(i[0]))
                f.write("\n" + str(i[1]))
                f.write("\n" + str(i[2]))
                f.write("\n" + str(i[3]))
                f.write("\n" + str(i[4]) + ", " + str([5]) + str(i[6]))
                f.write(tabulate(reciept, headers=["Inv/Pay Number", "Date", "Type",
                                         "Amount", "Balance"], tablefmt="github", floatfmt=".2f")+ "\n")
                f.write(tabulate(reciept_bottom, headers=["Credit Limit", "Prev Balance", "Current Invoice",
                                                "Current Payment", "Current Balance"],
                       tablefmt="github", floatfmt=".2f")+"\n")
        f.close()

    reporting()

def reportMonthlyComReport():
    db_cursor.execute("SELECT sales_rep.SRNUM, sales_rep.SRNAME, \
                       sales_rep.SRADDRESS, sales_rep.SRCITY, sales_rep.SRSTATE,\
                       sales_rep.SRZIP, sales_rep_sales.SRMTDSALES, sales_rep_sales.SRYTDSALES, \
                       sales_rep_sales.SRMTDCOMMISSION, sales_rep_sales.SRYTDCOMMISSION, \
                       sales_rep_sales.SRCOMISSIONRATE\
                       FROM sales_rep \
                       INNER JOIN sales_rep_sales \
                       ON sales_rep.SRNUM = sales_rep_sales.SRNUM")

    sales_rep = db_cursor.fetchall()

    print("                        " + "HOLT DISTRIBUTORS MONTHLY COMMISSION REPORT")
    print((tabulate(sales_rep, headers=["Sales Rep Number", "Sales Rep Name", "Address", "City",
                                        "State", "Zip", "MTD Sales", "YTD Sales", "MTD commission",
                                        "YTD commission", "Commission Rate"], tablefmt="github", floatfmt=".2f")))

    with open('Monthly_Commission_Report.txt', 'w') as f:
        f.write("                        " + "HOLT DISTRIBUTORS MONTHLY COMMISSION REPORT\n")
        f.write((tabulate(sales_rep, headers=["Sales Rep Number", "Sales Rep Name", "Address", "City",
                                        "State", "Zip", "MTD Sales", "YTD Sales", "MTD commission",
                                        "YTD commission", "Commission Rate"], tablefmt="github", floatfmt=".2f")+"\n"))
    f.close()

    reporting()

def reportTrailBalance():
    today = date.today()
    month = today.month
    today = today.strftime("%m/%d/%y")

    msg = "Enter Date in mm-dd-yyyy format"
    title = "Aged Trail Balance"
    fieldNames = ["Start Date", "End Date"]
    fieldValues = []  # we start with blanks for the values
    fieldValues = multenterbox(msg, title, fieldNames)

    while 1:  # do forever, until we find acceptable values and break out
        if fieldValues == None:
            break
        errmsg = ""

        # look for errors in the returned values
        for i in range(len(fieldNames)):
            if fieldValues[i].strip() == "":
                errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])

        if errmsg == "":
            break  # no problems found
        else:
            # show the box again, with the errmsg as the message
            fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)

    start_date = fieldValues[0].split("-")
    start_day = int(start_date[0])
    start_month = int(start_date[1])
    start_year = int(start_date[2])
    start_date = datetime.date(start_year, start_month, start_day)

    end_date = fieldValues[1].split("-")
    end_day = int(end_date[0])
    end_month = int(end_date[1])
    end_year = int(end_date[2])
    end_date = datetime.date(end_year, end_month, end_day)
    print(end_date)

    db_cursor.execute("SELECT customer.cnum, customer.cname,\
                      customer.cfladdress, customer.csladdress,\
                      customer.ccity, customer.cstate, customer.czip, \
                      sales_rep.SRADDRESS, sales_rep.SRCITY, sales_rep.SRSTATE,\
                      sales_rep.SRZIP \
                      FROM customer\
                      INNER JOIN sales_rep\
                      ON customer.salesrepno = sales_rep.SRNUM")

    customer = db_cursor.fetchall()

    prev_balance = 0
    current_invoice = 0
    current_payment = 0
    current_balance = 0
    balance = 0
    with open('Trail_Balance_Report.txt', 'w') as f:
        for i in customer:
            print("                         " + "HOLT DISTRIBUTORS" + "                       " + today)
            print("                         " + i[7])
            print("                         " + i[8] + ", " + i[9] + " ", i[10])
            print("Customer Number: ", i[0])
            print(i[1])
            print(i[2])
            print(i[3])
            print(i[4] + ", " + i[5], i[6])

            f.write("\n                         " + "HOLT DISTRIBUTORS" + "                       " + today)
            f.write("\n                         " + str(i[7]))
            f.write("\n                         " + str(i[8]) + ", " + str(i[9]) + " " + str(i[10]))
            f.write("\nCustomer Number: " + str(i[0]))
            f.write("\n" + str(i[1]))
            f.write("\n" + str(i[2]))
            f.write("\n" + str(i[3]))
            f.write("\n" + str(i[4]) + ", " + str([5]) + str(i[6])+"\n")

            db_cursor.execute("SELECT invoice.inum, invoice.ishipdate, invoice.total \
                              FROM invoice \
                              INNER JOIN orders \
                              ON invoice.orderno = orders.onum \
                              WHERE orders.customernum = (%s)", (i[0],))

            invoice = db_cursor.fetchall()
            invoices = []
            for voice in invoice:
                voice = list(voice)
                voice.append("invoice")
                invoices.append(voice)

            db_cursor.execute("SELECT payment.pynum, payment.pydate, pyamt \
                              FROM payment \
                              WHERE customer = (%s)", (i[0],))

            payment = db_cursor.fetchall()
            payments = []
            for pay in payment:
                pay = list(pay)
                pay.append("payment")
                payments.append(pay)

            all_transactions = payments + invoices
            reciept = []
            for transaction in all_transactions:
                if (transaction[1] < start_date):
                    if transaction[3] == "payment":
                        prev_balance = prev_balance - transaction[2]
                    elif transaction[3] == "invoice":
                        prev_balance = prev_balance + transaction[2]
                elif (transaction[1] >= start_date and transaction[1] < end_date):
                    if transaction[3] == "payment":
                        current_payment += transaction[2]
                        current_balance = current_balance - transaction[2]
                    elif transaction[3] == "invoice":
                        current_invoice += transaction[2]
                        balance = balance + transaction[2]

                    amount = transaction.pop(2)
                    transaction.append(amount)
                    transaction.append(balance)
                    reciept.append(transaction)
            current_balance = prev_balance + current_invoice - current_payment
            db_cursor.execute("SELECT CREDITLIMIT FROM customer_sales\
                                              WHERE CNUM = (%s)", (i[0],))
            credit_limit = float(db_cursor.fetchall()[0][0])
            reciept_bottom = [[credit_limit, prev_balance, current_invoice, current_payment, current_balance]]
            print(tabulate(reciept, headers=["Inv/Pay Number", "Date", "Type",
                                             "Amount", "Balance"], tablefmt="github", floatfmt=".2f"))
            print(tabulate(reciept_bottom, headers=["Credit Limit", "Prev Balance", "Current Invoice",
                                                    "Current Payment", "Current Balance"],
                           tablefmt="github", floatfmt=".2f"))
            f.write(tabulate(reciept, headers=["Inv/Pay Number", "Date", "Type",
                                               "Amount", "Balance"], tablefmt="github", floatfmt=".2f") + "\n")
            f.write(tabulate(reciept_bottom, headers=["Credit Limit", "Prev Balance", "Current Invoice",
                                                      "Current Payment", "Current Balance"],
                             tablefmt="github", floatfmt=".2f") + "\n")


    f.close()

    reporting()

def reporting():
    title = "Reporting Options"

    msg = "Select an option"

    choice = ["Territory List", "Customer Master List", "Open Orders by Customer",
              "Open Orders by Item", "Daily Invoice Register", "Monthly Invoice Register",
              "Stock Status Report", "Reorder Point List", "Vendor List",
              "Daily Cash Reciepts Journal", "Monthly Cash Receipts Journal",
              "Customer Mailing Labels", "Statements", "Monthly Sales Rep Commision Report",
              "Aged Trail Balance", "Return to Main Menu"]

    output = choicebox(msg, title, choice)
    if output == "Territory List":
        reportTerList()
    elif output == "Customer Master List":
        reportCustMasterList()
    elif output == "Open Orders by Customer":
        reportCustOpenOrders()
    elif output == "Open Orders by Item":
        reportItemOpenOrders()
    elif output == "Daily Invoice Register":
        reportDailyInvoice()
    elif output == "Monthly Invoice Register":
        reportMonthlyInvoice()
    elif output == "Stock Status Report":
        reportStockStatus()
    elif output == "Reorder Point List":
        reorderPointList()
    elif output == "Vendor List":
        reportVendorList()
    elif output == "Daily Cash Reciepts Journal":
        reportDailyCash()
    elif output == "Monthly Cash Receipts Journal":
        reportMonthlyCash()
    elif output == "Customer Mailing Labels":
        reportCustMail()
    elif output == "Statements":
        reportStatements()
    elif output == "Monthly Sales Rep Commision Report":
        reportMonthlyComReport()
    elif output == "Aged Trail Balance":
        reportTrailBalance()
    elif output == "Return to Main Menu":
        main()
##############################################################################################
#                                                                                            #
#                                   TRANSACTIONS                                             #
#                                                                                            #
#                                                                                            #
##############################################################################################

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

    db_cursor.execute("SELECT MAX(cnum) FROM customer")
    cnum = db_cursor.fetchall()[0][0]+1

    if shipping:
        fieldnames = ["Name", "FL Address", "SL Address", "City", "State", "Zip", "FL Shipping Address",
                      "SL Shipping Address", "Shipping City", "Shipping State", "Shipping Zip", "Territory Number",
                      "Sales Rep Number", "Balance", "Credit Limit"]
        output = multenterbox(msg, title, fieldnames)


        name, faddr, saddr, city, st, zipc, sfaddr, ssaddr, scity, sst, szipc, tnum, snum, bal, cl = output

    else:
        fieldnames = ["Name", "FL Address", "SL Address", "City", "State", "Zip",
                      "Territory Number", "Sales Rep Number", "Balance", "Credit Limit"]
        output = multenterbox(msg, title, fieldnames)

        name, faddr, saddr, city, st, zipc, tnum, snum, bal, cl = output
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

    title = "Modify Customer"
    msg = "Select Customer You Wish To Alter"
    cname = choicebox(msg, title, listb)

    tsql = "SELECT cnum FROM customer WHERE cname='" + cname + "'"
    db_cursor.execute(tsql)
    myresult = db_cursor.fetchone()
    cnum = myresult[0]

    msg = "Enter Customer Information"
    title = "Update Customer"
    messages = ["cname", "cfladdress","csladdress", "ccity", "cstate", "czip", "cstfladdress", "cstsladdress", "cstcity", "cststate", "cstzip", "territorynum", "salesrepno"]
    output = []
    for msg in messages:
        db_cursor.execute("SELECT " + msg + " FROM customer WHERE cnum=" + str(cnum))
        strforchoice = db_cursor.fetchall()
        choice1 = enterbox(msg, "Modify Customer", default=strforchoice[0])
        output.append(choice1)

    cname, cfladdress,csladdress, ccity, cstate, czip, cstfladdress, cstsladdress, cstcity, cststate, cstzip, territorynum, salesrepno = output
    tsql = "UPDATE customer SET cname=%s, cfladdress=%s, csladdress=%s, ccity=%s, cstate =%s, czip=%s, cstfladdress=%s, cstsladdress=%s, cstcity=%s, cststate=%s, cstzip=%s, territorynum=%s, salesrepno=%s WHERE(cnum=%s)"
    val = (cname, cfladdress, csladdress, ccity, cstate, czip, cstfladdress, cstsladdress, cstcity, cststate, cstzip, territorynum, salesrepno, cnum)
    db_cursor.execute(tsql, val)

    db_connection.commit()

    print(db_cursor.rowcount, "record updated.")

    printTable("customer")


def insertSalesRep():
    msg = "Enter Sales Rep Information"
    title = "Add New Sales Rep"
    fieldNames = ["Name", "Address", "City", "State", "ZIP",
                  "Commission Rate", "Territory Number"]
    fieldValues = multenterbox(msg, title, fieldNames)
    srname, sraddr, srcity, srstate, srzip, srcomm, tnum = fieldValues

    db_cursor.execute("SELECT MAX(srnum) FROM sales_rep")
    srint= db_cursor.fetchall()[0][0]+1

    tsql = "INSERT INTO sales_rep_sales VALUES (%s,0,0,0,0,%s,%s)"
    val = (srint, float(srcomm), int(tnum),)
    db_cursor.execute(tsql, val)

    db_connection.commit()

    print(db_cursor.rowcount, "record inserted.")

    printTable("sales_rep_sales")

    tsql = "INSERT INTO sales_rep VALUES (%s,%s,%s,%s,%s,%s,%s)"
    val = (srint, srname, sraddr, srcity, srstate, int(srzip), int(tnum))
    db_cursor.execute(tsql, val)

    db_connection.commit()

    #print(db_cursor.rowcount, "record inserted.")

    printTable("sales_rep_sales")


def modifySalesRep():

    db_cursor.execute("SELECT SRNAME FROM sales_rep")
    myresult = db_cursor.fetchall()
    lista = str(myresult)
    lista = lista.split("'")
    count = 0
    listb = []
    for x in lista:
        count += 1
        if (count % 2 == 0):
            listb.append(x)

    title = "Modify Sales Rep"
    msg = "Select Sales Rep You Wish To Alter"
    srname = choicebox(msg, title, listb)

    tsql = "SELECT SRNUM FROM sales_rep WHERE SRNAME='" + srname + "'"
    db_cursor.execute(tsql)
    myresult = db_cursor.fetchone()
    srnum = myresult[0]

    msg = "Enter Sales Rep Information"
    title = "Update Sales Rep"
    messages = ["SRNAME", "SRADDRESS", "SRCITY", "SRSTATE", "SRZIP","TNO"]
    output = []
    for msg in messages:
        db_cursor.execute("SELECT " + msg + " FROM sales_rep WHERE srnum=" + str(srnum))
        strforchoice = db_cursor.fetchall()
        choice1 = enterbox(msg, "Modify Vendor", default=strforchoice[0])
        output.append(choice1)

    SRNAME, SRADDRESS, SRCITY, SRSTATE, SRZIP,TNO = output
    tsql = "UPDATE sales_rep SET SRNAME=%s, SRADDRESS=%s, SRCITY=%s, SRSTATE=%s, SRZIP=%s, TNO=%s WHERE(srnum=%s)"
    val = (SRNAME, SRADDRESS, SRCITY, SRSTATE, SRZIP,TNO, srnum)
    db_cursor.execute(tsql, val)

    db_connection.commit()

    print(db_cursor.rowcount, "record updated.")

    printTable("vendor")


def insertPart():
    msg = "Enter Part Information"
    title = "Add New Part"
    fieldNames = ["Part ID", "Description", "Price", "Units On Hand", "Reorder Point"]
    fieldValues = multenterbox(msg, title, fieldNames)

    partnumber, partdescription, partprice, partunitsonhand, partreorderpoint = fieldValues

    tsql = "INSERT INTO part VALUES (%s, %s, %s, 0, 0, %s, 0, %s)"
    val = (partnumber, partdescription, partprice, partunitsonhand, partreorderpoint)

    db_cursor.execute(tsql, val)
    db_connection.commit()

    print(db_cursor.rowcount, "record inserted.")

    printTable("part")


def modifyPart():
    db_cursor.execute("SELECT prtnum, prtdesc FROM part")
    title = "Modify Part"
    msg = str(db_cursor.fetchall())
    dtext = "Enter number you wish to modify"

    output = enterbox(msg, title, dtext)

    msg = "Enter Part Information"
    title = "Update Part"
    fieldNames = ["Description", "Price", "Units On Hand", "Reorder Point"]
    fieldValues = multenterbox(msg, title, fieldNames)

    desc, price, uoh, rp = fieldValues

    tsql = "UPDATE part SET prtdesc=%s, prtprice=%s, prtunitsonhand=%s, prtreorderpoint=%s WHERE(prtnum=%s)"
    val = (desc, price, uoh, rp, output)
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
            deleteFromTable("srnum","srname", tblname)
        if tblname == "customer":
            deleteFromTable("cnum","cname", tblname)
        if tblname == "vendor":
            deleteFromTable("vnum", "vname", tblname)
        if tblname == "part":
            deleteFromTable("prtnum", tblname)
    if reply == "Return to Main Menu":
        main()


def newPayment():
    db_cursor.execute("SELECT MAX(pynum) FROM payment")
    strrow = str(db_cursor.fetchall())
    str1 = strrow.split(',')
    first = str1[0]
    fr = int(first[2:]) + 1

    msg = "Enter Payment Information"
    title = "Add Payment"
    fieldNames = ["Day", "Month", "Year", "Amount", "Customer ID"]
    fieldValues = multenterbox(msg, title, fieldNames)

    dy, mth, yr, amt, cid = fieldValues
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
    fr = int(first[2:]) + 1

    msg = "Enter Order Information"
    title = "Add Order"
    fieldNames = ["Day", "Month", "Year", "Order Number", "Description", "Customer ID",
                  "Part Number", "Amount of Parts"]
    fieldValues = multenterbox(msg, title, fieldNames)

    dy, mth, yr, onum, desc, cid, prtnum, prtamt = fieldValues

    tsql = "SELECT prtnum, prtdesc, prtprice FROM part WHERE (prtnum= %s );"
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

    db_cursor.execute("SELECT MAX(ocustponum) FROM orders WHERE (customernum=" + cid + ")");
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


########################################################################################################
#                                                                                                      #
#                                                                                                      #
#                               MONTH END TRANSACTIONS                                                 #
#                                                                                                      #
########################################################################################################

def resetInvoice():
    title = "Reset Invoice, Current Payment, and Current Balance"

    msg = "Are you sure you want to Proceed? Hitting yes will set the current invoice total to zero, \
           set the current payment total to zero and the previous balance will be set to the current \
           balance in preparation for the coming month"

    choices = ["Yes", "No"]

    output = choicebox(msg, title, choices)
    if output == "Yes":
        db_cursor.execute("UPDATE customer_sales SET customer_sales.INVOICETOTAL = 0, customer_sales.CURPAYMENT = 0, \
                           customer_sales.PREVBALANCE = customer_sales.BALANCE")
        db_cursor.execute("SELECT * FROM customer_sales")
        test = db_cursor.fetchall()
        print(tabulate(test))

        db_connection.commit()

    if output == "No":
        main()
    pass


def resetMTDYTD():
    title = "Resetting all MTD fields and YTD fields"

    msg = "Is it year end?"

    choices = ["Yes", "No", "Return to Main Menu"]

    output = choicebox(msg, title, choices)
    if output == "Yes":
        db_cursor.execute("UPDATE customer_sales SET customer_sales.MTDSALES = 0, customer_sales.YTDSALES = 0")
        db_cursor.execute("SELECT * FROM customer_sales")
        test = db_cursor.fetchall()
        print(tabulate(test))

        db_cursor.execute("UPDATE sales_rep_sales SET sales_rep_sales.SRMTDSALES = 0, sales_rep_sales.SRMTDCOMMISSION = 0, \
                                   sales_rep_sales.SRYTDSALES = 0, sales_rep_sales.SRYTDCOMMISSION = 0")
        db_cursor.execute("SELECT * FROM sales_rep_sales")
        test2 = db_cursor.fetchall()
        print(tabulate(test2))

        db_connection.commit()

    elif output == "No":
        db_cursor.execute("UPDATE customer_sales SET customer_sales.MTDSALES = 0")
        db_cursor.execute("SELECT * FROM customer_sales")
        test = db_cursor.fetchall()
        print(tabulate(test))

        db_cursor.execute("UPDATE sales_rep_sales SET sales_rep_sales.SRMTDSALES = 0, sales_rep_sales.SRMTDCOMMISSION = 0")
        db_cursor.execute("SELECT * FROM sales_rep_sales")
        test2 = db_cursor.fetchall()
        print(tabulate(test2))

        db_connection.commit()

    elif output == "Return to Main Menu":
        main()
    pass


def removeRec():
    title = "Remove all Cash Receipts and Invoice Summary Records"

    msg = "Are you sure you want to delete all cash receipts and invoice summary records?"

    choices = ["Yes", "No"]
    output = choicebox(msg, title, choices)
    if output == "Yes":
        db_cursor.execute("DROP TABLE invoice, payment")
        db_connection.commit()
    if output == "No":
        main()
    pass


def monthEnd():
    title = "Month-End Processing"

    msg = "Select an option"

    choices = ["Update Customer Account Info", "Reset Invoice, Current Payment, and Current Balance", "Print Monthly Invoice & Cash Receipts",
               "Print Monthly Sales Commission Report", "Zero out MTD/YTD", "Remove Cash Receipts & Invoice Records",
               "Return to Main Menu"]

    output = choicebox(msg, title, choices)
    if output == "Update Customer Account Info":
        reportStatements()
    elif output == "Reset Invoice, Current Payment, and Current Balance":
        resetInvoice()
    elif output == "Print Monthly Invoice":
        reportMonthlyInvoice()
        reportMonthlyCash()
    elif output == "Print Monthly Sales Commission Report":
        reportMonthlyComReport()
    elif output == "Zero out MTD/YTD":
        resetMTDYTD()
    elif output == "Remove Cash Receipts & Invoice Records":
        removeRec()
    elif output == "Return to Main Menu":
        main()
#############################################################################################
#                                   INVOICE CYCLING                                         #
#                                                                                           #
#                                                                                           #
#############################################################################################


def updateOrdersShipped(shipped, orderno):

    db_cursor.execute("UPDATE orderhaspart \
                       SET numordered = %s \
                       WHERE onum = %s", [(shipped),(orderno)])
    db_connection.commit()

def updateCustomer(cnum, total, pre_tax):

    db_cursor.execute("UPDATE customer_sales \
                      SET \
                      INVOICETOTAL = INVOICETOTAL + %s,\
                      MTDSALES = MTDSALES + %s,\
                      YTDSALES = YTDSALES + %s,\
                      BALANCE = BALANCE + %s \
                      WHERE CNUM = %s", [total, pre_tax, pre_tax, total, cnum])
    db_connection.commit()



def updateSalesRep(srno, total, pre_tax):
    db_cursor.execute("SELECT SRCOMISSIONRATE FROM sales_rep_sales\
                      WHERE SRNUM = %s", (srno,))
    c_rate = db_cursor.fetchall()[0][0]
    c_total = pre_tax*c_rate

    db_cursor.execute("UPDATE sales_rep_sales \
                      SET \
                      SRMTDSALES = SRMTDSALES + %s,\
                      SRYTDSALES = SRYTDSALES + %s,\
                      SRMTDCOMMISSION = SRMTDCOMMISSION + %s, \
                      SRYTDCOMMISSION = SRYTDCOMMISSION + %s  \
                      WHERE SRNUM = %s", [pre_tax, pre_tax, c_total, c_total, srno])

    db_connection.commit()

def updateParts(orderno):
    db_cursor.execute("SELECT prtnum, numordered \
                       FROM orderhaspart \
                       WHERE onum = %s", (orderno,))

    part_nos = db_cursor.fetchall()

    for parts in part_nos:
        part_no = parts[0]
        part_quantity = parts[1]
        db_cursor.execute("UPDATE part \
                          SET \
                          PRTUNITSONHAND = PRTUNITSONHAND - %s, \
                          PRTUNITSALLOCATED = PRTUNITSALLOCATED - %s \
                          WHERE PRTNUM = %s", [part_quantity,part_quantity,part_no])
    db_connection.commit()


def deleteReleasedOrders(orderno):
    db_cursor.execute("DELETE FROM invoice \
                       WHERE orderno = %s", (orderno,))
    db_cursor.execute("DELETE FROM orderhaspart \
                       WHERE onum = %s", (orderno,))
    db_cursor.execute("DELETE FROM orders \
                      WHERE onum = %s", (orderno,))
    db_connection.commit()


def printInvoice(inum, onum, shipped):
    today = date.today()
    today = today.strftime("%m/%d/%y")

    db_cursor.execute("SELECT invoice.inum, orders.ocustponum, \
                       orders.odate, customer.cnum, \
                       customer.cname, customer.cfladdress, customer.csladdress, \
                       customer.ccity, customer.cstate, customer.czip, customer.cstfladdress, \
                       customer.cstsladdress, customer.cstcity, customer.cststate, customer.cstzip, \
                       sales_rep.srnum, sales_rep.srname \
                       FROM invoice \
                       INNER JOIN orders \
                       ON invoice.orderno = orders.onum \
                       INNER JOIN customer \
                       ON orders.customernum = customer.cnum \
                       INNER JOIN sales_rep \
                       ON customer.salesrepno = sales_rep.srnum \
                       WHERE invoice.inum = %s", (inum,) )


    info = db_cursor.fetchall()
    inum = info[0][0]
    cponum = info[0][1]
    odate = info[0][2]
    cnum = info[0][3]
    cname = info[0][4]
    caddress1 = info[0][5]
    caddress2 = info[0][6]
    ccity = info[0][7]
    cstate = info[0][8]
    czip = info[0][9]
    saddress1 = info[0][10]
    saddress2 = info[0][11]
    scity = info[0][12]
    sstate = info[0][13]
    szip = info[0][14]
    srno = info[0][15]
    srname = info[0][16]
    sales_rep = str(srno)+ "-" +srname

    print("                                   INVOICE                                         ")
    print(today + "                                                           Invoice No.: ",inum)
    print("                         " + "HOLT DISTRIBUTORS" + "                               ")
    print("Sold To:                                                        Ship To: ")
    print(cname)
    print(caddress1 + "                                                                     " + saddress1)
    print(caddress2 + "                                                                    " + saddress2)
    print(ccity + ", " + cstate, czip, "                                                          " + scity + ", " + sstate, szip)
    table1 = [[cnum, cponum, odate, sales_rep]]
    print(tabulate(table1, headers=["Cust No.", "P.O. No.", "Order Date", "SLS-REP"]
                       , tablefmt="github", floatfmt=".2f"))

    db_cursor.execute("SELECT orderhaspart.prtnum, part.PRTDESC, orderhaspart.quotedprice, orderhaspart.numordered \
                      FROM orderhaspart \
                      INNER JOIN part \
                      ON orderhaspart.prtnum = part.PRTNUM \
                      WHERE orderhaspart.onum = %s", (onum,))
    orders = db_cursor.fetchall()

    table2 = [[]]
    count = 0
    for order in orders:
        partnum = order[0]
        desc = order[1]
        qp = order[2]
        quantity = order[3]
        amount = qp*quantity
        table2.append([partnum,desc,qp,quantity,shipped[count],amount])
        count = count +1


    print(tabulate(table2, headers=["Item No.", "Description", "Unit Price",
                                                "Order-Qty", "Ship-Qty", "Amount"],
                       tablefmt="github", floatfmt=".2f"))

    db_cursor.execute("SELECT ishipcharge, itax, total \
                       FROM invoice \
                       WHERE inum = %s", (inum,))
    details = db_cursor.fetchall()

    ship_price = details [0][0]
    tax = details[0][1]
    total = details[0][2]

    print("                                                                    Shipping:", ship_price)
    print("                                                                        Tax: ", tax)
    print("Comment:                                                            Total: ", total)

    with open('Invoice_Report.txt', 'w') as f:
        f.write("                                   INVOICE                                         \n")
        f.write(today + "                                                           Invoice No.: " + str(inum) + "\n")
        f.write("                         " + "HOLT DISTRIBUTORS" + "                               \n")
        f.write("Sold To:                                                        Ship To: \n")
        f.write(cname)
        f.write(caddress1 + "                                                                     " + saddress1 + "\n")
        f.write(caddress2 + "                                                                    " + saddress2 + "\n")
        f.write(ccity + ", " + cstate + str(czip) + \
                "                                                          " + scity + ", " + sstate + str(szip) + "\n")

        f.write(tabulate(table1, headers=["Cust No.", "P.O. No.", "Order Date", "SLS-REP"]
                         , tablefmt="github", floatfmt=".2f") + "\n")
        f.write(tabulate(table2, headers=["Item No.", "Description", "Unit Price",
                                          "Order-Qty", "Ship-Qty", "Amount"],
                         tablefmt="github", floatfmt=".2f") + "\n")

        f.write("                                                                    Shipping:" + str(ship_price)+"\n")
        f.write("                                                                        Tax: " + str(tax) +"\n")
        f.write("Comment:                                                            Total: " + str(total) +"\n")

    f.close()

def getTotal(inum):

    db_cursor.execute("SELECT total FROM invoice \
                      WHERE inum = %s", (inum,))
    total = db_cursor.fetchall()[0][0]
    return total

def getPreTax(onum):
    db_cursor.execute("SELECT SUM(numordered*quotedprice) \
                       FROM orderhaspart \
                       WHERE onum = %s", (onum,))
    pre_tax = db_cursor.fetchall()[0][0]
    return pre_tax

def createInvoiceRecord(invoice_record):
    inum = invoice_record[0]
    date = invoice_record[1]
    cnum = invoice_record[2]
    srnum = invoice_record[3]
    invoice_total = invoice_record[4]
    db_cursor.execute("CREATE TABLE IF NOT EXISTS invoice_records(\
                inum INT, \
                date DATE, \
                cnum INT, \
                srnum INT, \
                invoice_total DECIMAL(10,2))")

    db_cursor.execute("INSERT INTO invoice_records (inum, date, cnum, srnum, invoice_total) \
                       VALUES (%s, %s, %s, %s, %s)",[inum, date, cnum, srnum, invoice_total])

def newInvoice():

    msg = "Enter the Order Number"

    title = "Invoice Details"
    fieldNames = ["Order Number", "Ship Date", "Shipping Charge", "Tax"]
    fieldValues = []  # we start with blanks for the values
    fieldValues = multenterbox(msg, title, fieldNames)

    shipped = []

    orderno = fieldValues[0]
    ship_date = fieldValues[1]
    ship_charge = fieldValues[2]
    tax = fieldValues[3]
    f_or_p = 0

    db_cursor.execute("SELECT * FROM orderhaspart \
                       WHERE onum = %s", (orderno,))
    orders = db_cursor.fetchall()

    for order in orders:
        smsg = "Was part number"+str(order[1])+" Fully or Partially shipped?"
        choices = ["Fully Shipped", "Partially Shipped"]
        choice = choicebox(smsg, title, choices)

        if choice == "Fully Shipped":
            f_or_p = 'f'
            shipped.append(order[2])
        elif choice =="Partially Shipped":
            f_or_p = 'p'
            psmsg = "How many were shipped?"
            psFields = ["Number Shipped"]
            shipped_q = multenterbox(psmsg, title, psFields)
            shipped_q = int(shipped[0])
            shipped.append(shipped_q)
            updateOrdersShipped(shipped, orderno)

    #Create Invoice Number
    db_cursor.execute("SELECT inum FROM invoice ORDER BY inum desc limit 0,1")
    inum = db_cursor.fetchall()
    inum = inum[0][0] +1

    #get Customer Number
    db_cursor.execute("SELECT customernum FROM orders \
                       WHERE onum = %s", (orderno,))
    cnum = db_cursor.fetchall()[0][0]

    #get Sales Rep Number
    db_cursor.execute("SELECT salesrepno FROM customer \
                       WHERE cnum = %s", (cnum,))
    srno = db_cursor.fetchall()[0][0]

    #Add invoice to Table
    db_cursor.execute("INSERT INTO invoice (inum, ishipdate, ishipcharge, itax, ifullpartially, orderno) \
                       VALUES (%s, %s, %s, %s, %s, %s)", [inum,ship_date, ship_charge, tax, f_or_p, orderno])
    db_connection.commit()



    printInvoice(inum,orderno,shipped)

    total = getTotal(inum)
    pre_tax = getPreTax(orderno)

    invoice_record = [inum, ship_date, cnum, srno, total]

    updateCustomer(cnum, total, pre_tax)
    updateSalesRep(srno, total, pre_tax)
    updateParts(orderno)
    createInvoiceRecord(invoice_record)
    #deleteReleasedOrders(orderno)

    transactions()

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
        monthEnd()


main()

db_cursor.close()
db_connection.close()