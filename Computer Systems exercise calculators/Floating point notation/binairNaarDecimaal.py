def convertToInt(mantissa_str): 
  
    
    power_count = -1
  
    
    mantissa_int = 0
  
    
    for i in mantissa_str: 
  
        
        mantissa_int += (int(i) * pow(2, power_count)) 
  
        
        power_count -= 1
          

    return (mantissa_int + 1) 
  
if __name__ == "__main__": 
    
    #print("geef binair nummer in dit formaat '0|10000111|00000111010011001100110'")
    ieee_32 = '0|10000111|00000111010011001100110'
  
    
    sign_bit = int(ieee_32[0]) 
  
    
    exponent_bias = int(ieee_32[2 : 10], 2) 
  
    
    exponent_unbias = exponent_bias - 127
  
    
    mantissa_str = ieee_32[11 : ] 
  
    
    mantissa_int = convertToInt(mantissa_str) 
  

    real_no = pow(-1, sign_bit) * mantissa_int * pow(2, exponent_unbias) 
  
    
    print("The float value of the given IEEE-754 representation is :",real_no)
