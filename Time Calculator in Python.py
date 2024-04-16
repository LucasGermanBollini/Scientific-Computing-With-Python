def add_time(start, duration,day = ''):
        #Horas/Minutos de hora a sumar
        hours_duration = duration.split(":")[0]
        minutes_duration = duration.split(":")[1]
        #Horas de hora de inicio
        hours_start = start.split(":")[0]
        count_hours = int(hours_start)
        #Minutos de hora de inicio
        minutes_start = start.split(" ")[0].split(":")[1]
        count_minutes = int(minutes_start)
        add_hours = 0
        minutes_duration = int(minutes_duration)
        hours_duration = int(hours_duration)
        
        #Contador de dias
        count_days = 0
        time = start.split(" ")[1]
        
        
        #Dias de la semana
        week_days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        if day != '':
            day = day.capitalize()
            day = week_days.index(day)
            
        
        total_minutes = minutes_duration + count_minutes
       
        if total_minutes > 59:
            total_minutes = total_minutes - 60
            add_hours += 1
            
        total_hours = hours_duration + count_hours + add_hours
        
        while total_hours >= 12:
            total_hours = total_hours - 12
            if time == "PM":
                time = "AM"
                count_days += 1
                if day != '':
                    if day == 6:
                        day = 0
                    else:
                        day += 1
                    
                    
            else:
                time = "PM"
        if total_hours == 0:
            total_hours = 12
            
        total_minutes = str(total_minutes)
        if len(total_minutes) == 1:
            total_minutes = f"0{total_minutes}"
        
        if day == '':
            if count_days == 1:
                count_days = "(next day)"
                new_time = f"{total_hours}:{total_minutes} {time} {count_days}"
            elif count_days == 0:
                new_time = f"{total_hours}:{total_minutes} {time}"
            else:
                new_time = f"{total_hours}:{total_minutes} {time} ({count_days} days later)"
        elif day != '':
            if count_days == 0:
                new_time = f"{total_hours}:{total_minutes} {time}, {week_days[day]}"
            elif count_days == 1:
                new_time = f"{total_hours}:{total_minutes} {time}, {week_days[day]} (next day)"
            else:
                new_time = f"{total_hours}:{total_minutes} {time}, {week_days[day]} ({count_days} days later)"
        
            
        
        return new_time
        
        
            
        
        


print(add_time('8:16 PM', '466:02', 'tuesday'))
        
#add_time('8:16 PM', '466:02', 'tuesday')

#add_time('3:00 PM', '3:10')
    # Returns: 6:10 PM

add_time('11:30 AM', '2:32', 'Monday')
    # Returns: 2:02 PM, Monday

add_time('11:43 AM', '00:20')
    # Returns: 12:03 PM

add_time('10:10 PM', '3:30')
    # Returns: 1:40 AM (next day)

add_time('11:43 PM', '24:20', 'tueSday')
    # Returns: 12:03 AM, Thursday (2 days later)

add_time('6:30 PM', '205:12')
    # Returns: 7:42 AM (9 days later)
