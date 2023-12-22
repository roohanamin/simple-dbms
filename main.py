#importing os module
import os
import re

existingDatabases = set()
existingTables = set()
globalTable = []
productOnly = []
currentDatabase = ""
userInput = ""
commitProcess_real = ""
locked = 0
endingResult = ""
endingPath = ""

while True:
    userInput = input("")
    if userInput == "":
        pass
    else:
        tokens = userInput.split()
        if userInput == ".EXIT" or userInput == ".exit":
            break
        if tokens[0] == "USE":
            databaseName = tokens[1].replace(";","")
            currentDatabase = databaseName
            print("Using database {}.".format(databaseName))
        if (tokens[0] == "create" and tokens[1] == "table") and len(tokens) == 7:
            tableNameRep = tokens[2] #Flights
            tableName = re.sub("\(.*", "", tableNameRep)
            varName1Rep = tokens[3]
            varName1 = re.sub(".*\(", "", varName1Rep) #id
            varType = tokens[4].replace(",", "") #int
            varName2 = tokens[5]
            varType2 = tokens[6].replace(");", "")
            parent_dir = os.getcwd()
            path = os.path.join(parent_dir, currentDatabase)
            table_path = os.path.join(path, tableName + ".txt")
            if table_path in existingTables:
                print("!Failed to create table {} because it already exists.".format(tableName))
            else:
                existingTables.add(table_path)
                tableColumn = []
                tableColumn.append(varName1)
                tableColumn.append(varType)
                tableColumn.append(varName2)
                tableColumn.append(varType2)
                separatorIndex = 2
                firstSublist = tableColumn[:2]
                secondSublist = tableColumn[2:]
                result = " ".join(firstSublist) + "|" + " ".join(secondSublist) + "\n"
                f = open(table_path, "w")
                f.write(result)
                f.close()
                print("Table {} created.".format(tableName))
        if tokens[0] == "DROP" and tokens[1] == "TABLE":
            tableName = tokens[2].replace(";","")
            parent_dir = os.getcwd()
            table_path = os.path.join(parent_dir, currentDatabase, tableName + ".txt")
            if table_path in existingTables:
                print("Table {} deleted.".format(tableName))
                existingTables.remove(table_path)
                os.remove(table_path)
            else:
                print("!Failed to delete {} because it does not exist.".format(tableName))
        # if tokens[0] == "select" and tokens[1] == "*" and tokens[2] == "from" and tokens[7] == "where" and len(tokens) == 11:
        #     tableName1 = tokens[3]
        #     tableName2 = tokens[5]
        #     parent_dir = os.getcwd()
        #     path = os.path.join(parent_dir, currentDatabase)
        #     table_path1 = os.path.join(path, tableName1 + ".txt")
        #     table_path2 = os.path.join(path, tableName2 + ".txt")
        #     with open(table_path1, "r") as emp_file, open(table_path2, "r") as sales_file:
        #         emp_header = emp_file.readline().strip()
        #         sales_header = sales_file.readline().strip()
        #         headers = emp_header + "|" + sales_header
        #         print(headers)
        #         employee_dict = {}
        #         for line in emp_file:
        #             line = line.strip().split("|")
        #             employee_dict[line[0]] = line[1]
        #         for line in sales_file:
        #             line = line.strip().split("|")
        #             employee_id = line[0]
        #             product_id = line[1]
        #             employee_name = employee_dict[employee_id]
        #             print(employee_id + "|" + employee_name + "|" + employee_id + "|" + product_id)
        # if tokens[0] == "select" and tokens[1] == "*" and tokens[2] == "from" and tokens[5] == "inner" and  tokens[6] == "join" and len(tokens) == 13:
        #     tableName1 = tokens[3]
        #     tableName2 = tokens[7]
        #     parent_dir = os.getcwd()
        #     path = os.path.join(parent_dir, currentDatabase)
        #     table_path1 = os.path.join(path, tableName1 + ".txt")
        #     table_path2 = os.path.join(path, tableName2 + ".txt")
        #     with open(table_path1, "r") as emp_file, open(table_path2, "r") as sales_file:
        #         emp_header = emp_file.readline().strip()
        #         sales_header = sales_file.readline().strip()
        #         headers = emp_header + "|" + sales_header
        #         print(headers)
        #         employee_dict = {}
        #         for line in emp_file:
        #             line = line.strip().split("|")
        #             employee_dict[line[0]] = line[1]
        #         for line in sales_file:
        #             line = line.strip().split("|")
        #             employee_id = line[0]
        #             product_id = line[1]
        #             employee_name = employee_dict[employee_id]
        #             print(employee_id + "|" + employee_name + "|" + employee_id + "|" + product_id)
        # if tokens[0] == "select" and tokens[1] == "*" and tokens[2] == "from" and tokens[5] == "left" and tokens[6] == "outer" and tokens[7] == "join":
        #     tableName1 = tokens[3]
        #     tableName2 = tokens[8]
        #     parent_dir = os.getcwd()
        #     path = os.path.join(parent_dir, currentDatabase)
        #     table_path1 = os.path.join(path, tableName1 + ".txt")
        #     table_path2 = os.path.join(path, tableName2 + ".txt")
        #     employee_data = {}
        #     with open(table_path1, "r") as emp_file, open(table_path2, "r") as sales_file:
        #         emp_header = emp_file.readline().strip()
        #         sales_header = sales_file.readline().strip()
        #         headers = emp_header + "|" + sales_header
        #         print(headers)
        #     employee_data = {}
        #     with open(table_path1, "r") as f:
        #         header = f.readline().strip().split("|")
        #         for line in f:
        #             line = line.strip().split("|")
        #             employee_data[line[0]] = line[1]
        #     sales_data = []
        #     with open(table_path2, "r") as f:
        #         header = f.readline().strip().split("|")
        #         for line in f:
        #             line = line.strip().split("|")
        #             sales_data.append((line[0], line[1]))
        #     for employee_id, name in employee_data.items():
        #         found_match = False
        #         for sale in sales_data:
        #             if employee_id == sale[0]:
        #                 print(f"{employee_id}|{name}|{sale[0]}|{sale[1]}")
        #                 found_match = True
        #         if not found_match:
        #             print(f"{employee_id}|{name}| | ")
        # if (tokens[0] == "select" and tokens[1] == "*" and tokens[2] == "from" and tokens[7] == "where" and tokens[8] == "E.id" and tokens[9] == "=" and tokens[10] == "S.employeeID;"):
        #     # Join Employee and Sales tables on the id and employeeID columns, respectively
        #     result = []
        #     employeeTable = []
        #     salesTable = []
        #     parent_dir = os.getcwd()
        #     employeeTableName = tokens[3]
        #     employeeVar = tokens[4].replace(",", "")
        #     salesTableName = tokens[5]
        #     salesVar = tokens[6]
        #     employeeTablePath = os.path.join(parent_dir, currentDatabase, employeeTableName + ".txt")
        #     salesTablePath = os.path.join(parent_dir, currentDatabase, salesTableName + ".txt")
            # if os.path.exists(employeeTablePath) and os.path.exists(salesTablePath):
            #     # Read the Employee table
            #     with open(employeeTablePath, "r") as f:
            #         employeeTable = f.readlines()
            #     # Read the Sales table
            #     with open(salesTablePath, "r") as f:
            #         salesTable = f.readlines()
            #     # Join the tables
            #     header1 = employeeTable[0]
            #     header2 = salesTable[0]
            #     result.append(header1.strip() + "|" + header2.strip().split("|")[1])
            #     for line1 in employeeTable[1:]:
            #         for line2 in salesTable[1:]:
            #             row1 = line1.strip().split("|")
            #             row2 = line2.strip().split("|")
            #             if row1[0] == row2[1]:
            #                 result.append(line1.strip() + "|" + row2[1])
            #     # Print the result
            #     for line in result:
            #         print(line)
            # else:
            #     print("!Failed to query tables because one or both of them do not exist.")
        if (tokens[0] == "SELECT" and tokens[1] == "*" and tokens[2] == "FROM") or (tokens[0] == "select" and tokens[1] == "*" and tokens[2] == "from"):
            tableName = tokens[3].replace(";","")
            parent_dir = os.getcwd()
            path = os.path.join(parent_dir, currentDatabase, tableName + ".txt")
            if os.path.exists(path):
                f = open(path)
                print(f.read())
                f.close()
            else:
                print("!Failed to query table {} because it does not exist.".format(tableName))
        # Query
        if (tokens[0] == "select" and tokens[1] == "name," and tokens[2] == "price" and tokens[3] == "from" and tokens[5] == "where"):
            tableName = tokens[4].title()
            parent_dir = os.getcwd()
            path = os.path.join(parent_dir, currentDatabase, tableName + ".txt")
            pid = tokens[6]
            equalityOperator = tokens[7]
            pidValue = tokens[8].replace(";", "")
            if os.path.exists(path):
                f = open(path, "r")
                selectTable = []
                selectTable = f.readlines()
                header = selectTable[0]
                splitHeader = header.split("|")
                poppedHeader = splitHeader.pop(1)
                headerResult = '|'.join(poppedHeader)
                print(poppedHeader + "|" + splitHeader[1], end='')
                for line in selectTable[1:]:
                    row = line.split("|")
                    if row[0].strip() != '':
                        if (equalityOperator == "!=" and row[0] != pidValue) or (equalityOperator == "=" and row[0] == pidValue):
                            print(row[1] + "|" + row[2].strip())
                f.close()
        if tokens[0] == "ALTER" and tokens[1] == "TABLE" and tokens[3] == "ADD":
            tableName = tokens[2]
            varName = tokens[4]
            var = tokens[5].replace(";","")
            columnEntry = []
            columnEntry.append(varName)
            columnEntry.append(var)
            result = " ".join(columnEntry)
            parent_dir = os.getcwd()
            path = os.path.join(parent_dir, currentDatabase, tableName + ".txt")
            f = open(path, "a")
            f.write(" | " + result)
            f.close()
            print("Table {} modified.".format(tableName))
        if tokens[0] == "CREATE" and tokens[1] == "DATABASE":
            databaseName = tokens[2].replace(";","")
            parent_dir = os.getcwd()
            path = os.path.join(parent_dir, databaseName)
            if databaseName in existingDatabases:
                print("!Failed to create database {} because it already exists.".format(databaseName))
            else:
                existingDatabases.add(databaseName)
                os.mkdir(path)
                print("Database {} created.".format(databaseName))
        if tokens[0] == "DROP" and tokens[1] == "DATABASE":
            databaseName = tokens[2].replace(";","")
            parent_dir = os.getcwd()
            removePath = os.path.join(parent_dir, databaseName)
            if databaseName in existingDatabases:
                print("Database {} deleted.".format(databaseName))
                existingDatabases.remove(databaseName)
                os.rmdir(removePath)
            else:
                print("!Failed to delete {} because it does not exist.".format(databaseName))
        if tokens[0] == "insert" and tokens[1] == "into":
            tableColumn = []
            tableName = tokens[2]
            parent_dir = os.getcwd()
            path = os.path.join(parent_dir, currentDatabase, tableName + ".txt")

            values = tokens[4].replace("(", "") #seats
            values = values.replace(");", "")
            values = values.replace(",", " ")
            values_list = values.split(" ")

            tableColumn.extend(values_list)
            separatorIndex = 2
            firstSublist = tableColumn[0]
            secondSublist = tableColumn[1]
            result = "".join(firstSublist) + "|" + "".join(secondSublist) + "\n"
            with open(path, "a") as f:
                f.write(result)
            print("1 new record inserted.")
        if tokens[0] == "update" and tokens[2] == "set" and tokens[3] == "status" and tokens[6] == "where" and tokens[7] == "seat":
            tableName_prev = tokens[1]
            tableName = tableName_prev[0].upper() + tableName_prev[1:]
            parent_dir = os.getcwd()
            path = os.path.join(parent_dir, currentDatabase, tableName + ".txt")
            endingPath = path
            status = tokens[5]
            seatNum = tokens[9].replace(";", "")

            data = []
            recordCount = 0
            with open(path) as f:
                lines = [line.rstrip('\n') for line in f]
                for line in lines:
                    data.append(line + "\n")
            #print(data)
            for i in range(len(data)):
                line = data[i].split("|")
                #print(line)
                if line[0] == str(seatNum):
                    line[1] = str(status)
                    recordCount += 1
                    temp = " "
                    data[i] = "|".join(line) + "\n"
            if locked == 1:
                endingResult = data
                if recordCount == 1:
                    print(f"{recordCount} record modified.")
                    #print(commitProcess_real + " committed.")
                else:
                    print(f"{recordCount} records modified.")
        # Table Modification
        # if tokens[0] == "update" and tokens[2] == "set" and tokens[3] == "price" and tokens[6] == "where" and tokens[7] == "name":
        #     tableName = tokens[1]
        #     parent_dir = os.getcwd()
        #     path = os.path.join(parent_dir, currentDatabase, tableName + ".txt")

        #     productName_lhs = tokens[9].replace("'", "") 
        #     productName = productName_lhs.replace(";", "")
        #     newPrice = tokens[5]
        #     recordCount = 0
        #     f = open(path, "r")
        #     globalTable = f.readlines()
        #     for i in range(1, len(globalTable)):
        #         productOnly = globalTable[i].split("|")
        #         if productName in productOnly[1]:
        #             productOnly[2] = newPrice
        #             globalTable[i] = "|".join(productOnly) + "\n"
        #             if productOnly[1] == productName:
        #                 recordCount += 1
        #                 continue
        #     f.close()

        #     f = open(path, "w")
        #     for line in globalTable:
        #         f.write(line)
        #     f.close()

        #     if recordCount == 1:
        #         print(f"{recordCount} record modified.")
        #         print("")
        #     else:
        #         print(f"{recordCount} records modified.")
        # Table Deletion
        if tokens[0] == "delete" and tokens[1] == "from" and tokens[3] == "where":
            if tokens[4] == "name":
                tableName = tokens[2].title()
                parent_dir = os.getcwd()
                path = os.path.join(parent_dir, currentDatabase, tableName + ".txt")

                productName_lhs = tokens[6].replace("'", "")
                productName = productName_lhs.replace(";", "")

                f = open(path, "r")
                globalTable = f.readlines()
                f.close()

                instanceTable = [globalTable[0]]
                recordCount = 0
                for i in range(1, len(globalTable)):
                    productOnly = globalTable[i].split("|")
                    if productOnly[1] == productName:
                        recordCount += 1
                        continue
                    instanceTable.append(globalTable[i])
        
                f = open(path, "w")
                for i in instanceTable:
                    f.write(i)
                f.close()

                if recordCount == 1:
                    print(f"{recordCount} record deleted.")
                else:
                    print(f"{recordCount} records deleted.")
            if tokens[4] == "price":
                tableName = tokens[2].title()
                parent_dir = os.getcwd()
                path = os.path.join(parent_dir, currentDatabase, tableName + ".txt")

                inequalityOperator = tokens[5]
                priceValue = float(tokens[6].replace(";", ""))

                f = open(path, "r")
                globalTable = f.readlines()
                f.close()

                instanceTable = [globalTable[0]]
                recordCount = 0
                for i in range(1, len(globalTable)):
                    productOnly = globalTable[i].split("|")
                    if inequalityOperator == ">" and float(productOnly[2]) > priceValue:
                        recordCount += 1
                        continue
                    instanceTable.append(globalTable[i])
                
                f = open(path, "w")
                for line in instanceTable:
                    f.write(line)
                f.close()

                if recordCount == 1:
                    print(f"{recordCount} record deleted.")
                else:
                    print(f"{recordCount} records deleted.")
        if tokens[0] == "begin":
            commitProcess = tokens[1].replace(";", "")
            commitProcess_real = commitProcess[0].upper() + commitProcess[1:]
            print(commitProcess_real + " starts.")
            parent_dir = os.getcwd()
            path = os.path.join(parent_dir, currentDatabase)
            lockPath = os.path.join(path, "lock.txt")
            if os.path.exists(lockPath) == False:
                f2 = open(lockPath, "w")
                f2.write("Lock")
                f2.close()
                locked = 1
            else:
                locked = -1
        if tokens[0] == "commit;":
            if locked == 1:
                print(commitProcess_real + " committed.")
                locked = 2
                f = open(path, "w")
                f.writelines(endingResult)
                f.close()
            else:
                print("Error: Table " + commitProcess_real + " is locked!")
                print("Transaction abort.")
