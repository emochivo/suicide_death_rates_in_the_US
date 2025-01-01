import psycopg2

conn = psycopg2.connect(
    database='postgres',
    user='postgres',
    password='12345678',
    options='-c search_path=suicide_death_rates_us'
)

cur = conn.cursor()


def sex():

    userChoice = int(input('\nChoose the number of the subcategory:\n1) Male\n2) Female\n3) Average death (Male and Female)\n'))

    if userChoice == 1:
        # The estimated deaths per 100,000 people: Male, sorted by descending order
        cur.execute(
            """
                select year, estimate
                from data
                where unit_num = 1 and stub_label_num = 2.1
                order by estimate desc;
            """
        )
        results = cur.fetchall()

        print('\nMale:')
        print('     Year             Estimated deaths (per 100k ppl.)')
        for i in results:
            print(f'     {i[0]}                          {i[1]}')


    elif userChoice == 2:
        # The estimated deaths per 100,000 people: Female, sorted by descending order
        cur.execute(
            """
                select year, estimate
                from data
                where unit_num = 1 and stub_label_num = 2.2
                order by estimate desc;
            """
        )
        results = cur.fetchall()

        print('\nFemale:')
        print('     Year             Estimated deaths (per 100k ppl.)')
        for i in results:
            print(f'     {i[0]}                          {i[1]}')

    
    elif userChoice == 3:
        # The average death per 100,000 people: Male vs Female
        cur.execute(
            """
                select stub_label, floor(avg(estimate)) as avg_suicide_death_cases
                from data
                where unit_num = 1 and stub_name_num = 2
                group by stub_label;
            """
        )
        results = cur.fetchall()

        print('\nAverage death:')
        print('     Sex             Estimated deaths (per 100k ppl.)')
        for i in results:
            print(f'     {i[0]}')
            print(f'                                    {i[1]}')




def race():

    userChoice = int(input('\nChoose the number of the subcategory:\n1) White\n2) Black\n3) Asian\n4) Indian American\n'))

    if userChoice == 1:
        # The estimated deaths per 100,000 people: White, sorted by descending order
        cur.execute(
            """
                select year, floor(sum(estimate)) as suicide_death_rates
                from data
                where unit_num = 1
                    and stub_label like '%White%'
                    and stub_name_num = 4
                group by year_num, year
                order by suicide_death_rates desc;
            """
        )
        results = cur.fetchall()

        print('\nWhite:')
        print('     Year             Estimated deaths (per 100k ppl.)')
        for i in results:
            print(f'     {i[0]}                          {i[1]}')


    elif userChoice == 2:
        # The estimated deaths per 100,000 people: Black, sorted by descending order
        cur.execute(
            """
                select year, floor(sum(estimate)) as suicide_death_rates
                from data
                where unit_num = 1
                    and stub_label like '%Black%'
                    and stub_name_num = 4
                group by year_num, year
                order by suicide_death_rates desc;
            """
        )
        results = cur.fetchall()

        print('\nBlack:')
        print('     Year             Estimated deaths (per 100k ppl.)')
        for i in results:
            print(f'     {i[0]}                          {i[1]}')



    elif userChoice == 3:
        # The estimated deaths per 100,000 people: Asian, sorted by descending order
        cur.execute(
            """
                select year, floor(sum(estimate)) as suicide_death_rates
                from data
                where unit_num = 1
                    and stub_label like '%Asian%'
                    and stub_name_num = 4
                group by year_num, year
                order by suicide_death_rates desc;
            """
        )
        results = cur.fetchall()

        print('\nAsian:')
        print('     Year             Estimated deaths (per 100k ppl.)')
        for i in results:
            print(f'     {i[0]}                          {i[1]}')        



    elif userChoice == 4:
        # The estimated deaths per 100,000 people: Indian American, sorted by descending order
        cur.execute(
            """
                select year, floor(sum(estimate)) as suicide_death_rates
                from data
                where unit_num = 1
                    and stub_label like '%Indian%'
                    and stub_name_num = 4
                group by year_num, year
                order by suicide_death_rates desc;
            """
        )
        results = cur.fetchall()

        print('\nIndian American:')
        print('     Year             Estimated deaths (per 100k ppl.)')
        for i in results:
            print(f'     {i[0]}                          {i[1]}')       




def sex_and_race():

    userChoice = int(input('\nChoose the number of the subcategory:\n1) White male\n2) White female\n3) Black male\n4) Black female\n5) Asian male\n6) Asian female\n7) Indian American male\n8) Indian American female\n9) All sexes and races combined\n'))

    if userChoice == 1:
        # The estimated deaths per 100,000 people: White male, sorted by descending order
        cur.execute(
            """
                select year, estimate
                from data
                where unit_num = 1
                    and stub_name_num = 4
                    and stub_label_num = 4.11
                order by estimate desc;
            """
        )
        results = cur.fetchall()

        print('\nWhite male:')
        print('     Year             Estimated deaths (per 100k ppl.)')
        for i in results:
            print(f'     {i[0]}                          {i[1]}')   



    elif userChoice == 2:
        # The estimated deaths per 100,000 people: White female, sorted by descending order
        cur.execute(
            """
                select year, estimate
                from data
                where unit_num = 1
                    and stub_name_num = 4
                    and stub_label_num = 4.21
                order by estimate desc;
            """
        )
        results = cur.fetchall()

        print('\nWhite female:')
        print('     Year             Estimated deaths (per 100k ppl.)')
        for i in results:
            print(f'     {i[0]}                          {i[1]}') 



    elif userChoice == 3:
        # The estimated deaths per 100,000 people: Black male, sorted by descending order
        cur.execute(
            """
                select year, estimate
                from data
                where unit_num = 1
                    and stub_name_num = 4
                    and stub_label_num = 4.12
                order by estimate desc;
            """
        )
        results = cur.fetchall()

        print('\nBlack male:')
        print('     Year             Estimated deaths (per 100k ppl.)')
        for i in results:
            print(f'     {i[0]}                          {i[1]}') 



    elif userChoice == 4:
        # The estimated deaths per 100,000 people: Black female, sorted by descending order
        cur.execute(
            """
                select year, estimate
                from data
                where unit_num = 1
                    and stub_name_num = 4
                    and stub_label_num = 4.22
                order by estimate desc;
            """
        )
        results = cur.fetchall()

        print('\nBlack female:')
        print('     Year             Estimated deaths (per 100k ppl.)')
        for i in results:
            print(f'     {i[0]}                          {i[1]}') 



    elif userChoice == 5:
        # The estimated deaths per 100,000 people: Asian male, sorted by descending order
        cur.execute(
            """
                select year, estimate
                from data
                where unit_num = 1
                    and stub_name_num = 4
                    and stub_label_num = 4.14
                order by estimate desc;
            """
        )
        results = cur.fetchall()

        print('\nAsian male:')
        print('     Year             Estimated deaths (per 100k ppl.)')
        for i in results:
            print(f'     {i[0]}                          {i[1]}') 


    elif userChoice == 6:
        # The estimated deaths per 100,000 people: Asian female, sorted by descending order
        cur.execute(
            """
                select year, estimate
                from data
                where unit_num = 1
                    and stub_name_num = 4
                    and stub_label_num = 4.24
                order by estimate desc;
            """
        )
        results = cur.fetchall()

        print('\nAsian female:')
        print('     Year             Estimated deaths (per 100k ppl.)')
        for i in results:
            print(f'     {i[0]}                          {i[1]}')



    elif userChoice == 7:
        # The estimated deaths per 100,000 people: Indian American male, sorted by descending order
        cur.execute(
            """
                select year, estimate
                from data
                where unit_num = 1
                    and stub_name_num = 4
                    and stub_label_num = 4.13
                order by estimate desc;
            """
        )
        results = cur.fetchall()

        print('\nIndian American male:')
        print('     Year             Estimated deaths (per 100k ppl.)')
        for i in results:
            print(f'     {i[0]}                          {i[1]}')



    elif userChoice == 8:
        # The estimated deaths per 100,000 people: Indian American female, sorted by descending order
        cur.execute(
            """
                select year, estimate
                from data
                where unit_num = 1
                    and stub_name_num = 4
                    and stub_label_num = 4.23
                order by estimate desc;
            """
        )
        results = cur.fetchall()

        print('\nIndian American female:')
        print('     Year             Estimated deaths (per 100k ppl.)')
        for i in results:
            print(f'     {i[0]}                          {i[1]}')


    elif userChoice == 9:
        # The average death per 100,000 people: All sexes and races combined, sorted by descending order
        cur.execute(
            """
                select stub_label, floor(avg(estimate)) as avg_suicide_death_rates
                from data
                where unit_num = 1
                    and stub_name_num = 4
                group by stub_label_num, stub_label
                order by avg_suicide_death_rates desc;
            """
        )
        results = cur.fetchall()

        print('\nAverage death:')
        print('     Year                                                    Estimated deaths (per 100k ppl.)')
        for i in results:
            print(f'     {i[0]}')
            print(f'                                                                 {i[1]}')