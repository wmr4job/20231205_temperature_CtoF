#攝氏C、華氏F溫度轉換器
temp_C = input('請輸入攝氏溫度(C)：')
temp_C = float(temp_C) #input輸入的值為str，要轉成float做運算>>casting型別轉換
temp_F = temp_C * 9 / 5 + 32
print('攝氏', temp_C, '度C，等於華氏', temp_F, '度F')