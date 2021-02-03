#parse phone numbers from string

#+373-022-123456

#ce intra ce iese
def validate_region_code(code):
    region_codes=[
        "022",
        "043",
        "054",
    ]

    if code in region_codes:
        return True
    else:
        return False



#in/str--> out/bool
########################################
def validate_country_code(code):
    country_codes=[
        "373",
        "40",
        "1242",
    ]

    if code in country_codes:
        return True
    else:
        return False

#in/str--> out/dict
def parse_phone_number(input):
    return {
        "country_code": input[-14:-11],
        "region_code": input[-10:-7],
        "number":input[-6:],}
########################################

p_str= "+373-022-123456"
p_1=parse_phone_number(p_str)

  
print(p_1)
if validate_country_code(p_1["country_code"])==True and validate_region_code(p_1["region_code"])==True:
     print("Your number is registred")
else:
    print("Your number is not registred!!!")
