######################
def transform_money( input ):
    currency= input[-3:]
    value=float(input[:-3])
    output={
        "value":value,
        "currency":currency
    }
    return output
######################

def space_cleaner(input):
    output=input.strip()
    return output

def transform_money_back(input):
    valoare=input
    output1=int(valoare.get("value"))
    output2=str(output1)
    output3=str(" ")
    output4=str(valoare.get("currency"))
    transfomed_in_string=output2+output3+output4

    return transfomed_in_string



data_1="                100 MDL"
no_space=space_cleaner(data_1)
res_1=transform_money(no_space)
res_2=transform_money_back(res_1)

print("1.",data_1,"->",res_1,"->",res_2)


