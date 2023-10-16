import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from myapp.models import Disclosure_data_fy16

class Command(BaseCommand):
    help = 'Import data from a CSV file into the database'
    
    
    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='/Users/diviksatija/Desktop/STGI HACKATHON/hello/H-1B_Disclosure_Data_FY16.csv')

    def handle(self, *args, **kwargs):
        print("inside func")
        print(args)
        csv_file = kwargs['csv_file']
    # csv_file = csv.DictReader(÷'/Users/diviksatija/Desktop/STGI HACKATHON/hello/H-1B_Disclosure_Data_FY16.csv')
    # def import_data_from_csv(csv_file):
        with open(csv_file, 'r') as file:
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
if __name__ == "__main__":
    csv_file = '/Users/diviksatija/Desktop/STGI HACKATHON/hello/H-1B_Disclosure_Data_FY16.csv'
    object = Command()
    object.import_data_from_csv(csv_file)