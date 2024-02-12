#Reading data and keeping it in dictionaries for further actions
with open('CompanyA_Quarter1.txt' , 'r') as a_q1:
    lines_list_a1 = [row.strip() for row in a_q1.readlines()]
    words_list_a1 = [word.split(':') for word in lines_list_a1]
    info_a_q1 = {}
    for i in range(len(words_list_a1)):
        info_a_q1[words_list_a1[i][0]] = words_list_a1[i][1]
    
with open('CompanyA_Quarter2.txt' , 'r') as a_q2:
    lines_list_a2 = [row.strip() for row in a_q2.readlines()]
    words_list_a2 = [word.split(':') for word in lines_list_a2]
    info_a_q2 = {}
    for i in range(len(words_list_a2)):
        info_a_q2[words_list_a2[i][0]] = words_list_a2[i][1]

with open('CompanyB_Quarter1.txt' , 'r') as b_q1:
    lines_list_b1 = [row.strip() for row in b_q1.readlines()]
    words_list_b1 = [word.split(':') for word in lines_list_b1]
    info_b_q1 = {}
    for i in range(len(words_list_b1)):
        info_b_q1[words_list_b1[i][0]] = words_list_b1[i][1]

with open('CompanyB_Quarter2.txt' , 'r') as b_q2:
    lines_list_b2 = [row.strip() for row in b_q2.readlines()]
    words_list_b2 = [word.split(':') for word in lines_list_b2]
    info_b_q2 = {}
    for i in range(len(words_list_b2)):
        info_b_q2[words_list_b2[i][0]] = words_list_b2[i][1]

def for_numbers(info):
    """This function is for casting numbers of our info to float 
        in order to count difference between two quarters.
    Parameters: info (dict): dictionary containing information of the company
    Returns: res (dict): dictionary with the same information , but the data with numbers is transformed 
    so that we can take mathematical actions on it.
    """
    
    res = {}
    for i in info:
        if i != 'Company' and i != 'Quarter':
            n = info[i][2:].split(',')
            m = ''
            for j in n:
                m += j
            res[i] = float(m)
        else:
            res['Company'] = info['Company']
            res['Quarter'] = info['Quarter']
    return res

comp_name = input('Please enter company name: Company A or Company B')
if comp_name != 'Company A' and comp_name != 'Company B':
    raise ValueError('Company name not valid.')

def statistics(company):
    """This function is made to compare two quarters for specific company.
    Parameters: company (str): the company statistics of which we want
    Returns: None
    Print statistics comparing two quarters for a company.
    """

    if company == 'Company A':
        res_q1 = for_numbers(info_a_q1)
        res_q2 = for_numbers(info_a_q2)
        for i in res_q1:
            if i != 'Quarter' and i != 'Company':
                compare = res_q1[i] - res_q2[i]
                if compare > 0:
                    print(f'{i} of Company A decreased by ${compare} in the second quarter.')
                elif compare < 0:
                    print(f'{i} of Company A increased by ${abs(compare)} in the second quarter.')
                else:
                    print(f'{i} of Company A did not change during the second quarter.')

    elif company == 'Company B':
        res_q1 = for_numbers(info_b_q1)
        res_q2 = for_numbers(info_b_q2)
        for i in res_q1:
            if i != 'Quarter' and i != 'Company':
                compare = res_q1[i] - res_q2[i]
                if compare > 0:
                    print(f'{i} of Company B decreased by ${compare} in the second quarter.')
                elif compare < 0:
                    print(f'{i} of Company B increased by ${abs(compare)} in the second quarter.')
                else:
                    print(f'{i} of Company B did not change during the second quarter.')
        
statistics(comp_name)
    