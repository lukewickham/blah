#Written by Vlastimil Hovan 2016  
#Please include text above in any redistribution
#Thanks

from microbit import *
import random

remind          = -1
operation_      = 0
number_1        = 0
number_2        = 0
answer          = 0
action_         = 0
correct_counter = 0
cycle_counter   = 0
ran_number      = 0

tick = Image("00000:"
             "00009:"
             "00090:"
             "90900:"
             "09000")

cross = Image("90009:"
              "09090:"
              "00900:"
              "09090:"
              "90009")

display.scroll("Simple Maths game. To start press button A", delay=100)
display.show(Image.ARROW_W)

while True:
    if (remind == -1): # Start button function
        if (button_a.is_pressed() == 1):
            
            display.scroll("Starting in :",delay = 100)
            sleep(500)
            count = 5
            while (count > 0):
                display.show(str(count))
                sleep(500)
                count = count - 1
                            
            remind = 0
            
    
    if (remind == 0):
        
        operation_ = random.randint(1, 4)
# -----------------------------------------------------------       
        if (operation_ == 1): # Addition
            
            action_ = random.randint(1, 10)
            number_1 = random.randint(1, 7)
            ran_number = 9 - number_1
            number_2 = random.randint(1, ran_number)
            answer = number_1 + number_2
        
            if (action_ % 2 == 0): # show correct answer
            
                remind = 1 
            
            else:                   # show incorrect answer
            
                remind = 2
                answer = answer - 2
            
            display.scroll("%d + %d =" % (number_1,number_2), delay=100,) 
            sleep(500)
            display.show(str(answer))
        
# ------------------------------------------------------------        
        if (operation_ == 2): # Substraction
           
            action_ = random.randint(1, 10)
            
            number_1 = random.randint(2, 7)
            ran_number = number_1 - 1
            
            number_2 = random.randint(0, ran_number)
            answer = number_1 - number_2
        
            if (action_ % 2 == 0): # show correct answer
            
                remind = 1 
            
            else:                   # show incorrect answer
            
                remind = 2
                answer = answer + 2
                   
            display.scroll("%d - %d =" % (number_1,number_2), delay=100,) 
            sleep(500)
            display.show(str(answer))    

# -----------------------------------------------------------  
        if (operation_ == 3):                   # Multiplication
           
            action_ = random.randint(1, 9)
            
            if (action_ == 1):
                number_1 = 2
                number_2 = 2
                answer = 2*2
                
            elif (action_ == 2):
                number_1 = 2
                number_2 = 3
                answer = 2*3
                
            elif (action_ == 3):
                number_1 = 2
                number_2 = 4
                answer = 2*4
                
            elif (action_ == 4):
                number_1 = 1
                number_2 = 9
                answer = 1*9
                
            elif (action_ == 5):
                number_1 = 3
                number_2 = 3
                answer = 3*3
                
            elif (action_ == 6):
                number_1 = 4
                number_2 = 2
                answer = 4*2
                
            elif (action_ == 7):
                number_1 = 3
                number_2 = 2
                answer = 3*2
                
            elif (action_ == 8):
                number_1 = 1
                number_2 = 7
                answer = 1*7
                
            elif (action_ == 9):
                number_1 = 5
                number_2 = 1
                answer = 5*1
            
            action_ = random.randint(1, 10)
          
                 
            if (action_ % 2 == 0): # show correct answer
            
                remind = 1 
            
            else:                   # show incorrect answer
            
                remind = 2
                answer = answer - (random.randint(1, 4))
                   
            display.scroll("%d * %d =" % (number_1,number_2), delay=100,) 
            sleep(500)
            display.show(str(answer))    

# ------------------------------------------------------------------------
        if (operation_ == 4):                   # Division
           
            action_ = random.randint(1, 9)
            
            if (action_ == 1):
                number_1 = 2
                number_2 = 2
                answer = 2/2
                
            elif (action_ == 2):
                number_1 = 4
                number_2 = 2
                answer = 4/2
                
            elif (action_ == 3):
                number_1 = 6
                number_2 = 2
                answer = 6/2
                
            elif (action_ == 4):
                number_1 = 8
                number_2 = 2
                answer = 8/2
                
            elif (action_ == 5):
                number_1 = 8
                number_2 = 4
                answer = 8/4
                
            elif (action_ == 6):
                number_1 = 10
                number_2 = 2
                answer = 10/2
                
            elif (action_ == 7):
                number_1 = 10
                number_2 = 5
                answer = 10/5
                
            elif (action_ == 8):
                number_1 = 5
                number_2 = 5
                answer = 5/5
                
            elif (action_ == 9):
                number_1 = 8
                number_2 = 8
                answer = 8/8
            
            action_ = random.randint(1, 10)
          
                 
            if (action_ % 2 == 0): # show correct answer
            
                remind = 1 
            
            else:                   # show incorrect answer
            
                remind = 2
                answer = answer + (random.randint(1, 4))
                   
            display.scroll("%d / %d =" % (number_1,number_2), delay=100,) 
            sleep(500)
            display.show("%.0f" % (answer))  

        
    if (remind > 0 ):
        if (button_a.is_pressed() == 1):
            cycle_counter = cycle_counter + 1
            
            if (remind == 1):
                
                correct_counter = correct_counter + 1
                display.show(tick)
                sleep(1000)
                display.clear()
        
            else:
                
                display.show(cross)
                sleep(1000)
                display.clear()
            
            remind = 0    
    
    if (remind > 0 ):
        if (button_b.is_pressed() == 1):
            cycle_counter = cycle_counter + 1
            
            if (remind == 1):
                
                #correct_counter = correct_counter + 1
                display.show(cross)
                sleep(1000)
                display.clear()
        
            else:
                
                correct_counter = correct_counter + 1
                display.show(tick)
                sleep(1000)
                display.clear()
            
            remind = 0
            
    if (cycle_counter == 10):
        remind = -2
        sleep(1000)
        if (correct_counter > 5):
            display.scroll("Correct answers %d out of 10 well done" % (correct_counter), delay=100,)
            sleep(1000)
            display.show(Image.HAPPY)
        
        if (correct_counter <= 5):
            display.scroll("Correct answers %d out of 10" % (correct_counter), delay=100,)
            sleep(1000)
            display.show(Image.SAD)        
        cycle_counter = 0
        correct_counter = 0      