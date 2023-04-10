import copy
from common_functions import skip_list, search, is_amount, assign_blank
from advance.config import header
from advance.config import part1
from advance.config import part2
from advance.config import part3
# from advance.config import part4
# from advance.config import part5


def fetch_part1(file_list, document_data):
    '''Function for fetching the Part  table'''
    flag = False
    
    try:
        temp_index = search(
            file_list, "1. Details of item to be exported/supplied under the Authorisation")
        temp_index = search(file_list, "realisation)",
                            start_index=temp_index)
        temp_index2 = search(file_list, "2. Details of items sought to be imported duty free under the Authorisation", start_index=temp_index)
        skip_word_list = [
         "realisation)"
        ]
        document_data = assign_blank(document_data)
        srno = '1'
        while temp_index < temp_index2:
            datalist = []
            temp_index = skip_list(file_list, temp_index, skip_word_list)
            if srno == file_list[temp_index+4]:

                document_data["Sl.No"][-1] = srno   
                next_srno = str(int(srno)+1)

                while srno != next_srno and temp_index < temp_index2:
                    datalist.append(file_list[temp_index])
                    
                    if file_list[temp_index+1] == str(int(srno)+1):
                        srno =str(int(srno)+1)
                        break
                    temp_index += 1
                document_data = fetch_datalist11(document_data, datalist)
            temp_index += 1
        flag = True
    except Exception as exception:
        print(exception)
        flag = False
    return document_data, flag

def fetch_part2(file_list, document_data):
    '''Function for fetching the Part  table'''
    flag = False
    
    try:
        temp_index = search(
            file_list, "2. Details of items sought to be imported duty free under the Authorisation")
        temp_index = search(file_list, "CIF (Rs.)",
                            start_index=temp_index)
        temp_index2 = search(file_list, "3. Name and Address of the Supporting Manufacturer /factory / premises / Project site(s)", start_index=temp_index)
        skip_word_list = [
         "CIF (Rs.)"
        ]
        document_data = assign_blank(document_data)
        srno = '1'
        while temp_index < temp_index2:
            datalist = []
            temp_index = skip_list(file_list, temp_index, skip_word_list)
            if srno == file_list[temp_index+2]:

                document_data["Sl.No"][-1] = srno   
                next_srno = str(int(srno)+1)

                

                while srno != next_srno and temp_index < temp_index2:
                    datalist.append(file_list[temp_index])
                    
                    if file_list[temp_index+1] == str(int(srno)+1):
                        srno =str(int(srno)+1)
                        break
                    temp_index += 1
                document_data = fetch_datalist11(document_data, datalist)
            temp_index += 1
        flag = True
    except Exception as exception:
        print(exception)
        flag = False
    return document_data, flag

def fetch_part3(file_list, document_data):
    '''Function for fetching the Part  table'''
    flag = False
    
    try:
        temp_index = search(
            file_list, "3. Name and Address of the Supporting Manufacturer /factory / premises / Project site(s)")
        temp_index = search(file_list, "Excise Authority",
                            start_index=temp_index)
        temp_index2 = search(file_list, "4. Name and Address of the Co-Licensee : Not Available", start_index=temp_index)
        skip_word_list = [
         "Excise Authority"
        ]
        document_data = assign_blank(document_data)
        srno = '1'
        while temp_index < temp_index2:
            datalist = []
            temp_index = skip_list(file_list, temp_index, skip_word_list)
            if srno == file_list[temp_index+4]:

                document_data["Sl.No"][-1] = srno   
                next_srno = str(int(srno)+1)

                

                while srno != next_srno and temp_index < temp_index2:
                    datalist.append(file_list[temp_index])
                    
                    if file_list[temp_index+1] == str(int(srno)+1):
                        srno =str(int(srno)+1)
                        break
                    temp_index += 1
                document_data = fetch_datalist11(document_data, datalist)
            temp_index += 1
        flag = True
    except Exception as exception:
        print(exception)
        flag = False
    return document_data, flag



def fetch_amount(document_data, amount_list):
    '''Function for fetching the amount of part 11 table'''
    try:
        if len(amount_list) == 6:
            document_data["ITCHS Code"][-1] = amount_list[0]
            document_data["Export Item Name"][-1] = amount_list[1]
            document_data["Qty"][-1] = amount_list[2]
            document_data["UOM"][-1] = amount_list[3]
            document_data["FOB/FOR(Rs.)"][-1] = amount_list[4]
            document_data["FOB/FOR(In currency of realisation)"][-1] = amount_list[5]
        if len(amount_list) == 5:
            document_data["ITCHS Code"][-1] = amount_list[0]
            document_data["Import Item Name"][-1] = amount_list[1]
            document_data["Qty"][-1] = amount_list[2]
            document_data["UOM"][-1] = amount_list[3]
            document_data["CIF (Rs.)"][-1] = amount_list[4]
        if len(amount_list) == 6:
            document_data["Name"][-1] = amount_list[0]
            document_data["Address"][-1] = amount_list[1]
            document_data["Type of Unit"][-1] = amount_list[2]
            document_data["Reg. No."][-1] = amount_list[3]
            document_data["Date"][-1] = amount_list[4]
            document_data["Address of the jurisdictional Central sExcise Authority"][-1] = amount_list[5]
    except Exception as exception:
        print(exception)
    return document_data
def fetch_header(file_list, document_data):
    '''Function for fetching the Header table'''
    flag = False
    try:
        temp_index = search(file_list, "LICENCE/AUTHORISATION/SCRIP")
        document_data['LICENCE/AUTHORISATION/SCRIP Authorisation'] = file_list[temp_index + 1]

        temp_index = search(file_list, "Name of Office issuing")
        document_data['Name of Office issuing Authorisation'] = file_list[temp_index - 1]+" "+file_list[temp_index + 1]+" "+file_list[temp_index + 3]

        temp_index = search(file_list, "Name")
        document_data['Name'] = file_list[temp_index + 1]

        temp_index = search(file_list, "Address of Applicant")
        document_data['Address of Applicant'] = file_list[temp_index - 1]+" "+file_list[temp_index + 1]

        temp_index = search(file_list, "IEC")
        document_data['IEC'] = file_list[temp_index + 1]

        temp_index = search(file_list, "Exporter Type")
        document_data['Exporter Type'] = file_list[temp_index + 1]

        temp_index = search(file_list, "Exporter Status")
        document_data['Exporter Status'] = file_list[temp_index + 1]

        temp_index = search(file_list, "Transferable/Actual User")
        document_data['Transferable/Actual User'] = file_list[temp_index + 1]

        temp_index = search(file_list, "File Number")
        document_data['File Number'] = file_list[temp_index + 1]

        temp_index = search(file_list, "Licence/Authorisation/Scrip No.")
        document_data['Licence/Authorisation/Scrip No.'] = file_list[temp_index + 1]

        temp_index = search(file_list, "Date of Issue")
        document_data['Date of Issue'] = file_list[temp_index + 1]

        temp_index = search(file_list, "FOB Value (In Rs.)")
        document_data['FOB Value (In Rs.)'] = file_list[temp_index + 1]

        temp_index = search(file_list, "FOB Value (In US$)")
        document_data['FOB Value (In US$)'] = file_list[temp_index + 1]

        temp_index = search(file_list, "CIF in Rs.")
        document_data['CIF in Rs.'] = file_list[temp_index - 1]+" "+file_list[temp_index + 1]+" "+file_list[temp_index + 2]

        temp_index = search(file_list, "CIF in FFE")
        document_data['CIF in FFE'] = file_list[temp_index - 1]+" "+file_list[temp_index + 1]

        temp_index = search(file_list, "Port of Registration")
        document_data['Port of Registration'] = file_list[temp_index + 1]

        temp_index = search(file_list, "Period of Shipment (Export")
        document_data['Period of Shipment (Export Obligation Period)'] = file_list[temp_index + 1]

        temp_index = search(file_list, "Validity of Authorisation / Scrip for")
        document_data['Validity of Authorisation / Scrip for Import'] = file_list[temp_index + 1]

        temp_index = search(file_list, "Custom Notification Number")
        document_data['Custom Notification Number'] = file_list[temp_index + 1]
    
        temp_index = search(file_list, "Currency Area")
        document_data['Currency Area'] = file_list[temp_index + 1]

        temp_index = search(file_list, "Utilization/Transferability")
        document_data['Utilization/Transferability'] = file_list[temp_index + 1]

        flag = True
    except Exception as exception:
        print(exception)
        flag = False
    return document_data, flag
def fetch_datalist11(document_data, datalist):
    '''Function for fetching the Row of part 11 table'''
    try:
        document_data = assign_blank(document_data)
        desc = ""
        amount_list = []
        for data in datalist:
            # if check_aplhabet(data):
            #     document_data["Sr.No"][-1] = data
            if is_amount(data):
                amount_list.append(data)
            # elif is_amount(data.replace(",","").replace(".","")):
            #     amount_list.append(data)

            else:
                desc += data

        # document_data['Nature of Supplies'][-1] = desc

        document_data['ITCHS Code'][-1] = desc

        document_data = fetch_amount(document_data, amount_list)

    except Exception as exception:
        print(exception)
    return document_data


def main(file_list):
    '''Main function for fetching tables data'''
    flag = False
    header_flag = part1_flag =part2_flag=part3_flag=False
    try:
        document_data = copy.deepcopy(header)
        header_node, header_flag = fetch_header(file_list, document_data)

        document_data = copy.deepcopy(part1)
        part_1_node, part1_flag = fetch_part1(file_list, document_data)

        document_data = copy.deepcopy(part2)
        part_2_node, part2_flag = fetch_part2(file_list, document_data)

        
        document_data = copy.deepcopy(part3)
        part_3_node, part3_flag = fetch_part3(file_list, document_data)

        node_list = [
            header_node,
            part_1_node,
            part_2_node,
            part_3_node
        ]
        if header_flag and part1_flag and part2_flag and part3_flag:
            flag = True
    except Exception:
        flag = False
    return node_list, flag


