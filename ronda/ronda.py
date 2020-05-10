from datetime import datetime
import winsound
import time
import json
import input as io


init_shift = { # 24:00 init must be always converted to 00:00
    'hh': 22,
    'mm': 0
}
end_shift = { # 00:00 end must be alaways converted to 24:00
    'hh': 3,
    'mm': 0
}
next_check = {
    'hh': 20,
    'mm': 0
}
current_time = {
    'hh': 0,
    'mm': 0
}
interval = 5
warning = 3
check_count = 0
checklist =  [] #unlike python, arduino is required to have the max items preset
service_enabled = True
has_checkpoint = False

def generate_checklist():
    start_t = time_to_int(init_shift)
    print('# start_t = ', start_t)
    stop_t = time_to_int(end_shift)
    print('# stop_t = ', stop_t)
    duration = 0   

    if start_t > stop_t:
        duration = (1440 - start_t) + stop_t
    else:
        duration = stop_t - start_t
    
    check_count = duration // interval
    print('# check_count = ', check_count)
    
    aux = start_t
    for  i in range(check_count):
        aux += interval
        if aux > 1440:
            aux -= 1440

        checklist.append(aux)        

def time_to_int(h_m):
    return h_m['hh'] * 60 + h_m['mm']

def int_to_time(hm):
    time_dict = {
        'hh': 0,
        'mm': 0
    }
    time_dict['hh'] = hm // 60
    time_dict['mm'] = round(((hm / 60) - (hm // 60)) * 60)
    return time_dict

def get_int_time_now():
    return time_to_int(get_time_now())

def get_time_now():
    time_now = datetime.now()
    current = {
        'hh': datetime.now().hour,
        'mm': datetime.now().minute
    }
    return current

def closest_checkpoint(): # in production, remove arg
    global warning
    warn_info = {'check_time': False, 'start':0, 'stop':0}
    time_int = get_int_time_now()
    #################
    #time_int = fake_time # remove after debugging
    #########################
    for x in checklist:
        check_t = x - warning
        if check_t == time_int:
            print('checkpoint - 3 = ', check_t)
            print('time_int - 3 = ', time_int)

            print('Round reached a checkpoint', x)
            warn_info['start'] = time_int
            warn_info['stop'] = x
            warn_info['check_time'] = True
            #print(warn_info)
            break    
    return warn_info

#Beep variables
beep_count = 0
silence_time = False
silence_time_start = 0
time_intended = 1
B_WARN = 1 # WARNING BEEP
B_FAIL = 2 # FAIL BEEP
B_OK = 3 # SHIFT BEEP OK
B_MUTE = 4 # SILENCE TIME BETWEEN SHIFTS

def beep(beep_type):    
    if beep_type == B_MUTE: return
    
    global silence_time
    global silence_time_start
    global beep_count
    global time_intended

    freq = 2300
    dur = 95

    if beep_type == B_WARN:
        check_silence_time()
        if silence_time == True:
            return
    
    if(beep_type == B_WARN):# short for led pulse
        
        if beep_count == 4:
            silence_time = True
            beep_count = 0
            time_intended = time.time() + 3 
            print('silence...')           
            return
                
        winsound.Beep(freq, dur)
        beep_count += 1
        print(beep_count)
        #time_intended = 1     
        #silence_time_start = time.time()
        #silence_time_start = time.time()
        
    elif(beep_type == B_FAIL):# long for shift failed
        print('shift failed!')
        dur = 700
        winsound.Beep(freq, dur)
        time.sleep(.100)
        winsound.Beep(freq, dur)
        time.sleep(.100)
        dur = 1200
        winsound.Beep(freq, dur)     
        time.sleep(3)   
        #silence_time = True
        return
    else: # medium for round ok
        print('shift ok')
        dur = 700
        winsound.Beep(freq, dur)           
        time.sleep(3)
        #silence_time = True
        return

    #is_silence_time()  
    
def check_silence_time():
    global time_intended
    global silence_time
    time_now = time.time()    
    #print(int(time_intended))
    
    if time_now >= time_intended:
        silence_time = False                
        
    else:        
        silence_time = True


HIGH = 1 # constant for the button
def input():
    new_data = 0
    with open('input.json') as json_file:
        new_data = json.load(json_file)        
    if new_data['new_input']:
        new_data['new_input'] = False
        with open('input.json', 'w') as json_file:
            json.dump(new_data, json_file)

        return new_data['input_type']
    return 0      

def setup():
    generate_checklist() # important
    checklist.sort() # important
    print('# list =\n', checklist) #debug   
    
    #closest_checkpoint(1397) #debug

    main_loop() # important

def main_loop():
    global silence_time    
    button = io.Input()
    #debug_point = 1397 # debug

    while True:                        
        #shift_data = closest_checkpoint(debug_point)
        shift_data = closest_checkpoint()
        print('#### MAIN LOOP ####')
        print(shift_data)

        while shift_data['check_time']:
            time_now = get_int_time_now()
            #time_now = 1398
            if shift_data['stop'] > time_now:
                beep(B_WARN)
            elif shift_data['stop'] == time_now:
                beep(B_FAIL)
                print('SYSTEM IN PAUSE FOR 60 SECONDS DUE TO SHIFT FAIL')
                time.sleep(60)
                break
            
            if button.watch_file() == HIGH:
                beep(B_OK)                
                delay_time = ((shift_data['stop'] - time_now) + 1) * 60
                print('SYSTEM IN PAUSE FOR {} SECONDS'.format(delay_time))
                # force pause until check_time is false, avoiding this loop
                #time.sleep(10)
                time.sleep(delay_time)
                debug_point = 1402 # debug
                break    


        time.sleep(.4)       
            

        # 1 - if it's checkpoint time, set flag with start and keep warning period
        # 2 - keep checking for input HIGH or LOW, while beep(B_WARN)
        # 3 - keep checking for end warning period    


        
        
        """ new_input = button.watch_file()   

        if new_input != None:
            silence_time = False
            beep(new_input)
        else:            
            beep(1)        
        
        time.sleep(.1)
         """
        


def loop():    
    if service_enabled == False:
        current_time = get_time_now()
        time_now = time_to_int(current_time)
        time_next = time_to_int(next_check)

        if has_checkpoint == False:
            next_check = next_checkpoint(next_check, interval)

        if time_now >= time_next - warning:
            print('agora', time_now)
            print('proximo - advertencia', time_next - warning)
            #break


#main_loop()

setup()