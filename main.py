from bill_report import BillReportUtil
from house_report import HouseReport
import json
import pandas as pd


# reportObj = BillReportUtil(path="2024-10-OCTUBRE IBIZA.xlsx")
# reportL = reportObj.generatereport()


# with open('reporte.json', 'w') as json_file:
#     json.dump([report.to_dict() for report in reportL], json_file, indent=4)


houseReportObj = HouseReport(path="2024-10-OCTUBRE IBIZA.xlsx")
houses = houseReportObj.gethousesreport()


with open("houses.json", "w") as json_file:
    json.dump([report.to_nuvi() for report in houses], json_file, indent=4)
