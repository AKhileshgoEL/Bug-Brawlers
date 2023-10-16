import select
from django.shortcuts import render, HttpResponse, redirect
from .models import Disclosure_data_fy16
from django.db import connection
from rest_framework.response import Response
from rest_framework.views import APIView

import csv

def index(request):
    #return HttpResponse("Welcome to Home Page")
    return render(request,'index.html')


def import_data_from_csv(request):
        if request.method == 'POST' and request.FILES['csv_file']:
          csv_file = request.FILES['csv_file']

        if not csv_file.name.endswith('.csv'):
            return HttpResponse('Invalid file type. Please upload a CSV file.')



        #with open('/Users/diviksatija/Desktop/STGI HACKATHON/hello/H-1B_Disclosure_Data_FY16.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
               Disclosure_data_fy16 = Disclosure_data_fy16.objects.create( 
                    case_number = row['case_number'],
                    case_status = row['case_status'],
                    case_submitted = row['case_submitted'],
                    decision_date = row['decision_date'],
                    visa_class = row['visa_class'],
                    employment_start_date = row['employment_start_date'],
                    employment_end_date = row['employment_end_date'],
                    employer_name = row['employer_name'],
                    employer_address = row['employer_address'],
                    employer_city = row['employer_city'],
                    employer_state = row['employer_state'],
                    employer_postal_code = row['employer_postal_code'],
                    employer_country = row['employer_country'],
                    employer_province = row['employer_province'],
                    employer_phone = row['employer_phone'],
                    agent_attorney_name = row['agent_attorney_name'],
                    agent_attorney_city = row['agent_attorney_city'],
                    agent_attorney_state = row['agent_attorney_state'],
                    job_title = row['job_title'],
                    soc_code = row['soc_code'],
                    soc_name = row['soc_name'],
                    naic_code = row['naic_code'],
                    total_workers = row['total_workers'],
                    full_time_position = row['full_time_position'],
                    prevailing_wage = row['prevailing_wage'],
                    pw_unit_of_pay = row['pw_unit_of_pay'],
                    pw_wage_source = row['pw_wage_source'],
                    pw_source_year = row['pw_source_year'],
                    pw_source_other = row['pw_source_other'],
                    wage_rate_of_pay_from = row['wage_rate_of_pay_from'],
                    wage_rate_of_pay_to = row['wage_rate_of_pay_to'],
                    wage_unit_of_pay = row['wage_unit_of_pay'],
                    h1bdependent = row['h1bdependent'],
                    willful_violator = row['willful_violator'],
                    worksite_city = row['worksite_city'],
                    worksite_county = row['worksite_county'],
                    worksite_state = row['worksite_state'],
                    worksite_postal_code = row['worksite_postal_code'],
                    original_cert_date = row['original_cert_date']
                    )
               return HttpResponse('Data from CSV file inserted successfully.')
        return HttpResponse('Invalid request method or missing file.')


    
class TotalResultsView(APIView):
    def get(self, request):
        total_results = Disclosure_data_fy16.objects.count()
        return Response({'total_results': '''SELECT count(DISTINCT id) as number_of_records
FROM Disclosure_data_fy16'''})
    
class AverageSalaryView(APIView):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute('''SELECT AVG(Total_Salary)
FROM (
    SELECT *
        CASE 
            WHEN wage_unit_of_pay = 'Year' THEN wage_rate_of_pay_from
            WHEN wage_unit_of_pay = 'Month' THEN wage_rate_of_pay_from * 12
            WHEN wage_unit_of_pay = 'Week' THEN wage_rate_of_pay_from * 52
            WHEN wage_unit_of_pay = 'Bi-Weekly' THEN wage_rate_of_pay_from * 104
            WHEN wage_unit_of_pay = 'Hour' THEN wage_rate_of_pay_from * 2080
        END AS Total_Salary
    FROM Disclosure_data_fy16
) AS Total_Salary''')
            result = cursor.fetchone()[0]

        return Response({'average_salary': result})
    

class Mediansalary(APIView):
    def get(self, request):
        result3 = '''SELECT PERCENTILE_COUNT(0.5) WITHIN GROUP (ORDER BY Total_Salary) OVER()
FROM (
    SELECT *
        CASE 
            WHEN wage_unit_of_pay = 'Year' THEN wage_rate_of_pay_from
            WHEN wage_unit_of_pay = 'Month' THEN wage_rate_of_pay_from * 12
            WHEN wage_unit_of_pay = 'Week' THEN wage_rate_of_pay_from * 52
            WHEN wage_unit_of_pay = 'Bi-Weekly' THEN wage_rate_of_pay_from * 104
            WHEN wage_unit_of_pay = 'Hour' THEN wage_rate_of_pay_from * 2080
        END AS Total_Salary
    FROM Disclosure_data_fy16
) AS Median_Salary '''
        return Response({'median': result3})
    
class oneforth(APIView):
    def get(self, request):
        result4 = '''SELECT PERCENTILE_COUNT(0.25) WITHIN GROUP (ORDER BY Total_Salary) OVER()
FROM (
    SELECT *
        CASE 
            WHEN wage_unit_of_pay = 'Year' THEN wage_rate_of_pay_from
            WHEN wage_unit_of_pay = 'Month' THEN wage_rate_of_pay_from * 12
            WHEN wage_unit_of_pay = 'Week' THEN wage_rate_of_pay_from * 52
            WHEN wage_unit_of_pay = 'Bi-Weekly' THEN wage_rate_of_pay_from * 104
            WHEN wage_unit_of_pay = 'Hour' THEN wage_rate_of_pay_from * 2080
        END AS Total_Salary
    FROM Disclosure_data_fy16
) AS Percentile_25 '''
        return Response({'one_forth': result4})
    
class threeforth(APIView):
    def get(self, request):
        result5 = '''SELECT PERCENTILE_COUNT(0.25) WITHIN GROUP (ORDER BY Total_Salary) OVER()
FROM (
    SELECT *
        CASE 
            WHEN wage_unit_of_pay = 'Year' THEN wage_rate_of_pay_from
            WHEN wage_unit_of_pay = 'Month' THEN wage_rate_of_pay_from * 12
            WHEN wage_unit_of_pay = 'Week' THEN wage_rate_of_pay_from * 52
            WHEN wage_unit_of_pay = 'Bi-Weekly' THEN wage_rate_of_pay_from * 104
            WHEN wage_unit_of_pay = 'Hour' THEN wage_rate_of_pay_from * 2080
        END AS Total_Salary
    FROM Disclosure_data_fy16
) AS Percentile_75'''
        return Response({'three_forth': result5})
    
def read_csv_file(file_path):
    data = []
    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            data.append(row)
    return data

def display_csv_data(request):
    file_path = 'Users/diviksatija/Desktop/STGI HACKATHON/hello/H-1B_Disclosure_Data_FY16.csv'
    data = read_csv_file(file_path)
    return render(request, 'template_name.html', {'data': data})

    

    
