movie_name = ["검은 사제들", "내부자들", "마션"]

movie_time_1 = ["1. 9:00", "2. 12:00", "3. 15:00", "4. 18:00", "5. close"]
movie_time_2 = ["1. 10:15", "2. 13:30", "3. 16:45", "4. 20:00", "5. close"]
movie_time_3 = ["1. 7:30", "2. 10:00", "3. 15:00", "4. close", "5. close"]


time = [movie_time_1, movie_time_2, movie_time_3] #각 영화의 시간을 의미하는 문자형 배열을 만들었습니다.



movie_seat_1_1 = [[0for col in range(5)] for row in range(5)]
movie_seat_1_2 = [[0for col in range(5)] for row in range(5)]
movie_seat_1_3 = [[0for col in range(5)] for row in range(5)]
movie_seat_1_4 = [[0for col in range(5)] for row in range(5)]

movie_seat_2_1 = [[0for col in range(5)] for row in range(5)]
movie_seat_2_2 = [[0for col in range(5)] for row in range(5)]
movie_seat_2_3 = [[0for col in range(5)] for row in range(5)]
movie_seat_2_4 = [[0for col in range(5)] for row in range(5)]

movie_seat_3_1 = [[0for col in range(5)] for row in range(5)]
movie_seat_3_2 = [[0for col in range(5)] for row in range(5)]
movie_seat_3_3 = [[0for col in range(5)] for row in range(5)]


movie_seat_1 = [movie_seat_1_1, movie_seat_1_2, movie_seat_1_3, movie_seat_1_4]
movie_seat_2 = [movie_seat_2_1, movie_seat_2_2, movie_seat_2_3, movie_seat_1_4]
movie_seat_3 = [movie_seat_3_1, movie_seat_3_2, movie_seat_3_3]

seat = [movie_seat_1, movie_seat_2, movie_seat_3]


print "원하시는 메뉴를 선택하세요."
menu=1
children = 0
adult = 0
adolescent = 0
n = 0
i=0
t=0
totalcost = 0

while menu != 4: #메뉴를 확인하여 4(종료)가 아닌 경우 프로그램을 계속 진행합니다. 초기값은 1로하여 시작을 하게 만들었습니다.
    print "1. 영화 예매"
    print "2. 영화 시간표 확인"
    print "3. 총 수입 확인"
    print "4. 종료"
    menu = int(input())
    if menu == 1: #영화 예매에 대한 내용을 시작합니다.
        print "--------------------------------------------------------------------------"
        print "A. 영화예매를 시작합니다."
        print "1. 검은 사제들   1관      9:00  |  12:00  |  15:00  |  18:00"
        print "2. 내부자들      2관      10:15  |  13:30  |  16:45  |  20:00"
        print "3. 마션         3관      7:30  |  10:00  |  15:00"

        check = 1
        while check == 1: #check를 만들어 1인경우 계속하게 하는데 아래의 동작중 제대로 작동하게 된다면 check를 0으로 바꾸어 while문을 나가도록 만들었습니다.
            print "--------------------------------------------------------------------------"
            print "B. 원하는 영화를 선택하세요. 1. 검은 사제들     2. 내부자들     3. 마션   4. close"
            i = int(input())
            
            if 0<i and i<5:
                print movie_name[i-1], "선택 하셨습니다."
                check = 0
            else:        
                print "1~4중의 숫자를 입력해 주세요."
            
        if i != 4:
            check = 1
            while check ==1: #위와 같은 방법으로 check를 만들어 시간을 확인합니다.
                print "--------------------------------------------------------------------------"
                print "C. 원하는 시간을 입력하세요. "
                print time[i-1]
                t = int(input())
                if i == 3 and t == 4: #마션을 선택하고 시간이 4인경우 예외처리를 하여 t != 5에 대한 if문을 실행하지 않도록 합니다.
                    t = 5
                    check = 0
                elif 0<t and t<6:
                    print time[i-1][t-1],"선택 하셨습니다."
                    check =0
                else:
                    print "1~5의 숫자를 입력해 주세요."
                
            if t != 5:
                check = 1 
                while check == 1: #위와 같은방법으로 check을 만들어 인원을 확인합니다.
                    print "--------------------------------------------------------------------------"
                    print "D. 총인원을 입력하세요. (1~25, 0을 입력하시면 종료됩니다.)" #0을 입력하시면 인원에 대한 if문을 수행하지 않아서 프로그램이 처음으로 돌아갑니다.
                    n = int(input())
                    if n == 0:
                        print "프로그램을 종료합니다."
                        check=0
                    elif 0 <n and n<25:
                        print n, "명을 선택하셨습니다."
                        check=0
                    else:
                        print" 0~25의 숫자를 입력해 주세요. (0을 입력하시면 종료됩니다.)"

                if n != 0: #위와 같은방법으로 check를 만들어 좌석의 위치를 확인합니다.
                    for a in range(n): 
                        print "--------------------------------------------------------------------------"
                        print "E. 좌석을 선택합니다."
                        for b in range(5):
                            print seat[i-1][t-1][b]
                        check = 1
                        while check == 1:
                            check2 = 1
                            while check2 == 1:
                                print "row를 입력하세요. (1~5)"
                                r = int(input())
                                print "col을 입력하세요. (1~5)"
                                c = int(input())
                                if( 0<r and r<6 and 0<c and c<6):
                                    check2 = 0
                                else:
                                    print "잘못된 값을 입력하셨습니다. 옳은 값을 다시 입력하세요."
                            if(seat[i-1][t-1][r-1][c-1] == 0):
                                seat[i-1][t-1][r-1][c-1] = 1
                                check = 0
                            else:
                                print "이미 예약된 좌석입니다. 빈자리를 선택해 주세요. "
                                check = 1

                    print "--------------------------------------------------------------------------"
                    check = 1
                    while check == 1: #위와 같은방법으로 check를 만들어 좌석의 위치를 확인합니다.
                        checknumber = n
                        print '청소년의 수는 몇명입니까?'
                        adolescent = int(input())
                        checknumber -= adolescent
                        if checknumber > 0 and adolescent > 0: #전체 인원수가 적절한 경우에만 다음단계로 넘어가고 최종적으로 완료되면 check에 0을 넣어서 while문을 끝냅니다. 
                            print '어린이의 수는 몇명입니까?'
                            children = int(input())
                            checknumber -= children
                            if checknumber > -1 and children > -1:
                                adult = checknumber
                                print '어른의 수는' , adult , '명입니다.'
                                print " 영화 예매가 모두 완료되었습니다."
                                check = 0
                        elif checknumber == 0:
                            print " 영화 예매가 모두 완료되었습니다."
                            check = 0
                        else:
                            print "인원수가 잘못 입력되었습니다. 인원수를 다시 입력하세요."

                    totalcost = totalcost + adult * 10000 + adolescent * 8000 + children * 5000 #total금액에 현재 예매의 가격을 더해서 최종값을 입력합니다.

        print "메뉴화면으로 이동합니다."

    elif menu == 2: #입력받은 menu가 2라면 영화 시간표를 출력하는 프로그램을 만들었습니다.
        print "2. 영화 시간표를 확인합니다."
        print "검은 사제들   1관      9:00	    12:00	15:00	18:00"
        print "내부자들      2관      10:15	13:30	    16:45	20:00"
        print "마션         3관      7:30	     10:00	15:00"

    elif menu == 3: #입력받은 menu가 3이라면 총수입을 출력하는 프로그램입니다.
        print "3. 영화관의 총 수입을 확인합니다."
        print '총 수입은' ,totalcost, '원 입니다.'


    elif menu == 4: #입력받은 menu가 4라면 처음 while문의 조건을 만족하지 못함으로 나갑니다.
        print "프로그램을 종료합니다."
    else: #입력받은 메뉴가 메뉴에 없다면 선택을 다시 하도록합니다.
        print "없는 메뉴입니다. 1~4중에 선택해 주세요."
    
